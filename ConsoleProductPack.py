# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Core.Global import Data

from Core.Global import DataBaseName
from Core.Assert import Assert
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_add_abroad_service import console_add_abroad_service
from Projects.PC.TestCases.Console.Admin.console_abroad_product_pack import console_abroad_product_pack
from Projects.PC.TestCases.Console.Admin.console_audit_abroad_ser_pass import console_audit_abroad_ser_pass
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_audit_pass import console_abroad_pro_audit_pass
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_upper import console_abroad_pro_upper
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_up_ad_pass import console_abroad_pro_up_ad_pass
from Projects.PC.TestCases.Console.Admin.console_check_goods_up_state import console_check_goods_up_state

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB

@test_scenario()
def ConsoleProductPack(*args, **kwargs):
    """
    后台登录-商品包装-商品审核通过-商品上架-上架审核通过
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
    data = Data.TEST_DATA['ConsoleProductPack']
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
    capu = console_abroad_pro_upper(*args, **kwargs)
    # 商品上架审核通过
    capuap = console_abroad_pro_up_ad_pass(*args, **kwargs)
    # 检查商品上架状态
    ccgss = console_check_goods_up_state(*args, **kwargs)
    Assert.is_equal(capp['packed_product_name'],ccgss['productname'])
    Assert.is_equal('立即上架',ccgss['shelf_method'])
    Assert.is_equal('审核通过',ccgss['audit_state'])
    Assert.is_equal('已上架',ccgss['upper_state'])
    Assert.is_equal('下架',ccgss['lower_text'])
    Assert.is_equal('审核记录',ccgss['audit_his'])
