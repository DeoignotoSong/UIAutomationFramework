# -*- encoding: utf-8 -*-
import datetime

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data,DataBaseName
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Housekeeper.keeper_login import keeper_login
from Projects.PC.TestCases.User.Teacher.user_search_contract import user_search_contract
from Projects.PC.TestCases.User.Housekeeper.check_select_school import check_select_school
from Projects.PC.TestCases.User.Teacher.user_select_school import user_select_school
from Projects.PC.TestCases.User.Teacher.user_create_contract import user_create_contract
from Projects.PC.TestCases.User.User.user_sign_contract import user_sign_contract
from Projects.PC.TestCases.User.Common.user_logout import user_logout

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ContractGenerateOrderAndSchool(*args, **kwargs):
    """
    顾问登录大学长-创建合同-用户签署-管家选校
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
    data = Data.TEST_DATA['ContractGenerateOrderAndSchool']
    # 顾问登录
    ul = user_login(*args, **kwargs)
    # 顾问创建合同
    ucc = user_create_contract(*args, **kwargs)
    # 退出登录
    ulo = user_logout(*args, **kwargs)
    # 用户登录
    ul1 = user_login(*args, **kwargs)
    # 用户签署
    usc = user_sign_contract(*args, **kwargs)
    # 退出登录
    ulo1 = user_logout(*args, **kwargs)
    # 顾问登录
    ul1 = user_login(*args, **kwargs)
    # 顾问选校
    uss = user_select_school(*args, **kwargs)
    #Assert.is_equal('合同发送成功',uss['success_message'])
    # 管家登录
    kl = keeper_login(*args, **kwargs)
    # 合同管理
    usco = user_search_contract(*args, **kwargs)
    Assert.is_equal(ucc['contract_id'],usco['contract_id'])
    Assert.is_equal(usc['order_no'],usco['order_id'])
    Assert.is_equal('已签署',usco['contract_status'])
    Assert.is_equal('',usco['check_select_school'])
    Assert.is_equal('查看合同',usco['check_contract_text'])
    Assert.is_equal('徐**',usco['client_name'])
    string = list(ucc['client_name'])
    for num in range(3,7):
        string[num]='*'
    client_mobile = ''.join(string)
    Assert.is_equal(client_mobile,usco['client_mobile'])
    Assert.is_equal(usc['sign_time'],usco['contract_sign_time'])
    # 查看选校确认书
    css = check_select_school(*args, **kwargs)
    Assert.is_equal(uss['contract_id'],css['contract_id'])


