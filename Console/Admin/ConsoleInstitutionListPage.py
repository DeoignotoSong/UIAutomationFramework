from Utils.Log import log

"""
后台-用户中心-机构院校列表
console_url/university/list
"""


class ConsoleInstitutionListPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/university/list'
        # region Fields
        # 提交成功提示信息
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 下拉列表
        self._drop_down_list_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 搜索-机构院校名称
        self._search_institute_name_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[1]/div/div/input'
        # 搜索-机构院校性质
        self._search_institute_nature_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[2]/div/div/input'
        # 搜素-联系人姓名
        self._search_institute_contact_name_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[3]/div/div/input'
        # 搜索-联系电话
        self._search_institute_contact_mobile_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[4]/div/div/input'
        # 搜索-所属国家
        self._search_country_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[5]/div/div'
        # 搜索-状态
        self._search_state_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[6]/div/div'
        # 搜索-是否金吉列
        self._search_is_jjl_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[7]/div/div'
        # 搜搜-是否合作院校
        self._search_is_cooperation_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[8]/div/div'
        # 搜索-类型
        self._search_type_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[9]/div/div'
        # 搜索-注册时间-开始日期
        self._search_register_time_start_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[10]/div/div/input[1]'
        # 搜索-注册时间-结束日期
        self._search_register_time_end_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[10]/div/div/input[2]'
        # 搜索-查询
        self._search_query_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[last()-1]/div/button'
        # 搜索-清除
        self._search_clear_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[last()]/div/button'
        # 新增
        self._add_institution_button_tag = '//*[@id="tableSearch"]/form/div[2]/div/div/button'
        # 列表-第一行-机构院校ID
        self._list_first_institute_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 列表-第一行-机构院校名称
        self._list_first_institute_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 列表-第一行-所属国家
        self._list_first_country_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 列表-第一行-联系电话
        self._list_first_contact_mobile_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 列表-第一行-联系人姓名
        self._list_first_contact_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 列表-第一行-类型
        self._list_first_type_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div'
        # 列表-第一行-机构院校性质
        self._list_first_institute_nature_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div'
        # 列表-第一行-状态
        self._list_first_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div'
        # 列表-是否合作院校
        self._list_is_cooperation_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[10]/div'
        # 列表-注册时间
        self._list_register_time_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[11]/div'
        # 列表-操作-第一个操作
        self._list_execute_first_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[13]/div/a[1]'
        # 列表-操作-第二个操作
        self._list_execute_second_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[13]/div/a[2]'
        # 列表-操作-第三个操作
        self._list_execute_third_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[5]/td[13]/div/a[3]'
        # 新增-标题
        self._add_title_text_tag = '//*[@id="app"]/div/section/main/div/div[1]/div[1]/div[2]'
        # 新增-第一个菜单
        self._add_tab_first_button_tag = '//*[@id="app"]/div/section/main/div/div[1]/div[2]/ul/li[1]'
        # 新增-用户账号
        self._add_username_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[3]/div[1]/div/div/div[1]/input'
        # 新增-用户密码
        self._add_password_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div/div[1]/input'
        # 新增-真实姓名
        self._add_real_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[4]/div[1]/div/div/div[1]/input'
        # 新增-用户昵称
        self._add_nick_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[4]/div[2]/div/div/div[1]/input'
        # 新增-机构院校名称
        self._add_institute_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[5]/div[1]/div/div/div[1]/input'
        # 新增-机构院校名称（英文）
        self._add_institute_name_en_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[5]/div[2]/div/div/div[1]/input'
        # 新增-联系人
        self._add_institute_contact_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[6]/div[1]/div/div/div[1]/input'
        # 新增-联系电话-区号
        self._add_contact_phone_area_code_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[6]/div[2]/div/div/div[1]'
        # 新增-联系电话-电话号码
        self._add_contact_phone_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[6]/div[2]/div/div/div[2]/input'
        # 新增-机构院校性质
        self._add_institute_nature_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[7]/div[1]/div/div/div[1]/input'
        # 新增-联系人手机号
        self._add_contact_mobile_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[7]/div[2]/div/div/div[1]/input'
        # 新增-所属国家
        self._add_country_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[8]/div[1]/div/div/div'
        # 新增-邮箱
        self._add_email_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[8]/div[2]/div/div/div[1]/input'
        # 新增-类型
        self._add_type_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[9]/div[1]/div/div/div'
        # 新增-所属频道
        self._add_category_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[9]/div[2]/div/div/div'
        # 新增-主要领域
        self._add_main_field_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[10]/div[1]/div/div/div'
        # 新增-申请频道-第一个
        self._add_apply_channel_first_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[10]/div[2]/div/div/div/label[1]'
        # 新增-申请频道-第二个
        self._add_apply_channel_second_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[10]/div[2]/div/div/div/label[2]'
        # 新增-申请频道-第三个
        self._add_apply_channel_third_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[10]/div[2]/div/div/div/label[3]'
        # 新增-申请频道-第四个
        self._add_apply_channel_fourth_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[10]/div[2]/div/div/div/label[4]'
        # 新增-申请频道-第五个
        self._add_apply_channel_fifth_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[10]/div[2]/div/div/div/label[5]'
        # 新增-银行卡号码
        self._add_bank_card_number_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[11]/div[1]/div/div/div/input'
        # 新增-开户行名称
        self._add_open_bank_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[11]/div[2]/div/div/div/input'
        # 新增-行号
        self._add_bank_code_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[12]/div[1]/div/div/div/input'
        # 新增-公司全称
        self._add_company_full_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[12]/div[2]/div/div/div/input'
        # 新增-机构-是否属于金吉列-是
        self._add_institute_is_jjl_yes_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[13]/div/div/div/div/label[1]'
        # 新增-机构-是否属于金吉列-否
        self._add_institute_is_jjl_no_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[13]/div/div/div/div/label[2]'
        # 新增-机构-联系地址
        self._add_institute_address_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[14]/div/div/div/div[1]/input'
        # 新增-机构-机构院校类型
        self._add_institute_institute_type_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[15]/div/div/div/div[1]/input'
        # 新增-机构-机构官网
        self._add_institute_official_website_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[16]/div/div/div/div[1]/input'
        # 新增-机构-机构院校介绍
        self._add_institute_institute_introduction_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[17]/div/div/div/div[1]/textarea'
        # 新增-机构-授权委托书
        self._add_institute_power_of_attorney_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[18]/div[1]/div/div/span/div/div/div/div/div/input'
        # 新增-机构-营业执照或其他合法资质证照
        self._add_institute_business_license_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[18]/div[2]/div/div/span/div/div/div/div/div/input'
        # 新增-机构-机构院校logo
        self._add_institute_institute_logo_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[19]/div[1]/div/div/div/div/div/input'
        # 新增-机构-机构院校主页背景
        self._add_institute_institute_background_main_page_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[19]/div[2]/div/div/div/div/div/input'
        # 新增-机构-创立时间
        self._add_institute_create_time_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[20]/div[1]/div/div/div/input'
        # 新增-机构-法人
        self._add_institute_juridical_person_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[20]/div[2]/div/div/div[1]/input'
        # 新增-院校-是否合作院校-是
        self._edit_school_is_cooperation_yes_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[13]/div/div/div/div/label[1]'
        # 编辑-院校-是否合作院校-否
        self._edit_school_is_cooperation_no_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[13]/div/div/div/div/label[2]'
        # 编辑-院校-学历-第一个
        self._edit_school_qualification_first_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[14]/div/div/div/div/label[1]'
        # 编辑-院校-学历-第二个
        self._edit_school_qualification_second_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[14]/div/div/div/div/label[2]'
        # 编辑-院校-专业-第一个
        self._edit_school_specialities_first_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[15]/div/div/div/div/label[1]'
        # 编辑-院校-专业-第二个
        self._edit_school_specialities_second_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[15]/div/div/div/div/label[2]'
        # 编辑-院校-联系地址
        self._edit_school_address_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[16]/div/div/div/div/input'
        # 编辑-院校-机构院校类型
        self._edit_school_institute_type_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[17]/div/div/div/div[1]/input'
        # 编辑-院校-机构官网
        self._edit_school_official_website_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[18]/div/div/div/div[1]/input'
        # 编辑-院校-机构院校介绍
        self._edit_school_institute_introduction_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[19]/div/div/div/div[1]/textarea'
        # 编辑-院校-授权委托书
        self._edit_school_power_of_attorney_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[20]/div[1]/div/div/span/div/div/div/div/div/input'
        # 编辑-院校-营业执照或其他合法资质证照
        self._edit_school_business_license_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[20]/div[2]/div/div/span/div/div/div/div/div/input'
        # 编辑-院校-机构院校logo
        self._edit_school_institute_logo_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[21]/div[1]/div/div/div/div/div/input'
        # 编辑-院校-机构院校主页背景
        self._edit_school_institute_background_main_page_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[21]/div[2]/div/div/div/div/div/input'
        # 编辑-院校-创立时间
        self._edit_school_create_time_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[22]/div[1]/div/div/div/input'
        # 编辑-院校-法人
        self._edit_school_juridical_person_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[22]/div[2]/div/div/div[1]/input'
        # 编辑-院校-合作开始时间
        self._edit_school_cooperation_start_time_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[23]/div[1]/div/div/div/input'
        # 编辑-院校-合作结束时间
        self._edit_school_cooperation_end_time_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[23]/div[2]/div/div/div/input'
        # 新增-提交
        self._add_commit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[last()]/div[1]/div/div/button[1]'
        # 新增-取消
        self._add_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[last()]/div[1]/div/div/button[2]'
        # 编辑-标题
        self._edit_title_text_tag = '//*[@id="app"]/div/section/main/div/div[1]/div[1]/div[2]'
        # 编辑-第一个菜单
        self._edit_tab_first_button_tag = '//*[@id="app"]/div/section/main/div/div[1]/div[2]/ul/li[1]'
        # 编辑-机构院校ID
        self._edit_institute_id_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[1]/div[1]/div/div/div/input'
        # 编辑-注册时间
        self._edit_register_time_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[1]/div[2]/div/div/div/input'
        # 编辑-创建人员
        self._edit_create_user_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[2]/div[1]/div/div/div/input'
        # 编辑-审核状态
        self._edit_review_state_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div/div/input'
        # 编辑-用户账号
        self._edit_username_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[3]/div[1]/div/div/div[1]/input'
        # 编辑-用户密码
        self._edit_password_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div/div[1]/input'
        # 编辑-真实姓名
        self._edit_real_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[4]/div[1]/div/div/div[1]/input'
        # 编辑-用户昵称
        self._edit_nick_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[4]/div[2]/div/div/div[1]/input'
        # 编辑-机构院校名称
        self._edit_institute_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[5]/div[1]/div/div/div[1]/input'
        # 编辑-机构院校名称（英文）
        self._edit_institute_name_en_input_tag = '/html/body/div/div/section/main/div/div[2]/div/div[2]/form/div[6]/div/div/div/div[1]/input'
        # 编辑-联系人
        self._edit_institute_contact_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[7]/div[1]/div/div/div[1]/input'
        # 编辑-联系电话-区号
        self._edit_contact_phone_area_code_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[7]/div[2]/div/div/div[1]'
        # 编辑-联系电话-电话号码
        self._edit_contact_phone_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[7]/div[2]/div/div/div[2]/input'
        # 编辑-机构院校性质
        self._edit_institute_nature_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[8]/div[1]/div/div/div[1]/input'
        # 编辑-联系人手机号
        self._edit_contact_mobile_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[8]/div[2]/div/div/div[2]/input'
        # 编辑-所属国家
        self._edit_country_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[9]/div[1]/div/div/div'
        # 编辑-邮箱
        self._edit_email_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[9]/div[2]/div/div/div[1]/input'
        # 编辑-类型
        self._edit_type_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[10]/div[1]/div/div/div'
        # 编辑-所属频道
        self._edit_category_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[10]/div[2]/div/div/div'
        # 编辑-主要领域
        self._edit_main_field_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[11]/div[1]/div/div/div'
        # 编辑-申请频道-第一个
        self._edit_apply_channel_first_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[11]/div[2]/div/div/div/label[1]'
        # 编辑-申请频道-第二个
        self._edit_apply_channel_second_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[11]/div[2]/div/div/div/label[2]'
        # 编辑-申请频道-第三个
        self._edit_apply_channel_third_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[11]/div[2]/div/div/div/label[3]'
        # 编辑-申请频道-第四个
        self._edit_apply_channel_fourth_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[11]/div[2]/div/div/div/label[4]'
        # 编辑-申请频道-第五个
        self._edit_apply_channel_fifth_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[11]/div[2]/div/div/div/label[5]'
        # 编辑-银行卡号码
        self._edit_bank_card_number_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[12]/div[1]/div/div/div/input'
        # 编辑-开户行名称
        self._edit_open_bank_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[12]/div[2]/div/div/div/input'
        # 编辑-行号
        self._edit_bank_code_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[13]/div[1]/div/div/div/input'
        # 编辑-公司全称
        self._edit_company_full_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[13]/div[2]/div/div/div/input'
        # 编辑-机构-是否属于金吉列-是
        self._edit_institute_is_jjl_yes_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[14]/div/div/div/div/label[1]'
        # 编辑-机构-是否属于金吉列-否
        self._edit_institute_is_jjl_no_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[14]/div/div/div/div/label[2]'
        # 编辑-机构-联系地址
        self._edit_institute_address_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[15]/div/div/div/div[1]/input'
        # 编辑-机构-机构院校类型
        self._edit_institute_institute_type_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[16]/div/div/div/div[1]/input'
        # 编辑-机构-机构官网
        self._edit_institute_official_website_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[17]/div/div/div/div[1]/input'
        # 编辑-机构-机构院校介绍
        self._edit_institute_institute_introduction_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[18]/div/div/div/div[1]/textarea'
        # 编辑-机构-授权委托书
        self._edit_institute_power_of_attorney_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[19]/div[1]/div/div/span/div/div/div/div/div/input'
        # 编辑-机构-营业执照或其他合法资质证照
        self._edit_institute_business_license_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[19]/div[2]/div/div/span/div/div/div/div/div/input'
        # 编辑-机构-机构院校logo
        self._edit_institute_institute_logo_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[20]/div[1]/div/div/div/div/div/input'
        # 编辑-机构-机构院校主页背景
        self._edit_institute_institute_background_main_page_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[20]/div[2]/div/div/div/div/div/input'
        # 编辑-机构-创立时间
        self._edit_institute_create_time_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[21]/div[1]/div/div/div/input'
        # 编辑-机构-法人
        self._edit_institute_juridical_person_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[21]/div[2]/div/div/div[1]/input'
        # 编辑-院校-国家及地区
        self._edit_school_country_region_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[2]/form/div[13]/div/div/div/div/div/input'
        # 编辑-院校-是否合作院校-是
        self._edit_school_is_cooperation_yes_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[2]/form/div[14]/div/div/div/div/label[1]/span[1]/span'
        # 编辑-院校-是否合作院校-否
        self._edit_school_is_cooperation_no_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[2]/form/div[14]/div/div/div/div/label[2]/span[1]/span'
        # 编辑-院校-学历-第一个
        self._edit_school_qualification_first_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[15]/div/div/div/div/label[1]'
        # 编辑-院校-学历-第二个
        self._edit_school_qualification_second_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[15]/div/div/div/div/label[2]'
        # 编辑-院校-专业-第一个
        self._edit_school_specialities_first_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[16]/div/div/div/div/label[1]'
        # 编辑-院校-专业-第二个
        self._edit_school_specialities_second_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[16]/div/div/div/div/label[2]'
        # 编辑-院校-联系地址
        self._edit_school_address_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[17]/div/div/div/div/input'
        # 编辑-院校-机构院校类型
        self._edit_school_institute_type_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[2]/form/div[18]/div/div/div/div[1]/input'
        # 编辑-院校-机构官网
        self._edit_school_official_website_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[2]/form/div[19]/div/div/div/div[1]/input'
        # 编辑-院校-机构院校介绍
        self._edit_school_institute_introduction_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[2]/form/div[20]/div/div/div/div[1]/textarea'
        # 编辑-院校-授权委托书
        self._edit_school_power_of_attorney_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[21]/div[1]/div/div/span/div/div/div/div/div/input'
        # 编辑-院校-营业执照或其他合法资质证照
        self._edit_school_business_license_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[21]/div[2]/div/div/span/div/div/div/div/div/input'
        # 编辑-院校-机构院校logo
        self._edit_school_institute_logo_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[22]/div[1]/div/div/div/div/div/input'
        # 编辑-院校-机构院校主页背景
        self._edit_school_institute_background_main_page_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[22]/div[2]/div/div/div/div/div/input'
        # 编辑-院校-创立时间
        self._edit_school_create_time_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[23]/div[1]/div/div/div/input'
        # 编辑-院校-法人
        self._edit_school_juridical_person_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[23]/div[2]/div/div/div[1]/input'
        # 编辑-院校-合作开始时间
        self._edit_school_cooperation_start_time_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[24]/div[1]/div/div/div/input'
        # 编辑-院校-合作结束时间
        self._edit_school_cooperation_end_time_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[24]/div[2]/div/div/div/input'
        # 编辑-提交
        self._edit_commit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[last()]/div[1]/div/div/button[1]'
        # 编辑-取消
        self._edit_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[last()]/div[1]/div/div/button[2]'
        # 用户中心导航
        self._console_user_center_top_button_tag = '//*[@id="app"]/div/header/div[2]/ul/li[3]'
        # 机构院校管理左侧导航
        self._console_institution_manage_left_button_tag = '//*[@id="app"]/div/section/aside/ul/li[1]/div/span'
        # 机构院校列表按钮
        self._console_institution_list_button_tag = '//*[@id="app"]/div/section/aside/ul/li[1]/ul/li[1]/span'
        # 机构院校列表表名
        self._console_institution_list_name_text_tag = '//*[@id="app"]/div/section/main/div/div[1]/div[2]/ul/li'
        # 联系人电话输入
        self._console_contact_mobile_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[4]/div/div/input'
        # 是否金吉列
        self._console_is_not_jjl_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[7]/div/div/div[1]/input'
        # 是否金吉列(否)
        self._console_is_not_jjl_not_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[3]'
        # 是否金吉列(是)
        self._console_is_not_jjl_yes_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[2]'
        # 是否合作院校
        self._console_is_not_teamwork_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[8]/div/div/div[1]/input'
        # 是否合作院校(是)
        self._console_is_not_teamwork_yes_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[2]'
        # 是否合作院校(否)
        self._console_is_not_teamwork_not_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[3]'
        # 所属国家
        self._console_at_country_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[5]/div/div/div[1]/input'
        # 所属国家(中国)
        self._console_at_country_china_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[45]'
        # 状态
        self._console_status_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[6]/div/div/div[1]/input'
        # 状态(正常)
        self._console_status_on_button_tag = '/html/body/div[6]/div[1]/div[1]/ul/li[2]'
        # 状态(禁用)
        self._console_status_off_button_tag = '/html/body/div[6]/div[1]/div[1]/ul/li[3]'
        # 联系人姓名输入
        self._console_contact_name_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[3]/div/div/input'
        # 类型
        self._console_category_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[9]/div/div/div[1]/input'
        # 类别(机构)
        self._console_category_institution_button_tag = '/html/body/div[7]/div[1]/div[1]/ul/li[2]'
        # 类别(院校)
        self._console_category_school_button_tag = '/html/body/div[7]/div[1]/div[1]/ul/li[3]'
        # 机构院校名称输入
        self._console_institution_school_name_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[1]/div/div/input'
        # 查询按钮
        self._console_inquiry_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[last()-1]/div/button/span'
        # 清除按钮
        self._console_clean_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[last()]/div/button'
        # 新增按钮
        self._console_institution_school_create_button_tag = '//*[@id="tableSearch"]/form/div[2]/div/div/button/span'
        # 查询数据名称
        self._console_inquiry_value_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[3]/div'
        # 编辑操作按钮
        self._console_inquiry_value_edit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[13]/div/a[1]/span'
        # 编辑页表单名称
        self._console_edit_form_text_tag = '//*[@id="app"]/div/section/main/div/div[1]/div[2]/ul/li'
        # 用户账号输入
        self._console_edit_user_account_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[3]/div[1]/div/div/div[1]/input'
        # 用户密码输入
        self._console_edit_user_passwd_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div/div[1]/input'
        # 真实姓名输入框
        self._console_real_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[4]/div[1]/div/div/div[1]/input'
        # 用户昵称输入
        self._console_user_nick_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[4]/div[2]/div/div/div[1]/input'
        # 机构院校名称输入
        self._console_edit_institution_school_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[5]/div[1]/div/div/div[1]/input'
        # 机构院校简称
        self._console_edit_institution_school_short_input_tag = '/html/body/div/div/section/main/div/div[2]/div/div[2]/form/div[5]/div[2]/div/div/div/input'
        # 机构院校英文名称输入
        self._console_english_name_input_tag = '/html/body/div/div/section/main/div/div[2]/div/div[2]/form/div[6]/div/div/div/div[1]/input'
        # 联系人输入
        self._console_edit_contact_person_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[7]/div[1]/div/div/div[1]/input'
        # 联系电话输入
        self._console_edit_contact_mobile_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[7]/div[2]/div/div/div[2]/input'
        # 机构院校性质输入
        self._console_nature_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[8]/div[1]/div/div/div[1]/input'
        # 联系人手机号输入
        self._console_contact_user_mobile_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[8]/div[2]/div/div/div[2]/input'
        # 所属国家
        self._console_user_at_country_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[9]/div[1]/div/div/div[1]/div/input'
        # 中国
        self._console_user_at_china_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[237]'
        # 哥伦比亚
        self._console_user_at_colombia_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[73]'
        # 邮箱输入
        self._console_email_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[9]/div[2]/div/div/div[1]/input'
        # 类型选择
        self._console_edit_type_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[10]/div[1]/div/div/div/div/input'
        # 类型(机构)
        self._console_edit_type_institution_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[1]'
        # 类型(院校)
        self._console_edit_type_school_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[2]'
        # 所属频道
        self._console_channel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[10]/div[2]/div/div/div'
        # 所属频道(语言培训)
        self._console_channel_language_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]'
        # 所属频道(语言培训创建)
        self._console_channel_language_create_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]/span'
        # 主要领域
        self._console_main_areas_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[11]/div[1]/div/div/div/div[1]/input'
        # 主要领域(语言培训)
        self._console_main_areas_language_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[1]'
        # 是否金吉列(是)
        self._console_edit_whether_jjl_yes_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[14]/div/div/div/div/label[1]/span[1]/span'
        # 是否金吉列(否)
        self._console_edit_whether_jjl_no_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[14]/div/div/div/div/label[2]/span[1]/span'
        # 联系地址
        self._console_edit_contact_address_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[15]/div/div/div/div[1]/input'
        # 机构院校类型输入
        self._console_user_type_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[16]/div/div/div/div[1]/input'
        # 官网输入
        self._console_website_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[17]/div/div/div/div[1]/input'
        # 机构院校介绍输入
        self._console_institution_school_present_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[18]/div/div/div/div[1]/textarea'
        # 委托授权书
        self._console_edit_power_attorney_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[19]/div[1]/div/div/span/div[2]/div/div/div/div'
        # 委托授权书按钮
        self._console_edit_power_attorney_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[19]/div[1]/div/div/span/div[2]/div/div/div/div'
        # 委托授权书上传
        self._console_edit_power_attorney_upload_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[19]/div[1]/div/div/span/div[2]/div/div/div/div/input'
        # 营业执照
        self._console_edit_business_license_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[19]/div[2]/div/div/span/div[2]/div/div/div/div'
        # 营业执照按钮
        self._console_edit_business_license_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[19]/div[2]/div/div/span/div[2]/div/div/div/div'
        # 营业执照上传
        self._console_edit_business_license_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[2]/form/div[19]/div[2]/div/div/span/div/div/div/div/div/input'
        # 机构院校logo
        self._console_edit_institution_school_logo_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[20]/div[1]/div/div/div/div/div/i'
        # 机构院校logo按钮
        self._console_edit_institution_school_logo_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[20]/div[1]/div/div/div/div/div/i'
        # 机构院校logo上传
        self._console_edit_institution_school_logo_upload_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[20]/div[1]/div/div/div/div/div/input'
        # 机构院校主要背景
        self._console_edit_institution_school_background_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[20]/div[2]/div/div/div/div/div/i'
        # 机构院校主要背景按钮
        self._console_edit_institution_school_background_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[20]/div[2]/div/div/div/div/div/i'
        # 机构院校主要背景上传
        self._console_edit_institution_school_background_upload_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[20]/div[2]/div/div/div/div/div/input'
        # 创立时间输入
        self._console_create_time_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[21]/div[1]/div/div/div[1]/input'
        # 法人输入
        self._console_legal_person_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[21]/div[2]/div/div/div[1]/input'
        # 提交按钮
        self._console_refer_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[22]/div[1]/div/div/button[1]/span'
        # endregion Fields

    # region Properties
    @property
    def message_content_text(self):
        """
        属性: 提交成功提示信息
        :return: 提交成功提示信息
        """
        element = None
        try:
            element = self.project.get_element(self._message_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def drop_down_list_select(self):
        """
        属性: 下拉列表
        :return: 下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._drop_down_list_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_institute_name_input(self):
        """
        属性: 搜索-机构院校名称
        :return: 搜索-机构院校名称
        """
        element = None
        try:
            element = self.project.get_element(self._search_institute_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_institute_nature_input(self):
        """
        属性: 搜索-机构院校性质
        :return: 搜索-机构院校性质
        """
        element = None
        try:
            element = self.project.get_element(self._search_institute_nature_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_institute_contact_name_input(self):
        """
        属性: 搜素-联系人姓名
        :return: 搜素-联系人姓名
        """
        element = None
        try:
            element = self.project.get_element(self._search_institute_contact_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_institute_contact_mobile_input(self):
        """
        属性: 搜索-联系电话
        :return: 搜索-联系电话
        """
        element = None
        try:
            element = self.project.get_element(self._search_institute_contact_mobile_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_country_button(self):
        """
        属性: 搜索-所属国家
        :return: 搜索-所属国家
        """
        element = None
        try:
            element = self.project.get_element(self._search_country_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_state_button(self):
        """
        属性: 搜索-状态
        :return: 搜索-状态
        """
        element = None
        try:
            element = self.project.get_element(self._search_state_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_is_jjl_button(self):
        """
        属性: 搜索-是否金吉列
        :return: 搜索-是否金吉列
        """
        element = None
        try:
            element = self.project.get_element(self._search_is_jjl_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_is_cooperation_button(self):
        """
        属性: 搜搜-是否合作院校
        :return: 搜搜-是否合作院校
        """
        element = None
        try:
            element = self.project.get_element(self._search_is_cooperation_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_type_button(self):
        """
        属性: 搜索-类型
        :return: 搜索-类型
        """
        element = None
        try:
            element = self.project.get_element(self._search_type_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_register_time_start_input(self):
        """
        属性: 搜索-注册时间-开始日期
        :return: 搜索-注册时间-开始日期
        """
        element = None
        try:
            element = self.project.get_element(self._search_register_time_start_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_register_time_end_input(self):
        """
        属性: 搜索-注册时间-结束日期
        :return: 搜索-注册时间-结束日期
        """
        element = None
        try:
            element = self.project.get_element(self._search_register_time_end_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_query_button(self):
        """
        属性: 搜索-查询
        :return: 搜索-查询
        """
        element = None
        try:
            element = self.project.get_element(self._search_query_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_clear_button(self):
        """
        属性: 搜索-清除
        :return: 搜索-清除
        """
        element = None
        try:
            element = self.project.get_element(self._search_clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institution_button(self):
        """
        属性: 新增
        :return: 新增
        """
        element = None
        try:
            element = self.project.get_element(self._add_institution_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_institute_id_text(self):
        """
        属性: 列表-第一行-机构院校ID
        :return: 列表-第一行-机构院校ID
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_institute_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_institute_name_text(self):
        """
        属性: 列表-第一行-机构院校名称
        :return: 列表-第一行-机构院校名称
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_institute_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_country_text(self):
        """
        属性: 列表-第一行-所属国家
        :return: 列表-第一行-所属国家
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_country_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_contact_mobile_text(self):
        """
        属性: 列表-第一行-联系电话
        :return: 列表-第一行-联系电话
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_contact_mobile_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_contact_name_text(self):
        """
        属性: 列表-第一行-联系人姓名
        :return: 列表-第一行-联系人姓名
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_contact_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_type_text(self):
        """
        属性: 列表-第一行-类型
        :return: 列表-第一行-类型
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_institute_nature_text(self):
        """
        属性: 列表-第一行-机构院校性质
        :return: 列表-第一行-机构院校性质
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_institute_nature_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_state_text(self):
        """
        属性: 列表-第一行-状态
        :return: 列表-第一行-状态
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_is_cooperation_text(self):
        """
        属性: 列表-是否合作院校
        :return: 列表-是否合作院校
        """
        element = None
        try:
            element = self.project.get_element(self._list_is_cooperation_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_register_time_text(self):
        """
        属性: 列表-注册时间
        :return: 列表-注册时间
        """
        element = None
        try:
            element = self.project.get_element(self._list_register_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_execute_first_button(self):
        """
        属性: 列表-操作-第一个操作
        :return: 列表-操作-第一个操作
        """
        element = None
        try:
            element = self.project.get_element(self._list_execute_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_execute_second_button(self):
        """
        属性: 列表-操作-第二个操作
        :return: 列表-操作-第二个操作
        """
        element = None
        try:
            element = self.project.get_element(self._list_execute_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_execute_third_button(self):
        """
        属性: 列表-操作-第三个操作
        :return: 列表-操作-第三个操作
        """
        element = None
        try:
            element = self.project.get_element(self._list_execute_third_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_title_text(self):
        """
        属性: 新增-标题
        :return: 新增-标题
        """
        element = None
        try:
            element = self.project.get_element(self._add_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_tab_first_button(self):
        """
        属性: 新增-第一个菜单
        :return: 新增-第一个菜单
        """
        element = None
        try:
            element = self.project.get_element(self._add_tab_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_username_input(self):
        """
        属性: 新增-用户账号
        :return: 新增-用户账号
        """
        element = None
        try:
            element = self.project.get_element(self._add_username_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_password_input(self):
        """
        属性: 新增-用户密码
        :return: 新增-用户密码
        """
        element = None
        try:
            element = self.project.get_element(self._add_password_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_real_name_input(self):
        """
        属性: 新增-真实姓名
        :return: 新增-真实姓名
        """
        element = None
        try:
            element = self.project.get_element(self._add_real_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_nick_input(self):
        """
        属性: 新增-用户昵称
        :return: 新增-用户昵称
        """
        element = None
        try:
            element = self.project.get_element(self._add_nick_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_name_input(self):
        """
        属性: 新增-机构院校名称
        :return: 新增-机构院校名称
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_name_en_input(self):
        """
        属性: 新增-机构院校名称（英文）
        :return: 新增-机构院校名称（英文）
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_name_en_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_contact_name_input(self):
        """
        属性: 新增-联系人
        :return: 新增-联系人
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_contact_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_contact_phone_area_code_button(self):
        """
        属性: 新增-联系电话-区号
        :return: 新增-联系电话-区号
        """
        element = None
        try:
            element = self.project.get_element(self._add_contact_phone_area_code_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_contact_phone_input(self):
        """
        属性: 新增-联系电话-电话号码
        :return: 新增-联系电话-电话号码
        """
        element = None
        try:
            element = self.project.get_element(self._add_contact_phone_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_nature_input(self):
        """
        属性: 新增-机构院校性质
        :return: 新增-机构院校性质
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_nature_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_contact_mobile_input(self):
        """
        属性: 新增-联系人手机号
        :return: 新增-联系人手机号
        """
        element = None
        try:
            element = self.project.get_element(self._add_contact_mobile_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_country_button(self):
        """
        属性: 新增-所属国家
        :return: 新增-所属国家
        """
        element = None
        try:
            element = self.project.get_element(self._add_country_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_email_input(self):
        """
        属性: 新增-邮箱
        :return: 新增-邮箱
        """
        element = None
        try:
            element = self.project.get_element(self._add_email_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_type_button(self):
        """
        属性: 新增-类型
        :return: 新增-类型
        """
        element = None
        try:
            element = self.project.get_element(self._add_type_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_category_button(self):
        """
        属性: 新增-所属频道
        :return: 新增-所属频道
        """
        element = None
        try:
            element = self.project.get_element(self._add_category_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_main_field_button(self):
        """
        属性: 新增-主要领域
        :return: 新增-主要领域
        """
        element = None
        try:
            element = self.project.get_element(self._add_main_field_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_apply_channel_first_button(self):
        """
        属性: 新增-申请频道-第一个
        :return: 新增-申请频道-第一个
        """
        element = None
        try:
            element = self.project.get_element(self._add_apply_channel_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_apply_channel_second_button(self):
        """
        属性: 新增-申请频道-第二个
        :return: 新增-申请频道-第二个
        """
        element = None
        try:
            element = self.project.get_element(self._add_apply_channel_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_apply_channel_third_button(self):
        """
        属性: 新增-申请频道-第三个
        :return: 新增-申请频道-第三个
        """
        element = None
        try:
            element = self.project.get_element(self._add_apply_channel_third_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_apply_channel_fourth_button(self):
        """
        属性: 新增-申请频道-第四个
        :return: 新增-申请频道-第四个
        """
        element = None
        try:
            element = self.project.get_element(self._add_apply_channel_fourth_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_apply_channel_fifth_button(self):
        """
        属性: 新增-申请频道-第五个
        :return: 新增-申请频道-第五个
        """
        element = None
        try:
            element = self.project.get_element(self._add_apply_channel_fifth_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_bank_card_number_input(self):
        """
        属性: 新增-银行卡号码
        :return: 新增-银行卡号码
        """
        element = None
        try:
            element = self.project.get_element(self._add_bank_card_number_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_open_bank_name_input(self):
        """
        属性: 新增-开户行名称
        :return: 新增-开户行名称
        """
        element = None
        try:
            element = self.project.get_element(self._add_open_bank_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_bank_code_input(self):
        """
        属性: 新增-行号
        :return: 新增-行号
        """
        element = None
        try:
            element = self.project.get_element(self._add_bank_code_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_company_full_name_input(self):
        """
        属性: 新增-公司全称
        :return: 新增-公司全称
        """
        element = None
        try:
            element = self.project.get_element(self._add_company_full_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_is_jjl_yes_button(self):
        """
        属性: 新增-机构-是否属于金吉列-是
        :return: 新增-机构-是否属于金吉列-是
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_is_jjl_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_is_jjl_no_button(self):
        """
        属性: 新增-机构-是否属于金吉列-否
        :return: 新增-机构-是否属于金吉列-否
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_is_jjl_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_address_input(self):
        """
        属性: 新增-机构-联系地址
        :return: 新增-机构-联系地址
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_address_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_institute_type_input(self):
        """
        属性: 新增-机构-机构院校类型
        :return: 新增-机构-机构院校类型
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_institute_type_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_official_website_input(self):
        """
        属性: 新增-机构-机构官网
        :return: 新增-机构-机构官网
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_official_website_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_institute_introduction_input(self):
        """
        属性: 新增-机构-机构院校介绍
        :return: 新增-机构-机构院校介绍
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_institute_introduction_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_power_of_attorney_input(self):
        """
        属性: 新增-机构-授权委托书
        :return: 新增-机构-授权委托书
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_power_of_attorney_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_business_license_input(self):
        """
        属性: 新增-机构-营业执照或其他合法资质证照
        :return: 新增-机构-营业执照或其他合法资质证照
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_business_license_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_institute_logo_input(self):
        """
        属性: 新增-机构-机构院校logo
        :return: 新增-机构-机构院校logo
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_institute_logo_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_institute_background_main_page_input(self):
        """
        属性: 新增-机构-机构院校主页背景
        :return: 新增-机构-机构院校主页背景
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_institute_background_main_page_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_create_time_input(self):
        """
        属性: 新增-机构-创立时间
        :return: 新增-机构-创立时间
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_create_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_institute_juridical_person_input(self):
        """
        属性: 新增-机构-法人
        :return: 新增-机构-法人
        """
        element = None
        try:
            element = self.project.get_element(self._add_institute_juridical_person_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_is_cooperation_yes_button(self):
        """
        属性: 新增-院校-是否合作院校-是
        :return: 新增-院校-是否合作院校-是
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_is_cooperation_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_is_cooperation_no_button(self):
        """
        属性: 编辑-院校-是否合作院校-否
        :return: 编辑-院校-是否合作院校-否
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_is_cooperation_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_qualification_first_button(self):
        """
        属性: 编辑-院校-学历-第一个
        :return: 编辑-院校-学历-第一个
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_qualification_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_qualification_second_button(self):
        """
        属性: 编辑-院校-学历-第二个
        :return: 编辑-院校-学历-第二个
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_qualification_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_specialities_first_button(self):
        """
        属性: 编辑-院校-专业-第一个
        :return: 编辑-院校-专业-第一个
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_specialities_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_specialities_second_button(self):
        """
        属性: 编辑-院校-专业-第二个
        :return: 编辑-院校-专业-第二个
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_specialities_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_address_input(self):
        """
        属性: 编辑-院校-联系地址
        :return: 编辑-院校-联系地址
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_address_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_institute_type_input(self):
        """
        属性: 编辑-院校-机构院校类型
        :return: 编辑-院校-机构院校类型
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_institute_type_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_official_website_input(self):
        """
        属性: 编辑-院校-机构官网
        :return: 编辑-院校-机构官网
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_official_website_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_institute_introduction_input(self):
        """
        属性: 编辑-院校-机构院校介绍
        :return: 编辑-院校-机构院校介绍
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_institute_introduction_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_power_of_attorney_input(self):
        """
        属性: 编辑-院校-授权委托书
        :return: 编辑-院校-授权委托书
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_power_of_attorney_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_business_license_input(self):
        """
        属性: 编辑-院校-营业执照或其他合法资质证照
        :return: 编辑-院校-营业执照或其他合法资质证照
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_business_license_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_institute_logo_input(self):
        """
        属性: 编辑-院校-机构院校logo
        :return: 编辑-院校-机构院校logo
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_institute_logo_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_institute_background_main_page_input(self):
        """
        属性: 编辑-院校-机构院校主页背景
        :return: 编辑-院校-机构院校主页背景
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_institute_background_main_page_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_create_time_input(self):
        """
        属性: 编辑-院校-创立时间
        :return: 编辑-院校-创立时间
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_create_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_juridical_person_input(self):
        """
        属性: 编辑-院校-法人
        :return: 编辑-院校-法人
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_juridical_person_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_cooperation_start_time_input(self):
        """
        属性: 编辑-院校-合作开始时间
        :return: 编辑-院校-合作开始时间
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_cooperation_start_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_cooperation_end_time_input(self):
        """
        属性: 编辑-院校-合作结束时间
        :return: 编辑-院校-合作结束时间
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_cooperation_end_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_commit_button(self):
        """
        属性: 新增-提交
        :return: 新增-提交
        """
        element = None
        try:
            element = self.project.get_element(self._add_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_cancel_button(self):
        """
        属性: 新增-取消
        :return: 新增-取消
        """
        element = None
        try:
            element = self.project.get_element(self._add_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_title_text(self):
        """
        属性: 编辑-标题
        :return: 编辑-标题
        """
        element = None
        try:
            element = self.project.get_element(self._edit_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_tab_first_button(self):
        """
        属性: 编辑-第一个菜单
        :return: 编辑-第一个菜单
        """
        element = None
        try:
            element = self.project.get_element(self._edit_tab_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_id_input(self):
        """
        属性: 编辑-机构院校ID
        :return: 编辑-机构院校ID
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_register_time_input(self):
        """
        属性: 编辑-注册时间
        :return: 编辑-注册时间
        """
        element = None
        try:
            element = self.project.get_element(self._edit_register_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_create_user_input(self):
        """
        属性: 编辑-创建人员
        :return: 编辑-创建人员
        """
        element = None
        try:
            element = self.project.get_element(self._edit_create_user_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_review_state_input(self):
        """
        属性: 编辑-审核状态
        :return: 编辑-审核状态
        """
        element = None
        try:
            element = self.project.get_element(self._edit_review_state_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_username_input(self):
        """
        属性: 编辑-用户账号
        :return: 编辑-用户账号
        """
        element = None
        try:
            element = self.project.get_element(self._edit_username_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_password_input(self):
        """
        属性: 编辑-用户密码
        :return: 编辑-用户密码
        """
        element = None
        try:
            element = self.project.get_element(self._edit_password_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_real_name_input(self):
        """
        属性: 编辑-真实姓名
        :return: 编辑-真实姓名
        """
        element = None
        try:
            element = self.project.get_element(self._edit_real_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_nick_input(self):
        """
        属性: 编辑-用户昵称
        :return: 编辑-用户昵称
        """
        element = None
        try:
            element = self.project.get_element(self._edit_nick_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_name_input(self):
        """
        属性: 编辑-机构院校名称
        :return: 编辑-机构院校名称
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_name_en_input(self):
        """
        属性: 编辑-机构院校名称（英文）
        :return: 编辑-机构院校名称（英文）
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_name_en_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_contact_name_input(self):
        """
        属性: 编辑-联系人
        :return: 编辑-联系人
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_contact_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_contact_phone_area_code_button(self):
        """
        属性: 编辑-联系电话-区号
        :return: 编辑-联系电话-区号
        """
        element = None
        try:
            element = self.project.get_element(self._edit_contact_phone_area_code_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_contact_phone_input(self):
        """
        属性: 编辑-联系电话-电话号码
        :return: 编辑-联系电话-电话号码
        """
        element = None
        try:
            element = self.project.get_element(self._edit_contact_phone_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_nature_input(self):
        """
        属性: 编辑-机构院校性质
        :return: 编辑-机构院校性质
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_nature_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_contact_mobile_input(self):
        """
        属性: 编辑-联系人手机号
        :return: 编辑-联系人手机号
        """
        element = None
        try:
            element = self.project.get_element(self._edit_contact_mobile_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_country_button(self):
        """
        属性: 编辑-所属国家
        :return: 编辑-所属国家
        """
        element = None
        try:
            element = self.project.get_element(self._edit_country_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_email_input(self):
        """
        属性: 编辑-邮箱
        :return: 编辑-邮箱
        """
        element = None
        try:
            element = self.project.get_element(self._edit_email_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_type_button(self):
        """
        属性: 编辑-类型
        :return: 编辑-类型
        """
        element = None
        try:
            element = self.project.get_element(self._edit_type_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_category_button(self):
        """
        属性: 编辑-所属频道
        :return: 编辑-所属频道
        """
        element = None
        try:
            element = self.project.get_element(self._edit_category_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_main_field_button(self):
        """
        属性: 编辑-主要领域
        :return: 编辑-主要领域
        """
        element = None
        try:
            element = self.project.get_element(self._edit_main_field_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_apply_channel_first_button(self):
        """
        属性: 编辑-申请频道-第一个
        :return: 编辑-申请频道-第一个
        """
        element = None
        try:
            element = self.project.get_element(self._edit_apply_channel_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_apply_channel_second_button(self):
        """
        属性: 编辑-申请频道-第二个
        :return: 编辑-申请频道-第二个
        """
        element = None
        try:
            element = self.project.get_element(self._edit_apply_channel_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_apply_channel_third_button(self):
        """
        属性: 编辑-申请频道-第三个
        :return: 编辑-申请频道-第三个
        """
        element = None
        try:
            element = self.project.get_element(self._edit_apply_channel_third_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_apply_channel_fourth_button(self):
        """
        属性: 编辑-申请频道-第四个
        :return: 编辑-申请频道-第四个
        """
        element = None
        try:
            element = self.project.get_element(self._edit_apply_channel_fourth_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_apply_channel_fifth_button(self):
        """
        属性: 编辑-申请频道-第五个
        :return: 编辑-申请频道-第五个
        """
        element = None
        try:
            element = self.project.get_element(self._edit_apply_channel_fifth_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_bank_card_number_input(self):
        """
        属性: 编辑-银行卡号码
        :return: 编辑-银行卡号码
        """
        element = None
        try:
            element = self.project.get_element(self._edit_bank_card_number_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_open_bank_name_input(self):
        """
        属性: 编辑-开户行名称
        :return: 编辑-开户行名称
        """
        element = None
        try:
            element = self.project.get_element(self._edit_open_bank_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_bank_code_input(self):
        """
        属性: 编辑-行号
        :return: 编辑-行号
        """
        element = None
        try:
            element = self.project.get_element(self._edit_bank_code_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_company_full_name_input(self):
        """
        属性: 编辑-公司全称
        :return: 编辑-公司全称
        """
        element = None
        try:
            element = self.project.get_element(self._edit_company_full_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_is_jjl_yes_button(self):
        """
        属性: 编辑-机构-是否属于金吉列-是
        :return: 编辑-机构-是否属于金吉列-是
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_is_jjl_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_is_jjl_no_button(self):
        """
        属性: 编辑-机构-是否属于金吉列-否
        :return: 编辑-机构-是否属于金吉列-否
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_is_jjl_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_address_input(self):
        """
        属性: 编辑-机构-联系地址
        :return: 编辑-机构-联系地址
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_address_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_institute_type_input(self):
        """
        属性: 编辑-机构-机构院校类型
        :return: 编辑-机构-机构院校类型
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_institute_type_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_official_website_input(self):
        """
        属性: 编辑-机构-机构官网
        :return: 编辑-机构-机构官网
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_official_website_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_institute_introduction_input(self):
        """
        属性: 编辑-机构-机构院校介绍
        :return: 编辑-机构-机构院校介绍
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_institute_introduction_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_power_of_attorney_input(self):
        """
        属性: 编辑-机构-授权委托书
        :return: 编辑-机构-授权委托书
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_power_of_attorney_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_business_license_input(self):
        """
        属性: 编辑-机构-营业执照或其他合法资质证照
        :return: 编辑-机构-营业执照或其他合法资质证照
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_business_license_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_institute_logo_input(self):
        """
        属性: 编辑-机构-机构院校logo
        :return: 编辑-机构-机构院校logo
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_institute_logo_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_institute_background_main_page_input(self):
        """
        属性: 编辑-机构-机构院校主页背景
        :return: 编辑-机构-机构院校主页背景
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_institute_background_main_page_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_create_time_input(self):
        """
        属性: 编辑-机构-创立时间
        :return: 编辑-机构-创立时间
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_create_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_institute_juridical_person_input(self):
        """
        属性: 编辑-机构-法人
        :return: 编辑-机构-法人
        """
        element = None
        try:
            element = self.project.get_element(self._edit_institute_juridical_person_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_country_region_button(self):
        """
        属性: 编辑-院校-国家及地区
        :return: 编辑-院校-国家及地区
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_country_region_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_is_cooperation_yes_button(self):
        """
        属性: 编辑-院校-是否合作院校-是
        :return: 编辑-院校-是否合作院校-是
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_is_cooperation_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_is_cooperation_no_button(self):
        """
        属性: 编辑-院校-是否合作院校-否
        :return: 编辑-院校-是否合作院校-否
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_is_cooperation_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_qualification_first_button(self):
        """
        属性: 编辑-院校-学历-第一个
        :return: 编辑-院校-学历-第一个
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_qualification_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_qualification_second_button(self):
        """
        属性: 编辑-院校-学历-第二个
        :return: 编辑-院校-学历-第二个
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_qualification_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_specialities_first_button(self):
        """
        属性: 编辑-院校-专业-第一个
        :return: 编辑-院校-专业-第一个
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_specialities_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_specialities_second_button(self):
        """
        属性: 编辑-院校-专业-第二个
        :return: 编辑-院校-专业-第二个
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_specialities_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_address_input(self):
        """
        属性: 编辑-院校-联系地址
        :return: 编辑-院校-联系地址
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_address_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_institute_type_input(self):
        """
        属性: 编辑-院校-机构院校类型
        :return: 编辑-院校-机构院校类型
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_institute_type_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_official_website_input(self):
        """
        属性: 编辑-院校-机构官网
        :return: 编辑-院校-机构官网
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_official_website_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_institute_introduction_input(self):
        """
        属性: 编辑-院校-机构院校介绍
        :return: 编辑-院校-机构院校介绍
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_institute_introduction_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_power_of_attorney_input(self):
        """
        属性: 编辑-院校-授权委托书
        :return: 编辑-院校-授权委托书
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_power_of_attorney_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_business_license_input(self):
        """
        属性: 编辑-院校-营业执照或其他合法资质证照
        :return: 编辑-院校-营业执照或其他合法资质证照
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_business_license_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_institute_logo_input(self):
        """
        属性: 编辑-院校-机构院校logo
        :return: 编辑-院校-机构院校logo
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_institute_logo_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_institute_background_main_page_input(self):
        """
        属性: 编辑-院校-机构院校主页背景
        :return: 编辑-院校-机构院校主页背景
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_institute_background_main_page_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_create_time_input(self):
        """
        属性: 编辑-院校-创立时间
        :return: 编辑-院校-创立时间
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_create_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_juridical_person_input(self):
        """
        属性: 编辑-院校-法人
        :return: 编辑-院校-法人
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_juridical_person_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_cooperation_start_time_input(self):
        """
        属性: 编辑-院校-合作开始时间
        :return: 编辑-院校-合作开始时间
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_cooperation_start_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_school_cooperation_end_time_input(self):
        """
        属性: 编辑-院校-合作结束时间
        :return: 编辑-院校-合作结束时间
        """
        element = None
        try:
            element = self.project.get_element(self._edit_school_cooperation_end_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_commit_button(self):
        """
        属性: 编辑-提交
        :return: 编辑-提交
        """
        element = None
        try:
            element = self.project.get_element(self._edit_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_cancel_button(self):
        """
        属性: 编辑-取消
        :return: 编辑-取消
        """
        element = None
        try:
            element = self.project.get_element(self._edit_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_user_center_top_button(self):
        """
        属性: 用户中心导航
        :return: 用户中心导航
        """
        element = None
        try:
            element = self.project.get_element(self._console_user_center_top_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_institution_manage_left_button(self):
        """
        属性: 机构院校管理左侧导航
        :return: 机构院校管理左侧导航
        """
        element = None
        try:
            element = self.project.get_element(self._console_institution_manage_left_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_institution_list_button(self):
        """
        属性: 机构院校列表按钮
        :return: 机构院校列表按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_institution_list_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_institution_list_name_text(self):
        """
        属性: 机构院校列表表名
        :return: 机构院校列表表名
        """
        element = None
        try:
            element = self.project.get_element(self._console_institution_list_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_contact_mobile_input(self):
        """
        属性: 联系人电话输入
        :return: 联系人电话输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_contact_mobile_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_is_not_jjl_button(self):
        """
        属性: 是否金吉列
        :return: 是否金吉列
        """
        element = None
        try:
            element = self.project.get_element(self._console_is_not_jjl_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_is_not_jjl_not_button(self):
        """
        属性: 是否金吉列(否)
        :return: 是否金吉列(否)
        """
        element = None
        try:
            element = self.project.get_element(self._console_is_not_jjl_not_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_is_not_jjl_yes_button(self):
        """
        属性: 是否金吉列(是)
        :return: 是否金吉列(是)
        """
        element = None
        try:
            element = self.project.get_element(self._console_is_not_jjl_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_is_not_teamwork_button(self):
        """
        属性: 是否合作院校
        :return: 是否合作院校
        """
        element = None
        try:
            element = self.project.get_element(self._console_is_not_teamwork_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_is_not_teamwork_yes_button(self):
        """
        属性: 是否合作院校(是)
        :return: 是否合作院校(是)
        """
        element = None
        try:
            element = self.project.get_element(self._console_is_not_teamwork_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_is_not_teamwork_not_button(self):
        """
        属性: 是否合作院校(否)
        :return: 是否合作院校(否)
        """
        element = None
        try:
            element = self.project.get_element(self._console_is_not_teamwork_not_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_at_country_button(self):
        """
        属性: 所属国家
        :return: 所属国家
        """
        element = None
        try:
            element = self.project.get_element(self._console_at_country_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_at_country_china_button(self):
        """
        属性: 所属国家(中国)
        :return: 所属国家(中国)
        """
        element = None
        try:
            element = self.project.get_element(self._console_at_country_china_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_status_button(self):
        """
        属性: 状态
        :return: 状态
        """
        element = None
        try:
            element = self.project.get_element(self._console_status_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_status_on_button(self):
        """
        属性: 状态(正常)
        :return: 状态(正常)
        """
        element = None
        try:
            element = self.project.get_element(self._console_status_on_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_status_off_button(self):
        """
        属性: 状态(禁用)
        :return: 状态(禁用)
        """
        element = None
        try:
            element = self.project.get_element(self._console_status_off_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_contact_name_input(self):
        """
        属性: 联系人姓名输入
        :return: 联系人姓名输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_contact_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_category_button(self):
        """
        属性: 类型
        :return: 类型
        """
        element = None
        try:
            element = self.project.get_element(self._console_category_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_category_institution_button(self):
        """
        属性: 类别(机构)
        :return: 类别(机构)
        """
        element = None
        try:
            element = self.project.get_element(self._console_category_institution_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_category_school_button(self):
        """
        属性: 类别(院校)
        :return: 类别(院校)
        """
        element = None
        try:
            element = self.project.get_element(self._console_category_school_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_institution_school_name_input(self):
        """
        属性: 机构院校名称输入
        :return: 机构院校名称输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_institution_school_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_inquiry_button(self):
        """
        属性: 查询按钮
        :return: 查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_inquiry_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_clean_button(self):
        """
        属性: 清除按钮
        :return: 清除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_clean_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_institution_school_create_button(self):
        """
        属性: 新增按钮
        :return: 新增按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_institution_school_create_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_inquiry_value_name_text(self):
        """
        属性: 查询数据名称
        :return: 查询数据名称
        """
        element = None
        try:
            element = self.project.get_element(self._console_inquiry_value_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_inquiry_value_edit_button(self):
        """
        属性: 编辑操作按钮
        :return: 编辑操作按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_inquiry_value_edit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_form_text(self):
        """
        属性: 编辑页表单名称
        :return: 编辑页表单名称
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_form_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_user_account_input(self):
        """
        属性: 用户账号输入
        :return: 用户账号输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_user_account_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_user_passwd_input(self):
        """
        属性: 用户密码输入
        :return: 用户密码输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_user_passwd_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_real_name_input(self):
        """
        属性: 真实姓名输入框
        :return: 真实姓名输入框
        """
        element = None
        try:
            element = self.project.get_element(self._console_real_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_user_nick_name_input(self):
        """
        属性: 用户昵称输入
        :return: 用户昵称输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_user_nick_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_institution_school_input(self):
        """
        属性: 机构院校名称输入
        :return: 机构院校名称输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_institution_school_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_institution_school_short_input(self):
        """
        属性: 机构院校简称
        :return: 机构院校简称
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_institution_school_short_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_english_name_input(self):
        """
        属性: 机构院校英文名称输入
        :return: 机构院校英文名称输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_english_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_contact_person_input(self):
        """
        属性: 联系人输入
        :return: 联系人输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_contact_person_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_contact_mobile_input(self):
        """
        属性: 联系电话输入
        :return: 联系电话输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_contact_mobile_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_nature_input(self):
        """
        属性: 机构院校性质输入
        :return: 机构院校性质输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_nature_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_contact_user_mobile_input(self):
        """
        属性: 联系人手机号输入
        :return: 联系人手机号输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_contact_user_mobile_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_user_at_country_button(self):
        """
        属性: 所属国家
        :return: 所属国家
        """
        element = None
        try:
            element = self.project.get_element(self._console_user_at_country_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_user_at_china_button(self):
        """
        属性: 中国
        :return: 中国
        """
        element = None
        try:
            element = self.project.get_element(self._console_user_at_china_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_user_at_colombia_button(self):
        """
        属性: 哥伦比亚
        :return: 哥伦比亚
        """
        element = None
        try:
            element = self.project.get_element(self._console_user_at_colombia_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_email_input(self):
        """
        属性: 邮箱输入
        :return: 邮箱输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_email_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_type_button(self):
        """
        属性: 类型选择
        :return: 类型选择
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_type_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_type_institution_button(self):
        """
        属性: 类型(机构)
        :return: 类型(机构)
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_type_institution_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_type_school_button(self):
        """
        属性: 类型(院校)
        :return: 类型(院校)
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_type_school_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_channel_button(self):
        """
        属性: 所属频道
        :return: 所属频道
        """
        element = None
        try:
            element = self.project.get_element(self._console_channel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_channel_language_button(self):
        """
        属性: 所属频道(语言培训)
        :return: 所属频道(语言培训)
        """
        element = None
        try:
            element = self.project.get_element(self._console_channel_language_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_channel_language_create_button(self):
        """
        属性: 所属频道(语言培训创建)
        :return: 所属频道(语言培训创建)
        """
        element = None
        try:
            element = self.project.get_element(self._console_channel_language_create_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_main_areas_button(self):
        """
        属性: 主要领域
        :return: 主要领域
        """
        element = None
        try:
            element = self.project.get_element(self._console_main_areas_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_main_areas_language_button(self):
        """
        属性: 主要领域(语言培训)
        :return: 主要领域(语言培训)
        """
        element = None
        try:
            element = self.project.get_element(self._console_main_areas_language_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_whether_jjl_yes_button(self):
        """
        属性: 是否金吉列(是)
        :return: 是否金吉列(是)
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_whether_jjl_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_whether_jjl_no_button(self):
        """
        属性: 是否金吉列(否)
        :return: 是否金吉列(否)
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_whether_jjl_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_contact_address_input(self):
        """
        属性: 联系地址
        :return: 联系地址
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_contact_address_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_user_type_input(self):
        """
        属性: 机构院校类型输入
        :return: 机构院校类型输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_user_type_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_website_input(self):
        """
        属性: 官网输入
        :return: 官网输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_website_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_institution_school_present_input(self):
        """
        属性: 机构院校介绍输入
        :return: 机构院校介绍输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_institution_school_present_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_power_attorney_input(self):
        """
        属性: 委托授权书
        :return: 委托授权书
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_power_attorney_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_power_attorney_button(self):
        """
        属性: 委托授权书按钮
        :return: 委托授权书按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_power_attorney_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_power_attorney_upload_input(self):
        """
        属性: 委托授权书上传
        :return: 委托授权书上传
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_power_attorney_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_business_license_input(self):
        """
        属性: 营业执照
        :return: 营业执照
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_business_license_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_business_license_button(self):
        """
        属性: 营业执照按钮
        :return: 营业执照按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_business_license_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_business_license_upload_input(self):
        """
        属性: 营业执照上传
        :return: 营业执照上传
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_business_license_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_institution_school_logo_input(self):
        """
        属性: 机构院校logo
        :return: 机构院校logo
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_institution_school_logo_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_institution_school_logo_button(self):
        """
        属性: 机构院校logo按钮
        :return: 机构院校logo按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_institution_school_logo_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_institution_school_logo_upload_input(self):
        """
        属性: 机构院校logo上传
        :return: 机构院校logo上传
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_institution_school_logo_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_institution_school_background_input(self):
        """
        属性: 机构院校主要背景
        :return: 机构院校主要背景
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_institution_school_background_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_institution_school_background_button(self):
        """
        属性: 机构院校主要背景按钮
        :return: 机构院校主要背景按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_institution_school_background_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_edit_institution_school_background_upload_input(self):
        """
        属性: 机构院校主要背景上传
        :return: 机构院校主要背景上传
        """
        element = None
        try:
            element = self.project.get_element(self._console_edit_institution_school_background_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_create_time_input(self):
        """
        属性: 创立时间输入
        :return: 创立时间输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_create_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_legal_person_input(self):
        """
        属性: 法人输入
        :return: 法人输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_legal_person_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_refer_button(self):
        """
        属性: 提交按钮
        :return: 提交按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_refer_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def get_message_content_text_action(self):
        """
        动作：获取提交成功提示信息的文本
        :return: '提交成功提示信息'的文本
        """
        control_content = self.project.get_element_text(self.message_content_text)
        return control_content

    def get_select_drop_down_list_action(self, drop_down_list_select):
        """
        动作：获取下拉列表列表选中的文本
        :param drop_down_list_select: 下拉列表列表索引或文本
        :return: '下拉列表'的文本
        """
        control_content = self.project.get_select_content(self.drop_down_list_select, drop_down_list_select)
        return control_content

    def select_drop_down_list_action(self, drop_down_list_select):
        """
        动作：选择下拉列表
        :param drop_down_list_select: 下拉列表列表索引或文本
        :return: 选择'下拉列表'选择器后的页面
        """
        self.project.select_control(self.drop_down_list_select, drop_down_list_select)
        return self.project.get_current_page_source()

    def set_search_institute_name_input_action(self, search_institute_name_input):
        """
        动作：设置搜索-机构院校名称
        :param search_institute_name_input: 搜索-机构院校名称
        :return: 设置'搜索-机构院校名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_institute_name_input, search_institute_name_input)
        return self.project.get_current_page_source()

    def set_search_institute_nature_input_action(self, search_institute_nature_input):
        """
        动作：设置搜索-机构院校性质
        :param search_institute_nature_input: 搜索-机构院校性质
        :return: 设置'搜索-机构院校性质'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_institute_nature_input, search_institute_nature_input)
        return self.project.get_current_page_source()

    def set_search_institute_contact_name_input_action(self, search_institute_contact_name_input):
        """
        动作：设置搜素-联系人姓名
        :param search_institute_contact_name_input: 搜素-联系人姓名
        :return: 设置'搜素-联系人姓名'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_institute_contact_name_input, search_institute_contact_name_input)
        return self.project.get_current_page_source()

    def set_search_institute_contact_mobile_input_action(self, search_institute_contact_mobile_input):
        """
        动作：设置搜索-联系电话
        :param search_institute_contact_mobile_input: 搜索-联系电话
        :return: 设置'搜索-联系电话'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_institute_contact_mobile_input, search_institute_contact_mobile_input)
        return self.project.get_current_page_source()

    def click_search_country_button_action(self):
        """
        动作：点击搜索-所属国家
        :return: 点击'搜索-所属国家'按钮后的页面
        """
        self.project.click(self.search_country_button)
        return self.project.get_current_page_source()

    def click_search_state_button_action(self):
        """
        动作：点击搜索-状态
        :return: 点击'搜索-状态'按钮后的页面
        """
        self.project.click(self.search_state_button)
        return self.project.get_current_page_source()

    def click_search_is_jjl_button_action(self):
        """
        动作：点击搜索-是否金吉列
        :return: 点击'搜索-是否金吉列'按钮后的页面
        """
        self.project.click(self.search_is_jjl_button)
        return self.project.get_current_page_source()

    def click_search_is_cooperation_button_action(self):
        """
        动作：点击搜搜-是否合作院校
        :return: 点击'搜搜-是否合作院校'按钮后的页面
        """
        self.project.click(self.search_is_cooperation_button)
        return self.project.get_current_page_source()

    def click_search_type_button_action(self):
        """
        动作：点击搜索-类型
        :return: 点击'搜索-类型'按钮后的页面
        """
        self.project.click(self.search_type_button)
        return self.project.get_current_page_source()

    def set_search_register_time_start_input_action(self, search_register_time_start_input):
        """
        动作：设置搜索-注册时间-开始日期
        :param search_register_time_start_input: 搜索-注册时间-开始日期
        :return: 设置'搜索-注册时间-开始日期'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_register_time_start_input, search_register_time_start_input)
        return self.project.get_current_page_source()

    def set_search_register_time_end_input_action(self, search_register_time_end_input):
        """
        动作：设置搜索-注册时间-结束日期
        :param search_register_time_end_input: 搜索-注册时间-结束日期
        :return: 设置'搜索-注册时间-结束日期'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_register_time_end_input, search_register_time_end_input)
        return self.project.get_current_page_source()

    def click_search_query_button_action(self):
        """
        动作：点击搜索-查询
        :return: 点击'搜索-查询'按钮后的页面
        """
        self.project.click(self.search_query_button)
        return self.project.get_current_page_source()

    def click_search_clear_button_action(self):
        """
        动作：点击搜索-清除
        :return: 点击'搜索-清除'按钮后的页面
        """
        self.project.click(self.search_clear_button)
        return self.project.get_current_page_source()

    def click_add_institution_button_action(self):
        """
        动作：点击新增
        :return: 点击'新增'按钮后的页面
        """
        self.project.click(self.add_institution_button)
        return self.project.get_current_page_source()

    def get_list_first_institute_id_text_action(self):
        """
        动作：获取列表-第一行-机构院校ID的文本
        :return: '列表-第一行-机构院校ID'的文本
        """
        control_content = self.project.get_element_text(self.list_first_institute_id_text)
        return control_content

    def get_list_first_institute_name_text_action(self):
        """
        动作：获取列表-第一行-机构院校名称的文本
        :return: '列表-第一行-机构院校名称'的文本
        """
        control_content = self.project.get_element_text(self.list_first_institute_name_text)
        return control_content

    def get_list_first_country_text_action(self):
        """
        动作：获取列表-第一行-所属国家的文本
        :return: '列表-第一行-所属国家'的文本
        """
        control_content = self.project.get_element_text(self.list_first_country_text)
        return control_content

    def get_list_first_contact_mobile_text_action(self):
        """
        动作：获取列表-第一行-联系电话的文本
        :return: '列表-第一行-联系电话'的文本
        """
        control_content = self.project.get_element_text(self.list_first_contact_mobile_text)
        return control_content

    def get_list_first_contact_name_text_action(self):
        """
        动作：获取列表-第一行-联系人姓名的文本
        :return: '列表-第一行-联系人姓名'的文本
        """
        control_content = self.project.get_element_text(self.list_first_contact_name_text)
        return control_content

    def get_list_first_type_text_action(self):
        """
        动作：获取列表-第一行-类型的文本
        :return: '列表-第一行-类型'的文本
        """
        control_content = self.project.get_element_text(self.list_first_type_text)
        return control_content

    def get_list_first_institute_nature_text_action(self):
        """
        动作：获取列表-第一行-机构院校性质的文本
        :return: '列表-第一行-机构院校性质'的文本
        """
        control_content = self.project.get_element_text(self.list_first_institute_nature_text)
        return control_content

    def get_list_first_state_text_action(self):
        """
        动作：获取列表-第一行-状态的文本
        :return: '列表-第一行-状态'的文本
        """
        control_content = self.project.get_element_text(self.list_first_state_text)
        return control_content

    def get_list_is_cooperation_text_action(self):
        """
        动作：获取列表-是否合作院校的文本
        :return: '列表-是否合作院校'的文本
        """
        control_content = self.project.get_element_text(self.list_is_cooperation_text)
        return control_content

    def get_list_register_time_text_action(self):
        """
        动作：获取列表-注册时间的文本
        :return: '列表-注册时间'的文本
        """
        control_content = self.project.get_element_text(self.list_register_time_text)
        return control_content

    def click_list_execute_first_button_action(self):
        """
        动作：点击列表-操作-第一个操作
        :return: 点击'列表-操作-第一个操作'按钮后的页面
        """
        self.project.click(self.list_execute_first_button)
        return self.project.get_current_page_source()

    def click_list_execute_second_button_action(self):
        """
        动作：点击列表-操作-第二个操作
        :return: 点击'列表-操作-第二个操作'按钮后的页面
        """
        self.project.click(self.list_execute_second_button)
        return self.project.get_current_page_source()

    def click_list_execute_third_button_action(self):
        """
        动作：点击列表-操作-第三个操作
        :return: 点击'列表-操作-第三个操作'按钮后的页面
        """
        self.project.click(self.list_execute_third_button)
        return self.project.get_current_page_source()

    def get_add_title_text_action(self):
        """
        动作：获取新增-标题的文本
        :return: '新增-标题'的文本
        """
        control_content = self.project.get_element_text(self.add_title_text)
        return control_content

    def click_add_tab_first_button_action(self):
        """
        动作：点击新增-第一个菜单
        :return: 点击'新增-第一个菜单'按钮后的页面
        """
        self.project.click(self.add_tab_first_button)
        return self.project.get_current_page_source()

    def set_add_username_input_action(self, add_username_input):
        """
        动作：设置新增-用户账号
        :param add_username_input: 新增-用户账号
        :return: 设置'新增-用户账号'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_username_input, add_username_input)
        return self.project.get_current_page_source()

    def set_add_password_input_action(self, add_password_input):
        """
        动作：设置新增-用户密码
        :param add_password_input: 新增-用户密码
        :return: 设置'新增-用户密码'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_password_input, add_password_input)
        return self.project.get_current_page_source()

    def set_add_real_name_input_action(self, add_real_name_input):
        """
        动作：设置新增-真实姓名
        :param add_real_name_input: 新增-真实姓名
        :return: 设置'新增-真实姓名'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_real_name_input, add_real_name_input)
        return self.project.get_current_page_source()

    def set_add_nick_input_action(self, add_nick_input):
        """
        动作：设置新增-用户昵称
        :param add_nick_input: 新增-用户昵称
        :return: 设置'新增-用户昵称'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_nick_input, add_nick_input)
        return self.project.get_current_page_source()

    def set_add_institute_name_input_action(self, add_institute_name_input):
        """
        动作：设置新增-机构院校名称
        :param add_institute_name_input: 新增-机构院校名称
        :return: 设置'新增-机构院校名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_institute_name_input, add_institute_name_input)
        return self.project.get_current_page_source()

    def set_add_institute_name_en_input_action(self, add_institute_name_en_input):
        """
        动作：设置新增-机构院校名称（英文）
        :param add_institute_name_en_input: 新增-机构院校名称（英文）
        :return: 设置'新增-机构院校名称（英文）'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_institute_name_en_input, add_institute_name_en_input)
        return self.project.get_current_page_source()

    def set_add_institute_contact_name_input_action(self, add_institute_contact_name_input):
        """
        动作：设置新增-联系人
        :param add_institute_contact_name_input: 新增-联系人
        :return: 设置'新增-联系人'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_institute_contact_name_input, add_institute_contact_name_input)
        return self.project.get_current_page_source()

    def click_add_contact_phone_area_code_button_action(self):
        """
        动作：点击新增-联系电话-区号
        :return: 点击'新增-联系电话-区号'按钮后的页面
        """
        self.project.click(self.add_contact_phone_area_code_button)
        return self.project.get_current_page_source()

    def set_add_contact_phone_input_action(self, add_contact_phone_input):
        """
        动作：设置新增-联系电话-电话号码
        :param add_contact_phone_input: 新增-联系电话-电话号码
        :return: 设置'新增-联系电话-电话号码'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_contact_phone_input, add_contact_phone_input)
        return self.project.get_current_page_source()

    def set_add_institute_nature_input_action(self, add_institute_nature_input):
        """
        动作：设置新增-机构院校性质
        :param add_institute_nature_input: 新增-机构院校性质
        :return: 设置'新增-机构院校性质'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_institute_nature_input, add_institute_nature_input)
        return self.project.get_current_page_source()

    def set_add_contact_mobile_input_action(self, add_contact_mobile_input):
        """
        动作：设置新增-联系人手机号
        :param add_contact_mobile_input: 新增-联系人手机号
        :return: 设置'新增-联系人手机号'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_contact_mobile_input, add_contact_mobile_input)
        return self.project.get_current_page_source()

    def click_add_country_button_action(self):
        """
        动作：点击新增-所属国家
        :return: 点击'新增-所属国家'按钮后的页面
        """
        self.project.click(self.add_country_button)
        return self.project.get_current_page_source()

    def set_add_email_input_action(self, add_email_input):
        """
        动作：设置新增-邮箱
        :param add_email_input: 新增-邮箱
        :return: 设置'新增-邮箱'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_email_input, add_email_input)
        return self.project.get_current_page_source()

    def click_add_type_button_action(self):
        """
        动作：点击新增-类型
        :return: 点击'新增-类型'按钮后的页面
        """
        self.project.click(self.add_type_button)
        return self.project.get_current_page_source()

    def click_add_category_button_action(self):
        """
        动作：点击新增-所属频道
        :return: 点击'新增-所属频道'按钮后的页面
        """
        self.project.click(self.add_category_button)
        return self.project.get_current_page_source()

    def click_add_main_field_button_action(self):
        """
        动作：点击新增-主要领域
        :return: 点击'新增-主要领域'按钮后的页面
        """
        self.project.click(self.add_main_field_button)
        return self.project.get_current_page_source()

    def click_add_apply_channel_first_button_action(self):
        """
        动作：点击新增-申请频道-第一个
        :return: 点击'新增-申请频道-第一个'按钮后的页面
        """
        self.project.click(self.add_apply_channel_first_button)
        return self.project.get_current_page_source()

    def click_add_apply_channel_second_button_action(self):
        """
        动作：点击新增-申请频道-第二个
        :return: 点击'新增-申请频道-第二个'按钮后的页面
        """
        self.project.click(self.add_apply_channel_second_button)
        return self.project.get_current_page_source()

    def click_add_apply_channel_third_button_action(self):
        """
        动作：点击新增-申请频道-第三个
        :return: 点击'新增-申请频道-第三个'按钮后的页面
        """
        self.project.click(self.add_apply_channel_third_button)
        return self.project.get_current_page_source()

    def click_add_apply_channel_fourth_button_action(self):
        """
        动作：点击新增-申请频道-第四个
        :return: 点击'新增-申请频道-第四个'按钮后的页面
        """
        self.project.click(self.add_apply_channel_fourth_button)
        return self.project.get_current_page_source()

    def click_add_apply_channel_fifth_button_action(self):
        """
        动作：点击新增-申请频道-第五个
        :return: 点击'新增-申请频道-第五个'按钮后的页面
        """
        self.project.click(self.add_apply_channel_fifth_button)
        return self.project.get_current_page_source()

    def set_add_bank_card_number_input_action(self, add_bank_card_number_input):
        """
        动作：设置新增-银行卡号码
        :param add_bank_card_number_input: 新增-银行卡号码
        :return: 设置'新增-银行卡号码'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_bank_card_number_input, add_bank_card_number_input)
        return self.project.get_current_page_source()

    def set_add_open_bank_name_input_action(self, add_open_bank_name_input):
        """
        动作：设置新增-开户行名称
        :param add_open_bank_name_input: 新增-开户行名称
        :return: 设置'新增-开户行名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_open_bank_name_input, add_open_bank_name_input)
        return self.project.get_current_page_source()

    def set_add_bank_code_input_action(self, add_bank_code_input):
        """
        动作：设置新增-行号
        :param add_bank_code_input: 新增-行号
        :return: 设置'新增-行号'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_bank_code_input, add_bank_code_input)
        return self.project.get_current_page_source()

    def set_add_company_full_name_input_action(self, add_company_full_name_input):
        """
        动作：设置新增-公司全称
        :param add_company_full_name_input: 新增-公司全称
        :return: 设置'新增-公司全称'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_company_full_name_input, add_company_full_name_input)
        return self.project.get_current_page_source()

    def click_add_institute_is_jjl_yes_button_action(self):
        """
        动作：点击新增-机构-是否属于金吉列-是
        :return: 点击'新增-机构-是否属于金吉列-是'按钮后的页面
        """
        self.project.click(self.add_institute_is_jjl_yes_button)
        return self.project.get_current_page_source()

    def click_add_institute_is_jjl_no_button_action(self):
        """
        动作：点击新增-机构-是否属于金吉列-否
        :return: 点击'新增-机构-是否属于金吉列-否'按钮后的页面
        """
        self.project.click(self.add_institute_is_jjl_no_button)
        return self.project.get_current_page_source()

    def set_add_institute_address_input_action(self, add_institute_address_input):
        """
        动作：设置新增-机构-联系地址
        :param add_institute_address_input: 新增-机构-联系地址
        :return: 设置'新增-机构-联系地址'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_institute_address_input, add_institute_address_input)
        return self.project.get_current_page_source()

    def set_add_institute_institute_type_input_action(self, add_institute_institute_type_input):
        """
        动作：设置新增-机构-机构院校类型
        :param add_institute_institute_type_input: 新增-机构-机构院校类型
        :return: 设置'新增-机构-机构院校类型'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_institute_institute_type_input, add_institute_institute_type_input)
        return self.project.get_current_page_source()

    def set_add_institute_official_website_input_action(self, add_institute_official_website_input):
        """
        动作：设置新增-机构-机构官网
        :param add_institute_official_website_input: 新增-机构-机构官网
        :return: 设置'新增-机构-机构官网'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_institute_official_website_input, add_institute_official_website_input)
        return self.project.get_current_page_source()

    def set_add_institute_institute_introduction_input_action(self, add_institute_institute_introduction_input):
        """
        动作：设置新增-机构-机构院校介绍
        :param add_institute_institute_introduction_input: 新增-机构-机构院校介绍
        :return: 设置'新增-机构-机构院校介绍'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_institute_institute_introduction_input, add_institute_institute_introduction_input)
        return self.project.get_current_page_source()

    def set_add_institute_power_of_attorney_input_action(self, add_institute_power_of_attorney_input):
        """
        动作：设置新增-机构-授权委托书
        :param add_institute_power_of_attorney_input: 新增-机构-授权委托书
        :return: 设置'新增-机构-授权委托书'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_institute_power_of_attorney_input, add_institute_power_of_attorney_input)
        return self.project.get_current_page_source()

    def set_add_institute_business_license_input_action(self, add_institute_business_license_input):
        """
        动作：设置新增-机构-营业执照或其他合法资质证照
        :param add_institute_business_license_input: 新增-机构-营业执照或其他合法资质证照
        :return: 设置'新增-机构-营业执照或其他合法资质证照'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_institute_business_license_input, add_institute_business_license_input)
        return self.project.get_current_page_source()

    def set_add_institute_institute_logo_input_action(self, add_institute_institute_logo_input):
        """
        动作：设置新增-机构-机构院校logo
        :param add_institute_institute_logo_input: 新增-机构-机构院校logo
        :return: 设置'新增-机构-机构院校logo'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_institute_institute_logo_input, add_institute_institute_logo_input)
        return self.project.get_current_page_source()

    def set_add_institute_institute_background_main_page_input_action(self, add_institute_institute_background_main_page_input):
        """
        动作：设置新增-机构-机构院校主页背景
        :param add_institute_institute_background_main_page_input: 新增-机构-机构院校主页背景
        :return: 设置'新增-机构-机构院校主页背景'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_institute_institute_background_main_page_input, add_institute_institute_background_main_page_input)
        return self.project.get_current_page_source()

    def set_add_institute_create_time_input_action(self, add_institute_create_time_input):
        """
        动作：设置新增-机构-创立时间
        :param add_institute_create_time_input: 新增-机构-创立时间
        :return: 设置'新增-机构-创立时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_institute_create_time_input, add_institute_create_time_input)
        return self.project.get_current_page_source()

    def set_add_institute_juridical_person_input_action(self, add_institute_juridical_person_input):
        """
        动作：设置新增-机构-法人
        :param add_institute_juridical_person_input: 新增-机构-法人
        :return: 设置'新增-机构-法人'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_institute_juridical_person_input, add_institute_juridical_person_input)
        return self.project.get_current_page_source()

    def click_edit_school_is_cooperation_yes_button_action(self):
        """
        动作：点击新增-院校-是否合作院校-是
        :return: 点击'新增-院校-是否合作院校-是'按钮后的页面
        """
        self.project.click(self.edit_school_is_cooperation_yes_button)
        return self.project.get_current_page_source()

    def click_edit_school_is_cooperation_no_button_action(self):
        """
        动作：点击编辑-院校-是否合作院校-否
        :return: 点击'编辑-院校-是否合作院校-否'按钮后的页面
        """
        self.project.click(self.edit_school_is_cooperation_no_button)
        return self.project.get_current_page_source()

    def click_edit_school_qualification_first_button_action(self):
        """
        动作：点击编辑-院校-学历-第一个
        :return: 点击'编辑-院校-学历-第一个'按钮后的页面
        """
        self.project.click(self.edit_school_qualification_first_button)
        return self.project.get_current_page_source()

    def click_edit_school_qualification_second_button_action(self):
        """
        动作：点击编辑-院校-学历-第二个
        :return: 点击'编辑-院校-学历-第二个'按钮后的页面
        """
        self.project.click(self.edit_school_qualification_second_button)
        return self.project.get_current_page_source()

    def click_edit_school_specialities_first_button_action(self):
        """
        动作：点击编辑-院校-专业-第一个
        :return: 点击'编辑-院校-专业-第一个'按钮后的页面
        """
        self.project.click(self.edit_school_specialities_first_button)
        return self.project.get_current_page_source()

    def click_edit_school_specialities_second_button_action(self):
        """
        动作：点击编辑-院校-专业-第二个
        :return: 点击'编辑-院校-专业-第二个'按钮后的页面
        """
        self.project.click(self.edit_school_specialities_second_button)
        return self.project.get_current_page_source()

    def set_edit_school_address_input_action(self, edit_school_address_input):
        """
        动作：设置编辑-院校-联系地址
        :param edit_school_address_input: 编辑-院校-联系地址
        :return: 设置'编辑-院校-联系地址'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_address_input, edit_school_address_input)
        return self.project.get_current_page_source()

    def set_edit_school_institute_type_input_action(self, edit_school_institute_type_input):
        """
        动作：设置编辑-院校-机构院校类型
        :param edit_school_institute_type_input: 编辑-院校-机构院校类型
        :return: 设置'编辑-院校-机构院校类型'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_institute_type_input, edit_school_institute_type_input)
        return self.project.get_current_page_source()

    def set_edit_school_official_website_input_action(self, edit_school_official_website_input):
        """
        动作：设置编辑-院校-机构官网
        :param edit_school_official_website_input: 编辑-院校-机构官网
        :return: 设置'编辑-院校-机构官网'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_official_website_input, edit_school_official_website_input)
        return self.project.get_current_page_source()

    def set_edit_school_institute_introduction_input_action(self, edit_school_institute_introduction_input):
        """
        动作：设置编辑-院校-机构院校介绍
        :param edit_school_institute_introduction_input: 编辑-院校-机构院校介绍
        :return: 设置'编辑-院校-机构院校介绍'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_institute_introduction_input, edit_school_institute_introduction_input)
        return self.project.get_current_page_source()

    def set_edit_school_power_of_attorney_input_action(self, edit_school_power_of_attorney_input):
        """
        动作：设置编辑-院校-授权委托书
        :param edit_school_power_of_attorney_input: 编辑-院校-授权委托书
        :return: 设置'编辑-院校-授权委托书'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_power_of_attorney_input, edit_school_power_of_attorney_input)
        return self.project.get_current_page_source()

    def set_edit_school_business_license_input_action(self, edit_school_business_license_input):
        """
        动作：设置编辑-院校-营业执照或其他合法资质证照
        :param edit_school_business_license_input: 编辑-院校-营业执照或其他合法资质证照
        :return: 设置'编辑-院校-营业执照或其他合法资质证照'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_business_license_input, edit_school_business_license_input)
        return self.project.get_current_page_source()

    def set_edit_school_institute_logo_input_action(self, edit_school_institute_logo_input):
        """
        动作：设置编辑-院校-机构院校logo
        :param edit_school_institute_logo_input: 编辑-院校-机构院校logo
        :return: 设置'编辑-院校-机构院校logo'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_institute_logo_input, edit_school_institute_logo_input)
        return self.project.get_current_page_source()

    def set_edit_school_institute_background_main_page_input_action(self, edit_school_institute_background_main_page_input):
        """
        动作：设置编辑-院校-机构院校主页背景
        :param edit_school_institute_background_main_page_input: 编辑-院校-机构院校主页背景
        :return: 设置'编辑-院校-机构院校主页背景'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_institute_background_main_page_input, edit_school_institute_background_main_page_input)
        return self.project.get_current_page_source()

    def set_edit_school_create_time_input_action(self, edit_school_create_time_input):
        """
        动作：设置编辑-院校-创立时间
        :param edit_school_create_time_input: 编辑-院校-创立时间
        :return: 设置'编辑-院校-创立时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_create_time_input, edit_school_create_time_input)
        return self.project.get_current_page_source()

    def set_edit_school_juridical_person_input_action(self, edit_school_juridical_person_input):
        """
        动作：设置编辑-院校-法人
        :param edit_school_juridical_person_input: 编辑-院校-法人
        :return: 设置'编辑-院校-法人'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_juridical_person_input, edit_school_juridical_person_input)
        return self.project.get_current_page_source()

    def set_edit_school_cooperation_start_time_input_action(self, edit_school_cooperation_start_time_input):
        """
        动作：设置编辑-院校-合作开始时间
        :param edit_school_cooperation_start_time_input: 编辑-院校-合作开始时间
        :return: 设置'编辑-院校-合作开始时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_cooperation_start_time_input, edit_school_cooperation_start_time_input)
        return self.project.get_current_page_source()

    def set_edit_school_cooperation_end_time_input_action(self, edit_school_cooperation_end_time_input):
        """
        动作：设置编辑-院校-合作结束时间
        :param edit_school_cooperation_end_time_input: 编辑-院校-合作结束时间
        :return: 设置'编辑-院校-合作结束时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_cooperation_end_time_input, edit_school_cooperation_end_time_input)
        return self.project.get_current_page_source()

    def click_add_commit_button_action(self):
        """
        动作：点击新增-提交
        :return: 点击'新增-提交'按钮后的页面
        """
        self.project.click(self.add_commit_button)
        return self.project.get_current_page_source()

    def click_add_cancel_button_action(self):
        """
        动作：点击新增-取消
        :return: 点击'新增-取消'按钮后的页面
        """
        self.project.click(self.add_cancel_button)
        return self.project.get_current_page_source()

    def get_edit_title_text_action(self):
        """
        动作：获取编辑-标题的文本
        :return: '编辑-标题'的文本
        """
        control_content = self.project.get_element_text(self.edit_title_text)
        return control_content

    def click_edit_tab_first_button_action(self):
        """
        动作：点击编辑-第一个菜单
        :return: 点击'编辑-第一个菜单'按钮后的页面
        """
        self.project.click(self.edit_tab_first_button)
        return self.project.get_current_page_source()

    def set_edit_institute_id_input_action(self, edit_institute_id_input):
        """
        动作：设置编辑-机构院校ID
        :param edit_institute_id_input: 编辑-机构院校ID
        :return: 设置'编辑-机构院校ID'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_institute_id_input, edit_institute_id_input)
        return self.project.get_current_page_source()

    def set_edit_register_time_input_action(self, edit_register_time_input):
        """
        动作：设置编辑-注册时间
        :param edit_register_time_input: 编辑-注册时间
        :return: 设置'编辑-注册时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_register_time_input, edit_register_time_input)
        return self.project.get_current_page_source()

    def set_edit_create_user_input_action(self, edit_create_user_input):
        """
        动作：设置编辑-创建人员
        :param edit_create_user_input: 编辑-创建人员
        :return: 设置'编辑-创建人员'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_create_user_input, edit_create_user_input)
        return self.project.get_current_page_source()

    def set_edit_review_state_input_action(self, edit_review_state_input):
        """
        动作：设置编辑-审核状态
        :param edit_review_state_input: 编辑-审核状态
        :return: 设置'编辑-审核状态'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_review_state_input, edit_review_state_input)
        return self.project.get_current_page_source()

    def set_edit_username_input_action(self, edit_username_input):
        """
        动作：设置编辑-用户账号
        :param edit_username_input: 编辑-用户账号
        :return: 设置'编辑-用户账号'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_username_input, edit_username_input)
        return self.project.get_current_page_source()

    def set_edit_password_input_action(self, edit_password_input):
        """
        动作：设置编辑-用户密码
        :param edit_password_input: 编辑-用户密码
        :return: 设置'编辑-用户密码'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_password_input, edit_password_input)
        return self.project.get_current_page_source()

    def set_edit_real_name_input_action(self, edit_real_name_input):
        """
        动作：设置编辑-真实姓名
        :param edit_real_name_input: 编辑-真实姓名
        :return: 设置'编辑-真实姓名'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_real_name_input, edit_real_name_input)
        return self.project.get_current_page_source()

    def set_edit_nick_input_action(self, edit_nick_input):
        """
        动作：设置编辑-用户昵称
        :param edit_nick_input: 编辑-用户昵称
        :return: 设置'编辑-用户昵称'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_nick_input, edit_nick_input)
        return self.project.get_current_page_source()

    def set_edit_institute_name_input_action(self, edit_institute_name_input):
        """
        动作：设置编辑-机构院校名称
        :param edit_institute_name_input: 编辑-机构院校名称
        :return: 设置'编辑-机构院校名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_institute_name_input, edit_institute_name_input)
        return self.project.get_current_page_source()

    def set_edit_institute_name_en_input_action(self, edit_institute_name_en_input):
        """
        动作：设置编辑-机构院校名称（英文）
        :param edit_institute_name_en_input: 编辑-机构院校名称（英文）
        :return: 设置'编辑-机构院校名称（英文）'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_institute_name_en_input, edit_institute_name_en_input)
        return self.project.get_current_page_source()

    def set_edit_institute_contact_name_input_action(self, edit_institute_contact_name_input):
        """
        动作：设置编辑-联系人
        :param edit_institute_contact_name_input: 编辑-联系人
        :return: 设置'编辑-联系人'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_institute_contact_name_input, edit_institute_contact_name_input)
        return self.project.get_current_page_source()

    def click_edit_contact_phone_area_code_button_action(self):
        """
        动作：点击编辑-联系电话-区号
        :return: 点击'编辑-联系电话-区号'按钮后的页面
        """
        self.project.click(self.edit_contact_phone_area_code_button)
        return self.project.get_current_page_source()

    def set_edit_contact_phone_input_action(self, edit_contact_phone_input):
        """
        动作：设置编辑-联系电话-电话号码
        :param edit_contact_phone_input: 编辑-联系电话-电话号码
        :return: 设置'编辑-联系电话-电话号码'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_contact_phone_input, edit_contact_phone_input)
        return self.project.get_current_page_source()

    def set_edit_institute_nature_input_action(self, edit_institute_nature_input):
        """
        动作：设置编辑-机构院校性质
        :param edit_institute_nature_input: 编辑-机构院校性质
        :return: 设置'编辑-机构院校性质'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_institute_nature_input, edit_institute_nature_input)
        return self.project.get_current_page_source()

    def set_edit_contact_mobile_input_action(self, edit_contact_mobile_input):
        """
        动作：设置编辑-联系人手机号
        :param edit_contact_mobile_input: 编辑-联系人手机号
        :return: 设置'编辑-联系人手机号'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_contact_mobile_input, edit_contact_mobile_input)
        return self.project.get_current_page_source()

    def click_edit_country_button_action(self):
        """
        动作：点击编辑-所属国家
        :return: 点击'编辑-所属国家'按钮后的页面
        """
        self.project.click(self.edit_country_button)
        return self.project.get_current_page_source()

    def set_edit_email_input_action(self, edit_email_input):
        """
        动作：设置编辑-邮箱
        :param edit_email_input: 编辑-邮箱
        :return: 设置'编辑-邮箱'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_email_input, edit_email_input)
        return self.project.get_current_page_source()

    def click_edit_type_button_action(self):
        """
        动作：点击编辑-类型
        :return: 点击'编辑-类型'按钮后的页面
        """
        self.project.click(self.edit_type_button)
        return self.project.get_current_page_source()

    def click_edit_category_button_action(self):
        """
        动作：点击编辑-所属频道
        :return: 点击'编辑-所属频道'按钮后的页面
        """
        self.project.click(self.edit_category_button)
        return self.project.get_current_page_source()

    def click_edit_main_field_button_action(self):
        """
        动作：点击编辑-主要领域
        :return: 点击'编辑-主要领域'按钮后的页面
        """
        self.project.click(self.edit_main_field_button)
        return self.project.get_current_page_source()

    def click_edit_apply_channel_first_button_action(self):
        """
        动作：点击编辑-申请频道-第一个
        :return: 点击'编辑-申请频道-第一个'按钮后的页面
        """
        self.project.click(self.edit_apply_channel_first_button)
        return self.project.get_current_page_source()

    def click_edit_apply_channel_second_button_action(self):
        """
        动作：点击编辑-申请频道-第二个
        :return: 点击'编辑-申请频道-第二个'按钮后的页面
        """
        self.project.click(self.edit_apply_channel_second_button)
        return self.project.get_current_page_source()

    def click_edit_apply_channel_third_button_action(self):
        """
        动作：点击编辑-申请频道-第三个
        :return: 点击'编辑-申请频道-第三个'按钮后的页面
        """
        self.project.click(self.edit_apply_channel_third_button)
        return self.project.get_current_page_source()

    def click_edit_apply_channel_fourth_button_action(self):
        """
        动作：点击编辑-申请频道-第四个
        :return: 点击'编辑-申请频道-第四个'按钮后的页面
        """
        self.project.click(self.edit_apply_channel_fourth_button)
        return self.project.get_current_page_source()

    def click_edit_apply_channel_fifth_button_action(self):
        """
        动作：点击编辑-申请频道-第五个
        :return: 点击'编辑-申请频道-第五个'按钮后的页面
        """
        self.project.click(self.edit_apply_channel_fifth_button)
        return self.project.get_current_page_source()

    def set_edit_bank_card_number_input_action(self, edit_bank_card_number_input):
        """
        动作：设置编辑-银行卡号码
        :param edit_bank_card_number_input: 编辑-银行卡号码
        :return: 设置'编辑-银行卡号码'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_bank_card_number_input, edit_bank_card_number_input)
        return self.project.get_current_page_source()

    def set_edit_open_bank_name_input_action(self, edit_open_bank_name_input):
        """
        动作：设置编辑-开户行名称
        :param edit_open_bank_name_input: 编辑-开户行名称
        :return: 设置'编辑-开户行名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_open_bank_name_input, edit_open_bank_name_input)
        return self.project.get_current_page_source()

    def set_edit_bank_code_input_action(self, edit_bank_code_input):
        """
        动作：设置编辑-行号
        :param edit_bank_code_input: 编辑-行号
        :return: 设置'编辑-行号'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_bank_code_input, edit_bank_code_input)
        return self.project.get_current_page_source()

    def set_edit_company_full_name_input_action(self, edit_company_full_name_input):
        """
        动作：设置编辑-公司全称
        :param edit_company_full_name_input: 编辑-公司全称
        :return: 设置'编辑-公司全称'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_company_full_name_input, edit_company_full_name_input)
        return self.project.get_current_page_source()

    def click_edit_institute_is_jjl_yes_button_action(self):
        """
        动作：点击编辑-机构-是否属于金吉列-是
        :return: 点击'编辑-机构-是否属于金吉列-是'按钮后的页面
        """
        self.project.click(self.edit_institute_is_jjl_yes_button)
        return self.project.get_current_page_source()

    def click_edit_institute_is_jjl_no_button_action(self):
        """
        动作：点击编辑-机构-是否属于金吉列-否
        :return: 点击'编辑-机构-是否属于金吉列-否'按钮后的页面
        """
        self.project.click(self.edit_institute_is_jjl_no_button)
        return self.project.get_current_page_source()

    def set_edit_institute_address_input_action(self, edit_institute_address_input):
        """
        动作：设置编辑-机构-联系地址
        :param edit_institute_address_input: 编辑-机构-联系地址
        :return: 设置'编辑-机构-联系地址'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_institute_address_input, edit_institute_address_input)
        return self.project.get_current_page_source()

    def set_edit_institute_institute_type_input_action(self, edit_institute_institute_type_input):
        """
        动作：设置编辑-机构-机构院校类型
        :param edit_institute_institute_type_input: 编辑-机构-机构院校类型
        :return: 设置'编辑-机构-机构院校类型'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_institute_institute_type_input, edit_institute_institute_type_input)
        return self.project.get_current_page_source()

    def set_edit_institute_official_website_input_action(self, edit_institute_official_website_input):
        """
        动作：设置编辑-机构-机构官网
        :param edit_institute_official_website_input: 编辑-机构-机构官网
        :return: 设置'编辑-机构-机构官网'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_institute_official_website_input, edit_institute_official_website_input)
        return self.project.get_current_page_source()

    def set_edit_institute_institute_introduction_input_action(self, edit_institute_institute_introduction_input):
        """
        动作：设置编辑-机构-机构院校介绍
        :param edit_institute_institute_introduction_input: 编辑-机构-机构院校介绍
        :return: 设置'编辑-机构-机构院校介绍'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_institute_institute_introduction_input, edit_institute_institute_introduction_input)
        return self.project.get_current_page_source()

    def set_edit_institute_power_of_attorney_input_action(self, edit_institute_power_of_attorney_input):
        """
        动作：设置编辑-机构-授权委托书
        :param edit_institute_power_of_attorney_input: 编辑-机构-授权委托书
        :return: 设置'编辑-机构-授权委托书'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_institute_power_of_attorney_input, edit_institute_power_of_attorney_input)
        return self.project.get_current_page_source()

    def set_edit_institute_business_license_input_action(self, edit_institute_business_license_input):
        """
        动作：设置编辑-机构-营业执照或其他合法资质证照
        :param edit_institute_business_license_input: 编辑-机构-营业执照或其他合法资质证照
        :return: 设置'编辑-机构-营业执照或其他合法资质证照'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_institute_business_license_input, edit_institute_business_license_input)
        return self.project.get_current_page_source()

    def set_edit_institute_institute_logo_input_action(self, edit_institute_institute_logo_input):
        """
        动作：设置编辑-机构-机构院校logo
        :param edit_institute_institute_logo_input: 编辑-机构-机构院校logo
        :return: 设置'编辑-机构-机构院校logo'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_institute_institute_logo_input, edit_institute_institute_logo_input)
        return self.project.get_current_page_source()

    def set_edit_institute_institute_background_main_page_input_action(self, edit_institute_institute_background_main_page_input):
        """
        动作：设置编辑-机构-机构院校主页背景
        :param edit_institute_institute_background_main_page_input: 编辑-机构-机构院校主页背景
        :return: 设置'编辑-机构-机构院校主页背景'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_institute_institute_background_main_page_input, edit_institute_institute_background_main_page_input)
        return self.project.get_current_page_source()

    def set_edit_institute_create_time_input_action(self, edit_institute_create_time_input):
        """
        动作：设置编辑-机构-创立时间
        :param edit_institute_create_time_input: 编辑-机构-创立时间
        :return: 设置'编辑-机构-创立时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_institute_create_time_input, edit_institute_create_time_input)
        return self.project.get_current_page_source()

    def set_edit_institute_juridical_person_input_action(self, edit_institute_juridical_person_input):
        """
        动作：设置编辑-机构-法人
        :param edit_institute_juridical_person_input: 编辑-机构-法人
        :return: 设置'编辑-机构-法人'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_institute_juridical_person_input, edit_institute_juridical_person_input)
        return self.project.get_current_page_source()

    def click_edit_school_country_region_button_action(self):
        """
        动作：点击编辑-院校-国家及地区
        :return: 点击'编辑-院校-国家及地区'按钮后的页面
        """
        self.project.click(self.edit_school_country_region_button)
        return self.project.get_current_page_source()

    def click_edit_school_is_cooperation_yes_button_action(self):
        """
        动作：点击编辑-院校-是否合作院校-是
        :return: 点击'编辑-院校-是否合作院校-是'按钮后的页面
        """
        self.project.click(self.edit_school_is_cooperation_yes_button)
        return self.project.get_current_page_source()

    def click_edit_school_is_cooperation_no_button_action(self):
        """
        动作：点击编辑-院校-是否合作院校-否
        :return: 点击'编辑-院校-是否合作院校-否'按钮后的页面
        """
        self.project.click(self.edit_school_is_cooperation_no_button)
        return self.project.get_current_page_source()

    def click_edit_school_qualification_first_button_action(self):
        """
        动作：点击编辑-院校-学历-第一个
        :return: 点击'编辑-院校-学历-第一个'按钮后的页面
        """
        self.project.click(self.edit_school_qualification_first_button)
        return self.project.get_current_page_source()

    def click_edit_school_qualification_second_button_action(self):
        """
        动作：点击编辑-院校-学历-第二个
        :return: 点击'编辑-院校-学历-第二个'按钮后的页面
        """
        self.project.click(self.edit_school_qualification_second_button)
        return self.project.get_current_page_source()

    def click_edit_school_specialities_first_button_action(self):
        """
        动作：点击编辑-院校-专业-第一个
        :return: 点击'编辑-院校-专业-第一个'按钮后的页面
        """
        self.project.click(self.edit_school_specialities_first_button)
        return self.project.get_current_page_source()

    def click_edit_school_specialities_second_button_action(self):
        """
        动作：点击编辑-院校-专业-第二个
        :return: 点击'编辑-院校-专业-第二个'按钮后的页面
        """
        self.project.click(self.edit_school_specialities_second_button)
        return self.project.get_current_page_source()

    def set_edit_school_address_input_action(self, edit_school_address_input):
        """
        动作：设置编辑-院校-联系地址
        :param edit_school_address_input: 编辑-院校-联系地址
        :return: 设置'编辑-院校-联系地址'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_address_input, edit_school_address_input)
        return self.project.get_current_page_source()

    def set_edit_school_institute_type_input_action(self, edit_school_institute_type_input):
        """
        动作：设置编辑-院校-机构院校类型
        :param edit_school_institute_type_input: 编辑-院校-机构院校类型
        :return: 设置'编辑-院校-机构院校类型'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_institute_type_input, edit_school_institute_type_input)
        return self.project.get_current_page_source()

    def set_edit_school_official_website_input_action(self, edit_school_official_website_input):
        """
        动作：设置编辑-院校-机构官网
        :param edit_school_official_website_input: 编辑-院校-机构官网
        :return: 设置'编辑-院校-机构官网'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_official_website_input, edit_school_official_website_input)
        return self.project.get_current_page_source()

    def set_edit_school_institute_introduction_input_action(self, edit_school_institute_introduction_input):
        """
        动作：设置编辑-院校-机构院校介绍
        :param edit_school_institute_introduction_input: 编辑-院校-机构院校介绍
        :return: 设置'编辑-院校-机构院校介绍'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_institute_introduction_input, edit_school_institute_introduction_input)
        return self.project.get_current_page_source()

    def set_edit_school_power_of_attorney_input_action(self, edit_school_power_of_attorney_input):
        """
        动作：设置编辑-院校-授权委托书
        :param edit_school_power_of_attorney_input: 编辑-院校-授权委托书
        :return: 设置'编辑-院校-授权委托书'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_power_of_attorney_input, edit_school_power_of_attorney_input)
        return self.project.get_current_page_source()

    def set_edit_school_business_license_input_action(self, edit_school_business_license_input):
        """
        动作：设置编辑-院校-营业执照或其他合法资质证照
        :param edit_school_business_license_input: 编辑-院校-营业执照或其他合法资质证照
        :return: 设置'编辑-院校-营业执照或其他合法资质证照'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_business_license_input, edit_school_business_license_input)
        return self.project.get_current_page_source()

    def set_edit_school_institute_logo_input_action(self, edit_school_institute_logo_input):
        """
        动作：设置编辑-院校-机构院校logo
        :param edit_school_institute_logo_input: 编辑-院校-机构院校logo
        :return: 设置'编辑-院校-机构院校logo'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_institute_logo_input, edit_school_institute_logo_input)
        return self.project.get_current_page_source()

    def set_edit_school_institute_background_main_page_input_action(self, edit_school_institute_background_main_page_input):
        """
        动作：设置编辑-院校-机构院校主页背景
        :param edit_school_institute_background_main_page_input: 编辑-院校-机构院校主页背景
        :return: 设置'编辑-院校-机构院校主页背景'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_institute_background_main_page_input, edit_school_institute_background_main_page_input)
        return self.project.get_current_page_source()

    def set_edit_school_create_time_input_action(self, edit_school_create_time_input):
        """
        动作：设置编辑-院校-创立时间
        :param edit_school_create_time_input: 编辑-院校-创立时间
        :return: 设置'编辑-院校-创立时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_create_time_input, edit_school_create_time_input)
        return self.project.get_current_page_source()

    def set_edit_school_juridical_person_input_action(self, edit_school_juridical_person_input):
        """
        动作：设置编辑-院校-法人
        :param edit_school_juridical_person_input: 编辑-院校-法人
        :return: 设置'编辑-院校-法人'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_juridical_person_input, edit_school_juridical_person_input)
        return self.project.get_current_page_source()

    def set_edit_school_cooperation_start_time_input_action(self, edit_school_cooperation_start_time_input):
        """
        动作：设置编辑-院校-合作开始时间
        :param edit_school_cooperation_start_time_input: 编辑-院校-合作开始时间
        :return: 设置'编辑-院校-合作开始时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_cooperation_start_time_input, edit_school_cooperation_start_time_input)
        return self.project.get_current_page_source()

    def set_edit_school_cooperation_end_time_input_action(self, edit_school_cooperation_end_time_input):
        """
        动作：设置编辑-院校-合作结束时间
        :param edit_school_cooperation_end_time_input: 编辑-院校-合作结束时间
        :return: 设置'编辑-院校-合作结束时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_school_cooperation_end_time_input, edit_school_cooperation_end_time_input)
        return self.project.get_current_page_source()

    def click_edit_commit_button_action(self):
        """
        动作：点击编辑-提交
        :return: 点击'编辑-提交'按钮后的页面
        """
        self.project.click(self.edit_commit_button)
        return self.project.get_current_page_source()

    def click_edit_cancel_button_action(self):
        """
        动作：点击编辑-取消
        :return: 点击'编辑-取消'按钮后的页面
        """
        self.project.click(self.edit_cancel_button)
        return self.project.get_current_page_source()

    def click_console_user_center_top_button_action(self):
        """
        动作：点击用户中心导航
        :return: 点击'用户中心导航'按钮后的页面
        """
        self.project.click(self.console_user_center_top_button)
        return self.project.get_current_page_source()

    def click_console_institution_manage_left_button_action(self):
        """
        动作：点击机构院校管理左侧导航
        :return: 点击'机构院校管理左侧导航'按钮后的页面
        """
        self.project.click(self.console_institution_manage_left_button)
        return self.project.get_current_page_source()

    def click_console_institution_list_button_action(self):
        """
        动作：点击机构院校列表按钮
        :return: 点击'机构院校列表按钮'按钮后的页面
        """
        self.project.click(self.console_institution_list_button)
        return self.project.get_current_page_source()

    def get_console_institution_list_name_text_action(self):
        """
        动作：获取机构院校列表表名的文本
        :return: '机构院校列表表名'的文本
        """
        control_content = self.project.get_element_text(self.console_institution_list_name_text)
        return control_content

    def set_console_contact_mobile_input_action(self, console_contact_mobile_input):
        """
        动作：设置联系人电话输入
        :param console_contact_mobile_input: 联系人电话输入
        :return: 设置'联系人电话输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_contact_mobile_input, console_contact_mobile_input)
        return self.project.get_current_page_source()

    def click_console_is_not_jjl_button_action(self):
        """
        动作：点击是否金吉列
        :return: 点击'是否金吉列'按钮后的页面
        """
        self.project.click(self.console_is_not_jjl_button)
        return self.project.get_current_page_source()

    def click_console_is_not_jjl_not_button_action(self):
        """
        动作：点击是否金吉列(否)
        :return: 点击'是否金吉列(否)'按钮后的页面
        """
        self.project.click(self.console_is_not_jjl_not_button)
        return self.project.get_current_page_source()

    def click_console_is_not_jjl_yes_button_action(self):
        """
        动作：点击是否金吉列(是)
        :return: 点击'是否金吉列(是)'按钮后的页面
        """
        self.project.click(self.console_is_not_jjl_yes_button)
        return self.project.get_current_page_source()

    def click_console_is_not_teamwork_button_action(self):
        """
        动作：点击是否合作院校
        :return: 点击'是否合作院校'按钮后的页面
        """
        self.project.click(self.console_is_not_teamwork_button)
        return self.project.get_current_page_source()

    def click_console_is_not_teamwork_yes_button_action(self):
        """
        动作：点击是否合作院校(是)
        :return: 点击'是否合作院校(是)'按钮后的页面
        """
        self.project.click(self.console_is_not_teamwork_yes_button)
        return self.project.get_current_page_source()

    def click_console_is_not_teamwork_not_button_action(self):
        """
        动作：点击是否合作院校(否)
        :return: 点击'是否合作院校(否)'按钮后的页面
        """
        self.project.click(self.console_is_not_teamwork_not_button)
        return self.project.get_current_page_source()

    def click_console_at_country_button_action(self):
        """
        动作：点击所属国家
        :return: 点击'所属国家'按钮后的页面
        """
        self.project.click(self.console_at_country_button)
        return self.project.get_current_page_source()

    def click_console_at_country_china_button_action(self):
        """
        动作：点击所属国家(中国)
        :return: 点击'所属国家(中国)'按钮后的页面
        """
        self.project.click(self.console_at_country_china_button)
        return self.project.get_current_page_source()

    def click_console_status_button_action(self):
        """
        动作：点击状态
        :return: 点击'状态'按钮后的页面
        """
        self.project.click(self.console_status_button)
        return self.project.get_current_page_source()

    def click_console_status_on_button_action(self):
        """
        动作：点击状态(正常)
        :return: 点击'状态(正常)'按钮后的页面
        """
        self.project.click(self.console_status_on_button)
        return self.project.get_current_page_source()

    def click_console_status_off_button_action(self):
        """
        动作：点击状态(禁用)
        :return: 点击'状态(禁用)'按钮后的页面
        """
        self.project.click(self.console_status_off_button)
        return self.project.get_current_page_source()

    def set_console_contact_name_input_action(self, console_contact_name_input):
        """
        动作：设置联系人姓名输入
        :param console_contact_name_input: 联系人姓名输入
        :return: 设置'联系人姓名输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_contact_name_input, console_contact_name_input)
        return self.project.get_current_page_source()

    def click_console_category_button_action(self):
        """
        动作：点击类型
        :return: 点击'类型'按钮后的页面
        """
        self.project.click(self.console_category_button)
        return self.project.get_current_page_source()

    def click_console_category_institution_button_action(self):
        """
        动作：点击类别(机构)
        :return: 点击'类别(机构)'按钮后的页面
        """
        self.project.click(self.console_category_institution_button)
        return self.project.get_current_page_source()

    def click_console_category_school_button_action(self):
        """
        动作：点击类别(院校)
        :return: 点击'类别(院校)'按钮后的页面
        """
        self.project.click(self.console_category_school_button)
        return self.project.get_current_page_source()

    def set_console_institution_school_name_input_action(self, console_institution_school_name_input):
        """
        动作：设置机构院校名称输入
        :param console_institution_school_name_input: 机构院校名称输入
        :return: 设置'机构院校名称输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_institution_school_name_input, console_institution_school_name_input)
        return self.project.get_current_page_source()

    def click_console_inquiry_button_action(self):
        """
        动作：点击查询按钮
        :return: 点击'查询按钮'按钮后的页面
        """
        self.project.click(self.console_inquiry_button)
        return self.project.get_current_page_source()

    def click_console_clean_button_action(self):
        """
        动作：点击清除按钮
        :return: 点击'清除按钮'按钮后的页面
        """
        self.project.click(self.console_clean_button)
        return self.project.get_current_page_source()

    def click_console_institution_school_create_button_action(self):
        """
        动作：点击新增按钮
        :return: 点击'新增按钮'按钮后的页面
        """
        self.project.click(self.console_institution_school_create_button)
        return self.project.get_current_page_source()

    def get_console_inquiry_value_name_text_action(self):
        """
        动作：获取查询数据名称的文本
        :return: '查询数据名称'的文本
        """
        control_content = self.project.get_element_text(self.console_inquiry_value_name_text)
        return control_content

    def click_console_inquiry_value_edit_button_action(self):
        """
        动作：点击编辑操作按钮
        :return: 点击'编辑操作按钮'按钮后的页面
        """
        self.project.click(self.console_inquiry_value_edit_button)
        return self.project.get_current_page_source()

    def get_console_edit_form_text_action(self):
        """
        动作：获取编辑页表单名称的文本
        :return: '编辑页表单名称'的文本
        """
        control_content = self.project.get_element_text(self.console_edit_form_text)
        return control_content

    def set_console_edit_user_account_input_action(self, console_edit_user_account_input):
        """
        动作：设置用户账号输入
        :param console_edit_user_account_input: 用户账号输入
        :return: 设置'用户账号输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_edit_user_account_input, console_edit_user_account_input)
        return self.project.get_current_page_source()

    def set_console_edit_user_passwd_input_action(self, console_edit_user_passwd_input):
        """
        动作：设置用户密码输入
        :param console_edit_user_passwd_input: 用户密码输入
        :return: 设置'用户密码输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_edit_user_passwd_input, console_edit_user_passwd_input)
        return self.project.get_current_page_source()

    def set_console_real_name_input_action(self, console_real_name_input):
        """
        动作：设置真实姓名输入框
        :param console_real_name_input: 真实姓名输入框
        :return: 设置'真实姓名输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_real_name_input, console_real_name_input)
        return self.project.get_current_page_source()

    def set_console_user_nick_name_input_action(self, console_user_nick_name_input):
        """
        动作：设置用户昵称输入
        :param console_user_nick_name_input: 用户昵称输入
        :return: 设置'用户昵称输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_user_nick_name_input, console_user_nick_name_input)
        return self.project.get_current_page_source()

    def set_console_edit_institution_school_input_action(self, console_edit_institution_school_input):
        """
        动作：设置机构院校名称输入
        :param console_edit_institution_school_input: 机构院校名称输入
        :return: 设置'机构院校名称输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_edit_institution_school_input, console_edit_institution_school_input)
        return self.project.get_current_page_source()

    def set_console_edit_institution_school_short_input_action(self, console_edit_institution_school_short_input):
        """
        动作：设置机构院校简称
        :param console_edit_institution_school_short_input: 机构院校简称
        :return: 设置'机构院校简称'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_edit_institution_school_short_input, console_edit_institution_school_short_input)
        return self.project.get_current_page_source()

    def set_console_english_name_input_action(self, console_english_name_input):
        """
        动作：设置机构院校英文名称输入
        :param console_english_name_input: 机构院校英文名称输入
        :return: 设置'机构院校英文名称输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_english_name_input, console_english_name_input)
        return self.project.get_current_page_source()

    def set_console_edit_contact_person_input_action(self, console_edit_contact_person_input):
        """
        动作：设置联系人输入
        :param console_edit_contact_person_input: 联系人输入
        :return: 设置'联系人输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_edit_contact_person_input, console_edit_contact_person_input)
        return self.project.get_current_page_source()

    def set_console_edit_contact_mobile_input_action(self, console_edit_contact_mobile_input):
        """
        动作：设置联系电话输入
        :param console_edit_contact_mobile_input: 联系电话输入
        :return: 设置'联系电话输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_edit_contact_mobile_input, console_edit_contact_mobile_input)
        return self.project.get_current_page_source()

    def set_console_nature_input_action(self, console_nature_input):
        """
        动作：设置机构院校性质输入
        :param console_nature_input: 机构院校性质输入
        :return: 设置'机构院校性质输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_nature_input, console_nature_input)
        return self.project.get_current_page_source()

    def set_console_contact_user_mobile_input_action(self, console_contact_user_mobile_input):
        """
        动作：设置联系人手机号输入
        :param console_contact_user_mobile_input: 联系人手机号输入
        :return: 设置'联系人手机号输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_contact_user_mobile_input, console_contact_user_mobile_input)
        return self.project.get_current_page_source()

    def click_console_user_at_country_button_action(self):
        """
        动作：点击所属国家
        :return: 点击'所属国家'按钮后的页面
        """
        self.project.click(self.console_user_at_country_button)
        return self.project.get_current_page_source()

    def click_console_user_at_china_button_action(self):
        """
        动作：点击中国
        :return: 点击'中国'按钮后的页面
        """
        self.project.click(self.console_user_at_china_button)
        return self.project.get_current_page_source()

    def click_console_user_at_colombia_button_action(self):
        """
        动作：点击哥伦比亚
        :return: 点击'哥伦比亚'按钮后的页面
        """
        self.project.click(self.console_user_at_colombia_button)
        return self.project.get_current_page_source()

    def set_console_email_input_action(self, console_email_input):
        """
        动作：设置邮箱输入
        :param console_email_input: 邮箱输入
        :return: 设置'邮箱输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_email_input, console_email_input)
        return self.project.get_current_page_source()

    def click_console_edit_type_button_action(self):
        """
        动作：点击类型选择
        :return: 点击'类型选择'按钮后的页面
        """
        self.project.click(self.console_edit_type_button)
        return self.project.get_current_page_source()

    def click_console_edit_type_institution_button_action(self):
        """
        动作：点击类型(机构)
        :return: 点击'类型(机构)'按钮后的页面
        """
        self.project.click(self.console_edit_type_institution_button)
        return self.project.get_current_page_source()

    def click_console_edit_type_school_button_action(self):
        """
        动作：点击类型(院校)
        :return: 点击'类型(院校)'按钮后的页面
        """
        self.project.click(self.console_edit_type_school_button)
        return self.project.get_current_page_source()

    def click_console_channel_button_action(self):
        """
        动作：点击所属频道
        :return: 点击'所属频道'按钮后的页面
        """
        self.project.click(self.console_channel_button)
        return self.project.get_current_page_source()

    def click_console_channel_language_button_action(self):
        """
        动作：点击所属频道(语言培训)
        :return: 点击'所属频道(语言培训)'按钮后的页面
        """
        self.project.click(self.console_channel_language_button)
        return self.project.get_current_page_source()

    def click_console_channel_language_create_button_action(self):
        """
        动作：点击所属频道(语言培训创建)
        :return: 点击'所属频道(语言培训创建)'按钮后的页面
        """
        self.project.click(self.console_channel_language_create_button)
        return self.project.get_current_page_source()

    def click_console_main_areas_button_action(self):
        """
        动作：点击主要领域
        :return: 点击'主要领域'按钮后的页面
        """
        self.project.click(self.console_main_areas_button)
        return self.project.get_current_page_source()

    def click_console_main_areas_language_button_action(self):
        """
        动作：点击主要领域(语言培训)
        :return: 点击'主要领域(语言培训)'按钮后的页面
        """
        self.project.click(self.console_main_areas_language_button)
        return self.project.get_current_page_source()

    def click_console_edit_whether_jjl_yes_button_action(self):
        """
        动作：点击是否金吉列(是)
        :return: 点击'是否金吉列(是)'按钮后的页面
        """
        self.project.click(self.console_edit_whether_jjl_yes_button)
        return self.project.get_current_page_source()

    def click_console_edit_whether_jjl_no_button_action(self):
        """
        动作：点击是否金吉列(否)
        :return: 点击'是否金吉列(否)'按钮后的页面
        """
        self.project.click(self.console_edit_whether_jjl_no_button)
        return self.project.get_current_page_source()

    def set_console_edit_contact_address_input_action(self, console_edit_contact_address_input):
        """
        动作：设置联系地址
        :param console_edit_contact_address_input: 联系地址
        :return: 设置'联系地址'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_edit_contact_address_input, console_edit_contact_address_input)
        return self.project.get_current_page_source()

    def set_console_user_type_input_action(self, console_user_type_input):
        """
        动作：设置机构院校类型输入
        :param console_user_type_input: 机构院校类型输入
        :return: 设置'机构院校类型输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_user_type_input, console_user_type_input)
        return self.project.get_current_page_source()

    def set_console_website_input_action(self, console_website_input):
        """
        动作：设置官网输入
        :param console_website_input: 官网输入
        :return: 设置'官网输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_website_input, console_website_input)
        return self.project.get_current_page_source()

    def set_console_institution_school_present_input_action(self, console_institution_school_present_input):
        """
        动作：设置机构院校介绍输入
        :param console_institution_school_present_input: 机构院校介绍输入
        :return: 设置'机构院校介绍输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_institution_school_present_input, console_institution_school_present_input)
        return self.project.get_current_page_source()

    def set_console_edit_power_attorney_input_action(self, console_edit_power_attorney_input):
        """
        动作：设置委托授权书
        :param console_edit_power_attorney_input: 委托授权书
        :return: 设置'委托授权书'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_edit_power_attorney_input, console_edit_power_attorney_input)
        return self.project.get_current_page_source()

    def click_console_edit_power_attorney_button_action(self):
        """
        动作：点击委托授权书按钮
        :return: 点击'委托授权书按钮'按钮后的页面
        """
        self.project.click(self.console_edit_power_attorney_button)
        return self.project.get_current_page_source()

    def set_console_edit_power_attorney_upload_input_action(self, console_edit_power_attorney_upload_input):
        """
        动作：设置委托授权书上传
        :param console_edit_power_attorney_upload_input: 委托授权书上传
        :return: 设置'委托授权书上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_edit_power_attorney_upload_input, console_edit_power_attorney_upload_input)
        return self.project.get_current_page_source()

    def set_console_edit_business_license_input_action(self, console_edit_business_license_input):
        """
        动作：设置营业执照
        :param console_edit_business_license_input: 营业执照
        :return: 设置'营业执照'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_edit_business_license_input, console_edit_business_license_input)
        return self.project.get_current_page_source()

    def click_console_edit_business_license_button_action(self):
        """
        动作：点击营业执照按钮
        :return: 点击'营业执照按钮'按钮后的页面
        """
        self.project.click(self.console_edit_business_license_button)
        return self.project.get_current_page_source()

    def set_console_edit_business_license_upload_input_action(self, console_edit_business_license_upload_input):
        """
        动作：设置营业执照上传
        :param console_edit_business_license_upload_input: 营业执照上传
        :return: 设置'营业执照上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_edit_business_license_upload_input, console_edit_business_license_upload_input)
        return self.project.get_current_page_source()

    def set_console_edit_institution_school_logo_input_action(self, console_edit_institution_school_logo_input):
        """
        动作：设置机构院校logo
        :param console_edit_institution_school_logo_input: 机构院校logo
        :return: 设置'机构院校logo'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_edit_institution_school_logo_input, console_edit_institution_school_logo_input)
        return self.project.get_current_page_source()

    def click_console_edit_institution_school_logo_button_action(self):
        """
        动作：点击机构院校logo按钮
        :return: 点击'机构院校logo按钮'按钮后的页面
        """
        self.project.click(self.console_edit_institution_school_logo_button)
        return self.project.get_current_page_source()

    def set_console_edit_institution_school_logo_upload_input_action(self, console_edit_institution_school_logo_upload_input):
        """
        动作：设置机构院校logo上传
        :param console_edit_institution_school_logo_upload_input: 机构院校logo上传
        :return: 设置'机构院校logo上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_edit_institution_school_logo_upload_input, console_edit_institution_school_logo_upload_input)
        return self.project.get_current_page_source()

    def set_console_edit_institution_school_background_input_action(self, console_edit_institution_school_background_input):
        """
        动作：设置机构院校主要背景
        :param console_edit_institution_school_background_input: 机构院校主要背景
        :return: 设置'机构院校主要背景'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_edit_institution_school_background_input, console_edit_institution_school_background_input)
        return self.project.get_current_page_source()

    def click_console_edit_institution_school_background_button_action(self):
        """
        动作：点击机构院校主要背景按钮
        :return: 点击'机构院校主要背景按钮'按钮后的页面
        """
        self.project.click(self.console_edit_institution_school_background_button)
        return self.project.get_current_page_source()

    def set_console_edit_institution_school_background_upload_input_action(self, console_edit_institution_school_background_upload_input):
        """
        动作：设置机构院校主要背景上传
        :param console_edit_institution_school_background_upload_input: 机构院校主要背景上传
        :return: 设置'机构院校主要背景上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_edit_institution_school_background_upload_input, console_edit_institution_school_background_upload_input)
        return self.project.get_current_page_source()

    def set_console_create_time_input_action(self, console_create_time_input):
        """
        动作：设置创立时间输入
        :param console_create_time_input: 创立时间输入
        :return: 设置'创立时间输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_create_time_input, console_create_time_input)
        return self.project.get_current_page_source()

    def set_console_legal_person_input_action(self, console_legal_person_input):
        """
        动作：设置法人输入
        :param console_legal_person_input: 法人输入
        :return: 设置'法人输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_legal_person_input, console_legal_person_input)
        return self.project.get_current_page_source()

    def click_console_refer_button_action(self):
        """
        动作：点击提交按钮
        :return: 点击'提交按钮'按钮后的页面
        """
        self.project.click(self.console_refer_button)
        return self.project.get_current_page_source()

    # endregion Actions
