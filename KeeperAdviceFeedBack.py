# -*- encoding: utf-8 -*-
import datetime

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data,DataBaseName
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Housekeeper.keeper_login import keeper_login
from Projects.PC.TestCases.Console.Housekeeper.console_advice_feedback_deal import console_advice_feedback_deal
from Projects.PC.TestCases.User.Housekeeper.keeper_feedback import keeper_feedback
from Projects.PC.TestCases.User.Teacher.user_create_contract import user_create_contract
from Projects.PC.TestCases.User.User.user_sign_contract import user_sign_contract
from Projects.PC.TestCases.User.Common.user_logout import user_logout
from Projects.PC.TestCases.Console.Housekeeper.console_login import console_login

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def KeeperAdviceFeedBack(*args, **kwargs):
    """
    管家登录-意见反馈
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
    data = Data.TEST_DATA['KeeperAdviceFeedBack']
    # 管家登录
    kl = keeper_login(*args, **kwargs)
    # 意见反馈
    kf = keeper_feedback(*args, **kwargs)
    # 学长管家后台登录
    cl = console_login(*args, **kwargs)
    # 学长管家处理意见反馈
    cafd = console_advice_feedback_deal(*args, **kwargs)
    Assert.is_equal('待处理',cafd['deal_before_status'])
    Assert.is_equal('已处理',cafd['deal_after_status'])
    Assert.is_equal('none',cafd['option'])




