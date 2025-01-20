# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_disable_channel import console_disable_channel
from Projects.PC.TestCases.User.Common.check_home_channel import check_home_channel
from Projects.PC.TestCases.Console.Admin.console_enable_channel import console_enable_channel

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ConsoleDisableAndEnableChannel(*args, **kwargs):
    """
    后台登录-禁用频道-首页查看频道数量-启用频道-首页查看频道数量
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
    data = Data.TEST_DATA['ConsoleDisableAndEnableChannel']
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 后台禁用频道
    cdc = console_disable_channel(*args, **kwargs)
    # 首页查看频道
    cha = check_home_channel(*args, **kwargs)
    Assert.is_equal('', cha['channel_result'])
    # 后台禁用频道
    cec = console_enable_channel(*args, **kwargs)
    # 首页查看频道
    cha2 = check_home_channel(*args, **kwargs)
    Assert.is_equal(data['console_disable_channel']['In']['channel_name'], cha2['channel_result'])

