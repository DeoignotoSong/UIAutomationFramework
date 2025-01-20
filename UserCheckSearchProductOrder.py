# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data

from Core.Assert import Assert
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Common.check_search_product_order import check_search_product_order

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserCheckSearchProductOrder(*args, **kwargs):
    """
    登录-综搜产品按照价格排序-按照热度排序
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
    data = Data.TEST_DATA['UserCheckSearchProductOrder']
    # 登录
    ul = user_login(*args, **kwargs)
    # 草稿箱不可点击
    cspo = check_search_product_order(*args, **kwargs)


