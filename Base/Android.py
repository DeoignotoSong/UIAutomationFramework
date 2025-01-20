import importlib
import queue
import threading
from Utils.ThreadHandler import ThreadHandler
from Core.Global import Data, ThreadInfo
from Utils.Log import log
from Core.Project import Project as CoreProject
from Core.Global import DataBaseName
from Core.Global import Data, ProjectExtend
from STF.STFServer import STFServer
import time
import yaml
import os


class Android(CoreProject):
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
        super(Android, self).__init__(
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

        super(Android, self)._data_prepare()
        self.devices_info = self._init_devices_(kwargs['devices'])
        self.retry_times = int(self.project_config.get('Project', 'retry_times'))
        self.thread_count = len(ProjectExtend.DEVICES)
        self.default_drivers = ['Appium']
        self.browser = 'app'

        if is_distributed:
            self.nodes_count = len(self.nodes_info.keys())
            total_thread_count = self.thread_count * self.nodes_count
            db_count = total_thread_count
        else:
            self.nodes_count = 1
            db_count = self.thread_count

        if 'browser' in kwargs.keys():
            self.browser = 'app'
            self.start_appium = True

        if 'compatibility' in kwargs.keys():
            self.compatibility = kwargs['compatibility']
        else:
            self.compatibility = None
        self.scenarios_count = len(Data.TEST_DATA.keys())
        # super(Android, self)._init_db(['mysql', 'mongo'], db_count)
        # super(Android, self)._init_db_name()

    def _test_handle(self):
        # 初始化STF Server
        stf_server = STFServer()
        # 启动appium
        if self.start_appium:
            for device in ProjectExtend.DEVICES.keys():
                serial = ProjectExtend.DEVICES[device]["desired_caps"]["deviceName"]
                # 检查设备是否是远程设备
                info = stf_server.get_remote_used_devices_info(serial=serial)
                print(info)
                if info['success'] and not info['device']['using']:
                    # 创建远程手机调用
                    remote_connect_url = stf_server.remote_stf_call(serial=serial)
                    # 本地adb tcp 映射远程设备到本地
                    self.__create_adb_connect__(remote_connect_url)
                    # 更新设备信息
                    ProjectExtend.DEVICES[device]["desired_caps"]["deviceName"] = remote_connect_url
                    ProjectExtend.DEVICES[device]["desired_caps"]["udid"] = remote_connect_url
                    ProjectExtend.DEVICES[device]["desired_caps"]["platformVersion"] = info['device']['version']
                # 启动appium服务
                self.__start_appium_server__(device)
                time.sleep(3)

        params = {
            'project': self,
            'project_name': self.project,
            'need_store': self.need_store,
            'retries_failed': self.retries_failed,
            'retry_times': self.retry_times,
            'test_name': self.test_name,
            'default_drivers': self.default_drivers,
            'device': device,
            'start_appium': self.start_appium,
            'device': self.devices_info,
            'compatibility': self.compatibility,
            'browser': self.browser
        }

        for scenario_name in self.executed_scenarios_names:
            # 导入场景包
            test_scenario = importlib.import_module('Projects.' + self.project + '.TestScenario.' + scenario_name)

            # 执行场景方法
            eval(
                'test_scenario.{0}(**params)'.format(
                    scenario_name
                )
            )

    @staticmethod
    def __start_appium_server__(device):
        port_monitor = 'netstat -ano | findstr "{}"'.format(
            ProjectExtend.DEVICES[device]['port']
        )

        appium_listening = os.popen(port_monitor)

        time.sleep(2)

        appium_listening_str = appium_listening.read()

        if 'LISTENING' in appium_listening_str:
            log('Warning: The requested port may already in use')
        else:
            os.system('start appium -a 127.0.0.1 -p {0} -bp {1} -U {2}'.format(
                ProjectExtend.DEVICES[device]['port'],
                ProjectExtend.DEVICES[device]['bootstrap-port'],
                ProjectExtend.DEVICES[device]['desired_caps']['udid']
            ))

    def _init_devices_(self, devices):
        try:
            with open('./Projects/{}/Base/devices.yaml'.format(self.project),
                      'r',
                      encoding='utf8') as devices_info_file:
                devices_file_info = yaml.load(devices_info_file.read(),
                                              Loader=yaml.FullLoader)
        except FileNotFoundError as e:
            log(str(e) + '\nplease check your devices.yaml file')
            raise

        if devices is None or len(devices) == 0:
            devices = devices_file_info.keys()

        for key in devices:
            try:
                ProjectExtend.DEVICES[key] = devices_file_info[key]
            except KeyError:
                log('Has no {} device.'.format(key))

        if len(ProjectExtend.DEVICES.keys()) == 0:
            log('Has no valid device. Test finished')
            exit(0)
        return devices