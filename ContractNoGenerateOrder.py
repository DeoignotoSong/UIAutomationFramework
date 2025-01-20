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
def ContractNoGenerateOrder(*args, **kwargs):
    """
    顾问登录大学长-创建合同-管家登录-合同管理检查-合同详情检查
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
    data = Data.TEST_DATA['ContractNoGenerateOrder']
    # 顾问登录
    ul = user_login(*args, **kwargs)
    # 顾问创建合同
    ucc = user_create_contract(*args, **kwargs)
    # 管家登录
    kl = keeper_login(*args, **kwargs)
    # 合同管理
    usc = user_search_contract(*args, **kwargs)
    Assert.is_equal(ucc['contract_id'],usc['contract_id'])
    Assert.is_equal('',usc['order_id'])
    user_create_sql = 'SELECT created_at FROM ' + DataBaseName.DATABASE_NAME['dxz_m_abroad'] + '.dxz_contract WHERE contract_no="{}"'.format(usc['contract_id'])
    create_time = mysql.execute_select_sql(user_create_sql)[0]['created_at']
    deadline = (create_time + datetime.timedelta(days=14)).strftime("%Y-%m-%d %H:%M")
    Assert.is_containing(deadline,usc['contract_sign_deadline'])
    Assert.is_equal('',usc['contract_sign_time'])
    Assert.is_equal('',usc['check_select_school'])
    # 查看合同详情
    cc = check_contract(*args, **kwargs)
    Assert.is_equal(usc['contract_id'],cc['contract_id'])
    Assert.is_equal('立即签署',cc['contract_status'])


