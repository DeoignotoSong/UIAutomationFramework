# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.user_register import user_register
from Projects.PC.TestCases.User.Common.check_liked_article import check_liked_article
from Projects.PC.TestCases.User.Common.user_liked_article import user_liked_article

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserLikedArticle(*args, **kwargs):
    """
    用户注册-点赞文章-查看我的足迹点赞-取消点赞文章-查看我的足迹点赞
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
    data = Data.TEST_DATA['UserLikedArticle']
    # 用户注册
    ur = user_register(*args, **kwargs)
    # 点赞文章
    ula = user_liked_article(*args, **kwargs)
    Assert.is_equal('点赞', ula['liked_state_before'])
    Assert.is_equal('取消点赞', ula['liked_state_after'])
    Assert.is_equal(int(ula['liked_number_before']) + 1, ula['liked_number_after'])
    # 查看我的足迹点赞
    cla = check_liked_article(*args, **kwargs)
    Assert.is_equal(ula['article_title'], cla['article_title'])
    # 取消点赞
    ula2 = user_liked_article(*args, **kwargs)
    Assert.is_equal('取消点赞', ula2['liked_state_before'])
    Assert.is_equal('点赞', ula2['liked_state_after'])
    Assert.is_equal(int(ula2['liked_number_before']) - 1, ula2['liked_number_after'])
    # 查看我的足迹点赞2
    cla2 = check_liked_article(*args, **kwargs)
    Assert.is_equal('暂无数据', cla2['article_title'])
