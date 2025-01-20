# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data

from Core.Assert import Assert
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Common.check_abroad_product_8 import check_abroad_product_8

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserAbroadProCheck8(*args, **kwargs):
    """
    后台登录-留学产品8个商品1个广告位
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
    data = Data.TEST_DATA['UserAbroadProCheck8']
    # 后台登录
    ul = user_login(*args, **kwargs)
    # 留学产品8个商品1个广告位
    cap = check_abroad_product_8(*args, **kwargs)
    Assert.is_equal('card',cap['first_class'])
    Assert.is_equal('card', cap['second_class'])
    Assert.is_equal('card', cap['third_class'])
    Assert.is_equal('card', cap['fourth_class'])
    Assert.is_equal('card', cap['fifth_class'])
    Assert.is_equal('card', cap['six_class'])
    Assert.is_equal('card', cap['seven_class'])
    Assert.is_equal('card', cap['eight_class'])
    Assert.is_equal('list-advert', cap['nine_class'])