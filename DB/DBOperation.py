from abc import ABCMeta, abstractmethod


class DBOperation(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __connection__(self): pass

    @abstractmethod
    def __close__(self): pass

    @abstractmethod
    def execute_select_sql(self, sql): pass
