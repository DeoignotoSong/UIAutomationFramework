# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Common.user_publish_qa_with_bounty import user_publish_qa_with_bounty
from Projects.PC.TestCases.Common.alipay import alipay
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Common.user_check_publish_qa import user_check_publish_qa

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserPublishQaWithBounty(*args, **kwargs):
    """
    用户注册-首页-发布悬赏问答-进入个人中心页-问答管理-查看发布的问答
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
    data = Data.TEST_DATA['UserPublishQaWithBounty']
    # 用户登录
    ul = user_login(*args, **kwargs)
    # # 发布问答
    # upqwb = user_publish_qa_with_bounty(*args, **kwargs)
    # # 支付宝支付
    # ali_pay = alipay(*args, **kwargs)
    # # 进入我的中心页
    # gtuc = go_to_user_center(*args, **kwargs)
    # # 问答管理查看发布的问答
    # ucpq = user_check_publish_qa(*args, **kwargs)
    # Assert.is_containing(data['user_publish_qa_with_bounty']['In']['title'], ucpq['qa_title'])
