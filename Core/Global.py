from Core.ConfigOperation import ConfigOperation
import datetime
import socket
from Utils.RedisLock import *
import redis
import json
import os


class Data:
    """
    测试相关全局数据
    """
    # 测试场景数据，包括入参、出参等信息
    TEST_DATA = {}
    # 在同一场景下，测试用例计数器，计数同一场景下，相同测试用例个数
    TEST_CASE_STATISTICS_IN_SCENARIO = {}


class TestResult:
    """
    测试结果相关全局数据
    """
    # 当前执行的测试场景名/按线程id分组
    CURRENT_TEST_SCENARIO = {}
    # 当前测试场景的测试结果/按线程id分组
    CURRENT_TEST_SCENARIO_RESULT = {}
    # 所有场景的测试结果详情
    TEST_RESULTS = {}
    scenario_details = {}
    scenarios = {}
    summary = {}

    @staticmethod
    def update(test_name, need_store, collection_name, keys, value):
        try:
            keys_str = ''
            try:
                for item in keys:
                    keys_str += '[\'{}\']'.format(item)
            except TypeError:
                print('The keys: ' + str(keys))
            command_str = 'TestResult.{}{} = value'.format(
                collection_name,
                keys_str)
            exec(command_str)
        except Exception as e:
            print('Error: {}'.format(e))
        else:
            if need_store is True:
                TestResult.notify(test_name, collection_name, keys, value)

    @staticmethod
    def notify(test_name, collection_name, key, value):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        current_dir_path = os.path.abspath(os.path.dirname(__file__))
        config_file_path = current_dir_path + '/config.ini'
        con = ConfigOperation.load_config(config_file_path)
        redis_key = test_name + ':' + collection_name
        re = redis.Redis(
            host=con.get('Redis', 'host'),
            port=int(con.get('Redis', 'port')),
            decode_responses=True,
            db=int(con.get('Redis', 'persistent_db'))
        )
        worker_ip = get_host_ip()

        save_data = {}

        if collection_name == 'summary':
            condition = {
                'test_name': test_name
            }

            save_data['test_name'] = test_name
            if redis_key not in re.keys():
                lock = acquire_lock_with_timeout(
                    re,
                    redis_key
                )

                value['start_time'] = current_time

                save_data = json.dumps(value)

                re.set(
                    redis_key,
                    save_data,
                    ex=172800
                )

                release_lock(
                    re,
                    redis_key,
                    lock
                )
            else:
                lock = acquire_lock_with_timeout(
                    re,
                    redis_key
                )

                current_data = re.get(
                    redis_key
                )

                test_summary_item = json.loads(
                    current_data
                )

                try:
                    for item_key in test_summary_item:
                        if item_key in value.keys():
                            value[item_key] = int(value[item_key]) + int(test_summary_item[item_key])
                        else:
                            value[item_key] = test_summary_item[item_key]
                except ValueError:
                    pass
                value['end_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                save_data = json.dumps(value)

                re.set(
                    redis_key,
                    save_data,
                    ex=172800
                )
                release_lock(
                    re,
                    redis_key,
                    lock
                )

        else:
            for item in key:
                redis_key += ':' + str(item)

            lock = acquire_lock_with_timeout(
                re,
                redis_key
            )

            if collection_name == 'scenarios':
                value['worker'] = worker_ip
            save_data = {
                'scenario_details': str(value)
            }
            save_data_json = json.dumps(
                save_data,
                ensure_ascii=False)

            condition = {
                'test_name': test_name,
                'scenario_path': item
            }

            re.set(
                redis_key,
                save_data_json,
                ex=172800
            )
            release_lock(
                re,
                redis_key,
                lock
            )


def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    s = None
    try:
        s = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '0.0.0.0'
    finally:
        if s is not None:
            s.close()

    return ip


class NameMap:
    """
    测试场景及测试用例中英文名称映射
    """
    # 测试场景中英文名称映射
    TEST_SCENARIO_MAP = {}
    # 测试用例中英文名称映射
    TEST_CASE_MAP = {}


class PrepareData:
    """
    所有线程准备数据
    """
    # 存储所有准备数据
    PREPARE_DATA = {}
    # 正在使用的数据
    USING_DATA = {}
    # 环境urls
    URL = {}


class ProjectExtend:
    """
    项目扩展功能
    """
    NODES = {}
    # 设备连接
    DEVICES = {}
    # 数据库连接池
    DB_POOLS = {}


class DataBaseName:
    """
    数据库名称对应
    """
    DATABASE_NAME = {}


class RetriesFailedCount:
    """
    错误重试计数
    """
    Retries_Failed_Count = 0
    Retries_Failed_Scenarios = set()


class ThreadInfo:
    work_queue = None
    queue_lock = None
