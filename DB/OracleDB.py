import os
# import cx_Oracle
from Core.ConfigOperation import ConfigOperation
from DB.DBOperation import DBOperation


# 配置instant client环境变量
# os.environ['path'] = os.getcwd() + '\\venv\\OtherTools\\instantclient;' + os.environ['path']


class OracleDB(DBOperation):
    def __init__(self, config_path=None):
        config = ConfigOperation().load_config(config_path)

        self.__username__ = config.get('Oracle', 'username')
        self.__password__ = config.get('Oracle', 'password')
        self.__host__ = config.get('Oracle', 'host')
        self.__port__ = int(config.get('Oracle', 'port'))
        self.__server_name__ = config.get('Oracle', 'server')
        self.cursor = None
        self.db = None

    def __connection__(self):
        # tns = cx_Oracle.makedsn(self.__host__, self.__port__, self.__server_name__)
        # db = cx_Oracle.connect(self.__username__, self.__password__, tns)

        # self.db = db
        # self.cursor = db.cursor()
        pass

    def __close__(self):
        if self.cursor is not None:
            self.cursor.close()

        if self.cursor is not None:
            self.db.close()

    def execute_select_sql(self, sql):
        keys = []
        result_set = []
        self.__connection__()

        sql_result = self.cursor.execute(sql)

        for item in self.cursor.description:
            keys.append(item[0])

        for item in sql_result.fetchall():
            line = {}
            for i in range(0, len(keys)):
                line[keys[i]] = item[i]
            result_set.append(line)

        self.__close__()

        return result_set
