# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data, DataBaseName
from Projects.PC.TestCases.User.Common.user_register import user_register
from Projects.PC.TestCases.User.Common.check_liked_qa import check_liked_qa
from Projects.PC.TestCases.User.Common.user_liked_qa import user_liked_qa
from Projects.PC.Base.ProjectHandler import *
from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserLikedQa(*args, **kwargs):
    """
    用户注册-点赞问答-查看我的足迹点赞-取消点赞问答-查看我的足迹点赞
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
    data = Data.TEST_DATA['UserLikedQa']
    # 用户注册
    ur = user_register(*args, **kwargs)
    try:
        # 点赞文章
        ula = user_liked_qa(*args, **kwargs)
        Assert.is_equal(int(ula['liked_number_before']) + 1, ula['liked_number_after'])
        # 查看我的足迹点赞
        clq = check_liked_qa(*args, **kwargs)
        Assert.is_equal(ula['qa_title'], clq['article_title'])
        # 取消点赞
        ula2 = user_liked_qa(*args, **kwargs)
        Assert.is_equal(int(ula2['liked_number_before']) - 1, ula2['liked_number_after'])
        # 查看我的足迹点赞2
        cla2 = check_liked_qa(*args, **kwargs)
        Assert.is_equal('暂无数据', cla2['article_title'])
    finally:
        mobile_cipher = parse_encrypt_base64(mysql, data['user_register']['In']['mobile'])
        user_id_sql = 'SELECT * FROM {}.dxz_user WHERE mobile_cipher="{}"'.format(
            DataBaseName.DATABASE_NAME['dxz_lan'],
            mobile_cipher
        )

        user_id = mysql.execute_select_sql(user_id_sql)[0]['id']
        reset_sql = 'UPDATE {}.dxz_user_resource_access SET is_operation_cancel=1 WHERE user_id="{}" AND type=4 AND operation_type=4'.format(
            DataBaseName.DATABASE_NAME['dxz_lan'],
            user_id
        )

        log(reset_sql)
        mysql.execute_modify_sql(reset_sql)
