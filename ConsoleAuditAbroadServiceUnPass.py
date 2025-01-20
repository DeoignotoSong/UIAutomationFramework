# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data

from Core.Assert import Assert
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_add_abroad_service import console_add_abroad_service
from Projects.PC.TestCases.Console.Admin.console_audit_abroad_ser_unpass import console_audit_abroad_ser_unpass
from Projects.PC.TestCases.Console.Admin.console_audit_abroad_ser_check import console_audit_abroad_ser_check

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ConsoleAuditAbroadServiceUnPass(*args, **kwargs):
    """
    后台登录-创建服务-审核服务不通过
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
    data = Data.TEST_DATA['ConsoleAuditAbroadServiceUnPass']
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 创建服务
    ccrp = console_add_abroad_service(*args, **kwargs)
    # 审核不通过
    caasp = console_audit_abroad_ser_unpass(*args, **kwargs)
    # 审核详情页
    caasc = console_audit_abroad_ser_check(*args, **kwargs)
    Assert.is_equal(ccrp['service_name'],caasc['servicename'])
    Assert.is_equal(ccrp['first_category'],caasc['first_category'])
    Assert.is_equal(ccrp['third_category'], caasc['third_category'])
    Assert.is_equal('审核未通过', caasc['audit_state'])
    Assert.is_equal(ccrp['school_number'],caasc['number'])