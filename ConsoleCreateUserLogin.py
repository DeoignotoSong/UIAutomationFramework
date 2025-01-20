# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_create_user import console_create_user
from Projects.PC.TestCases.User.Common.user_login import user_login

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ConsoleCreateUserLogin(*args, **kwargs):
    """
    后台登录-后台创建用户-用户登录
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
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 后台新增用户
    ccu = console_create_user(*args, **kwargs)
    # 普通用户登录
    ul = user_login(*args, **kwargs)

