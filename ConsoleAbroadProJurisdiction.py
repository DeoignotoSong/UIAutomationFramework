# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data

from Core.Assert import Assert
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_jurisdiction import console_abroad_pro_jurisdiction

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ConsoleAbroadProJurisdiction(*args, **kwargs):
    """
    后台登录-权限校验
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
    data = Data.TEST_DATA['ConsoleAbroadProJurisdiction']
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 权限校验
    capj = console_abroad_pro_jurisdiction(*args, **kwargs)