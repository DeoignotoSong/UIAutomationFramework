# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Core.Global import Data,DataBaseName

from Core.Assert import Assert
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_add_abroad_service import console_add_abroad_service
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_pack_draft import console_abroad_pro_pack_draft
from Projects.PC.TestCases.Console.Admin.console_audit_abroad_ser_pass import console_audit_abroad_ser_pass
from Projects.PC.TestCases.Console.Admin.console_abroad_pro_draft_del import console_abroad_pro_draft_del

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB
from Core.ConfigOperation import ConfigOperation
from DB.DBFactory import DBFactory
@test_scenario()
def ConsoleProductPackDraftDel(*args, **kwargs):
    """
    后台登录-商品包装-删除
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
    data = Data.TEST_DATA['ConsoleProductPackDraftDel']
    """
    service_sql = 'SELECT is_enabled FROM '+DataBaseName.DATABASE_NAME['dxz_biz_abroad']+'.dxz_abroad_pack_service WHERE service_name = "自动化服务误删";'
    service_sql_result = mysql.execute_select_sql(service_sql)
    if service_sql_result[0]['is_enabled'] == 0:
        modify_sql = 'UPDATE '+DataBaseName.DATABASE_NAME['dxz_biz_abroad']+'.dxz_abroad_pack_service SET is_enabled=1 WHERE service_name = "自动化服务误删";'

        mysql.execute_modify_sql(modify_sql)
    """
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 商品保存
    capp = console_abroad_pro_pack_draft(*args, **kwargs)
    # 商品删除
    capdp= console_abroad_pro_draft_del(*args, **kwargs)
