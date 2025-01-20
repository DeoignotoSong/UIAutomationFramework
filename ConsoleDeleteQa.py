# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Common.user_logout import user_logout
from Projects.PC.TestCases.User.User.user_reply_qa_answer import user_reply_qa_answer
from Projects.PC.TestCases.User.Teacher.user_create_qa_answer import user_create_qa_answer
from Projects.PC.TestCases.User.User.user_publish_qa import user_publish_qa
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_delete_qa_lv_second import console_delete_qa_lv_second
from Projects.PC.TestCases.Console.Admin.console_delete_qa_lv_first import console_delete_qa_lv_first
from Projects.PC.TestCases.Console.Admin.console_delete_qa import console_delete_qa

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ConsoleDeleteQa(*args, **kwargs):
    """
    登录-发布普通问答-发布答案-回复答案-后台登录-删除问答二级回复-删除问答一级回复-删除问答
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
    data = Data.TEST_DATA['ConsoleDeleteQa']
    # 用户登录
    ul = user_login(*args, **kwargs)
    project.wait(2)
    # 发布问答
    upq = user_publish_qa(*args, **kwargs)
    # 用户登出
    ulo = user_logout(*args, **kwargs)
    # 回复者登录
    ul2 = user_login(*args, **kwargs)
    project.wait(2)
    # 发布问答回答
    ucqc = user_create_qa_answer(*args, **kwargs)
    # 用户登出
    ulo2 = user_logout(*args, **kwargs)
    # 问答创建者登录
    ul3 = user_login(*args, **kwargs)
    # 回复问答回答
    urqc = user_reply_qa_answer(*args, **kwargs)
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 删除问答二级回复
    cdqls = console_delete_qa_lv_second(*args, **kwargs)
    Assert.is_equal(data['user_publish_qa']['Out']['qa_id'], cdqls['qa_id'])
    Assert.is_equal(data['user_publish_qa']['In']['title'], cdqls['qa_title'])
    Assert.is_equal(data['user_reply_qa_answer']['In']['reply_answer'], cdqls['second_level_reply_content'])
    # 删除问答一级回复
    cdqlf = console_delete_qa_lv_first(*args, **kwargs)
    Assert.is_equal(data['user_publish_qa']['Out']['qa_id'], cdqlf['qa_id'])
    Assert.is_equal(data['user_publish_qa']['In']['title'], cdqlf['qa_title'])
    Assert.is_equal(data['user_create_qa_answer']['In']['answer'], cdqlf['first_level_reply_content'])
    # 删除问答
    cdq = console_delete_qa(*args, **kwargs)
    Assert.is_containing(data['user_publish_qa']['Out']['qa_id'], cdq['qa_id'])
    Assert.is_containing(data['user_publish_qa']['In']['title'], cdq['qa_title'])

