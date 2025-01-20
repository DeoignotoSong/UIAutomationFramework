# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Core.Global import Data,DataBaseName

from Core.Assert import Assert
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_add_abroad_service import console_add_abroad_service
from Projects.PC.TestCases.Console.Admin.console_abroad_product_pack import console_abroad_product_pack
from Projects.PC.TestCases.Console.Admin.console_audit_abroad_ser_pass import console_audit_abroad_ser_pass
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_audit_pass import console_abroad_pro_audit_pass
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_timing_upper import console_abroad_pro_timing_upper
from Projects.PC.TestCases.Console.Admin.console_audit_abroad_ser_ban import console_audit_abroad_ser_ban
from Projects.PC.TestCases.Console.Admin.console_check_goods_up_state import console_check_goods_up_state
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_up_ad_pass import console_abroad_pro_up_ad_pass

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB
import hashlib
@test_scenario()
def ConsoleProductAuditUpperServiceBan(*args, **kwargs):
    """
    后台登录-创建服务-审核服务-商品包装-商品审核通过-商品定时上架-审核通过-服务禁用
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
    data = Data.TEST_DATA['ConsoleProductAuditUpperServiceBan']
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 创建服务
    cabs = console_add_abroad_service(*args, **kwargs)
    # 审核服务通过
    caasp = console_audit_abroad_ser_pass(*args, **kwargs)
    # 商品打包
    capp = console_abroad_product_pack(*args, **kwargs)
    # 商品审核通过
    capap = console_abroad_pro_audit_pass(*args, **kwargs)
    # 商品上架
    capu = console_abroad_pro_timing_upper(*args, **kwargs)
    # 商品上架审核通过
    capuap = console_abroad_pro_up_ad_pass(*args, **kwargs)
    # 服务禁用
    caasb = console_audit_abroad_ser_ban(*args, **kwargs)
    # 检查商品上架状态
    ccgss = console_check_goods_up_state(*args, **kwargs)
    Assert.is_equal(capp['packed_product_name'],ccgss['productname'])
    Assert.is_equal('定时上架',ccgss['shelf_method'])
    Assert.is_equal('审核通过',ccgss['audit_state'])
    Assert.is_equal('服务下架',ccgss['upper_state'])
    Assert.is_equal('审核记录',ccgss['audit_his'])
    Assert.is_equal('审核通过',ccgss['audit_result'])
    Assert.is_equal('',ccgss['reject_reason'])
