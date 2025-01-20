# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.user_register import user_register
from Projects.PC.TestCases.User.Common.check_collection_article import check_collection_article
from Projects.PC.TestCases.User.Common.user_collection_article import user_collection_article

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserCollectionArticle(*args, **kwargs):
    """
    用户注册-收藏文章-查看我的足迹收藏-取消收藏文章-查看我的足迹收藏
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
    data = Data.TEST_DATA['UserCollectionArticle']
    # 用户注册
    ur = user_register(*args, **kwargs)
    # 收藏文章
    uca = user_collection_article(*args, **kwargs)
    Assert.is_equal('收藏', uca['collection_state_before'])
    Assert.is_equal('取消收藏', uca['collection_state_after'])
    Assert.is_equal(int(uca['collection_number_before']) + 1, uca['collection_number_after'])
    # 查看我的足迹收藏
    cca = check_collection_article(*args, **kwargs)
    Assert.is_equal(uca['article_title'], cca['article_title'])
    # 取消收藏
    uca2 = user_collection_article(*args, **kwargs)
    Assert.is_equal('取消收藏', uca2['collection_state_before'])
    Assert.is_equal('收藏', uca2['collection_state_after'])
    Assert.is_equal(int(uca2['collection_number_before']), uca2['collection_number_after'])
    # 查看我的足迹收藏2
    cca2 = check_collection_article(*args, **kwargs)
    Assert.is_equal('暂无数据', cca2['article_title'])
