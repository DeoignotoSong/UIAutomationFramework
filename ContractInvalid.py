# -*- encoding: utf-8 -*-
import datetime

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data,DataBaseName
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Housekeeper.keeper_login import keeper_login
from Projects.PC.TestCases.User.Teacher.user_search_contract import user_search_contract
from Projects.PC.TestCases.User.Housekeeper.check_contract import check_contract
from Projects.PC.TestCases.User.Teacher.user_create_contract import user_create_contract

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ContractInvalid(*args, **kwargs):
    """
    顾问登录大学长-创建合同-管家登录-合同管理检查-无效合同
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
    data = Data.TEST_DATA['ContractInvalid']
    # 顾问登录
    ul = user_login(*args, **kwargs)
    # 顾问创建合同
    ucc = user_create_contract(*args, **kwargs)
    # 管家登录
    kl = keeper_login(*args, **kwargs)
    # 合同时间修改
    deadline = datetime.datetime.now()
    create = (deadline + datetime.timedelta(days=-14)).strftime("%Y-%m-%d %H:%M:%S")
    deadline = deadline.strftime("%Y-%m-%d %H:%M:%S")
    update_time_sql = 'UPDATE ' + DataBaseName.DATABASE_NAME['dxz_m_abroad'] + '.dxz_contract SET send_time="{}",sign_end_time="{}" WHERE contract_no="{}"'.format(create,deadline,ucc['contract_id'])
    sql_result = mysql.execute_modify_sql(update_time_sql)
    # 合同管理
    usc = user_search_contract(*args, **kwargs)
    Assert.is_equal(ucc['contract_id'],usc['contract_id'])
    Assert.is_equal('',usc['order_id'])
    Assert.is_equal('',usc['contract_sign_time'])
    Assert.is_equal('',usc['check_select_school'])



