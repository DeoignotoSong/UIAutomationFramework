# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Projects.PC.TestCases.User.Common.user_register import user_register
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Common.user_sign_get_point import user_sign_get_point

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserSignGetPoint(*args, **kwargs):
    """
    用户注册-签到
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
    # 签到
    usgp = user_sign_get_point(*args, **kwargs)

