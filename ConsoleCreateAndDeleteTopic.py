# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_create_topic import console_create_topic
from Projects.PC.TestCases.Console.Admin.console_edit_topic import console_edit_topic
from Projects.PC.TestCases.Console.Admin.console_delete_topic import console_delete_topic

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ConsoleCreateAndDeleteTopic(*args, **kwargs):
    """
    后台登录-添加话题-编辑话题-删除话题
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
    data = Data.TEST_DATA['ConsoleCreateAndDeleteTopic']
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 添加话题
    cct = console_create_topic(*args, **kwargs)
    # 编辑话题
    cet = console_edit_topic(*args, **kwargs)
    # 删除话题
    cdt = console_delete_topic(*args, **kwargs)

