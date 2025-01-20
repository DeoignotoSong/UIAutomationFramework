# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Core.Global import Data,DataBaseName

from Core.Assert import Assert
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.Console.Admin.console_abroad_product_pack import console_abroad_product_pack
from Projects.PC.TestCases.User.Common.search_product import search_product
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_audit_pass import console_abroad_pro_audit_pass
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_upper import console_abroad_pro_upper
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_up_ad_pass import console_abroad_pro_up_ad_pass
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_pack_hide import console_abroad_pro_pack_hide

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB

@test_scenario()
def UserSearchProductHide(*args, **kwargs):
    """
    后台登录-商品包装-商品审核通过-商品上架-上架审核通过-综搜商品-商品前台隐藏-综搜商品
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
    data = Data.TEST_DATA['UserSearchProductHide']
    service_sql = 'SELECT is_enabled FROM '+DataBaseName.DATABASE_NAME['dxz_biz_abroad']+'.dxz_abroad_pack_service WHERE service_name = "自动化服务误删";'
    service_sql_result = mysql.execute_select_sql(service_sql)
    if service_sql_result[0]['is_enabled'] == 0:
        modify_sql = 'UPDATE '+DataBaseName.DATABASE_NAME['dxz_biz_abroad']+'.dxz_abroad_pack_service SET is_enabled=1 WHERE service_name = "自动化服务误删";'
        mysql.execute_modify_sql(modify_sql)
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
    # 用户登录
    ul = user_login(*args, **kwargs)
    # 搜索商品
    sp = search_product(*args, **kwargs)
    Assert.is_equal(capp['packed_product_name'],sp['search_product_title'])
    # 前台隐藏
    capph = console_abroad_pro_pack_hide(*args, **kwargs)
    # 搜索商品
    sp1 = search_product(*args, **kwargs)
    Assert.is_not_equal(capp['packed_product_name'],sp1['search_product_title'])
