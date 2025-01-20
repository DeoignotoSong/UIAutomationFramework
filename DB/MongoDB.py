# -*- encoding: utf-8 -*-
import pymongo
from DB.DBOperation import DBOperation
from Utils.Log import log


class MongoDB(DBOperation):
    def __init__(self, config, env):
        section_name = env.upper() + '.' + 'Mongo'
        self.__connection__ = None
        self.__collections__ = None
        self.__host__ = config.get(section_name, 'host')
        self.__username__ = config.get(section_name, 'username')
        self.__password__ = config.get(section_name, 'password')
        self.__database__ = config.get(section_name, 'database')
        self.__init_connection__()

    def __del__(self):
        if self.__connection__ is not None:
            self.__connection__.close()

    def __init_connection__(self):
        self.__connection__ = pymongo.MongoClient(
            'mongodb://{}:{}@{}'.format(
                self.__username__,
                self.__password__,
                self.__host__
            )
        )

        self.__collections__ = self.__connection__[self.__database__]

    def find_one(self, collection, condition=''):
        log(collection)
        log(condition)
        result = self.__collections__[collection].find_one(condition)

        if result is None:
            return_value = {}
        else:
            return_value = result

        return return_value

    def find(self, collection, condition=None):
        log(collection)
        log(condition)
        if condition is None:
            condition = {}

        return_value = []
        result = self.__collections__[collection].find(condition)

        for document in result:
            return_value.append(document)

        return return_value

    def update(self, collection, condition, value):
        log(collection)
        log(condition)
        log(value)
        return_value = []
        result = self.__collections__[collection].update(
            condition,
            value
        )

        return_value.append(result)

        return return_value
