# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Teacher.user_create_article import user_create_article
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_pass_article import console_pass_article
from Projects.PC.TestCases.User.Teacher.teacher_delete_article import teacher_delete_article

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def TeacherDeleteArticle(*args, **kwargs):
    """
    登录-发布文章-文章审核通过-删除文章
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
    data = Data.TEST_DATA['TeacherDeleteArticle']
    # 用户登录
    ul = user_login(*args, **kwargs)
    # 进入我的中心页
    gtuc = go_to_user_center(*args, **kwargs)
    # 发布文章
    uca = user_create_article(*args, **kwargs)
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 文章审核通过
    cpa = console_pass_article(*args, **kwargs)
    Assert.is_equal(data['user_create_article']['In']['title'], cpa['title'])
    Assert.is_equal(data['user_create_article']['In']['keyword'], cpa['keywords'])
    Assert.is_equal(data['user_create_article']['In']['description'], cpa['description'])
    Assert.is_equal(data['user_create_article']['In']['content'], cpa['main_text'])
    # 讲师删除文章
    tda = teacher_delete_article(*args, **kwargs)
    Assert.is_equal(data['user_create_article']['In']['title'], tda['article_title'])

