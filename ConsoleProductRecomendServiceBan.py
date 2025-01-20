# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data,DataBaseName

from Core.Assert import Assert
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_abroad_ser_ban_unpass import console_abroad_ser_ban_unpass

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ConsoleProductRecomendServiceBan(*args, **kwargs):
    """
    后台登录-推荐位商品服务禁用
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

    data = Data.TEST_DATA['ConsoleProductRecomendServiceBan']
    service_sql = 'SELECT is_enabled FROM '+DataBaseName.DATABASE_NAME['dxz_biz_abroad']+'.dxz_abroad_pack_service WHERE service_name = "自动化PCUI推荐位商品服务";'
    # service_sql = 'DELETE FROM dxz_abroad_pack_service WHERE unique_no = "1c571481134743cf431e2f3dadee3f49";'
    service_sql_result = mysql.execute_select_sql(service_sql)
    if service_sql_result[0]['is_enabled'] == 0:
        modify_sql = 'UPDATE '+DataBaseName.DATABASE_NAME['dxz_biz_abroad']+'.dxz_abroad_pack_service SET is_enabled=1 WHERE service_name = "自动化PCUI推荐位商品服务";'
        mysql.execute_modify_sql(modify_sql)
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 推荐位商品服务禁用
    caasb = console_abroad_ser_ban_unpass(*args, **kwargs)
    Assert.is_equal('该服务所包装的商品已被推荐位引用，不能禁用该服务，若想禁用服务，请先去推荐位管理中取消该服务所包装的商品的设置。',caasb['message'])


