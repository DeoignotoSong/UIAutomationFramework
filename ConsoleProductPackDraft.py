# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Core.Global import Data,DataBaseName

from Core.Assert import Assert
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_add_abroad_service import console_add_abroad_service
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_pack_draft import console_abroad_pro_pack_draft
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_draft_pack import console_abroad_pro_draft_pack
from Projects.PC.TestCases.Console.Admin.console_audit_abroad_ser_pass import console_audit_abroad_ser_pass

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB

@test_scenario()
def ConsoleProductPackDraft(*args, **kwargs):
    """
    后台登录-商品包装-保存到草稿-商品包装
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
    data = Data.TEST_DATA['ConsoleProductPackDraft']
    """
    service_sql = 'SELECT is_enabled FROM '+DataBaseName.DATABASE_NAME['dxz_biz_abroad']+'.dxz_abroad_pack_service WHERE service_name = "自动化服务误删";'
    # service_sql = 'DELETE FROM dxz_lan.dxz_abroad_pack_service WHERE unique_no = "1c571481134743cf431e2f3dadee3f49";'
    service_sql_result = mysql.execute_select_sql(service_sql)
    if service_sql_result[0]['is_enabled'] == 0:
        modify_sql = 'UPDATE '+DataBaseName.DATABASE_NAME['dxz_biz_abroad']+'.dxz_abroad_pack_service SET is_enabled=1 WHERE service_name = "自动化服务误删";'

        mysql.execute_modify_sql(modify_sql)
    """
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 商品保存
    capp = console_abroad_pro_pack_draft(*args, **kwargs)
    # 商品包装
    capdp= console_abroad_pro_draft_pack(*args, **kwargs)
