# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Core.Global import Data,DataBaseName

from Core.Assert import Assert
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.Console.Admin.console_abroad_product_pack import console_abroad_product_pack
from Projects.PC.TestCases.Console.Admin.console_add_abroad_service import console_add_abroad_service
from Projects.PC.TestCases.Console.Admin.console_audit_abroad_ser_pass import console_audit_abroad_ser_pass
from Projects.PC.TestCases.User.Common.search_product import search_product
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_audit_pass import console_abroad_pro_audit_pass
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_upper import console_abroad_pro_upper
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_up_ad_pass import console_abroad_pro_up_ad_pass
from Projects.PC.TestCases.Console.Admin.console_audit_abroad_ser_ban import console_audit_abroad_ser_ban

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB

@test_scenario()
def UserSearchProductServiceBan(*args, **kwargs):
    """
    后台登录-创建服务-服务审核-商品包装-商品审核通过-商品上架-上架审核通过-综搜商品-商品服务禁用-综搜商品
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
    data = Data.TEST_DATA['UserSearchProductServiceBan']
    # 选校数量1、服务5
    service_sql = 'DELETE FROM '+DataBaseName.DATABASE_NAME['dxz_biz_abroad']+'.dxz_abroad_pack_service WHERE unique_no = "7c5fcec104b58db69569bb30db48db90";'
    delete_service_sql_result = mysql.execute_modify_sql(service_sql)
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
    capu = console_abroad_pro_upper(*args, **kwargs)
    # 商品上架审核通过
    capuap = console_abroad_pro_up_ad_pass(*args, **kwargs)
    # 用户登录
    ul = user_login(*args, **kwargs)
    # 搜索商品
    sp = search_product(*args, **kwargs)
    Assert.is_equal(capp['packed_product_name'],sp['search_product_title'])
    # 服务禁用
    caasb = console_audit_abroad_ser_ban(*args, **kwargs)
    # 搜索商品
    sp1 = search_product(*args, **kwargs)
    Assert.is_not_equal(capp['packed_product_name'],sp1['search_product_title'])
