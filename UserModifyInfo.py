# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Core.Assert import Assert
from Projects.PC.TestCases.User.Common.user_register import user_register
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.User.user_modify_info import user_modify_info
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_check_user_info import console_check_user_info

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserModifyInfo(*args, **kwargs):
    """
    普通用户登录-进入我的中心页-修改个人信息-后台登录-后台查看用户信息
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
    data = Data.TEST_DATA['UserModifyInfo']
    # 用户注册
    ur = user_register(*args, **kwargs)
    # 进入我的中心页
    gtuc = go_to_user_center(*args, **kwargs)
    # 用户修改个人信息
    umi = user_modify_info(*args, **kwargs)
    # 后台登录
    cl = console_login(*args, **kwargs)
    Assert.is_containing('Hi', cl['console_name_content'])
    # 后台查看用户信息
    ccui = console_check_user_info(*args, **kwargs)
    Assert.is_equal(data['user_modify_info']['In']['nick'], ccui['list_nick'])
    Assert.is_equal('普通用户', ccui['list_role'])
    Assert.is_equal('正常', ccui['list_state'])
    Assert.is_equal(data['user_modify_info']['In']['nick'], ccui['edit_nick'])
    Assert.is_equal(umi['country'], ccui['edit_country'])

