import time
import os
import yaml
from abc import ABCMeta, abstractmethod
from Core.ExcelHandler import ExcelHandler
from Core.Global import ProjectExtend, TestResult, DataBaseName
from Core.PersistentHandler import PersistentHandler
from Utils.Log import log
from Utils.Utils import get_work_folder
from Core.ConfigOperation import ConfigOperation
from Core.TestReport import TestReport
from Core.Global import PrepareData,RetriesFailedCount
from DB.DBFactory import DBFactory


class Project(object):
    __metaclass__ = ABCMeta

    def __init__(
            self,
            project,
            env,
            need_mail,
            is_show,
            need_store,
            test_name,
            is_distributed,
            retries_failed,
            retries_failed_times,
            *args,
            **kwargs):
        self.work_folder = get_work_folder()
        self.project = project
        self.env = env
        self.need_mail = need_mail
        self.is_show = is_show
        self.need_store = need_store
        self.test_name = test_name
        self.is_distributed = is_distributed
        self.retries_failed = retries_failed
        self.retries_failed_times = retries_failed_times
        self.default_drivers = ['Selenium']
        self.executed_scenarios_names = []

        self._node_yaml_path = '{work_folder}\\Core\\nodes.yaml'.format(
            work_folder=self.work_folder
        )

        self._base_config_path = '{work_folder}\\Core\\config.ini'.format(
            work_folder=self.work_folder
        )
        self._project_config_path = '{work_folder}\\Projects\\{project}\\Base\\config.ini'.format(
            work_folder=self.work_folder,
            project=self.project
        )

        self.base_config = ConfigOperation().load_config(
            self._base_config_path
        )

        self.project_config = ConfigOperation().load_config(
            self._project_config_path
        )

        self.nodes_info = self._init_nodes(is_distributed)

    def _scenarios_load(self, scenarios):
        self.executed_scenarios_names = []
        execute_scenarios = []
        # 取出所有场景
        for root, dirs, files in os.walk('Projects/' + self.project + '/TestScenario'):
            for file in files:
                (filename, extension) = os.path.splitext(file)  # 将文件名拆分为文件名与后缀
                # 如果是.py文件，则加入执行场景列表
                if extension == '.py':
                    execute_scenarios.append(filename)
        log(execute_scenarios)
        log('------------------------------')

        # 过滤可执行场景
        if scenarios:
            # 取所有场景文件和main需要执行的场景交集
            execute_scenarios = list(set(execute_scenarios).intersection(set(scenarios)))
            log(execute_scenarios)
        else:
            log('执行全部场景')

        scenario_count = 0
        for scenario_name in execute_scenarios:
            TestResult.scenarios[scenario_name] = {}
            self.executed_scenarios_names.append(scenario_name)
            scenario_info = {
                'test_result': 1,
                'status': 'In Process',
                'scenario_executed_time': 0
            }

            TestResult.update(
                self.test_name,
                self.need_store,
                'scenarios',
                [scenario_name],
                scenario_info
            )

            scenario_count += 1

            ExcelHandler(
                self.project,
                scenario_name,
                self.default_drivers
            ).scenario_data()
        start_time = time.time()
        if (len(RetriesFailedCount.Retries_Failed_Scenarios) > 0) and \
                (RetriesFailedCount.Retries_Failed_Count > 0) and \
                (self.retries_failed is True):
            TestResult.update(
                self.test_name,
                self.need_store,
                'summary',
                None,
                {
                    'scenarios': 0,
                    'passed': 0,
                    'failed': 0
                }
            )
        else:
            TestResult.update(
                self.test_name,
                self.need_store,
                'summary',
                None,
                {
                    'scenarios': scenario_count,
                    'passed': 0,
                    'failed': 0,
                    'start_time': start_time
                }
            )

    def _report_handle(self, project_during_time):
        if self.need_store:
            persistent_handler = PersistentHandler()
            persistent_handler.result_analyse(self.test_name)

        # 生成测试报告
        report = TestReport(
            self.project,
            need_mail=self.need_mail,
            is_show=self.is_show,
            env=self.env,
            project_during_time=project_during_time)

        report.generate_report(self.test_name)

    def _init_db_name(self):
        """
        初始化数据库名称
        :return:
        """
        # 初始化测试数据
        for key, value in self.project_config.items('{}.Database'.format(self.env)):
            DataBaseName.DATABASE_NAME[key] = value

    def _init_db(self, db_types, count):
        """
        初始化数据库
        :return:
        """
        """
        for item in db_types:
            for index in range(0, count):
                db_instance = DBFactory().get_db_instances(
                    db_type=item,
                    config=self.project_config,
                    env=self.env)
                if item not in ProjectExtend.DB_POOLS.keys():
                    ProjectExtend.DB_POOLS[item] = []
                ProjectExtend.DB_POOLS[item].append(db_instance)
        """

    def _init_nodes(self, is_distributed):
        try:
            if is_distributed:
                with open(self._node_yaml_path, 'r', encoding='utf8') as nodes_info_file:
                    nodes = yaml.load(
                        nodes_info_file.read(),
                        Loader=yaml.FullLoader
                    )
            else:
                nodes = {
                    'nodes': {
                        'localhost': {
                            'ip': '192.168.0.1',
                            'port': 0,
                        }
                    }
                }
        except FileNotFoundError as e:
            log(str(e) + '\nplease check your nodes.yaml file')
            raise

        if len(ProjectExtend.NODES.keys()) == 0:
            log('Has no valid device. Test finished')

        return nodes['nodes']

    def _data_prepare(self):
        """
        初始化测试数据
        :return:
        """
        # 初始化测试数据
        for key, value in self.project_config.items('{}.PrepareData'.format(self.env)):
            value = value.split(',')
            PrepareData.PREPARE_DATA[key] = value

        for key, value in self.project_config.items('{}.Urls'.format(self.env)):
            PrepareData.URL[key] = value

        log(PrepareData.PREPARE_DATA)

    def execute(self, scenarios):
        start_time = time.time()

        self._scenarios_load(scenarios)

        self._test_handle()

        while (len(RetriesFailedCount.Retries_Failed_Scenarios) > 0) and \
                (RetriesFailedCount.Retries_Failed_Count < self.retries_failed_times) and \
                (self.retries_failed is True):
            RetriesFailedCount.Retries_Failed_Count = RetriesFailedCount.Retries_Failed_Count + 1
            self._scenarios_load(RetriesFailedCount.Retries_Failed_Scenarios)
            self._test_handle()

        end_time = time.time()

        self._report_handle(end_time - start_time)

    @abstractmethod
    def _test_handle(self, *args, **kwargs):
        pass
