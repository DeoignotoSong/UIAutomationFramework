# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data,DataBaseName

from Core.Assert import Assert
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_check_goods_up_state import console_check_goods_up_state
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_up_fail import console_abroad_pro_up_fail
from Projects.PC.TestCases.User.Common.check_abroad_recommend import check_abroad_recommend

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB
from Core.ConfigOperation import ConfigOperation
from DB.DBFactory import DBFactory
import datetime


@test_scenario()
def ConsoleProductRecomendLower(*args, **kwargs):
    """
    后台登录-商品立即下架-商品定时下架
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
    data = Data.TEST_DATA['ConsoleProductRecomendLower']
    service_sql = 'SELECT is_enabled FROM '+DataBaseName.DATABASE_NAME['dxz_biz_abroad']+'.dxz_abroad_pack_service WHERE service_name = "自动化PCUI推荐位商品服务";'
    # service_sql = 'DELETE FROM dxz_abroad_pack_service WHERE unique_no = "1c571481134743cf431e2f3dadee3f49";'
    service_sql_result = mysql.execute_select_sql(service_sql)
    if service_sql_result[0]['is_enabled'] == 0:
        modify_sql = 'UPDATE '+DataBaseName.DATABASE_NAME['dxz_biz_abroad']+'.dxz_abroad_pack_service SET is_enabled=1 WHERE service_name = "自动化PCUI推荐位商品服务";'
        mysql.execute_modify_sql(modify_sql)
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 商品立即下架
    capul = console_abroad_pro_up_fail(*args, **kwargs)
    Assert.is_equal('该商品已被推荐位引用，不能下架该商品，若想下架该商品，请先去推荐位管理中取消该商品的设置。',capul['message'])
    # 商品定时下架
    capul1 = console_abroad_pro_up_fail(*args, **kwargs)
    Assert.is_equal('该商品已被推荐位引用，不能下架该商品，若想下架该商品，请先去推荐位管理中取消该商品的设置。', capul1['message'])
    # 商品到定时下架时间
    lower_time = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
    modify_off_time_sql = 'UPDATE '+DataBaseName.DATABASE_NAME['dxz_biz_abroad']+'.dxz_abroad_product_sale SET off_sale_at=' + '"'+lower_time+'"' + ' WHERE product_no="PR020100045493";'
    mysql.execute_modify_sql(modify_off_time_sql)
    modify_off_his_sql = 'UPDATE '+DataBaseName.DATABASE_NAME['dxz_biz_abroad']+'.dxz_abroad_product_sale_his SET off_sale_at=' + '"' + lower_time + '"' + ' WHERE product_no="PR020100045493";'
    mysql.execute_modify_sql(modify_off_his_sql)
    project.wait(1)
    # 获取商品上下架状态
    ccgus = console_check_goods_up_state(*args, **kwargs)
    Assert.is_equal('已上架',ccgus['upper_state'])
    # 页面推荐位商品展示
    sp = check_abroad_recommend(*args, **kwargs)
    Assert.is_equal('自动化PCUI推荐商品',sp['title'])

