# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Common.user_check_publish_qa import user_check_publish_qa
from Projects.PC.TestCases.User.User.user_publish_qa import user_publish_qa

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserPublishQa(*args, **kwargs):
    """
    用户注册-首页-发布普通问答-进入个人中心页-问答管理-查看发布的问答
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
    data = Data.TEST_DATA['UserPublishQa']
    # 用户登录
    ul = user_login(*args, **kwargs)
    # 发布问答
    upq = user_publish_qa(*args, **kwargs)
    # 进入我的中心页
    gtuc = go_to_user_center(*args, **kwargs)
    # 问答管理查看发布的问答
    ucpq = user_check_publish_qa(*args, **kwargs)
    Assert.is_equal(data['user_publish_qa']['In']['title'], ucpq['qa_title'])
