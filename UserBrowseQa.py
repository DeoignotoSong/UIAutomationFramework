# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.user_register import user_register
from Projects.PC.TestCases.User.Common.check_browse_qa import check_browse_qa
from Projects.PC.TestCases.User.Common.user_browse_qa import user_browse_qa

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserBrowseQa(*args, **kwargs):
    """
    用户注册-浏览问答-查看我的足迹浏览
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
    data = Data.TEST_DATA['UserBrowseQa']
    # 用户注册
    ur = user_register(*args, **kwargs)
    # 浏览文章
    ubq = user_browse_qa(*args, **kwargs)
    # 查看我的足迹浏览
    clq = check_browse_qa(*args, **kwargs)
    Assert.is_containing(ubq['qa_title'], clq['browse_qa_title'])
