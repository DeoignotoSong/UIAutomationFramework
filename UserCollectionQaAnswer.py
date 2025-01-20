# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Projects.PC.Base.ProjectHandler import *
from Core.Assert import Assert
from Core.Global import Data, DataBaseName
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Common.user_logout import user_logout
from Projects.PC.TestCases.User.Teacher.user_create_qa_answer import user_create_qa_answer
from Projects.PC.TestCases.User.Common.user_collect_qa_answer import user_collect_qa_answer
from Projects.PC.TestCases.User.Common.user_cancel_collect_qa_answer import user_cancel_collect_qa_answer
from Projects.PC.TestCases.User.User.user_publish_qa import user_publish_qa
from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserCollectionQaAnswer(*args, **kwargs):
    """
    发布者登录-发布问答-用户登出-回答者登录-发布问答答案-收藏问答答案-取消收藏问答答案
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
    data = Data.TEST_DATA['UserCollectionQaAnswer']
    # 发布者登录
    ul = user_login(*args, **kwargs)
    # 发布问答
    upq = user_publish_qa(*args, **kwargs)
    # 用户登出
    ulo = user_logout(*args, **kwargs)
    # 回答者用户登录
    ul2 = user_login(*args, **kwargs)
    # 发布问答回答
    ucqc = user_create_qa_answer(*args, **kwargs)
    try:
        # 收藏问答答案
        ucq = user_collect_qa_answer(*args, **kwargs)
        # 取消收藏
        ucq2 = user_cancel_collect_qa_answer(*args, **kwargs)
        Assert.is_equal(ucq['qa_title'], ucq2['qa_title'])
        Assert.is_equal(ucq['qa_answer_user'], ucq2['qa_answer_user'])
        Assert.is_equal(ucq['qa_answer_content'], ucq2['qa_answer_content'])
    finally:
        mobile_cipher = parse_encrypt_base64(mysql, data['user_login.2']['In']['mobile'])
        user_id_sql = 'SELECT * FROM {}.dxz_user WHERE mobile_cipher = "{}"'.format(
            DataBaseName.DATABASE_NAME['dxz_lan'],
            mobile_cipher
        )

        user_id = mysql.execute_select_sql(user_id_sql)[0]['id']
        reset_sql = 'UPDATE {}.dxz_user_resource_access SET is_operation_cancel=1 WHERE user_id="{}" AND type=11 AND operation_type=2'.format(
            DataBaseName.DATABASE_NAME['dxz_lan'],
            user_id
        )

        log(reset_sql)
        mysql.execute_modify_sql(reset_sql)
