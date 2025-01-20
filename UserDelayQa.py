# -*- encoding: utf-8 -*-
import datetime
from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Common.user_publish_qa_with_bounty import user_publish_qa_with_bounty
from Projects.PC.TestCases.Common.alipay import alipay
from Projects.PC.TestCases.User.Common.user_check_publish_qa import user_check_publish_qa
from Projects.PC.TestCases.User.Common.user_delay_qa import user_delay_qa

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB
@test_scenario()
def UserDelayQa(*args, **kwargs):
    """
    用户注册-首页-发布问答-进入个人中心页-问答管理-查看发布的问答-悬赏问答延期
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
    data = Data.TEST_DATA['UserDelayQa']
    # 用户登录
    ul = user_login(*args, **kwargs)
    # # 发布问答
    # upqwb = user_publish_qa_with_bounty(*args, **kwargs)
    # # 支付宝支付
    # ali_pay = alipay(*args, **kwargs)
    # # 进入我的中心页
    # gtuc = go_to_user_center(*args, **kwargs)
    # # 问答管理查看发布的问答
    # ucpq = user_check_publish_qa(*args, **kwargs)
    # Assert.is_equal(data['user_publish_qa_with_bounty']['In']['title'], ucpq['qa_title'])
    # # 在数据库调整结束时间
    # # 获取4个小时之后个时间字符串，6小时以内的悬赏问答才能被延期（显示追加按钮）
    # time_stamp = datetime.datetime.now() + datetime.timedelta(hours=4)
    # end_time = time_stamp.strftime('%Y-%m-%d %H:%M:%S')
    # end_time_sql = 'UPDATE dxz_lan.dxz_article_question SET end_time = "{}" WHERE title = "{}"'.format(end_time, data['user_publish_qa_with_bounty']['In']['title'])

    # db.execute_modify_sql(end_time_sql)
    # # 问答延期
    # udq = user_delay_qa(*args, **kwargs)
    # Assert.is_containing('追加悬赏操作成功', udq['delay_success'])
