# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Common.user_logout import user_logout
from Projects.PC.TestCases.User.Teacher.user_create_qa_answer import user_create_qa_answer
from Projects.PC.TestCases.User.User.user_reply_qa_answer import user_reply_qa_answer
from Projects.PC.TestCases.User.User.user_publish_qa import user_publish_qa

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UsCreateAndReplyQaAnswer(*args, **kwargs):
    """
    发布者登录-发布问答-用户登出-回答者登录-发布问答回答-发布者登录-回复问答答案
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
    data = Data.TEST_DATA['UsCreateAndReplyQaAnswer']
    # 发布者注册登录
    ul = user_login(*args, **kwargs)
    # 发布问答
    upq = user_publish_qa(*args, **kwargs)
    # 用户登出
    ulo = user_logout(*args, **kwargs)
    # 回答者登录
    ul2 = user_login(*args, **kwargs)
    # 发布问答回答
    ucqc = user_create_qa_answer(*args, **kwargs)
    # 用户登出
    ulo2 = user_logout(*args, **kwargs)
    # 问答创建者登录
    ul3 = user_login(*args, **kwargs)
    # 回复问答回答
    urqc = user_reply_qa_answer(*args, **kwargs)

