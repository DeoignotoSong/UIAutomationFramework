# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.Organization.Institute.ins_info_manage import ins_info_manage
from Projects.PC.TestCases.Console.Admin.console_institution_rv_pass import console_institution_rv_pass
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Organization.Institute.institution_register import institution_register
from Projects.PC.TestCases.Organization.Common.organization_login import organization_login
from Projects.PC.TestCases.Organization.Institute.institution_home_review import institution_home_review
from Projects.PC.TestCases.Console.Admin.cons_ins_de_pass import cons_ins_de_pass
from Projects.PC.TestCases.Organization.Institute.ins_info_get import ins_info_get

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def InstitutionInfoManage(*args, **kwargs):
    """
    机构信息维护-机构信息审核通过
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
    data = Data.TEST_DATA['InstitutionInfoManage']
    # 机构注册
    ir = institution_register(*args, **kwargs)
    # 用户登录
    ol = organization_login(*args, **kwargs)
    # 输入信息提交审核
    ihr = institution_home_review(*args, **kwargs)
    # 管理后台用户登录
    cl = console_login(*args, **kwargs)
    # 审核通过
    cirp = console_institution_rv_pass(*args, **kwargs)
    # 用户登录
    ol2 = organization_login(*args, **kwargs)
    # 信息编辑
    inm = ins_info_manage(*args, **kwargs)
    # 管理后台审核
    cidp = cons_ins_de_pass(*args, **kwargs)
    # 修改后数据验证
    iig = ins_info_get(*args, **kwargs)
    Assert.is_equal(data['ins_info_manage']['In']['name'], iig['ch_name_message'])
    Assert.is_equal(data['ins_info_manage']['In']['create_time'], iig['ch_create_time_message'])
    Assert.is_equal(data['ins_info_manage']['In']['country'], iig['ch_country_message'])
    Assert.is_equal(data['ins_info_manage']['In']['registered_address'], iig['ch_registered_address_message'])
    Assert.is_equal(data['ins_info_manage']['In']['office_address'], iig['ch_office_address_message'])
    Assert.is_equal(data['ins_info_manage']['In']['full_address'], iig['ch_full_address_message'])
    Assert.is_equal(data['ins_info_manage']['In']['website'], iig['ch_website_message'])
    Assert.is_equal(data['ins_info_manage']['In']['summary'], iig['ch_summary_message'])
    Assert.is_equal(data['ins_info_manage']['In']['legal_person'], iig['ch_legal_person_message'])
    Assert.is_equal(data['ins_info_manage']['In']['contact_user_name'], iig['ch_contact_user_name_message'])
    Assert.is_equal(data['ins_info_manage']['In']['contact_mobile'][-2:], iig['ch_contact_mobile_message'][-2:])
    Assert.is_equal(data['ins_info_manage']['In']['contact_email'], iig['ch_contact_email_message'])
