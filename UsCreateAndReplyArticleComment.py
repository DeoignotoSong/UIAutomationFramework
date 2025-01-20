# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Common.user_create_article_comment import user_create_article_comment
from Projects.PC.TestCases.User.Common.user_reply_article_comment import user_reply_article_comment

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UsCreateAndReplyArticleComment(*args, **kwargs):
    """
    用户登录-创建文章评论-回复文章评论
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
    data = Data.TEST_DATA['UsCreateAndReplyArticleComment']
    # 用户登录
    ul = user_login(*args, **kwargs)
    # 创建文章评论
    ucac = user_create_article_comment(*args, **kwargs)
    # 回复文章评论
    urac = user_reply_article_comment(*args, **kwargs)

