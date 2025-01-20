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
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_upper_modify import console_abroad_pro_upper_modify
from Projects.PC.TestCases.Console.Admin.console_check_goods_up_state import console_check_goods_up_state

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB
from Core.ConfigOperation import ConfigOperation
from DB.DBFactory import DBFactory
@test_scenario()
def ConsoleProductPackExceedUpper(*args, **kwargs):
    """
    后台登录-商品包装-商品审核通过-商品定时上架-超过上架时间-修改-超过下架时间
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
    data = Data.TEST_DATA['ConsoleProductPackExceedUpper']
    """
    service_sql = 'SELECT is_enabled FROM '+DataBaseName.DATABASE_NAME['dxz_biz_abroad']+'.dxz_abroad_pack_service WHERE service_name = "自动化服务误删";'
    service_sql_result = mysql.execute_select_sql(service_sql)
    if service_sql_result[0]['is_enabled'] == 0:
        modify_sql = 'UPDATE '+DataBaseName.DATABASE_NAME['dxz_biz_abroad']+'.dxz_abroad_pack_service SET is_enabled=1 WHERE service_name = "自动化服务误删";'

        mysql.execute_modify_sql(modify_sql)
    """
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 商品打包
    capp = console_abroad_product_pack(*args, **kwargs)
    # 商品审核通过
    capap = console_abroad_pro_audit_pass(*args, **kwargs)
    # 商品上架
    captu = console_abroad_pro_timing_upper(*args, **kwargs)
    #project.wait(1)
    # 检查商品上架状态
    ccgss = console_check_goods_up_state(*args, **kwargs)
    Assert.is_equal(capp['packed_product_name'],ccgss['productname'])
    Assert.is_equal('定时上架',ccgss['shelf_method'])
    Assert.is_equal('审核未通过',ccgss['audit_state'])
    Assert.is_equal('修改',ccgss['lower_text'])
    Assert.is_equal('审核记录',ccgss['audit_his'])
    Assert.is_equal('审核未通过',ccgss['audit_result'])
    Assert.is_equal('审核逾期，系统自动驳回',ccgss['reject_reason'])
    capum = console_abroad_pro_upper_modify(*args, **kwargs)
    project.wait(1)
    # 检查商品上架状态
    ccgss1 = console_check_goods_up_state(*args, **kwargs)
    Assert.is_equal(capp['packed_product_name'], ccgss1['productname'])
    Assert.is_equal('定时上架', ccgss1['shelf_method'])
    Assert.is_equal('审核未通过', ccgss1['audit_state'])
    Assert.is_equal('修改', ccgss1['lower_text'])
    Assert.is_equal('审核记录', ccgss1['audit_his'])
    Assert.is_equal('审核未通过', ccgss1['audit_result'])
    Assert.is_equal('审核逾期，系统自动驳回', ccgss1['reject_reason'])
