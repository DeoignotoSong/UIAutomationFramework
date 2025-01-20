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
def ContractListNoData(*args, **kwargs):
    """
    管家登录-合同管理搜索-无数据
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
    data = Data.TEST_DATA['ContractListNoData']
    # 管家登录
    kl = keeper_login(*args, **kwargs)
    # 合同管理
    usc = user_search_contract(*args, **kwargs)
    Assert.is_equal('暂无数据',usc['no_data'])



