# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Common.user_share_article import user_share_article

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserShareArticle(*args, **kwargs):
    """
    用户登录-分享文章
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
    # 用户登录
    ul = user_login(*args, **kwargs)
    # 分享文章
    #usa = user_share_article(*args, **kwargs)

