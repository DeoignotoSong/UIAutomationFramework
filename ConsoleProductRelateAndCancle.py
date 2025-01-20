# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data

from Core.Assert import Assert
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_pack_relate import console_abroad_pro_pack_relate
from Projects.PC.TestCases.Console.Admin.console_abr_pro_cancle_relat import console_abr_pro_cancle_relat
from Projects.PC.TestCases.User.Common.search_product import search_product

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ConsoleProductRelateAndCancle(*args, **kwargs):
    """
    后台登录-关联商品-取消关联
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
    data = Data.TEST_DATA['ConsoleProductRelateAndCancle']
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 商品关联
    cappr = console_abroad_pro_pack_relate(*args, **kwargs)
    # 综搜页面关联商品展示
    sp = search_product(*args, **kwargs)
    Assert.is_equal(cappr['relproductname'],sp['recommend_title'])
    # 商品取消关联
    capar = console_abr_pro_cancle_relat(*args, **kwargs)
    # 综搜页面关联商品展示
    sp1 = search_product(*args, **kwargs)
    Assert.is_not_equal(cappr['relproductname'], sp1['recommend_title'])
