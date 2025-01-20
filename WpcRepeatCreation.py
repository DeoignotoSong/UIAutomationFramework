# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data,DataBaseName
from Projects.PC.TestCases.Console.Housekeeper.console_add_repeat_user import console_add_repeat_user
from Projects.PC.TestCases.Console.Housekeeper.console_login import console_login
from Projects.PC.TestCases.Console.Housekeeper.console_add_user import console_add_user

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB

@test_scenario()
def WpcRepeatCreation(*args, **kwargs):
    """
    学长管家后台重复注册
    :param args:
        0: ProjectBase
        1: mysql
        2: mongo
    :param kwargs:
    :return:
    """
    project = args[0]  # type: ProjectBase
    mysql = args[1]  # type: MysqlDB
    mongo = args[2]  # type: MongoDB
    # 初始化文件
    data = Data.TEST_DATA['WpcRepeatCreation']
    # 学长管家后台登录
    cl = console_login(*args, **kwargs)
    # 新增用户
    cau = console_add_user(*args, **kwargs)
    # 新增重复用户
    cau = console_add_repeat_user(*args, **kwargs)



