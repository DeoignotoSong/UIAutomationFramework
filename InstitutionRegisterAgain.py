# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Projects.PC.TestCases.Organization.Institute.institution_register_ag import institution_register_ag

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def InstitutionRegisterAgain(*args, **kwargs):
    """
    国内机构重复注册
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
    data = Data.TEST_DATA['InstitutionRegisterAgain']
    # 重复用户再次注册
    ira = institution_register_ag(*args, **kwargs)
