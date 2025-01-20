# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data

from Core.Assert import Assert
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_set_check import console_abroad_pro_set_check

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ConsoleAbroadProSetCheck(*args, **kwargs):
    """
    后台登录-上架管理-不可点击
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
    data = Data.TEST_DATA['ConsoleAbroadProSetCheck']
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 上架管理
    ccrp = console_abroad_pro_set_check(*args, **kwargs)


