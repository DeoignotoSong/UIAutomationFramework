# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Core.Global import Data,DataBaseName

from Core.Assert import Assert
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_add_abroad_service import console_add_abroad_service
from Projects.PC.TestCases.Console.Admin.console_abroad_product_pack import console_abroad_product_pack
from Projects.PC.TestCases.Console.Admin.console_audit_abroad_ser_pass import console_audit_abroad_ser_pass
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_audit_pass import console_abroad_pro_audit_pass
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_upper import console_abroad_pro_upper
from Projects.PC.TestCases.Console.Admin.console_audit_abroad_ser_ban import console_audit_abroad_ser_ban
from Projects.PC.TestCases.Console.Admin.console_audit_abroad_ser_enable import console_audit_abroad_ser_enable

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB
from Core.ConfigOperation import ConfigOperation
from DB.DBFactory import DBFactory
@test_scenario()
def ConsoleProductServiceBanAndEnable(*args, **kwargs):
    """
    后台登录-商品包装-商品审核通过-服务禁止-服务启用-上架设置成功
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
    data = Data.TEST_DATA['ConsoleProductServiceBanAndEnable']
    # 选校数量1、服务3
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
    # 商品服务禁用
    caasb = console_audit_abroad_ser_ban(*args, **kwargs)
    # 商品上架
    capu = console_abroad_pro_upper(*args, **kwargs)
    Assert.is_equal('无操作',capu['option'])
    # 商品服务启用
    caase = console_audit_abroad_ser_enable(*args, **kwargs)
    # 商品上架
    capu1 = console_abroad_pro_upper(*args, **kwargs)
    Assert.is_equal('设置', capu1['option'])
