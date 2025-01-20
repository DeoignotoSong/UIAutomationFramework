# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data,DataBaseName
from Projects.PC.TestCases.User.Common.user_register import user_register
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_ban_user import console_ban_user
from Projects.PC.TestCases.User.Common.user_ban_login import user_ban_login
from Projects.PC.TestCases.User.Common.user_logout import user_logout

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB
@test_scenario()
def ConsoleBanUserLogin(*args, **kwargs):
    """
    用户注册-后台登录-禁用用户-禁用用户登录-用户解禁
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
    data = Data.TEST_DATA['ConsoleBanUserLogin']
    # 用户注册
    ur = user_register(*args, **kwargs)
    # 用户登出
    ulo = user_logout(*args, **kwargs)
    # 后台登录
    cl = console_login(*args, **kwargs)
    try:
        # 后台禁用用户
        cbu = console_ban_user(*args, **kwargs)
        Assert.is_equal('正常', cbu['pre_state'])
        Assert.is_equal('禁用', cbu['done_state'])
        # 禁用用户登录
        ubl = user_ban_login(*args, **kwargs)
        # 用户解禁
        cbu2 = console_ban_user(*args, **kwargs)
        Assert.is_equal('禁用', cbu2['pre_state'])
        Assert.is_equal('正常', cbu2['done_state'])
    finally:
        reset_sql = 'UPDATE '+DataBaseName.DATABASE_NAME['dxz_lan']+'.dxz_user SET status = 0 WHERE mobile = "{}"'.format(data['user_register']['In']['mobile'])

        mysql.execute_modify_sql(reset_sql)
