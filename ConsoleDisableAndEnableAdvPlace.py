# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_operate_adv_place import *
from Projects.PC.TestCases.User.Common.check_advert_place import check_advert_place
from Projects.PC.TestCases.Console.Admin.console_add_adv_place import console_add_adv_place
from Projects.PC.TestCases.Console.Admin.console_add_adv import console_add_adv
from Projects.PC.TestCases.Console.Admin.console_advert_auditing_pass import console_advert_auditing_pass
from DB.MysqlDB import MysqlDB


@test_scenario()
def ConsoleDisableAndEnableAdvPlace(*args, **kwargs):
    """
    后台登录-搜索广告位-禁用广告位-登录前端-广告位不展示-重新启用广告位-登录前端-广告位展示
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
    data = Data.TEST_DATA['ConsoleDisableAndEnableAdvPlace']
    project['Selenium'].driver.maximize_window()
    # 后台用户登录
    cl = console_login(*args, **kwargs)
    Assert.is_containing('Hi', cl['console_name_content'])
    # 创建广告位标签
    create_advert_flag = False
    # 检查广告管理-广告位-是否存在指定广告位
    ccap = console_check_adv_place(*args, **kwargs)
    if not ccap["advert_list"]:
        # 添加广告位
        caap = console_add_adv_place(*args, **kwargs)
        Assert.is_containing('操作成功!', caap['message_content'])
        # 标记广告位创建
        create_advert_flag = True
        # 添加广告
        caa = console_add_adv(*args, **kwargs)
        Assert.is_containing('操作成功!', caa['message_content'])
        # 广告审核
        caap = console_advert_auditing_pass(*args, **kwargs)
        Assert.is_containing(
            data['console_advert_auditing_pass']['In']['dialog_message_content'],
            caap["dialog_message_content"]
        )

        Assert.is_containing('操作成功!', caap['message_content'])

    try:
        # 禁用指定广告位
        cdap = console_disable_adv_place(*args, **kwargs)
        Assert.is_containing(data['console_disable_adv_place']['In']['dialog_message_content'], cdap["dialog_message_content"])
        Assert.is_containing("操作成功!", cdap["message_content"])
        # 首页广告位获取
        cap = check_advert_place(*args, **kwargs)
        # 断言首页顶部广告不展示
        Assert.is_equal(None, cap["top_advert_place"])
        # 启用指定广告位
        ceap = console_enable_adv_place(*args, **kwargs)
        Assert.is_containing(data['console_enable_adv_place']['In']['dialog_message_content'], ceap["dialog_message_content"])
        Assert.is_containing("操作成功!", ceap["message_content"])
        # 首页广告位获取
        cap = check_advert_place(*args, **kwargs)
        # 断言首页顶部广告展示
        Assert.is_not_equal(None, cap["top_advert_place"])
    finally:
        # 删除已创建的广告位
        if create_advert_flag:
            # 删除创建广告位
            cdca = console_delete_create_advert(*args, **kwargs)
            Assert.is_containing(data['console_delete_create_advert']['In']['dialog_message_content'],
                                 cdca["dialog_message_content"])
            Assert.is_containing("操作成功!", cdca["message_content"])
