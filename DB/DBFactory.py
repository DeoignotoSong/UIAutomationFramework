# -*- encoding: utf-8 -*-
from Utils.Log import log
from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


class DBFactory(object):
    @staticmethod
    def get_db_instances(db_type, config, env):
        db_enum = {
            'mysql': MysqlDB(config, env),
            'mongo': MongoDB(config, env)
        }
        if db_type in db_enum.keys():
            db_instance = db_enum[db_type]
        else:
            db_instance = None
            log('数据库类型错误，默认选择mysql')

        return db_instance
