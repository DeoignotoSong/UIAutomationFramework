# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.user_register import user_register
from Projects.PC.TestCases.User.Common.search_product import search_product
from Projects.PC.TestCases.User.Common.user_collect_product import user_collect_product
from Projects.PC.TestCases.User.Common.check_collection_product import check_collection_product

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserCollectionProduct(*args, **kwargs):
    """
    用户注册-搜索商品-收藏商品-搜索商品-取消收藏-搜索商品
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
    data = Data.TEST_DATA['UserCollectionProduct']
    # 用户注册
    ur = user_register(*args, **kwargs)
    # 搜索商品
    sp = search_product(*args, **kwargs)
    # 收藏商品
    ucp = user_collect_product(*args, **kwargs)
    Assert.is_equal(sp['search_product_title'],ucp['product_title'])
    Assert.is_equal(int(ucp['collection_number_before'])+1,ucp['collection_number_after'])
    Assert.is_equal('收藏',ucp['collection_state_before'])
    Assert.is_equal('已收藏', ucp['collection_state_after'])
    # 查看我的足迹
    ccp = check_collection_product(*args, **kwargs)
    Assert.is_equal(sp['search_product_title'], ccp['product_title'])
    # 搜索商品
    sp1 = search_product(*args, **kwargs)
    Assert.is_equal(sp['search_product_title'],sp1['search_product_title'])
    # 取消收藏
    ucp1 = user_collect_product(*args, **kwargs)
    Assert.is_equal(sp1['search_product_title'], ucp1['product_title'])
    Assert.is_equal(ucp1['collection_number_before'], ucp1['collection_number_after'])
    Assert.is_equal('已收藏', ucp1['collection_state_before'])
    Assert.is_equal('收藏', ucp1['collection_state_after'])
    # 查看我的足迹
    ccp1 = check_collection_product(*args, **kwargs)
    Assert.is_equal('暂无数据', ccp1['product_title'])
    # 搜索商品
    sp2 = search_product(*args, **kwargs)
    Assert.is_equal(sp['search_product_title'], sp2['search_product_title'])

