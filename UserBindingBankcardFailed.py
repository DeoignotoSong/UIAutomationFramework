# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Projects.PC.TestCases.User.Common.user_register import user_register
from Projects.PC.TestCases.User.User.user_real_name_authentication import user_real_name_authentication
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Common.user_binding_bankcard_failed import user_binding_bankcard_failed

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserBindingBankcardFailed(*args, **kwargs):
    """
    用户注册-进入我的中心页-实名认证-绑定银行卡失败
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
    # 用户注册
    ur = user_register(*args, **kwargs)
    # 进入我的中心页
    gtuc = go_to_user_center(*args, **kwargs)
    # 实名认证
    urna = user_real_name_authentication(*args, **kwargs)
    # 绑定银行卡失败
    ubbf = user_binding_bankcard_failed(*args, **kwargs)

