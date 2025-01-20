import importlib
import queue
import threading
from Utils.ThreadHandler import ThreadHandler
from Core.Global import Data, ThreadInfo
from Utils.Log import log
from Core.Project import Project as CoreProject
from Core.Global import DataBaseName


class PC(CoreProject):
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
        super(PC, self).__init__(
            project=project,
            env=env,
            need_mail=need_mail,
            is_show=is_show,
            need_store=need_store,
            test_name=test_name,
            is_distributed=is_distributed,
            retries_failed=retries_failed,
            retries_failed_times=retries_failed_times,
            *args,
            **kwargs)

        super(PC, self)._data_prepare()

        self.retry_times = int(self.project_config.get('Project', 'retry_times'))
        self.thread_count = int(self.project_config.get('Project', 'thread_count'))

        if is_distributed:
            self.nodes_count = len(self.nodes_info.keys())
            total_thread_count = self.thread_count * self.nodes_count
            db_count = total_thread_count
        else:
            self.nodes_count = 1
            db_count = self.thread_count

        if 'browser' in kwargs.keys():
            self.browser = kwargs['browser']
        else:
            self.browser = 'firefox'

        if 'compatibility' in kwargs.keys():
            self.compatibility = kwargs['compatibility']
        else:
            self.compatibility = None

        self.scenarios_count = len(Data.TEST_DATA.keys())
        super(PC, self)._init_db(['mysql', 'mongo'], db_count)
        super(PC, self)._init_db_name()

    def _test_handle(self):
        node_thread = {}

        for node_key in self.nodes_info.keys():
            node_thread[node_key] = []
            for index_turn in range(0, self.thread_count):
                node_thread[node_key].append(
                    '{}_{}'.format(
                        node_key,
                        index_turn
                    )
                )

        ThreadInfo.queue_lock = threading.Lock()
        ThreadInfo.work_queue = queue.Queue(len(self.executed_scenarios_names))
        thread_list = []

        for node_key in node_thread:
            for thread_index in node_thread[node_key]:
                params = {
                    'is_distributed': self.is_distributed,
                    'node_name': node_key,
                    'node_index': thread_index,
                    'retry_times': self.retry_times,
                    'need_store': self.need_store,
                    'test_name': self.test_name
                }

                thread_executor = ThreadHandler(self._queue_handle, **params)
                thread_list.append(thread_executor)

        ThreadInfo.queue_lock.acquire()

        for scenario_name in self.executed_scenarios_names:
            ThreadInfo.work_queue.put(scenario_name)

        ThreadInfo.queue_lock.release()

        for thread_instance in thread_list:
            thread_instance.start()

        ThreadInfo.work_queue.join()

    def _queue_handle(self, **kwargs):
        while not ThreadInfo.work_queue.empty():
            ThreadInfo.queue_lock.acquire()
            scenario_name = ThreadInfo.work_queue.get()
            ThreadInfo.queue_lock.release()
            params = {
                'project': self,
                'project_name': self.project,
                'is_distributed': self.is_distributed,
                'node_info': self.nodes_info[kwargs['node_name']],
                'compatibility': self.compatibility,
                'browser': self.browser,
                'need_store': self.need_store,
                'retries_failed': self.retries_failed,
                'retry_times': self.retry_times,
                'test_name': self.test_name,
                'default_drivers': self.default_drivers
            }

            # 导入场景包
            test_scenario = importlib.import_module('Projects.' + self.project + '.TestScenario.' + scenario_name)

            # 执行场景方法
            eval(
                'test_scenario.{0}(**params)'.format(
                    scenario_name
                )
            )

            ThreadInfo.work_queue.task_done()
