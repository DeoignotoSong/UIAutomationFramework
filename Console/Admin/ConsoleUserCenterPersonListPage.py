from Utils.Log import log

"""
后台首页-用户中心-用户管理-用户列表
console_url/person/person-list
"""


class ConsoleUserCenterPersonListPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/person/person-list'
        # region Fields
        # 消息提示框按钮
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 用户昵称输入框
        self._user_nick_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[1]/div/div/input'
        # 注册频道下拉框按钮
        self._register_channel_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[2]/div/div'
        # 注册频道-全部按钮
        self._register_channel_all_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[1]'
        # 注册频道-总首页按钮
        self._register_channel_home_page_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[2]'
        # 注册频道-出国留学按钮
        self._register_channel_study_aboard_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[3]'
        # 注册频道-语言培训按钮
        self._register_channel_language_training_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[4]'
        # 注册频道-院校直通车按钮
        self._register_channel_college_direct_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[5]'
        # 注册频道-海外移民按钮
        self._register_channel_overseas_immigrants = '/html/body/div[3]/div[1]/div[1]/ul/li[6]'
        # 性别下拉框按钮
        self._sex_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[3]/div/div'
        # 性别-全部按钮
        self._sex_all_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[1]'
        # 性别-男按钮
        self._sex_male_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[2]'
        # 性别女按钮
        self._sex_female_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[3]'
        # 用户手机输入框
        self._mobile_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[4]/div/div/input'
        # 角色类型下拉框按钮
        self._role_type_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[5]/div/div'
        # 角色类型-全部按钮
        self._role_type_all_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[1]'
        # 角色类型-普通用户按钮
        self._role_type_user_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[2]'
        # 角色类型-讲师按钮
        self._role_type_teacher_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[2]'
        # 角色类型-顾问按钮
        self._role_type_adviser_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[4]'
        # 角色类型-大咖按钮
        self._role_type_celebrity_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[5]'
        # 认证情况下拉框按钮
        self._authentication_state_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[6]/div/div'
        # 认证情况-全部按钮
        self._authentication_state_all_button_tag = '/html/body/div[6]/div[1]/div[1]/ul/li[1]'
        # 认证情况-未认证按钮
        self._authentication_state_unpass_button_tag = '/html/body/div[6]/div[1]/div[1]/ul/li[2]'
        # 认证情况-已认证按钮
        self._authentication_state_pass_button_tag = '/html/body/div[6]/div[1]/div[1]/ul/li[3]'
        # 状态下拉框按钮
        self._state_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[7]/div/div'
        # 状态-全部按钮
        self._state_all_button_tag = '/html/body/div[7]/div[1]/div[1]/ul/li[1]'
        # 状态-正常按钮
        self._state_normal_button_tag = '/html/body/div[6]/div[1]/div[1]/ul/li[2]'
        # 状态-禁用按钮
        self._state_disable_button_tag = '/html/body/div[6]/div[1]/div[1]/ul/li[3]'
        # 用户id输入框
        self._user_id_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[8]/div/div/input'
        # 用户姓名输入框
        self._user_name_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[9]/div/div/input'
        # 查询按钮
        self._search_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[13]/div/button'
        # 清除按钮
        self._clear_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[14]/div/button'
        # 创建用户按钮
        self._create_user_button_tag = '//*[@id="tableSearch"]/form/div[2]/div[1]/div/button'
        # 创建用户-登录密码输入框
        self._create_user_password_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[1]/div[1]/div/div/div[1]/input'
        # 创建用户-登录密码错误提示
        self._create_user_password_error_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[1]/div[1]/div/div/div[2]'
        # 创建用户-用户昵称输入框
        self._create_user_nick_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[2]/div[1]/div/div/div[1]/input'
        # 创建用户-用于昵称错误提示
        self._create_user_nick_error_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[2]/div[1]/div/div/div[2]'
        # 创建用户-邮箱输入框
        self._create_user_email_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[3]/div[1]/div/div/div[1]/input'
        # 创建用户-邮箱错误提示
        self._create_user_email_error_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[3]/div[1]/div/div/div[2]'
        # 创建用户-联系电话输入框
        self._create_user_mobile_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[2]/div[2]/div/div/div[1]/input'
        # 创建用户-联系电话错误提示
        self._create_user_mobile_error_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[2]/div[2]/div/div/div[last()]'
        # 创建用户-所在国家下拉框
        self._create_user_country_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[3]/div[2]/div/div/div/div'
        # 创建用户-所在国家-第一个国家
        self._create_user_country_first_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[1]'
        # 创建用户-所在国家-中国
        self._create_user_country_china_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[44]'
        # 创建用户-出生地-省份错误提示
        self._create_user_born_province_error_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[4]/div[3]/div[1]/div/div[2]'
        # 创建用户-出生地-省份下拉框
        self._create_user_born_province_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[4]/div[3]/div[1]/div/div[1]/div'
        # 创建用户-出生地-省份-第一个省份
        self._create_user_born_province_first_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[1]'
        # 创建用户-出生地-城市错误提示
        self._create_user_born_city_error_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[4]/div[3]/div[2]/div/div[2]'
        # 创建用户-出生地-城市下拉框
        self._create_user_born_city_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[4]/div[3]/div[2]/div/div[1]/div'
        # 创建用户-出生地-城市-第一个城市
        self._create_user_born_city_first_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li'
        # 创建用户-出生地-县区-错误提示
        self._create_user_born_district_error_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[4]/div[3]/div[3]/div/div[2]'
        # 创建用户-出生地-县区下拉框
        self._create_user_born_district_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[4]/div[3]/div[3]/div/div[1]/div'
        # 创建用户-出生地-县区-第一个区
        self._create_user_born_district_first_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[1]'
        # 创建用户-出生地输入框
        self._create_user_born_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[4]/div[2]/div/div/div[1]/input'
        # 创建用户-出生地-错误提示
        self._create_user_born_error_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[4]/div[2]/div/div/div[2]'
        # 创建用户-性别下拉框
        self._create_user_sex_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[4]/div[1]/div/div/div/div'
        # 创建用户-性别-男
        self._create_user_sex_male_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[1]'
        # 创建用户-性别-女
        self._create_user_female_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[2]'
        # 创建用户-禁用状态下拉框
        self._create_user_state_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[5]/div[1]/div/div/div/div'
        # 创建用户-禁用状态-正常
        self._create_user_state_normal_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[1]'
        # 创建用户-禁用状态-禁用
        self._create_user_state_prohibition_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[2]'
        # 创建用户-用户头像
        self._create_user_avatar_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[6]/div/div/div/div/div/div/input'
        # 创建用户-用户头像错误提示
        self._create_user_avatar_error_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[6]/div/div/div/div[2]'
        # 创建用户-用户头像-上传后图片
        self._create_user_avatar_image_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[6]/div/div/div/div/div/div/div[1]/img'
        # 创建用户-提交用户信息按钮
        self._create_user_commit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[3]/span/button'
        # 创建展会用户
        self._create_exhibition_user_button_tag = '//*[@id="tableSearch"]/form/div[2]/div[2]/div/button'
        # 编辑用户-讲师-用户ID
        self._edit_teacher_id_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[1]/div[1]/div/div/div/input'
        # 编辑用户-讲师-登录密码
        self._edit_teacher_password_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[1]/div[2]/div/div/div/input'
        # 编辑用户-讲师-用户类型
        self._edit_teacher_role_type_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[2]/div[1]/div/div/div/input'
        # 编辑用户-讲师-头衔
        self._edit_teacher_title_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[2]/div[2]/div/div/div/input'
        # 编辑用户-讲师-机构院校名称
        self._edit_teacher_institute_name_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[3]/div[1]/div/div/div/input'
        # 编辑用户-讲师-认证时间
        self._edit_teacher_institute_authentication_time_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[3]/div[2]/div/div/div/input'
        # 编辑用户-讲师-用户账号
        self._edit_teacher_username_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[4]/div[1]/div/div/div/input'
        # 编辑用户-讲师-用户昵称
        self._edit_teacher_nick_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[4]/div[2]/div/div/div/input'
        # 编辑用户-讲师-联系电话
        self._edit_teacher_mobile_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[5]/div[1]/div/div/div/input'
        # 编辑用户-讲师-邮箱
        self._edit_teacher_email_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[5]/div[2]/div/div/div/input'
        # 编辑用户-讲师-所属国家下拉框
        self._edit_teacher_country_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[6]/div[1]/div/div/div/div'
        # 编辑用户-讲师-所在国家-第一个国家
        self._edit_teacher_country_first_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[44]'
        # 编辑用户-讲师-所在国家-中国
        self._edit_teacher_country_china_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[44]'
        # 编辑用户-讲师-所在国家输入框
        self._edit_teacher_country_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[6]/div[1]/div/div/div/div/input'
        # 编辑用户-讲师-性别
        self._edit_teacher_sex_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[6]/div[2]/div/div/div/div[1]/input'
        # 编辑用户-讲师-性别-全部
        self._edit_teacher_sex_all_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[1]'
        # 编辑用户-讲师-性别-男
        self._edit_teacher_sex_male_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[2]'
        # 编辑用户-讲师-性别-女
        self._edit_teacher_sex_female_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[3]'
        # 编辑用户-讲师-出生地-省份下拉框
        self._edit_teacher_born_province_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[7]/div[2]/div[1]/div/div/div'
        # 编辑用户-讲师-出生地-省份-第一个省份
        self._edit_teacher_born_province_first_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[1]'
        # 编辑用户-讲师-出生地-省份输入框
        self._edit_teacher_born_province_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[7]/div[2]/div[1]/div/div/div/input'
        # 编辑用户-讲师-出生地-城市下拉框
        self._edit_teacher_born_city_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[7]/div[2]/div[2]/div/div/div'
        # 编辑用户-讲师-出生地-城市-第一个城市
        self._edit_teacher_born_city_first_button_tag = '/html/body/div[6]/div[1]/div[1]/ul/li[1]'
        # 编辑用户-讲师-出生地-城市输入框
        self._edit_teacher_born_city_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[7]/div[2]/div[2]/div/div/div/input'
        # 编辑用户-讲师-出生地-县区下拉框
        self._edit_teacher_born_district_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[7]/div[2]/div[3]/div/div/div'
        # 编辑用户-讲师-出生地-县区-第一个县区
        self._edit_teacher_born_district_first_button_tag = '/html/body/div[6]/div[1]/div[1]/ul/li[1]'
        # 编辑用户-讲师-出生地-县区
        self._edit_teacher_born_district_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[7]/div[2]/div[3]/div/div/div/input'
        # 编辑用户-讲师-出生地输入框
        self._edit_teacher_born_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[7]/div[1]/div/div/div/input'
        # 编辑用户-讲师-禁用状态
        self._edit_teacher_state_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[7]/div[2]/div/div/div/div[1]/input'
        # 编辑用户-讲师-注册渠道
        self._edit_teacher_register_method_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[8]/div[1]/div/div/div/div[1]/input'
        # 编辑用户-讲师-用户姓名
        self._edit_teacher_real_name_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[8]/div[2]/div/div/div/input'
        # 编辑用户-讲师-证件类型
        self._edit_teacher_id_type_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[9]/div[1]/div/div/div/div[1]/input'
        # 编辑用户-讲师-证件号码
        self._edit_teacher_id_card_number_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[9]/div[2]/div/div/div/input'
        # 编辑用户-讲师-频道
        self._edit_teacher_channel_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[10]/div[1]/div/div/div/div[1]/input'
        # 编辑用户-讲师-认证状态已认证
        self._edit_teacher_authentication_state_pass_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[10]/div[2]/div/div/div/label[1]/span[1]'
        # 编辑用户-讲师-认证状态未认证
        self._edit_teacher_authentication_state_unpass_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[10]/div[2]/div/div/div/label[2]/span[1]'
        # 编辑用户-讲师-是否有首页-是
        self._edit_teacher_have_homepage_yes_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[11]/div/div/div/div/label[1]'
        # 编辑用户-讲师-是否有首页-否
        self._edit_teacher_have_homepage_no_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[11]/div/div/div/div/label[2]'
        # 编辑用户-讲师-用户头像-更换头像
        self._edit_teacher_avatar_change_avatar_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[12]/div/div/div/div/div/div/input'
        # 编辑用户-讲师-提交信息按钮
        self._edit_teacher_commit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[3]/span/button'
        # 编辑用户-讲师-关闭按钮
        self._edit_teacher_close_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[1]/button'
        # 编辑用户-普通用户-用户ID
        self._edit_user_id_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[1]/div[1]/div/div/div/input'
        # 编辑用户-普通用户-登录密码
        self._edit_user_password_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[1]/div[2]/div/div/div/input'
        # 编辑用户-普通用户-用户类型
        self._edit_user_role_type_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[2]/div[1]/div/div/div/input'
        # 编辑用户-普通用户-头衔
        self._edit_user_title_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[2]/div[2]/div/div/div/input'
        # 编辑用户-普通用户-用户账号
        self._edit_user_username_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[3]/div[1]/div/div/div/input'
        # 编辑用户-普通用户-用户昵称
        self._edit_user_nick_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[3]/div[2]/div/div/div/input'
        # 编辑用户-普通用户-联系电话
        self._edit_user_mobile_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[4]/div[1]/div/div/div/input'
        # 编辑用户-普通用户-邮箱
        self._edit_user_email_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[4]/div[2]/div/div/div/input'
        # 编辑用户-普通用户-所属国家下拉框
        self._edit_user_country_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[5]/div[1]/div/div/div/div'
        # 编辑用户-普通用户-所在国家-第一个国家
        self._edit_user_country_first_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[44]'
        # 编辑用户-普通用户-所在国家-中国
        self._edit_user_country_china_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[44]'
        # 编辑用户-普通用户-所在国家输入框
        self._edit_user_country_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[5]/div[1]/div/div/div/div/input'
        # 编辑用户-普通用户-性别
        self._edit_user_sex_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[5]/div[2]/div/div/div/div[1]/input'
        # 编辑用户-普通用户-性别-全部
        self._edit_user_sex_all_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 编辑用户-普通用户-性别-男
        self._edit_user_sex_male_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]'
        # 编辑用户-普通用户-性别-女
        self._edit_user_sex_female_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[3]'
        # 编辑用户-普通用户-出生地-省份下拉框
        self._edit_user_born_province_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[6]/div[2]/div[1]/div/div/div'
        # 编辑用户-普通用户-出生地-省份-第一个省份
        self._edit_user_born_province_first_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 编辑用户-普通用户-出生地-省份输入框
        self._edit_user_born_province_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[6]/div[2]/div[1]/div/div/div/input'
        # 编辑用户-普通用户-出生地-城市下拉框
        self._edit_user_born_city_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[6]/div[2]/div[2]/div/div/div'
        # 编辑用户-普通用户-出生地-城市-第一个城市
        self._edit_user_born_city_first_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 编辑用户-普通用户-出生地-城市输入框
        self._edit_user_born_city_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[6]/div[2]/div[2]/div/div/div/input'
        # 编辑用户-普通用户-出生地-县区下拉框
        self._edit_user_born_district_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[6]/div[2]/div[3]/div/div/div'
        # 编辑用户-普通用户-出生地-县区-第一个县区
        self._edit_user_born_district_first_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 编辑用户-普通用户-出生地-县区输入框
        self._edit_user_born_district_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[6]/div[2]/div[3]/div/div/div/input'
        # 编辑用户-普通用户-出生地输入框
        self._edit_user_born_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[6]/div[1]/div/div/div/input'
        # 编辑用户-普通用户-禁用状态
        self._edit_user_state_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[6]/div[2]/div/div/div/div[1]/input'
        # 编辑用户-普通用户-注册渠道
        self._edit_user_register_method_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[7]/div[1]/div/div/div/div[1]/input'
        # 编辑用户-普通用户-用户姓名
        self._edit_user_real_name_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[7]/div[2]/div/div/div/input'
        # 编辑用户-普通用户-证件类型
        self._edit_user_id_type_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[8]/div[1]/div/div/div/div[1]/input'
        # 编辑用户-普通用户-证件号码
        self._edit_user_id_card_number_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[8]/div[2]/div/div/div/input'
        # 编辑用户-普通用户-频道
        self._edit_user_channel_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[9]/div[1]/div/div/div/div[1]/input'
        # 编辑用户-普通用户-认证状态已认证
        self._edit_user_authentication_state_pass_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[9]/div[2]/div/div/div/label[1]/span[1]'
        # 编辑用户-普通用户-认证状态未认证
        self._edit_user_authentication_state_unpass_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[9]/div[2]/div/div/div/label[2]/span[1]'
        # 编辑用户-普通用户-是否有首页-是
        self._edit_user_have_homepage_yes_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[10]/div/div/div/div/label[1]'
        # 编辑用户-普通用户-是否有首页-否
        self._edit_user_have_homepage_no_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[10]/div/div/div/div/label[2]'
        # 编辑用户-普通用户-用户头像-更换头像
        self._edit_user_avatar_change_avatar_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[2]/form/div[11]/div/div/div/div/div/div/input'
        # 编辑用户-普通用户-提交信息按钮
        self._edit_user_commit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[3]/span/button'
        # 编辑用户-普通用户-关闭按钮
        self._edit_user_close_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div/div/div[1]/button'
        # 第一个-用户ID按钮
        self._first_user_id_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/a'
        # 第一行-用户ID
        self._first_user_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/a/span'
        # 第一行-用户昵称
        self._first_user_nick_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 第一行-用户姓名
        self._first_user_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 第一行-用户手机
        self._first_user_mobile_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 第一行-角色类型
        self._first_role_type_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 第一行-性别
        self._first_sex_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div'
        # 第一行-用户注册时间
        self._first_user_register_time_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div'
        # 第一行-最近活动时间
        self._first_last_active_time_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div'
        # 第一行-状态
        self._first_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[13]/div'
        # 第一行-认证情况
        self._first_authentication_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[14]/div'
        # 第一行-注册频道
        self._first_register_channel_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[15]/div'
        # 第一行-编辑按钮
        self._first_edit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[16]/div/a[1]'
        # 第一行禁用/解禁按钮
        self._first_ban_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[16]/div/a[2]'
        # 禁用理由输入框
        self._ban_reason_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div/div[2]/form/div[3]/div/div/textarea'
        # 禁用确认按钮
        self._ban_confirm_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div/div[3]/span/button[2]'
        # 禁用取消按钮
        self._ban_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div/div[3]/span/button[1]'
        # 解禁确认按钮
        self._lift_ban_confirm_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # 解禁取消按钮
        self._lift_ban_cancel_button_tag = '/html/body/div[2]/div/div[3]/button[1]'
        # endregion Fields

    # region Properties
    @property
    def message_content_text(self):
        """
        属性: 消息提示框按钮
        :return: 消息提示框按钮
        """
        element = None
        try:
            element = self.project.get_element(self._message_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def user_nick_input(self):
        """
        属性: 用户昵称输入框
        :return: 用户昵称输入框
        """
        element = None
        try:
            element = self.project.get_element(self._user_nick_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def register_channel_button(self):
        """
        属性: 注册频道下拉框按钮
        :return: 注册频道下拉框按钮
        """
        element = None
        try:
            element = self.project.get_element(self._register_channel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def register_channel_all_button(self):
        """
        属性: 注册频道-全部按钮
        :return: 注册频道-全部按钮
        """
        element = None
        try:
            element = self.project.get_element(self._register_channel_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def register_channel_home_page_button(self):
        """
        属性: 注册频道-总首页按钮
        :return: 注册频道-总首页按钮
        """
        element = None
        try:
            element = self.project.get_element(self._register_channel_home_page_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def register_channel_study_aboard_button(self):
        """
        属性: 注册频道-出国留学按钮
        :return: 注册频道-出国留学按钮
        """
        element = None
        try:
            element = self.project.get_element(self._register_channel_study_aboard_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def register_channel_language_training_button(self):
        """
        属性: 注册频道-语言培训按钮
        :return: 注册频道-语言培训按钮
        """
        element = None
        try:
            element = self.project.get_element(self._register_channel_language_training_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def register_channel_college_direct_button(self):
        """
        属性: 注册频道-院校直通车按钮
        :return: 注册频道-院校直通车按钮
        """
        element = None
        try:
            element = self.project.get_element(self._register_channel_college_direct_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def sex_button(self):
        """
        属性: 性别下拉框按钮
        :return: 性别下拉框按钮
        """
        element = None
        try:
            element = self.project.get_element(self._sex_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def sex_all_button(self):
        """
        属性: 性别-全部按钮
        :return: 性别-全部按钮
        """
        element = None
        try:
            element = self.project.get_element(self._sex_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def sex_male_button(self):
        """
        属性: 性别-男按钮
        :return: 性别-男按钮
        """
        element = None
        try:
            element = self.project.get_element(self._sex_male_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def sex_female_button(self):
        """
        属性: 性别女按钮
        :return: 性别女按钮
        """
        element = None
        try:
            element = self.project.get_element(self._sex_female_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def mobile_input(self):
        """
        属性: 用户手机输入框
        :return: 用户手机输入框
        """
        element = None
        try:
            element = self.project.get_element(self._mobile_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def role_type_button(self):
        """
        属性: 角色类型下拉框按钮
        :return: 角色类型下拉框按钮
        """
        element = None
        try:
            element = self.project.get_element(self._role_type_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def role_type_all_button(self):
        """
        属性: 角色类型-全部按钮
        :return: 角色类型-全部按钮
        """
        element = None
        try:
            element = self.project.get_element(self._role_type_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def role_type_user_button(self):
        """
        属性: 角色类型-普通用户按钮
        :return: 角色类型-普通用户按钮
        """
        element = None
        try:
            element = self.project.get_element(self._role_type_user_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def role_type_teacher_button(self):
        """
        属性: 角色类型-讲师按钮
        :return: 角色类型-讲师按钮
        """
        element = None
        try:
            element = self.project.get_element(self._role_type_teacher_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def role_type_adviser_button(self):
        """
        属性: 角色类型-顾问按钮
        :return: 角色类型-顾问按钮
        """
        element = None
        try:
            element = self.project.get_element(self._role_type_adviser_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def role_type_celebrity_button(self):
        """
        属性: 角色类型-大咖按钮
        :return: 角色类型-大咖按钮
        """
        element = None
        try:
            element = self.project.get_element(self._role_type_celebrity_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def authentication_state_button(self):
        """
        属性: 认证情况下拉框按钮
        :return: 认证情况下拉框按钮
        """
        element = None
        try:
            element = self.project.get_element(self._authentication_state_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def authentication_state_all_button(self):
        """
        属性: 认证情况-全部按钮
        :return: 认证情况-全部按钮
        """
        element = None
        try:
            element = self.project.get_element(self._authentication_state_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def authentication_state_unpass_button(self):
        """
        属性: 认证情况-未认证按钮
        :return: 认证情况-未认证按钮
        """
        element = None
        try:
            element = self.project.get_element(self._authentication_state_unpass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def authentication_state_pass_button(self):
        """
        属性: 认证情况-已认证按钮
        :return: 认证情况-已认证按钮
        """
        element = None
        try:
            element = self.project.get_element(self._authentication_state_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def state_button(self):
        """
        属性: 状态下拉框按钮
        :return: 状态下拉框按钮
        """
        element = None
        try:
            element = self.project.get_element(self._state_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def state_all_button(self):
        """
        属性: 状态-全部按钮
        :return: 状态-全部按钮
        """
        element = None
        try:
            element = self.project.get_element(self._state_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def state_normal_button(self):
        """
        属性: 状态-正常按钮
        :return: 状态-正常按钮
        """
        element = None
        try:
            element = self.project.get_element(self._state_normal_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def state_disable_button(self):
        """
        属性: 状态-禁用按钮
        :return: 状态-禁用按钮
        """
        element = None
        try:
            element = self.project.get_element(self._state_disable_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def user_id_input(self):
        """
        属性: 用户id输入框
        :return: 用户id输入框
        """
        element = None
        try:
            element = self.project.get_element(self._user_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def user_name_input(self):
        """
        属性: 用户姓名输入框
        :return: 用户姓名输入框
        """
        element = None
        try:
            element = self.project.get_element(self._user_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_button(self):
        """
        属性: 查询按钮
        :return: 查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def clear_button(self):
        """
        属性: 清楚按钮
        :return: 清楚按钮
        """
        element = None
        try:
            element = self.project.get_element(self._clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_button(self):
        """
        属性: 创建用户按钮
        :return: 创建用户按钮
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_password_input(self):
        """
        属性: 创建用户-登录密码输入框
        :return: 创建用户-登录密码输入框
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_password_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_password_error_text(self):
        """
        属性: 创建用户-登录密码错误提示
        :return: 创建用户-登录密码错误提示
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_password_error_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_nick_input(self):
        """
        属性: 创建用户-用户昵称输入框
        :return: 创建用户-用户昵称输入框
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_nick_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_nick_error_text(self):
        """
        属性: 创建用户-用于昵称错误提示
        :return: 创建用户-用于昵称错误提示
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_nick_error_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_email_input(self):
        """
        属性: 创建用户-邮箱输入框
        :return: 创建用户-邮箱输入框
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_email_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_email_error_text(self):
        """
        属性: 创建用户-邮箱错误提示
        :return: 创建用户-邮箱错误提示
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_email_error_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_mobile_input(self):
        """
        属性: 创建用户-联系电话输入框
        :return: 创建用户-联系电话输入框
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_mobile_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_mobile_error_text(self):
        """
        属性: 创建用户-联系电话错误提示
        :return: 创建用户-联系电话错误提示
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_mobile_error_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_country_button(self):
        """
        属性: 创建用户-所在国家下拉框
        :return: 创建用户-所在国家下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_country_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_country_first_button(self):
        """
        属性: 创建用户-所在国家-第一个国家
        :return: 创建用户-所在国家-第一个国家
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_country_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_country_china_button(self):
        """
        属性: 创建用户-所在国家-中国
        :return: 创建用户-所在国家-中国
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_country_china_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_born_province_error_text(self):
        """
        属性: 创建用户-出生地-省份错误提示
        :return: 创建用户-出生地-省份错误提示
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_born_province_error_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_born_province_button(self):
        """
        属性: 创建用户-出生地-省份下拉框
        :return: 创建用户-出生地-省份下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_born_province_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_born_province_first_button(self):
        """
        属性: 创建用户-出生地-省份-第一个省份
        :return: 创建用户-出生地-省份-第一个省份
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_born_province_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_born_city_error_text(self):
        """
        属性: 创建用户-出生地-城市错误提示
        :return: 创建用户-出生地-城市错误提示
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_born_city_error_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_born_city_button(self):
        """
        属性: 创建用户-出生地-城市下拉框
        :return: 创建用户-出生地-城市下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_born_city_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_born_city_first_button(self):
        """
        属性: 创建用户-出生地-城市-第一个城市
        :return: 创建用户-出生地-城市-第一个城市
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_born_city_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_born_district_error_text(self):
        """
        属性: 创建用户-出生地-县区-错误提示
        :return: 创建用户-出生地-县区-错误提示
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_born_district_error_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_born_district_button(self):
        """
        属性: 创建用户-出生地-县区下拉框
        :return: 创建用户-出生地-县区下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_born_district_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_born_district_first_button(self):
        """
        属性: 创建用户-出生地-县区-第一个区
        :return: 创建用户-出生地-县区-第一个区
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_born_district_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_born_input(self):
        """
        属性: 创建用户-出生地输入框
        :return: 创建用户-出生地输入框
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_born_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_born_error_text(self):
        """
        属性: 创建用户-出生地-错误提示
        :return: 创建用户-出生地-错误提示
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_born_error_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_sex_button(self):
        """
        属性: 创建用户-性别下拉框
        :return: 创建用户-性别下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_sex_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_sex_male_button(self):
        """
        属性: 创建用户-性别-男
        :return: 创建用户-性别-男
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_sex_male_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_female_button(self):
        """
        属性: 创建用户-性别-女
        :return: 创建用户-性别-女
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_female_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_state_button(self):
        """
        属性: 创建用户-禁用状态下拉框
        :return: 创建用户-禁用状态下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_state_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_state_normal_button(self):
        """
        属性: 创建用户-禁用状态-正常
        :return: 创建用户-禁用状态-正常
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_state_normal_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_state_prohibition_button(self):
        """
        属性: 创建用户-禁用状态-禁用
        :return: 创建用户-禁用状态-禁用
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_state_prohibition_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_avatar_input(self):
        """
        属性: 创建用户-用户头像
        :return: 创建用户-用户头像
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_avatar_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_avatar_error_text(self):
        """
        属性: 创建用户-用户头像错误提示
        :return: 创建用户-用户头像错误提示
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_avatar_error_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_avatar_image_button(self):
        """
        属性: 创建用户-用户头像-上传后图片
        :return: 创建用户-用户头像-上传后图片
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_avatar_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_user_commit_button(self):
        """
        属性: 创建用户-提交用户信息按钮
        :return: 创建用户-提交用户信息按钮
        """
        element = None
        try:
            element = self.project.get_element(self._create_user_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def create_exhibition_user_button(self):
        """
        属性: 创建展会用户
        :return: 创建展会用户
        """
        element = None
        try:
            element = self.project.get_element(self._create_exhibition_user_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_id(self):
        """
        属性: 编辑用户-讲师-用户ID
        :return: 编辑用户-讲师-用户ID
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_id_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_password_input(self):
        """
        属性: 编辑用户-讲师-登录密码
        :return: 编辑用户-讲师-登录密码
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_password_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_role_type(self):
        """
        属性: 编辑用户-讲师-用户类型
        :return: 编辑用户-讲师-用户类型
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_role_type_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_title_input(self):
        """
        属性: 编辑用户-讲师-头衔
        :return: 编辑用户-讲师-头衔
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_title_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_institute_name(self):
        """
        属性: 编辑用户-讲师-机构院校名称
        :return: 编辑用户-讲师-机构院校名称
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_institute_name_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_institute_authentication_time(self):
        """
        属性: 编辑用户-讲师-认证时间
        :return: 编辑用户-讲师-认证时间
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_institute_authentication_time_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_username(self):
        """
        属性: 编辑用户-讲师-用户账号
        :return: 编辑用户-讲师-用户账号
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_username_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_nick_input(self):
        """
        属性: 编辑用户-讲师-用户昵称
        :return: 编辑用户-讲师-用户昵称
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_nick_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_mobile(self):
        """
        属性: 编辑用户-讲师-联系电话
        :return: 编辑用户-讲师-联系电话
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_mobile_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_email(self):
        """
        属性: 编辑用户-讲师-邮箱
        :return: 编辑用户-讲师-邮箱
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_email_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_country_button(self):
        """
        属性: 编辑用户-讲师-所属国家下拉框
        :return: 编辑用户-讲师-所属国家下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_country_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_country_first_button(self):
        """
        属性: 编辑用户-讲师-所在国家-第一个国家
        :return: 编辑用户-讲师-所在国家-第一个国家
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_country_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_country_china_button(self):
        """
        属性: 编辑用户-讲师-所在国家-中国
        :return: 编辑用户-讲师-所在国家-中国
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_country_china_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_country_input(self):
        """
        属性: 编辑用户-讲师-所在国家输入框
        :return: 编辑用户-讲师-所在国家输入框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_country_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_sex_button(self):
        """
        属性: 编辑用户-讲师-性别
        :return: 编辑用户-讲师-性别
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_sex_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_sex_all_button(self):
        """
        属性: 编辑用户-讲师-性别-全部
        :return: 编辑用户-讲师-性别-全部
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_sex_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_sex_male_button(self):
        """
        属性: 编辑用户-讲师-性别-男
        :return: 编辑用户-讲师-性别-男
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_sex_male_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_sex_female_button(self):
        """
        属性: 编辑用户-讲师-性别-女
        :return: 编辑用户-讲师-性别-女
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_sex_female_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_born_province_button(self):
        """
        属性: 编辑用户-讲师-出生地-省份下拉框
        :return: 编辑用户-讲师-出生地-省份下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_born_province_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_born_province_first_button(self):
        """
        属性: 编辑用户-讲师-出生地-省份-第一个省份
        :return: 编辑用户-讲师-出生地-省份-第一个省份
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_born_province_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_born_province_input(self):
        """
        属性: 编辑用户-讲师-出生地-省份输入框
        :return: 编辑用户-讲师-出生地-省份输入框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_born_province_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_born_city_button(self):
        """
        属性: 编辑用户-讲师-出生地-城市下拉框
        :return: 编辑用户-讲师-出生地-城市下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_born_city_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_born_city_first_button(self):
        """
        属性: 编辑用户-讲师-出生地-城市-第一个城市
        :return: 编辑用户-讲师-出生地-城市-第一个城市
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_born_city_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_born_city_input(self):
        """
        属性: 编辑用户-讲师-出生地-城市输入框
        :return: 编辑用户-讲师-出生地-城市输入框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_born_city_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_born_district_button(self):
        """
        属性: 编辑用户-讲师-出生地-县区下拉框
        :return: 编辑用户-讲师-出生地-县区下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_born_district_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_born_district_first_button(self):
        """
        属性: 编辑用户-讲师-出生地-县区-第一个县区
        :return: 编辑用户-讲师-出生地-县区-第一个县区
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_born_district_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_born_district_input(self):
        """
        属性: 编辑用户-讲师-出生地-县区
        :return: 编辑用户-讲师-出生地-县区
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_born_district_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_born_input(self):
        """
        属性: 编辑用户-讲师-出生地输入框
        :return: 编辑用户-讲师-出生地输入框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_born_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_state(self):
        """
        属性: 编辑用户-讲师-禁用状态
        :return: 编辑用户-讲师-禁用状态
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_state_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_register_method(self):
        """
        属性: 编辑用户-讲师-注册渠道
        :return: 编辑用户-讲师-注册渠道
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_register_method_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_real_name(self):
        """
        属性: 编辑用户-讲师-用户姓名
        :return: 编辑用户-讲师-用户姓名
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_real_name_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_id_type(self):
        """
        属性: 编辑用户-讲师-证件类型
        :return: 编辑用户-讲师-证件类型
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_id_type_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_id_card_number(self):
        """
        属性: 编辑用户-讲师-证件号码
        :return: 编辑用户-讲师-证件号码
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_id_card_number_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_channel(self):
        """
        属性: 编辑用户-讲师-频道
        :return: 编辑用户-讲师-频道
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_channel_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_authentication_state_pass(self):
        """
        属性: 编辑用户-讲师-认证状态已认证
        :return: 编辑用户-讲师-认证状态已认证
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_authentication_state_pass_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_authentication_state_unpass(self):
        """
        属性: 编辑用户-讲师-认证状态未认证
        :return: 编辑用户-讲师-认证状态未认证
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_authentication_state_unpass_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_have_homepage_yes_button(self):
        """
        属性: 编辑用户-讲师-是否有首页-是
        :return: 编辑用户-讲师-是否有首页-是
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_have_homepage_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_have_homepage_no_button(self):
        """
        属性: 编辑用户-讲师-是否有首页-否
        :return: 编辑用户-讲师-是否有首页-否
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_have_homepage_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_avatar_change_avatar_input(self):
        """
        属性: 编辑用户-讲师-用户头像-更换头像
        :return: 编辑用户-讲师-用户头像-更换头像
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_avatar_change_avatar_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_commit_button(self):
        """
        属性: 编辑用户-讲师-提交信息按钮
        :return: 编辑用户-讲师-提交信息按钮
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_teacher_close_button(self):
        """
        属性: 编辑用户-讲师-关闭按钮
        :return: 编辑用户-讲师-关闭按钮
        """
        element = None
        try:
            element = self.project.get_element(self._edit_teacher_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_id(self):
        """
        属性: 编辑用户-普通用户-用户ID
        :return: 编辑用户-普通用户-用户ID
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_id_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_password_input(self):
        """
        属性: 编辑用户-普通用户-登录密码
        :return: 编辑用户-普通用户-登录密码
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_password_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_role_type(self):
        """
        属性: 编辑用户-普通用户-用户类型
        :return: 编辑用户-普通用户-用户类型
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_role_type_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_title_input(self):
        """
        属性: 编辑用户-普通用户-头衔
        :return: 编辑用户-普通用户-头衔
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_title_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_username(self):
        """
        属性: 编辑用户-普通用户-用户账号
        :return: 编辑用户-普通用户-用户账号
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_username_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_nick_input(self):
        """
        属性: 编辑用户-普通用户-用户昵称
        :return: 编辑用户-普通用户-用户昵称
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_nick_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_mobile(self):
        """
        属性: 编辑用户-普通用户-联系电话
        :return: 编辑用户-普通用户-联系电话
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_mobile_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_email(self):
        """
        属性: 编辑用户-普通用户-邮箱
        :return: 编辑用户-普通用户-邮箱
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_email_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_country_button(self):
        """
        属性: 编辑用户-普通用户-所属国家下拉框
        :return: 编辑用户-普通用户-所属国家下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_country_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_country_first_button(self):
        """
        属性: 编辑用户-普通用户-所在国家-第一个国家
        :return: 编辑用户-普通用户-所在国家-第一个国家
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_country_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_country_china_button(self):
        """
        属性: 编辑用户-普通用户-所在国家-中国
        :return: 编辑用户-普通用户-所在国家-中国
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_country_china_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_country_input(self):
        """
        属性: 编辑用户-普通用户-所在国家输入框
        :return: 编辑用户-普通用户-所在国家输入框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_country_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_sex_button(self):
        """
        属性: 编辑用户-普通用户-性别
        :return: 编辑用户-普通用户-性别
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_sex_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_sex_all_button(self):
        """
        属性: 编辑用户-普通用户-性别-全部
        :return: 编辑用户-普通用户-性别-全部
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_sex_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_sex_male_button(self):
        """
        属性: 编辑用户-普通用户-性别-男
        :return: 编辑用户-普通用户-性别-男
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_sex_male_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_sex_female_button(self):
        """
        属性: 编辑用户-普通用户-性别-女
        :return: 编辑用户-普通用户-性别-女
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_sex_female_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_born_province_button(self):
        """
        属性: 编辑用户-普通用户-出生地-省份下拉框
        :return: 编辑用户-普通用户-出生地-省份下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_born_province_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_born_province_first_button(self):
        """
        属性: 编辑用户-普通用户-出生地-省份-第一个省份
        :return: 编辑用户-普通用户-出生地-省份-第一个省份
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_born_province_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_born_province_input(self):
        """
        属性: 编辑用户-普通用户-出生地-省份输入框
        :return: 编辑用户-普通用户-出生地-省份输入框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_born_province_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_born_city_button(self):
        """
        属性: 编辑用户-普通用户-出生地-城市下拉框
        :return: 编辑用户-普通用户-出生地-城市下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_born_city_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_born_city_first_button(self):
        """
        属性: 编辑用户-普通用户-出生地-城市-第一个城市
        :return: 编辑用户-普通用户-出生地-城市-第一个城市
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_born_city_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_born_city_input(self):
        """
        属性: 编辑用户-普通用户-出生地-城市输入框
        :return: 编辑用户-普通用户-出生地-城市输入框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_born_city_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_born_district_button(self):
        """
        属性: 编辑用户-普通用户-出生地-县区下拉框
        :return: 编辑用户-普通用户-出生地-县区下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_born_district_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_born_district_first_button(self):
        """
        属性: 编辑用户-普通用户-出生地-县区-第一个县区
        :return: 编辑用户-普通用户-出生地-县区-第一个县区
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_born_district_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_born_district_input(self):
        """
        属性: 编辑用户-普通用户-出生地-县区输入框
        :return: 编辑用户-普通用户-出生地-县区输入框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_born_district_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_born_input(self):
        """
        属性: 编辑用户-普通用户-出生地输入框
        :return: 编辑用户-普通用户-出生地输入框
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_born_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_state(self):
        """
        属性: 编辑用户-普通用户-禁用状态
        :return: 编辑用户-普通用户-禁用状态
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_state_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_register_method(self):
        """
        属性: 编辑用户-普通用户-注册渠道
        :return: 编辑用户-普通用户-注册渠道
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_register_method_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_real_name(self):
        """
        属性: 编辑用户-普通用户-用户姓名
        :return: 编辑用户-普通用户-用户姓名
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_real_name_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_id_type(self):
        """
        属性: 编辑用户-普通用户-证件类型
        :return: 编辑用户-普通用户-证件类型
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_id_type_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_id_card_number(self):
        """
        属性: 编辑用户-普通用户-证件号码
        :return: 编辑用户-普通用户-证件号码
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_id_card_number_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_channel(self):
        """
        属性: 编辑用户-普通用户-频道
        :return: 编辑用户-普通用户-频道
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_channel_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_authentication_state_pass(self):
        """
        属性: 编辑用户-普通用户-认证状态已认证
        :return: 编辑用户-普通用户-认证状态已认证
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_authentication_state_pass_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_authentication_state_unpass(self):
        """
        属性: 编辑用户-普通用户-认证状态未认证
        :return: 编辑用户-普通用户-认证状态未认证
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_authentication_state_unpass_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_have_homepage_yes_button(self):
        """
        属性: 编辑用户-普通用户-是否有首页-是
        :return: 编辑用户-普通用户-是否有首页-是
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_have_homepage_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_have_homepage_no_button(self):
        """
        属性: 编辑用户-普通用户-是否有首页-否
        :return: 编辑用户-普通用户-是否有首页-否
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_have_homepage_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_avatar_change_avatar_input(self):
        """
        属性: 编辑用户-普通用户-用户头像-更换头像
        :return: 编辑用户-普通用户-用户头像-更换头像
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_avatar_change_avatar_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_commit_button(self):
        """
        属性: 编辑用户-普通用户-提交信息按钮
        :return: 编辑用户-普通用户-提交信息按钮
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_user_close_button(self):
        """
        属性: 编辑用户-普通用户-关闭按钮
        :return: 编辑用户-普通用户-关闭按钮
        """
        element = None
        try:
            element = self.project.get_element(self._edit_user_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_user_id_button(self):
        """
        属性: 第一个-用户ID按钮
        :return: 第一个-用户ID按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_user_id_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_user_id_text(self):
        """
        属性: 第一行-用户ID
        :return: 第一行-用户ID
        """
        element = None
        try:
            element = self.project.get_element(self._first_user_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_user_nick_text(self):
        """
        属性: 第一行-用户昵称
        :return: 第一行-用户昵称
        """
        element = None
        try:
            element = self.project.get_element(self._first_user_nick_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_user_name_text(self):
        """
        属性: 第一行-用户姓名
        :return: 第一行-用户姓名
        """
        element = None
        try:
            element = self.project.get_element(self._first_user_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_user_mobile_text(self):
        """
        属性: 第一行-用户手机
        :return: 第一行-用户手机
        """
        element = None
        try:
            element = self.project.get_element(self._first_user_mobile_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_role_type_text(self):
        """
        属性: 第一行-角色类型
        :return: 第一行-角色类型
        """
        element = None
        try:
            element = self.project.get_element(self._first_role_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_sex_text(self):
        """
        属性: 第一行-性别
        :return: 第一行-性别
        """
        element = None
        try:
            element = self.project.get_element(self._first_sex_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_user_register_time_text(self):
        """
        属性: 第一行-用户注册时间
        :return: 第一行-用户注册时间
        """
        element = None
        try:
            element = self.project.get_element(self._first_user_register_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_last_active_time_text(self):
        """
        属性: 第一行-最近活动时间
        :return: 第一行-最近活动时间
        """
        element = None
        try:
            element = self.project.get_element(self._first_last_active_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_state_text(self):
        """
        属性: 第一行-状态
        :return: 第一行-状态
        """
        element = None
        try:
            element = self.project.get_element(self._first_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_authentication_state_text(self):
        """
        属性: 第一行-认证情况
        :return: 第一行-认证情况
        """
        element = None
        try:
            element = self.project.get_element(self._first_authentication_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_register_channel_text(self):
        """
        属性: 第一行-注册频道
        :return: 第一行-注册频道
        """
        element = None
        try:
            element = self.project.get_element(self._first_register_channel_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_edit_button(self):
        """
        属性: 第一行-编辑按钮
        :return: 第一行-编辑按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_edit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_ban_button(self):
        """
        属性: 第一行禁用/解禁按钮
        :return: 第一行禁用/解禁按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_ban_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def ban_reason_input(self):
        """
        属性: 禁用理由输入框
        :return: 禁用理由输入框
        """
        element = None
        try:
            element = self.project.get_element(self._ban_reason_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def ban_confirm_button(self):
        """
        属性: 禁用确认按钮
        :return: 禁用确认按钮
        """
        element = None
        try:
            element = self.project.get_element(self._ban_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def ban_cancel_button(self):
        """
        属性: 禁用取消按钮
        :return: 禁用取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._ban_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def lift_ban_confirm_button(self):
        """
        属性: 解禁确认按钮
        :return: 解禁确认按钮
        """
        element = None
        try:
            element = self.project.get_element(self._lift_ban_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def lift_ban_cancel_button(self):
        """
        属性: 解禁取消按钮
        :return: 解禁取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._lift_ban_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def get_message_content_text_action(self):
        """
        动作：获取消息提示框按钮的文本
        :return: '消息提示框按钮'的文本
        """
        control_content = self.project.get_element_text(self.message_content_text)
        return control_content

    def set_user_nick_input_action(self, user_nick_input):
        """
        动作：设置用户昵称输入框
        :param user_nick_input: 用户昵称输入框
        :return: 设置'用户昵称输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.user_nick_input, user_nick_input)
        return self.project.get_current_page_source()

    def click_register_channel_button_action(self):
        """
        动作：点击注册频道下拉框按钮
        :return: 点击'注册频道下拉框按钮'按钮后的页面
        """
        self.project.click(self.register_channel_button)
        return self.project.get_current_page_source()

    def click_register_channel_all_button_action(self):
        """
        动作：点击注册频道-全部按钮
        :return: 点击'注册频道-全部按钮'按钮后的页面
        """
        self.project.click(self.register_channel_all_button)
        return self.project.get_current_page_source()

    def click_register_channel_home_page_button_action(self):
        """
        动作：点击注册频道-总首页按钮
        :return: 点击'注册频道-总首页按钮'按钮后的页面
        """
        self.project.click(self.register_channel_home_page_button)
        return self.project.get_current_page_source()

    def click_register_channel_study_aboard_button_action(self):
        """
        动作：点击注册频道-出国留学按钮
        :return: 点击'注册频道-出国留学按钮'按钮后的页面
        """
        self.project.click(self.register_channel_study_aboard_button)
        return self.project.get_current_page_source()

    def click_register_channel_language_training_button_action(self):
        """
        动作：点击注册频道-语言培训按钮
        :return: 点击'注册频道-语言培训按钮'按钮后的页面
        """
        self.project.click(self.register_channel_language_training_button)
        return self.project.get_current_page_source()

    def click_register_channel_college_direct_button_action(self):
        """
        动作：点击注册频道-院校直通车按钮
        :return: 点击'注册频道-院校直通车按钮'按钮后的页面
        """
        self.project.click(self.register_channel_college_direct_button)
        return self.project.get_current_page_source()

    def click_sex_button_action(self):
        """
        动作：点击性别下拉框按钮
        :return: 点击'性别下拉框按钮'按钮后的页面
        """
        self.project.click(self.sex_button)
        return self.project.get_current_page_source()

    def click_sex_all_button_action(self):
        """
        动作：点击性别-全部按钮
        :return: 点击'性别-全部按钮'按钮后的页面
        """
        self.project.click(self.sex_all_button)
        return self.project.get_current_page_source()

    def click_sex_male_button_action(self):
        """
        动作：点击性别-男按钮
        :return: 点击'性别-男按钮'按钮后的页面
        """
        self.project.click(self.sex_male_button)
        return self.project.get_current_page_source()

    def click_sex_female_button_action(self):
        """
        动作：点击性别女按钮
        :return: 点击'性别女按钮'按钮后的页面
        """
        self.project.click(self.sex_female_button)
        return self.project.get_current_page_source()

    def set_mobile_input_action(self, mobile_input):
        """
        动作：设置用户手机输入框
        :param mobile_input: 用户手机输入框
        :return: 设置'用户手机输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.mobile_input, mobile_input)
        return self.project.get_current_page_source()

    def click_role_type_button_action(self):
        """
        动作：点击角色类型下拉框按钮
        :return: 点击'角色类型下拉框按钮'按钮后的页面
        """
        self.project.click(self.role_type_button)
        return self.project.get_current_page_source()

    def click_role_type_all_button_action(self):
        """
        动作：点击角色类型-全部按钮
        :return: 点击'角色类型-全部按钮'按钮后的页面
        """
        self.project.click(self.role_type_all_button)
        return self.project.get_current_page_source()

    def click_role_type_user_button_action(self):
        """
        动作：点击角色类型-普通用户按钮
        :return: 点击'角色类型-普通用户按钮'按钮后的页面
        """
        self.project.click(self.role_type_user_button)
        return self.project.get_current_page_source()

    def click_role_type_teacher_button_action(self):
        """
        动作：点击角色类型-讲师按钮
        :return: 点击'角色类型-讲师按钮'按钮后的页面
        """
        self.project.click(self.role_type_teacher_button)
        return self.project.get_current_page_source()

    def click_role_type_adviser_button_action(self):
        """
        动作：点击角色类型-顾问按钮
        :return: 点击'角色类型-顾问按钮'按钮后的页面
        """
        self.project.click(self.role_type_adviser_button)
        return self.project.get_current_page_source()

    def click_role_type_celebrity_button_action(self):
        """
        动作：点击角色类型-大咖按钮
        :return: 点击'角色类型-大咖按钮'按钮后的页面
        """
        self.project.click(self.role_type_celebrity_button)
        return self.project.get_current_page_source()

    def click_authentication_state_button_action(self):
        """
        动作：点击认证情况下拉框按钮
        :return: 点击'认证情况下拉框按钮'按钮后的页面
        """
        self.project.click(self.authentication_state_button)
        return self.project.get_current_page_source()

    def click_authentication_state_all_button_action(self):
        """
        动作：点击认证情况-全部按钮
        :return: 点击'认证情况-全部按钮'按钮后的页面
        """
        self.project.click(self.authentication_state_all_button)
        return self.project.get_current_page_source()

    def click_authentication_state_unpass_button_action(self):
        """
        动作：点击认证情况-未认证按钮
        :return: 点击'认证情况-未认证按钮'按钮后的页面
        """
        self.project.click(self.authentication_state_unpass_button)
        return self.project.get_current_page_source()

    def click_authentication_state_pass_button_action(self):
        """
        动作：点击认证情况-已认证按钮
        :return: 点击'认证情况-已认证按钮'按钮后的页面
        """
        self.project.click(self.authentication_state_pass_button)
        return self.project.get_current_page_source()

    def click_state_button_action(self):
        """
        动作：点击状态下拉框按钮
        :return: 点击'状态下拉框按钮'按钮后的页面
        """
        self.project.click(self.state_button)
        return self.project.get_current_page_source()

    def click_state_all_button_action(self):
        """
        动作：点击状态-全部按钮
        :return: 点击'状态-全部按钮'按钮后的页面
        """
        self.project.click(self.state_all_button)
        return self.project.get_current_page_source()

    def click_state_normal_button_action(self):
        """
        动作：点击状态-正常按钮
        :return: 点击'状态-正常按钮'按钮后的页面
        """
        self.project.click(self.state_normal_button)
        return self.project.get_current_page_source()

    def click_state_disable_button_action(self):
        """
        动作：点击状态-禁用按钮
        :return: 点击'状态-禁用按钮'按钮后的页面
        """
        self.project.click(self.state_disable_button)
        return self.project.get_current_page_source()

    def set_user_id_input_action(self, user_id_input):
        """
        动作：设置用户id输入框
        :param user_id_input: 用户id输入框
        :return: 设置'用户id输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.user_id_input, user_id_input)
        return self.project.get_current_page_source()

    def set_user_name_input_action(self, user_name_input):
        """
        动作：设置用户姓名输入框
        :param user_name_input: 用户姓名输入框
        :return: 设置'用户姓名输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.user_name_input, user_name_input)
        return self.project.get_current_page_source()

    def click_search_button_action(self):
        """
        动作：点击查询按钮
        :return: 点击'查询按钮'按钮后的页面
        """
        self.project.click(self.search_button)
        return self.project.get_current_page_source()

    def click_clear_button_action(self):
        """
        动作：点击清楚按钮
        :return: 点击'清楚按钮'按钮后的页面
        """
        self.project.click(self.clear_button)
        return self.project.get_current_page_source()

    def click_create_user_button_action(self):
        """
        动作：点击创建用户按钮
        :return: 点击'创建用户按钮'按钮后的页面
        """
        self.project.click(self.create_user_button)
        return self.project.get_current_page_source()

    def set_create_user_password_input_action(self, create_user_password_input):
        """
        动作：设置创建用户-登录密码输入框
        :param create_user_password_input: 创建用户-登录密码输入框
        :return: 设置'创建用户-登录密码输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.create_user_password_input, create_user_password_input)
        return self.project.get_current_page_source()

    def get_create_user_password_error_text_action(self):
        """
        动作：获取创建用户-登录密码错误提示的文本
        :return: '创建用户-登录密码错误提示'的文本
        """
        control_content = self.project.get_element_text(self.create_user_password_error_text)
        return control_content

    def set_create_user_nick_input_action(self, create_user_nick_input):
        """
        动作：设置创建用户-用户昵称输入框
        :param create_user_nick_input: 创建用户-用户昵称输入框
        :return: 设置'创建用户-用户昵称输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.create_user_nick_input, create_user_nick_input)
        return self.project.get_current_page_source()

    def get_create_user_nick_error_text_action(self):
        """
        动作：获取创建用户-用于昵称错误提示的文本
        :return: '创建用户-用于昵称错误提示'的文本
        """
        control_content = self.project.get_element_text(self.create_user_nick_error_text)
        return control_content

    def set_create_user_email_input_action(self, create_user_email_input):
        """
        动作：设置创建用户-邮箱输入框
        :param create_user_email_input: 创建用户-邮箱输入框
        :return: 设置'创建用户-邮箱输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.create_user_email_input, create_user_email_input)
        return self.project.get_current_page_source()

    def get_create_user_email_error_text_action(self):
        """
        动作：获取创建用户-邮箱错误提示的文本
        :return: '创建用户-邮箱错误提示'的文本
        """
        control_content = self.project.get_element_text(self.create_user_email_error_text)
        return control_content

    def set_create_user_mobile_input_action(self, create_user_mobile_input):
        """
        动作：设置创建用户-联系电话输入框
        :param create_user_mobile_input: 创建用户-联系电话输入框
        :return: 设置'创建用户-联系电话输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.create_user_mobile_input, create_user_mobile_input)
        return self.project.get_current_page_source()

    def get_create_user_mobile_error_text_action(self):
        """
        动作：获取创建用户-联系电话错误提示的文本
        :return: '创建用户-联系电话错误提示'的文本
        """
        control_content = self.project.get_element_text(self.create_user_mobile_error_text)
        return control_content

    def click_create_user_country_button_action(self):
        """
        动作：点击创建用户-所在国家下拉框
        :return: 点击'创建用户-所在国家下拉框'按钮后的页面
        """
        self.project.click(self.create_user_country_button)
        return self.project.get_current_page_source()

    def click_create_user_country_first_button_action(self):
        """
        动作：点击创建用户-所在国家-第一个国家
        :return: 点击'创建用户-所在国家-第一个国家'按钮后的页面
        """
        self.project.click(self.create_user_country_first_button)
        return self.project.get_current_page_source()

    def click_create_user_country_china_button_action(self):
        """
        动作：点击创建用户-所在国家-中国
        :return: 点击'创建用户-所在国家-中国'按钮后的页面
        """
        self.project.click(self.create_user_country_china_button)
        return self.project.get_current_page_source()

    def get_create_user_born_province_error_text_action(self):
        """
        动作：获取创建用户-出生地-省份错误提示的文本
        :return: '创建用户-出生地-省份错误提示'的文本
        """
        control_content = self.project.get_element_text(self.create_user_born_province_error_text)
        return control_content

    def click_create_user_born_province_button_action(self):
        """
        动作：点击创建用户-出生地-省份下拉框
        :return: 点击'创建用户-出生地-省份下拉框'按钮后的页面
        """
        self.project.click(self.create_user_born_province_button)
        return self.project.get_current_page_source()

    def click_create_user_born_province_first_button_action(self):
        """
        动作：点击创建用户-出生地-省份-第一个省份
        :return: 点击'创建用户-出生地-省份-第一个省份'按钮后的页面
        """
        self.project.click(self.create_user_born_province_first_button)
        return self.project.get_current_page_source()

    def get_create_user_born_city_error_text_action(self):
        """
        动作：获取创建用户-出生地-城市错误提示的文本
        :return: '创建用户-出生地-城市错误提示'的文本
        """
        control_content = self.project.get_element_text(self.create_user_born_city_error_text)
        return control_content

    def click_create_user_born_city_button_action(self):
        """
        动作：点击创建用户-出生地-城市下拉框
        :return: 点击'创建用户-出生地-城市下拉框'按钮后的页面
        """
        self.project.click(self.create_user_born_city_button)
        return self.project.get_current_page_source()

    def click_create_user_born_city_first_button_action(self):
        """
        动作：点击创建用户-出生地-城市-第一个城市
        :return: 点击'创建用户-出生地-城市-第一个城市'按钮后的页面
        """
        self.project.click(self.create_user_born_city_first_button)
        return self.project.get_current_page_source()

    def get_create_user_born_district_error_text_action(self):
        """
        动作：获取创建用户-出生地-县区-错误提示的文本
        :return: '创建用户-出生地-县区-错误提示'的文本
        """
        control_content = self.project.get_element_text(self.create_user_born_district_error_text)
        return control_content

    def click_create_user_born_district_button_action(self):
        """
        动作：点击创建用户-出生地-县区下拉框
        :return: 点击'创建用户-出生地-县区下拉框'按钮后的页面
        """
        self.project.click(self.create_user_born_district_button)
        return self.project.get_current_page_source()

    def click_create_user_born_district_first_button_action(self):
        """
        动作：点击创建用户-出生地-县区-第一个区
        :return: 点击'创建用户-出生地-县区-第一个区'按钮后的页面
        """
        self.project.click(self.create_user_born_district_first_button)
        return self.project.get_current_page_source()

    def set_create_user_born_input_action(self, create_user_born_input):
        """
        动作：设置创建用户-出生地输入框
        :param create_user_born_input: 创建用户-出生地输入框
        :return: 设置'创建用户-出生地输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.create_user_born_input, create_user_born_input)
        return self.project.get_current_page_source()

    def get_create_user_born_error_text_action(self):
        """
        动作：获取创建用户-出生地-错误提示的文本
        :return: '创建用户-出生地-错误提示'的文本
        """
        control_content = self.project.get_element_text(self.create_user_born_error_text)
        return control_content

    def click_create_user_sex_button_action(self):
        """
        动作：点击创建用户-性别下拉框
        :return: 点击'创建用户-性别下拉框'按钮后的页面
        """
        self.project.click(self.create_user_sex_button)
        return self.project.get_current_page_source()

    def click_create_user_sex_male_button_action(self):
        """
        动作：点击创建用户-性别-男
        :return: 点击'创建用户-性别-男'按钮后的页面
        """
        self.project.click(self.create_user_sex_male_button)
        return self.project.get_current_page_source()

    def click_create_user_female_button_action(self):
        """
        动作：点击创建用户-性别-女
        :return: 点击'创建用户-性别-女'按钮后的页面
        """
        self.project.click(self.create_user_female_button)
        return self.project.get_current_page_source()

    def click_create_user_state_button_action(self):
        """
        动作：点击创建用户-禁用状态下拉框
        :return: 点击'创建用户-禁用状态下拉框'按钮后的页面
        """
        self.project.click(self.create_user_state_button)
        return self.project.get_current_page_source()

    def click_create_user_state_normal_button_action(self):
        """
        动作：点击创建用户-禁用状态-正常
        :return: 点击'创建用户-禁用状态-正常'按钮后的页面
        """
        self.project.click(self.create_user_state_normal_button)
        return self.project.get_current_page_source()

    def click_create_user_state_prohibition_button_action(self):
        """
        动作：点击创建用户-禁用状态-禁用
        :return: 点击'创建用户-禁用状态-禁用'按钮后的页面
        """
        self.project.click(self.create_user_state_prohibition_button)
        return self.project.get_current_page_source()

    def set_create_user_avatar_input_action(self, create_user_avatar_input):
        """
        动作：设置创建用户-用户头像
        :param create_user_avatar_input: 创建用户-用户头像
        :return: 设置'创建用户-用户头像'文本后的页面
        """
        self.project.clear_and_send_keys(self.create_user_avatar_input, create_user_avatar_input)
        return self.project.get_current_page_source()

    def get_create_user_avatar_error_text_action(self):
        """
        动作：获取创建用户-用户头像错误提示的文本
        :return: '创建用户-用户头像错误提示'的文本
        """
        control_content = self.project.get_element_text(self.create_user_avatar_error_text)
        return control_content

    def click_create_user_avatar_image_button_action(self):
        """
        动作：点击创建用户-用户头像-上传后图片
        :return: 点击'创建用户-用户头像-上传后图片'按钮后的页面
        """
        self.project.click(self.create_user_avatar_image_button)
        return self.project.get_current_page_source()

    def click_create_user_commit_button_action(self):
        """
        动作：点击创建用户-提交用户信息按钮
        :return: 点击'创建用户-提交用户信息按钮'按钮后的页面
        """
        self.project.click(self.create_user_commit_button)
        return self.project.get_current_page_source()

    def click_create_exhibition_user_button_action(self):
        """
        动作：点击创建展会用户
        :return: 点击'创建展会用户'按钮后的页面
        """
        self.project.click(self.create_exhibition_user_button)
        return self.project.get_current_page_source()

    def set_edit_teacher_password_input_action(self, edit_teacher_password_input):
        """
        动作：设置编辑用户-讲师-登录密码
        :param edit_teacher_password_input: 编辑用户-讲师-登录密码
        :return: 设置'编辑用户-讲师-登录密码'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_teacher_password_input, edit_teacher_password_input)
        return self.project.get_current_page_source()

    def set_edit_teacher_title_input_action(self, edit_teacher_title_input):
        """
        动作：设置编辑用户-讲师-头衔
        :param edit_teacher_title_input: 编辑用户-讲师-头衔
        :return: 设置'编辑用户-讲师-头衔'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_teacher_title_input, edit_teacher_title_input)
        return self.project.get_current_page_source()

    def set_edit_teacher_nick_input_action(self, edit_teacher_nick_input):
        """
        动作：设置编辑用户-讲师-用户昵称
        :param edit_teacher_nick_input: 编辑用户-讲师-用户昵称
        :return: 设置'编辑用户-讲师-用户昵称'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_teacher_nick_input, edit_teacher_nick_input)
        return self.project.get_current_page_source()

    def click_edit_teacher_country_button_action(self):
        """
        动作：点击编辑用户-讲师-所属国家下拉框
        :return: 点击'编辑用户-讲师-所属国家下拉框'按钮后的页面
        """
        self.project.click(self.edit_teacher_country_button)
        return self.project.get_current_page_source()

    def click_edit_teacher_country_first_button_action(self):
        """
        动作：点击编辑用户-讲师-所在国家-第一个国家
        :return: 点击'编辑用户-讲师-所在国家-第一个国家'按钮后的页面
        """
        self.project.click(self.edit_teacher_country_first_button)
        return self.project.get_current_page_source()

    def click_edit_teacher_country_china_button_action(self):
        """
        动作：点击编辑用户-讲师-所在国家-中国
        :return: 点击'编辑用户-讲师-所在国家-中国'按钮后的页面
        """
        self.project.click(self.edit_teacher_country_china_button)
        return self.project.get_current_page_source()

    def set_edit_teacher_country_input_action(self, edit_teacher_country_input):
        """
        动作：设置编辑用户-讲师-所在国家输入框
        :param edit_teacher_country_input: 编辑用户-讲师-所在国家输入框
        :return: 设置'编辑用户-讲师-所在国家输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_teacher_country_input, edit_teacher_country_input)
        return self.project.get_current_page_source()

    def click_edit_teacher_sex_button_action(self):
        """
        动作：点击编辑用户-讲师-性别
        :return: 点击'编辑用户-讲师-性别'按钮后的页面
        """
        self.project.click(self.edit_teacher_sex_button)
        return self.project.get_current_page_source()

    def click_edit_teacher_sex_all_button_action(self):
        """
        动作：点击编辑用户-讲师-性别-全部
        :return: 点击'编辑用户-讲师-性别-全部'按钮后的页面
        """
        self.project.click(self.edit_teacher_sex_all_button)
        return self.project.get_current_page_source()

    def click_edit_teacher_sex_male_button_action(self):
        """
        动作：点击编辑用户-讲师-性别-男
        :return: 点击'编辑用户-讲师-性别-男'按钮后的页面
        """
        self.project.click(self.edit_teacher_sex_male_button)
        return self.project.get_current_page_source()

    def click_edit_teacher_sex_female_button_action(self):
        """
        动作：点击编辑用户-讲师-性别-女
        :return: 点击'编辑用户-讲师-性别-女'按钮后的页面
        """
        self.project.click(self.edit_teacher_sex_female_button)
        return self.project.get_current_page_source()

    def click_edit_teacher_born_province_button_action(self):
        """
        动作：点击编辑用户-讲师-出生地-省份下拉框
        :return: 点击'编辑用户-讲师-出生地-省份下拉框'按钮后的页面
        """
        self.project.click(self.edit_teacher_born_province_button)
        return self.project.get_current_page_source()

    def click_edit_teacher_born_province_first_button_action(self):
        """
        动作：点击编辑用户-讲师-出生地-省份-第一个省份
        :return: 点击'编辑用户-讲师-出生地-省份-第一个省份'按钮后的页面
        """
        self.project.click(self.edit_teacher_born_province_first_button)
        return self.project.get_current_page_source()

    def set_edit_teacher_born_province_input_action(self, edit_teacher_born_province_input):
        """
        动作：设置编辑用户-讲师-出生地-省份输入框
        :param edit_teacher_born_province_input: 编辑用户-讲师-出生地-省份输入框
        :return: 设置'编辑用户-讲师-出生地-省份输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_teacher_born_province_input, edit_teacher_born_province_input)
        return self.project.get_current_page_source()

    def click_edit_teacher_born_city_button_action(self):
        """
        动作：点击编辑用户-讲师-出生地-城市下拉框
        :return: 点击'编辑用户-讲师-出生地-城市下拉框'按钮后的页面
        """
        self.project.click(self.edit_teacher_born_city_button)
        return self.project.get_current_page_source()

    def click_edit_teacher_born_city_first_button_action(self):
        """
        动作：点击编辑用户-讲师-出生地-城市-第一个城市
        :return: 点击'编辑用户-讲师-出生地-城市-第一个城市'按钮后的页面
        """
        self.project.click(self.edit_teacher_born_city_first_button)
        return self.project.get_current_page_source()

    def set_edit_teacher_born_city_input_action(self, edit_teacher_born_city_input):
        """
        动作：设置编辑用户-讲师-出生地-城市输入框
        :param edit_teacher_born_city_input: 编辑用户-讲师-出生地-城市输入框
        :return: 设置'编辑用户-讲师-出生地-城市输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_teacher_born_city_input, edit_teacher_born_city_input)
        return self.project.get_current_page_source()

    def click_edit_teacher_born_district_button_action(self):
        """
        动作：点击编辑用户-讲师-出生地-县区下拉框
        :return: 点击'编辑用户-讲师-出生地-县区下拉框'按钮后的页面
        """
        self.project.click(self.edit_teacher_born_district_button)
        return self.project.get_current_page_source()

    def click_edit_teacher_born_district_first_button_action(self):
        """
        动作：点击编辑用户-讲师-出生地-县区-第一个县区
        :return: 点击'编辑用户-讲师-出生地-县区-第一个县区'按钮后的页面
        """
        self.project.click(self.edit_teacher_born_district_first_button)
        return self.project.get_current_page_source()

    def set_edit_teacher_born_district_input_action(self, edit_teacher_born_district_input):
        """
        动作：设置编辑用户-讲师-出生地-县区
        :param edit_teacher_born_district_input: 编辑用户-讲师-出生地-县区
        :return: 设置'编辑用户-讲师-出生地-县区'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_teacher_born_district_input, edit_teacher_born_district_input)
        return self.project.get_current_page_source()

    def set_edit_teacher_born_input_action(self, edit_teacher_born_input):
        """
        动作：设置编辑用户-讲师-出生地输入框
        :param edit_teacher_born_input: 编辑用户-讲师-出生地输入框
        :return: 设置'编辑用户-讲师-出生地输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_teacher_born_input, edit_teacher_born_input)
        return self.project.get_current_page_source()

    def click_edit_teacher_have_homepage_yes_button_action(self):
        """
        动作：点击编辑用户-讲师-是否有首页-是
        :return: 点击'编辑用户-讲师-是否有首页-是'按钮后的页面
        """
        self.project.click(self.edit_teacher_have_homepage_yes_button)
        return self.project.get_current_page_source()

    def click_edit_teacher_have_homepage_no_button_action(self):
        """
        动作：点击编辑用户-讲师-是否有首页-否
        :return: 点击'编辑用户-讲师-是否有首页-否'按钮后的页面
        """
        self.project.click(self.edit_teacher_have_homepage_no_button)
        return self.project.get_current_page_source()

    def set_edit_teacher_avatar_change_avatar_input_action(self, edit_teacher_avatar_change_avatar_input):
        """
        动作：设置编辑用户-讲师-用户头像-更换头像
        :param edit_teacher_avatar_change_avatar_input: 编辑用户-讲师-用户头像-更换头像
        :return: 设置'编辑用户-讲师-用户头像-更换头像'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_teacher_avatar_change_avatar_input, edit_teacher_avatar_change_avatar_input)
        return self.project.get_current_page_source()

    def click_edit_teacher_commit_button_action(self):
        """
        动作：点击编辑用户-讲师-提交信息按钮
        :return: 点击'编辑用户-讲师-提交信息按钮'按钮后的页面
        """
        self.project.click(self.edit_teacher_commit_button)
        return self.project.get_current_page_source()

    def click_edit_teacher_close_button_action(self):
        """
        动作：点击编辑用户-讲师-关闭按钮
        :return: 点击'编辑用户-讲师-关闭按钮'按钮后的页面
        """
        self.project.click(self.edit_teacher_close_button)
        return self.project.get_current_page_source()

    def set_edit_user_password_input_action(self, edit_user_password_input):
        """
        动作：设置编辑用户-普通用户-登录密码
        :param edit_user_password_input: 编辑用户-普通用户-登录密码
        :return: 设置'编辑用户-普通用户-登录密码'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_user_password_input, edit_user_password_input)
        return self.project.get_current_page_source()

    def set_edit_user_title_input_action(self, edit_user_title_input):
        """
        动作：设置编辑用户-普通用户-头衔
        :param edit_user_title_input: 编辑用户-普通用户-头衔
        :return: 设置'编辑用户-普通用户-头衔'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_user_title_input, edit_user_title_input)
        return self.project.get_current_page_source()

    def set_edit_user_nick_input_action(self, edit_user_nick_input):
        """
        动作：设置编辑用户-普通用户-用户昵称
        :param edit_user_nick_input: 编辑用户-普通用户-用户昵称
        :return: 设置'编辑用户-普通用户-用户昵称'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_user_nick_input, edit_user_nick_input)
        return self.project.get_current_page_source()

    def click_edit_user_country_button_action(self):
        """
        动作：点击编辑用户-普通用户-所属国家下拉框
        :return: 点击'编辑用户-普通用户-所属国家下拉框'按钮后的页面
        """
        self.project.click(self.edit_user_country_button)
        return self.project.get_current_page_source()

    def click_edit_user_country_first_button_action(self):
        """
        动作：点击编辑用户-普通用户-所在国家-第一个国家
        :return: 点击'编辑用户-普通用户-所在国家-第一个国家'按钮后的页面
        """
        self.project.click(self.edit_user_country_first_button)
        return self.project.get_current_page_source()

    def click_edit_user_country_china_button_action(self):
        """
        动作：点击编辑用户-普通用户-所在国家-中国
        :return: 点击'编辑用户-普通用户-所在国家-中国'按钮后的页面
        """
        self.project.click(self.edit_user_country_china_button)
        return self.project.get_current_page_source()

    def set_edit_user_country_input_action(self, edit_user_country_input):
        """
        动作：设置编辑用户-普通用户-所在国家输入框
        :param edit_user_country_input: 编辑用户-普通用户-所在国家输入框
        :return: 设置'编辑用户-普通用户-所在国家输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_user_country_input, edit_user_country_input)
        return self.project.get_current_page_source()

    def click_edit_user_sex_button_action(self):
        """
        动作：点击编辑用户-普通用户-性别
        :return: 点击'编辑用户-普通用户-性别'按钮后的页面
        """
        self.project.click(self.edit_user_sex_button)
        return self.project.get_current_page_source()

    def click_edit_user_sex_all_button_action(self):
        """
        动作：点击编辑用户-普通用户-性别-全部
        :return: 点击'编辑用户-普通用户-性别-全部'按钮后的页面
        """
        self.project.click(self.edit_user_sex_all_button)
        return self.project.get_current_page_source()

    def click_edit_user_sex_male_button_action(self):
        """
        动作：点击编辑用户-普通用户-性别-男
        :return: 点击'编辑用户-普通用户-性别-男'按钮后的页面
        """
        self.project.click(self.edit_user_sex_male_button)
        return self.project.get_current_page_source()

    def click_edit_user_sex_female_button_action(self):
        """
        动作：点击编辑用户-普通用户-性别-女
        :return: 点击'编辑用户-普通用户-性别-女'按钮后的页面
        """
        self.project.click(self.edit_user_sex_female_button)
        return self.project.get_current_page_source()

    def click_edit_user_born_province_button_action(self):
        """
        动作：点击编辑用户-普通用户-出生地-省份下拉框
        :return: 点击'编辑用户-普通用户-出生地-省份下拉框'按钮后的页面
        """
        self.project.click(self.edit_user_born_province_button)
        return self.project.get_current_page_source()

    def click_edit_user_born_province_first_button_action(self):
        """
        动作：点击编辑用户-普通用户-出生地-省份-第一个省份
        :return: 点击'编辑用户-普通用户-出生地-省份-第一个省份'按钮后的页面
        """
        self.project.click(self.edit_user_born_province_first_button)
        return self.project.get_current_page_source()

    def set_edit_user_born_province_input_action(self, edit_user_born_province_input):
        """
        动作：设置编辑用户-普通用户-出生地-省份输入框
        :param edit_user_born_province_input: 编辑用户-普通用户-出生地-省份输入框
        :return: 设置'编辑用户-普通用户-出生地-省份输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_user_born_province_input, edit_user_born_province_input)
        return self.project.get_current_page_source()

    def click_edit_user_born_city_button_action(self):
        """
        动作：点击编辑用户-普通用户-出生地-城市下拉框
        :return: 点击'编辑用户-普通用户-出生地-城市下拉框'按钮后的页面
        """
        self.project.click(self.edit_user_born_city_button)
        return self.project.get_current_page_source()

    def click_edit_user_born_city_first_button_action(self):
        """
        动作：点击编辑用户-普通用户-出生地-城市-第一个城市
        :return: 点击'编辑用户-普通用户-出生地-城市-第一个城市'按钮后的页面
        """
        self.project.click(self.edit_user_born_city_first_button)
        return self.project.get_current_page_source()

    def set_edit_user_born_city_input_action(self, edit_user_born_city_input):
        """
        动作：设置编辑用户-普通用户-出生地-城市输入框
        :param edit_user_born_city_input: 编辑用户-普通用户-出生地-城市输入框
        :return: 设置'编辑用户-普通用户-出生地-城市输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_user_born_city_input, edit_user_born_city_input)
        return self.project.get_current_page_source()

    def click_edit_user_born_district_button_action(self):
        """
        动作：点击编辑用户-普通用户-出生地-县区下拉框
        :return: 点击'编辑用户-普通用户-出生地-县区下拉框'按钮后的页面
        """
        self.project.click(self.edit_user_born_district_button)
        return self.project.get_current_page_source()

    def click_edit_user_born_district_first_button_action(self):
        """
        动作：点击编辑用户-普通用户-出生地-县区-第一个县区
        :return: 点击'编辑用户-普通用户-出生地-县区-第一个县区'按钮后的页面
        """
        self.project.click(self.edit_user_born_district_first_button)
        return self.project.get_current_page_source()

    def set_edit_user_born_district_input_action(self, edit_user_born_district_input):
        """
        动作：设置编辑用户-普通用户-出生地-县区输入框
        :param edit_user_born_district_input: 编辑用户-普通用户-出生地-县区输入框
        :return: 设置'编辑用户-普通用户-出生地-县区输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_user_born_district_input, edit_user_born_district_input)
        return self.project.get_current_page_source()

    def set_edit_user_born_input_action(self, edit_user_born_input):
        """
        动作：设置编辑用户-普通用户-出生地输入框
        :param edit_user_born_input: 编辑用户-普通用户-出生地输入框
        :return: 设置'编辑用户-普通用户-出生地输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_user_born_input, edit_user_born_input)
        return self.project.get_current_page_source()

    def click_edit_user_have_homepage_yes_button_action(self):
        """
        动作：点击编辑用户-普通用户-是否有首页-是
        :return: 点击'编辑用户-普通用户-是否有首页-是'按钮后的页面
        """
        self.project.click(self.edit_user_have_homepage_yes_button)
        return self.project.get_current_page_source()

    def click_edit_user_have_homepage_no_button_action(self):
        """
        动作：点击编辑用户-普通用户-是否有首页-否
        :return: 点击'编辑用户-普通用户-是否有首页-否'按钮后的页面
        """
        self.project.click(self.edit_user_have_homepage_no_button)
        return self.project.get_current_page_source()

    def set_edit_user_avatar_change_avatar_input_action(self, edit_user_avatar_change_avatar_input):
        """
        动作：设置编辑用户-普通用户-用户头像-更换头像
        :param edit_user_avatar_change_avatar_input: 编辑用户-普通用户-用户头像-更换头像
        :return: 设置'编辑用户-普通用户-用户头像-更换头像'文本后的页面
        """
        self.project.clear_and_send_keys(self.edit_user_avatar_change_avatar_input, edit_user_avatar_change_avatar_input)
        return self.project.get_current_page_source()

    def click_edit_user_commit_button_action(self):
        """
        动作：点击编辑用户-普通用户-提交信息按钮
        :return: 点击'编辑用户-普通用户-提交信息按钮'按钮后的页面
        """
        self.project.click(self.edit_user_commit_button)
        return self.project.get_current_page_source()

    def click_edit_user_close_button_action(self):
        """
        动作：点击编辑用户-普通用户-关闭按钮
        :return: 点击'编辑用户-普通用户-关闭按钮'按钮后的页面
        """
        self.project.click(self.edit_user_close_button)
        return self.project.get_current_page_source()

    def click_first_user_id_button_action(self):
        """
        动作：点击第一个-用户ID按钮
        :return: 点击'第一个-用户ID按钮'按钮后的页面
        """
        self.project.click(self.first_user_id_button)
        return self.project.get_current_page_source()

    def get_first_user_id_text_action(self):
        """
        动作：获取第一行-用户ID的文本
        :return: '第一行-用户ID'的文本
        """
        control_content = self.project.get_element_text(self.first_user_id_text)
        return control_content

    def get_first_user_nick_text_action(self):
        """
        动作：获取第一行-用户昵称的文本
        :return: '第一行-用户昵称'的文本
        """
        control_content = self.project.get_element_text(self.first_user_nick_text)
        return control_content

    def get_first_user_name_text_action(self):
        """
        动作：获取第一行-用户姓名的文本
        :return: '第一行-用户姓名'的文本
        """
        control_content = self.project.get_element_text(self.first_user_name_text)
        return control_content

    def get_first_user_mobile_text_action(self):
        """
        动作：获取第一行-用户手机的文本
        :return: '第一行-用户手机'的文本
        """
        control_content = self.project.get_element_text(self.first_user_mobile_text)
        return control_content

    def get_first_role_type_text_action(self):
        """
        动作：获取第一行-角色类型的文本
        :return: '第一行-角色类型'的文本
        """
        control_content = self.project.get_element_text(self.first_role_type_text)
        return control_content

    def get_first_sex_text_action(self):
        """
        动作：获取第一行-性别的文本
        :return: '第一行-性别'的文本
        """
        control_content = self.project.get_element_text(self.first_sex_text)
        return control_content

    def get_first_user_register_time_text_action(self):
        """
        动作：获取第一行-用户注册时间的文本
        :return: '第一行-用户注册时间'的文本
        """
        control_content = self.project.get_element_text(self.first_user_register_time_text)
        return control_content

    def get_first_last_active_time_text_action(self):
        """
        动作：获取第一行-最近活动时间的文本
        :return: '第一行-最近活动时间'的文本
        """
        control_content = self.project.get_element_text(self.first_last_active_time_text)
        return control_content

    def get_first_state_text_action(self):
        """
        动作：获取第一行-状态的文本
        :return: '第一行-状态'的文本
        """
        control_content = self.project.get_element_text(self.first_state_text)
        return control_content

    def get_first_authentication_state_text_action(self):
        """
        动作：获取第一行-认证情况的文本
        :return: '第一行-认证情况'的文本
        """
        control_content = self.project.get_element_text(self.first_authentication_state_text)
        return control_content

    def get_first_register_channel_text_action(self):
        """
        动作：获取第一行-注册频道的文本
        :return: '第一行-注册频道'的文本
        """
        control_content = self.project.get_element_text(self.first_register_channel_text)
        return control_content

    def click_first_edit_button_action(self):
        """
        动作：点击第一行-编辑按钮
        :return: 点击'第一行-编辑按钮'按钮后的页面
        """
        self.project.click(self.first_edit_button)
        return self.project.get_current_page_source()

    def click_first_ban_button_action(self):
        """
        动作：点击第一行禁用/解禁按钮
        :return: 点击'第一行禁用/解禁按钮'按钮后的页面
        """
        self.project.click(self.first_ban_button)
        return self.project.get_current_page_source()

    def set_ban_reason_input_action(self, ban_reason_input):
        """
        动作：设置禁用理由输入框
        :param ban_reason_input: 禁用理由输入框
        :return: 设置'禁用理由输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.ban_reason_input, ban_reason_input)
        return self.project.get_current_page_source()

    def click_ban_confirm_button_action(self):
        """
        动作：点击禁用确认按钮
        :return: 点击'禁用确认按钮'按钮后的页面
        """
        self.project.click(self.ban_confirm_button)
        return self.project.get_current_page_source()

    def click_ban_cancel_button_action(self):
        """
        动作：点击禁用取消按钮
        :return: 点击'禁用取消按钮'按钮后的页面
        """
        self.project.click(self.ban_cancel_button)
        return self.project.get_current_page_source()

    def click_lift_ban_confirm_button_action(self):
        """
        动作：点击解禁确认按钮
        :return: 点击'解禁确认按钮'按钮后的页面
        """
        self.project.click(self.lift_ban_confirm_button)
        return self.project.get_current_page_source()

    def click_lift_ban_cancel_button_action(self):
        """
        动作：点击解禁取消按钮
        :return: 点击'解禁取消按钮'按钮后的页面
        """
        self.project.click(self.lift_ban_cancel_button)
        return self.project.get_current_page_source()

    # endregion Actions
