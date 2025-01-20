# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Projects.PC.TestCases.User.Common.check_home_first_category import check_home_first_category
from Projects.PC.TestCases.User.Common.check_home_second_category import check_home_second_category
from Projects.PC.TestCases.User.Common.check_home_fourth_category import check_home_fourth_category
from Projects.PC.TestCases.User.Common.check_home_fifth_category import check_home_fifth_category
from Projects.PC.TestCases.User.Common.check_home_third_category import check_home_third_category

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def CheckHomeCategories(*args, **kwargs):
    """
    检查首页赛道
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
    # 查看出国留学赛道
    chac = check_home_first_category(*args, **kwargs)
    Assert.is_equal('留学', chac['abroad_category'])
    Assert.is_containing('/abroad', chac['abroad_url'])
    # 查看语言培训赛道
    chlc = check_home_second_category(*args, **kwargs)
    Assert.is_equal('语言培训', chlc['language_category'])
    Assert.is_containing('/language', chlc['language_url'])
    # 查看学科辅导赛道
    chcc = check_home_third_category(*args, **kwargs)
    Assert.is_equal('学科辅导', chcc['coach_category'])
    Assert.is_containing('/coach', chcc['coach_url'])
    # 查看院校直通车赛道
    chsc = check_home_fourth_category(*args, **kwargs)
    Assert.is_equal('院校直通车', chsc['school_category'])
    Assert.is_containing('/school', chsc['school_url'])
    # 查看海外移民赛道
    chic = check_home_fifth_category(*args, **kwargs)
    Assert.is_equal('海外移民', chic['immi_category'])
    Assert.is_containing('/immi', chic['immi_url'])

