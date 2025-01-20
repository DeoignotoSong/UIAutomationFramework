from Utils.Log import log
import datetime
import json
import redis
import pymongo
import os
from Core.ConfigOperation import ConfigOperation


class PersistentHandler:
    def __init__(self):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        current_dir_path = os.path.abspath(os.path.dirname(__file__))
        config_file_path = current_dir_path + '/config.ini'
        con = ConfigOperation.load_config(config_file_path)
        redis_password = con.get('Redis', 'password')
        if redis_password == '':
            self._redis_connection = redis.Redis(
                host=con.get('Redis', 'host'),
                port=int(con.get('Redis', 'port')),
                decode_responses=True,
                db=int(con.get('Redis', 'persistent_db'))
            )
        else:
            self._redis_connection = redis.Redis(
                host=con.get('Redis', 'host'),
                port=int(con.get('Redis', 'port')),
                decode_responses=True,
                db=int(con.get('Redis', 'persistent_db')),
                password=con.get('Redis', 'password')
            )

        self._mongo_connection = pymongo.MongoClient(
            con.get(
                'Mongo',
                'address'
            )
        )

        db_name = con.get(
            'Mongo', 'db'
        )
        self._mongo_db = self._mongo_connection[db_name]

    def result_analyse(self, test_name):
        try:
            self._test_summary_analyse(test_name)

            self._test_scenarios_analyse(test_name)

            self._test_cases_analyse(test_name)

            self._clean_redis_namespace(test_name)
        except Exception:
            log('There are some exception when do persistent')

    def _test_summary_analyse(self, test_name):
        collection = self._mongo_db.summary
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        test_summary = json.loads(
            self._redis_connection.get(
                test_name + ':summary'
            )
        )

        test_summary['end_time'] = current_time

        condition = {
            'test_name': test_name
        }

        collection.update_one(
            condition,
            {
                '$set': test_summary
            },
            upsert=True
        )

    def _test_scenarios_analyse(self, test_name):
        collection = self._mongo_db.scenarios
        scenario_keys = self._redis_connection.keys(
            test_name + ':scenarios:*'
        )

        # scenarios_list = []
        for scenario_key in scenario_keys:
            scenario_tmp_info = self._redis_connection.get(
                scenario_key
            )

            scenario_path = scenario_key.replace(
                test_name + ':scenarios:',
                ''
            )

            scenario_info = {
                'scenario_path': scenario_path,
                'test_name': test_name,
                'scenario_details': scenario_tmp_info
            }

            collection.update_one(
                {
                    'test_name': test_name,
                    'scenario_path': scenario_path
                }, {
                    '$set': scenario_info
                },
                upsert=True
            )

    def _test_cases_analyse(self, test_name):
        collection = self._mongo_db.scenario_details
        case_keys = self._redis_connection.keys(
            test_name + ':scenario_details:*'
        )

        # scenarios_list = []
        for case_key in case_keys:
            scenario_details = self._redis_connection.get(
                case_key
            )

            scenario_details = {
                'scenario_path': case_key.replace(
                    test_name + ':scenario_details:',
                    ''
                ),
                'test_name': test_name,
                'scenario_details': scenario_details
            }

            collection.update_one(
                {
                    'test_name': test_name,
                    'scenario_path': case_key.replace(
                        test_name + ':scenario_details:',
                        ''
                    )
                }, {
                    '$set': scenario_details
                },
                upsert=True
            )

    def _clean_redis_namespace(self, test_name):
        namespace = test_name + ':*'
        namespace_keys = self._redis_connection.keys(namespace)

        for namespace_key in namespace_keys:
            self._redis_connection.delete(namespace_key)
