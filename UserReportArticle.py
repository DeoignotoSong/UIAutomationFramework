# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.user_register import user_register
from Projects.PC.TestCases.User.Common.user_report_article import user_report_article
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_check_report_info import console_check_report_info

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserReportArticle(*args, **kwargs):
    """
    用户注册-举报文章-后台登录-查看举报内容
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
    data = Data.TEST_DATA['UserReportArticle']
    # 用户注册
    ur = user_register(*args, **kwargs)
    # 举报文章
    ura = user_report_article(*args, **kwargs)
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 查看后台举报
    ccri = console_check_report_info(*args, **kwargs)
    Assert.is_equal(ura['report_reason'].strip(), ccri['report_reason'])
    Assert.is_equal(ura['article_title'].strip(), ccri['report_content'])

    # 手机号掩码转化
    number_list = list(data['user_register']['In']['mobile'])
    mask_mobile = ''
    for index in range(3, 7):
        number_list[index] = '*'
        mask_mobile = ''.join(number_list)

    Assert.is_equal(mask_mobile, ccri['report_mobile'])
