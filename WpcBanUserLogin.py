# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data,DataBaseName
from Projects.PC.TestCases.Console.Housekeeper.console_logout import console_logout
from Projects.PC.TestCases.Console.Housekeeper.console_login import console_login
from Projects.PC.TestCases.Console.Housekeeper.console_ban_user import console_ban_user
from Projects.PC.TestCases.Console.Housekeeper.console_ban_login import console_ban_login
from Projects.PC.TestCases.Console.Housekeeper.console_add_user import console_add_user

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB
@test_scenario()
def WpcBanUserLogin(*args, **kwargs):
    """
    学长管家后台登录-新增用户-禁用用户-禁用用户登录-用户解禁-解禁用户登录
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
    # data
    data = Data.TEST_DATA['WpcBanUserLogin']
    # 学长管家后台登录
    cl = console_login(*args, **kwargs)
    # 新增用户
    cau = console_add_user(*args, **kwargs)
    # 后台禁用用户
    cbu = console_ban_user(*args, **kwargs)
    Assert.is_equal('启用', cbu['pre_state'])
    Assert.is_equal('禁用', cbu['done_state'])
    # 后台登出
    clo = console_logout(*args, **kwargs)
    # 新增用户登录
    cl1 = console_ban_login(*args, **kwargs)
    error_message = '对不起，您的账号：'+cau['account']+' 已停用'
    Assert.is_equal(error_message,cl1['error_message'])
    # 学长管家后台登录
    cl2 = console_login(*args, **kwargs)
    # 用户解禁
    cbu1 = console_ban_user(*args, **kwargs)
    Assert.is_equal('禁用', cbu1['pre_state'])
    Assert.is_equal('启用', cbu1['done_state'])
    # 后台登出
    clo1 = console_logout(*args, **kwargs)
    # 解禁用户登录
    cl3 = console_login(*args, **kwargs)

