# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Projects.PC.TestCases.User.Common.user_register import user_register
from Projects.PC.TestCases.User.Common.user_browse_topic import user_browse_topic

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserBrowseTopic(*args, **kwargs):
    """
    用户注册-浏览话题
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
    data = Data.TEST_DATA['UserBrowseTopic']
    # 用户注册
    ur = user_register(*args, **kwargs)
    # 浏览话题
    ubt = user_browse_topic(*args, **kwargs)

