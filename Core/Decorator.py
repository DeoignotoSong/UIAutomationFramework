import os
import time
import datetime
import traceback
import threading
import importlib
import copy
from Core.Enum import TestStatus
from Core.FrameworkException import ValidateException
from Utils.Log import log
from Core.Global import Data, TestResult, NameMap, PrepareData, ProjectExtend,RetriesFailedCount
from Core.RetentionWords import RetentionWords


def test_case(**p_kwargs):
    def test_case_method(func):
        def wrapper(*args, **kwargs):
            test_name = kwargs['test_name']
            if 'driver_type' in p_kwargs.keys():
                driver = args[0][p_kwargs['driver_type']]
            else:
                driver = args[0][kwargs['default_drivers'][0]]

            processed_args = []
            for index in range(0, len(args)):
                if index == 0:
                    item = driver
                else:
                    item = args[index]

                processed_args.append(item)

            # 当前线程id
            thread_id = threading.current_thread().ident
            start_time = time.time()
            log('Execute test case: %s' % func.__name__)
            # 用例执行结果
            result_detail = ''
            # 测试用例返回值
            test_case_return = {}
            result = TestStatus.Pass
            current_test_case_key = func.__name__

            try:
                # 取场景方法第一行备注作为场景描述
                NameMap.TEST_CASE_MAP[func.__name__] = func.__doc__.split('\n')[1].strip()
            except Exception as name_format_error:
                NameMap.TEST_CASE_MAP[func.__name__] = ''

            try:
                # 初始化
                td = {}
                # 替换关键字replace_day()等等
                retention_words = RetentionWords()
                # test_case重名区分：test_case.2
                if func.__name__ in Data.TEST_CASE_STATISTICS_IN_SCENARIO[thread_id].keys():
                    Data.TEST_CASE_STATISTICS_IN_SCENARIO[thread_id][func.__name__] += 1
                    current_test_case_key = '{0}.{1}'.format(
                        current_test_case_key,
                        str(Data.TEST_CASE_STATISTICS_IN_SCENARIO[thread_id][func.__name__])
                    )
                else:
                    Data.TEST_CASE_STATISTICS_IN_SCENARIO[thread_id][func.__name__] = 1

                if current_test_case_key in Data.TEST_DATA[TestResult.CURRENT_TEST_SCENARIO[thread_id]].keys():
                    for key in Data.TEST_DATA[TestResult.CURRENT_TEST_SCENARIO[thread_id]][current_test_case_key]['In']:
                        Data.TEST_DATA[TestResult.CURRENT_TEST_SCENARIO[thread_id]][current_test_case_key]['In'][key] = retention_words.replace_value_for_special_quote(
                            TestResult.CURRENT_TEST_SCENARIO[thread_id],
                            Data.TEST_DATA[TestResult.CURRENT_TEST_SCENARIO[thread_id]][current_test_case_key]['In'][key])

                    # 将用例参数传入，从test_data中取出参数
                    td = Data.TEST_DATA[TestResult.CURRENT_TEST_SCENARIO[thread_id]][current_test_case_key]['In']
                else:
                    Data.TEST_DATA[TestResult.CURRENT_TEST_SCENARIO[thread_id]][current_test_case_key] = {
                        'In': None,
                        'Out': None
                    }

                test_case_return = func(*processed_args, **td)
                # 将测试用例返回值写入test_data
                Data.TEST_DATA[TestResult.CURRENT_TEST_SCENARIO[thread_id]][current_test_case_key]['Out'] = test_case_return
            except Exception as error:
                file_name = _get_screen_shot_path(kwargs['project_name'], func.__name__)
                driver.save_screen_shot(file_name)
                result_detail = error.__str__()
                log('Test case exception: ' + result_detail)
                result = TestStatus.Error
                TestResult.CURRENT_TEST_SCENARIO_RESULT[thread_id] = TestStatus.Error
                log(traceback.format_exc())
                raise error
            finally:
                # 用例执行结果写入
                TestResult.TEST_RESULTS[TestResult.CURRENT_TEST_SCENARIO[thread_id]]['test_case_details'].append(
                    dict(
                        test_step_name=current_test_case_key,
                        test_result=result,
                        result_detail=result_detail
                    )
                )

                current_scenario_data = \
                    TestResult.TEST_RESULTS[TestResult.CURRENT_TEST_SCENARIO[thread_id]]['test_case_details']
                end_time = time.time()
                # 用例执行时间
                duration = str(end_time - start_time)
                log('Test Case Result: ' + str(result))
                log('Test Case duration: %s\n' % duration)
                TestResult.update(
                    args[3],
                    args[4],
                    'scenario_details',
                    [TestResult.CURRENT_TEST_SCENARIO[thread_id]],
                    current_scenario_data
                )
            return test_case_return
        return wrapper
    return test_case_method


def test_scenario(**p_kwargs):
    def test_scenario_method(func):
        def wrapper(*args, **kwargs):
            # 当前线程id
            thread_id = threading.current_thread().ident
            project_name = kwargs['project_name']
            retry_times = kwargs['retry_times']
            device_name = None
            device_info = None

            if 'driver_type' in p_kwargs.keys():
                driver_types = p_kwargs['driver_type']
            else:
                driver_types = kwargs['default_drivers']

            # 兼容性测试
            if "compatibility" in kwargs.keys() and kwargs["compatibility"]:
                device_name = kwargs['device_name']
                kwargs['devices'] = ProjectExtend.DEVICES.get(device_name)
            else:
                if ProjectExtend.DEVICES:
                    device_name = list(ProjectExtend.DEVICES.keys())[0]
                    kwargs['devices'] = ProjectExtend.DEVICES.pop(device_name)
            drivers_dict = {}

            params = kwargs
            params.update(p_kwargs)

            # 判断重跑
            retry_count = 0
            scenario_during_time = 0

            while retry_count < retry_times:
                # 当前mysql连接
                # mysql = ProjectExtend.DB_POOLS['mysql'].pop(0)
                mysql = None

                # 当前mongo连接
                # mongo = ProjectExtend.DB_POOLS['mongo'].pop(0)
                mongo = None

                start_time = time.time()
                log('=========================================================')
                log('Execute test Scenario: %s\n' % func.__name__)

                try:
                    NameMap.TEST_SCENARIO_MAP[func.__name__] = func.__doc__.split('\n')[1].strip()
                except Exception as name_format_error:
                    NameMap.TEST_SCENARIO_MAP[func.__name__] = ''
                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                # 待优化
                try:
                    Data.TEST_CASE_STATISTICS_IN_SCENARIO[thread_id] = {}
                    TestResult.CURRENT_TEST_SCENARIO[thread_id] = func.__name__
                    if len(TestResult.TEST_RESULTS) > 0:
                        if func.__name__ in TestResult.TEST_RESULTS:
                            retry_time = TestResult.TEST_RESULTS[func.__name__]['retry_time']
                            TestResult.TEST_RESULTS[func.__name__] = {
                                'scenario_result': False,
                                'test_case_details': [],
                                'retry_time': retry_time}
                        else:
                            TestResult.TEST_RESULTS[func.__name__] = {
                                'scenario_result': False,
                                'test_case_details': []}
                    else:
                        TestResult.TEST_RESULTS[func.__name__] = {
                            'scenario_result': False,
                            'test_case_details': []
                        }

                    for driver_type in driver_types:
                        # 判断测试场景是否指定了浏览器
                        project_base = importlib.import_module('Utils.Driver.{project}'.format(project=driver_type))

                        temp_driver = eval('project_base.{}(**params)'.format(
                            driver_type
                        ))

                        s_kwargs = copy.deepcopy(kwargs)
                        s_kwargs.update(p_kwargs)
                        temp_driver.create_driver(
                            **s_kwargs
                        )

                        drivers_dict[driver_type] = temp_driver
                    TestResult.CURRENT_TEST_SCENARIO_RESULT[thread_id] = TestStatus.Pass
                    func(drivers_dict, mysql, mongo, kwargs['test_name'], kwargs['need_store'], **params)
                # 断言错误异常处理
                except ValidateException as error:
                    # file_name = _get_screen_shot_path(project_name, func.__name__)
                    # 异常截图
                    # project.save_screen_shot(file_name)
                    log('Test Scenario Failed: ' + error.message)
                    TestResult.CURRENT_TEST_SCENARIO_RESULT[thread_id] = TestStatus.Failed
                # 其余错误异常处理
                except Exception as error:
                    log('error: ' + str(error))
                    log(traceback.format_exc())
                    # file_name = _get_screen_shot_path(project_name, func.__name__)
                    # 异常截图
                    # project.save_screen_shot(file_name)
                    log('Test Scenario exception: ' + error.__str__())
                    TestResult.CURRENT_TEST_SCENARIO_RESULT[thread_id] = TestStatus.Error
                finally:
                    # 场景执行结果
                    TestResult.TEST_RESULTS[func.__name__]['scenario_result'] = TestResult.CURRENT_TEST_SCENARIO_RESULT[thread_id]

                    # 场景执行次数
                    retry_count += 1
                    if (RetriesFailedCount.Retries_Failed_Count > 0) and (kwargs['retries_failed'] is True):
                        TestResult.TEST_RESULTS[func.__name__]['retry_time'] += 1
                    else:
                        TestResult.TEST_RESULTS[func.__name__]['retry_time'] = retry_count
                    # 场景执行时间
                    duration = int(time.time() - start_time)
                    scenario_during_time += duration
                    if TestResult.TEST_RESULTS[func.__name__]['scenario_result'] != TestStatus.Pass:
                        RetriesFailedCount.Retries_Failed_Scenarios.add(func.__name__)
                    else:
                        current_scenario_summary = {
                            'test_result': 1,
                            'status': 'Finished',
                            'scenario_executed_time': scenario_during_time
                        }
                        TestResult.update(
                            kwargs['test_name'],
                            kwargs['need_store'],
                            'scenarios',
                            [func.__name__],
                            current_scenario_summary
                        )
                        RetriesFailedCount.Retries_Failed_Scenarios.discard(func.__name__)
                    TestResult.TEST_RESULTS[func.__name__]['scenario_during_time'] = str(scenario_during_time)

                    # project.close()

                    for key in drivers_dict.keys():
                        drivers_dict[key].close()

                    log('Test Result: ' + str(TestResult.CURRENT_TEST_SCENARIO_RESULT[thread_id]))
                    log('Test Scenario duration: ' + str(duration))
                    log('=========================================================')
                    log(Data.TEST_DATA[func.__name__])
                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    # 释放执行用户
                    if thread_id in list(PrepareData.USING_DATA.keys()):
                        for key in list(PrepareData.USING_DATA[thread_id].keys()):
                            release_user_list = PrepareData.USING_DATA[thread_id].pop(key)
                            for index in range(0, len(release_user_list)):
                                release_user = release_user_list.pop()
                                PrepareData.PREPARE_DATA[key].append(release_user)

                    # 释放数据库资源
                    # ProjectExtend.DB_POOLS['mysql'].append(mysql)
                    # ProjectExtend.DB_POOLS['mongo'].append(mongo)

                    # 释放设备资源
                    if device_name:
                        ProjectExtend.DEVICES[device_name] = device_info

                    # 判断场景是否失败重新执行
                    if TestResult.CURRENT_TEST_SCENARIO_RESULT[thread_id] == TestStatus.Pass:
                        break
            else:
                current_scenario_summary = {
                    'test_result': 2,
                    'status': 'Finished',
                    'scenario_executed_time': scenario_during_time
                }
                TestResult.update(
                    kwargs['test_name'],
                    kwargs['need_store'],
                    'scenarios',
                    [func.__name__],
                    current_scenario_summary
                )
                log(project_name + ' retry ' + str(retry_times) + ' times failed')

            if TestResult.TEST_RESULTS[func.__name__]['retry_time'] > retry_times:
                TestResult.update(
                    kwargs['test_name'],
                    kwargs['need_store'],
                    'summary',
                    None,
                    {
                        'scenarios': 0,
                        'passed': 1 if current_scenario_summary['test_result'] == 1 else 0,
                        'failed': 0 if current_scenario_summary['test_result'] != 1 else -1
                    }
                )
            else:
                TestResult.update(
                    kwargs['test_name'],
                    kwargs['need_store'],
                    'summary',
                    None,
                    {
                        'scenarios': 0,
                        'passed': 1 if current_scenario_summary['test_result'] == 1 else 0,
                        'failed': 1 if current_scenario_summary['test_result'] != 1 else 0
                    }
                )

        return wrapper
    return test_scenario_method


# 截图路径
def _get_screen_shot_path(project, test_case_name):
    screen_path = './Projects/' + project + '/TestReport/Screens/' + datetime.datetime.now().strftime('%Y-%m-%d') + '/'

    if not os.path.exists(screen_path):
        os.makedirs(screen_path)

    file_path = screen_path + datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S') + test_case_name

    return file_path
