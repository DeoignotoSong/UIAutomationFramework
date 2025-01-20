# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data

from Core.Assert import Assert
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_abroad_bat_lower import console_abroad_bat_lower
from Projects.PC.TestCases.Console.Admin.console_abroad_product_pack import console_abroad_product_pack
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_up_ad_pass import console_abroad_pro_up_ad_pass
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_audit_pass import console_abroad_pro_audit_pass
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_bat_upper import console_abroad_pro_bat_upper

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ConsoleProductBatchLower(*args, **kwargs):
    """
    后台登录-商品包装-商品审核通过-已设置批量商品立即上架-商品审核通过-已设置批量商品下架
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
    data = Data.TEST_DATA['ConsoleProductBatchLower']
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 商品打包
    capp = console_abroad_product_pack(*args, **kwargs)
    # 商品审核通过
    capap = console_abroad_pro_audit_pass(*args, **kwargs)
    # 商品打包
    capp1 = console_abroad_product_pack(*args, **kwargs)
    # 商品审核通过
    capap1 = console_abroad_pro_audit_pass(*args, **kwargs)
    # 商品批量上架
    cabtu = console_abroad_pro_bat_upper(*args, **kwargs)
    # 审核商品上架审核通过
    capuap = console_abroad_pro_up_ad_pass(*args, **kwargs)
    # 审核商品1上架审核通过
    capuap1 = console_abroad_pro_up_ad_pass(*args, **kwargs)
    # 商品已设置批量下架
    capbu = console_abroad_bat_lower(*args, **kwargs)


