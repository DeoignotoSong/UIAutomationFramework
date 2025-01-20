# -*- encoding: utf-8 -*-
import pymysql
from DB.DBOperation import DBOperation
from Utils.Log import log


class MysqlDB(DBOperation):
    def __init__(self, config, env):
        section_name = env.upper() + '.' + 'Mysql'
        self.__host__ = config.get(section_name, 'host')
        self.__port__ = int(config.get(section_name, 'port'))
        self.__username__ = config.get(section_name, 'username')
        self.__password__ = config.get(section_name, 'password')
        #self.__database__ = config.get(section_name, 'database')
        self.connection = self.__connection__()
        self.cursor = None

    def __connection__(self):
        self.connection = pymysql.connect(host=self.__host__,
                                          port=self.__port__,
                                          user=self.__username__,
                                          password=self.__password__,
                                          #db=self.__database__,
                                          charset='utf8',
                                          cursorclass=pymysql.cursors.DictCursor)

        return self.connection

    def __cursor_close__(self):
        if self.cursor is not None:
            self.cursor.close()

    def __connection_close__(self):
        self.connection.close()

    def execute_select_sql(self, sql):

        # try:
        #     self.connection.ping()
        #     # print('数据库连接正常')
        # except Exception:
        #     # print('数据库连接断开，重新连接')
        #     self.__connection__()

        self.connection.ping()
        self.cursor = self.connection.cursor()
        log(sql)
        self.cursor.execute(sql)

        result = self.cursor.fetchall()

        self.__cursor_close__()

        if len(result) > 0:
            return_value = result
        else:
            return_value = []

        return return_value

    def execute_modify_sql(self, sql):

        # try:
        #     self.connection.ping()
        #     # print('数据库连接正常')
        # except Exception:
        #     # print('数据库连接断开，重新连接')
        #     self.__connection__()

        self.connection.ping()
        result = []
        modify_row = {}

        self.cursor = self.connection.cursor()
        log(sql)
        self.cursor.execute(sql)

        modify_row['result'] = self.cursor.execute(sql)
        result.append(modify_row)
        print(modify_row)
        print(result)
        self.connection.commit()

        self.__cursor_close__()

        return result

    def get_db_thread_id(self):
        return self.connection.thread_id()
