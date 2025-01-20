from Utils.Log import log

"""
后台首页-用户中心-用户管理-平台讲师认证
console_url/person/person-authentication
"""


class ConsoleUserCenterPersonAuthenticationPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/person/person-authentication'
        # region Fields
        # 消息通知
        self._message_content_text_tag = '/html/body/div[last()]/div/div/p'
        # 用户姓名输入框
        self._person_authentication_real_name_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 用户手机输入框
        self._person_authentication_mobile_input_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 用户ID输入框
        self._person_authentication_id_input_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div/input'
        # 用户角色下拉框
        self._person_authentication_role_uuid_button_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div/div'
        # 用户角色-全部
        self._person_authentication_role_uuid_all_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[1]t'
        # 用户角色-普通用户
        self._person_authentication_role_uuid_user_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[2]'
        # 用户角色-讲师
        self._person_authentication_role_uuid_teacher_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[3]'
        # 用户角色-顾问
        self._person_authentication_role_uuid_adviser_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[4]'
        # 用户角色-大咖
        self._person_authentication_role_uuid_celebrity_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[5]'
        # 用户昵称输入框
        self._person_authentication_person_nickname_input_tag = '//*[@id="tableSearch"]/form/div/div[5]/div/div/input'
        # 审核状态下拉框
        self._person_authentication_examine_state_button_tag = '//*[@id="tableSearch"]/form/div/div[6]/div/div/div'
        # 审核状态-全部
        self._person_authentication_examine_state_all_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[1]'
        # 审核状态-审核不通过
        self._person_authentication_examine_state_unpass_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[2]'
        # 审核状态-待审核
        self._person_authentication_examine_state_pending_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[3]'
        # 审核状态-撤销认证
        self._person_authentication_examine_state_revoke_certification_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[4]'
        # 审核状态-审核通过
        self._person_authentication_examine_state_pass_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[5]'
        # 查询按钮
        self._person_authentication_search_button_tag = '//*[@id="tableSearch"]/form/div/div[7]/div/button'
        # 清楚按钮
        self._person_authentication_clear_button_tag = '//*[@id="tableSearch"]/form/div/div[8]/div/button'
        # 第一行数据按钮（审核/撤销）
        self._person_authentication_first_line_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/a'
        # 审核-不通过原因输入框
        self._person_authentication_unpass_reason_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[9]/div/div/div/div/textarea'
        # 审核-通过按钮
        self._person_authentication_examine_pass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[3]/span/div/div/button[1]'
        # 审核-不通过按钮
        self._person_authentication_examine_unpass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[3]/span/div/div/button[2]'
        # 审核-取消按钮
        self._person_authentication_examine_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[3]/span/div/div/button[3]'
        # 撤销-撤销原因输入框
        self._person_authentication_revoke_reason_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div/div[2]/form/div/div/div/div/div/textarea'
        # 撤销-确定按钮
        self._person_authentication_revoke_confirm_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div/div[3]/span/button[1]'
        # 撤销-取消按钮
        self._person_authentication_revoke_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div/div[3]/span/button[2]'
        # 撤销-关闭按钮
        self._person_authentication_revoke_close_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div/div[1]/button'
        # 批量撤销按钮
        self._person_authentication_batch_revoke_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[2]/div[1]/button'
        # 第一行审核状态按钮
        self._person_authentication_first_line_examine_state_text_tag = '/html/body/div/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[9]/div'
        # endregion Fields

    # region Properties
    @property
    def message_content_text(self):
        """
        属性: 消息通知
        :return: 消息通知
        """
        element = None
        try:
            element = self.project.get_element(self._message_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_real_name_input(self):
        """
        属性: 用户姓名输入框
        :return: 用户姓名输入框
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_real_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_mobile_input(self):
        """
        属性: 用户手机输入框
        :return: 用户手机输入框
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_mobile_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_id_input(self):
        """
        属性: 用户ID输入框
        :return: 用户ID输入框
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_role_uuid_button(self):
        """
        属性: 用户角色下拉框
        :return: 用户角色下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_role_uuid_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_role_uuid_all_button(self):
        """
        属性: 用户角色-全部
        :return: 用户角色-全部
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_role_uuid_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_role_uuid_user_button(self):
        """
        属性: 用户角色-普通用户
        :return: 用户角色-普通用户
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_role_uuid_user_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_role_uuid_teacher_button(self):
        """
        属性: 用户角色-讲师
        :return: 用户角色-讲师
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_role_uuid_teacher_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_role_uuid_adviser_button(self):
        """
        属性: 用户角色-顾问
        :return: 用户角色-顾问
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_role_uuid_adviser_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_role_uuid_celebrity_button(self):
        """
        属性: 用户角色-大咖
        :return: 用户角色-大咖
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_role_uuid_celebrity_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_person_nickname_input(self):
        """
        属性: 用户昵称输入框
        :return: 用户昵称输入框
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_person_nickname_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_examine_state_button(self):
        """
        属性: 审核状态下拉框
        :return: 审核状态下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_examine_state_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_examine_state_all_button(self):
        """
        属性: 审核状态-全部
        :return: 审核状态-全部
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_examine_state_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_examine_state_unpass_button(self):
        """
        属性: 审核状态-审核不通过
        :return: 审核状态-审核不通过
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_examine_state_unpass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_examine_state_pending_button(self):
        """
        属性: 审核状态-待审核
        :return: 审核状态-待审核
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_examine_state_pending_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_examine_state_revoke_certification_button(self):
        """
        属性: 审核状态-撤销认证
        :return: 审核状态-撤销认证
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_examine_state_revoke_certification_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_examine_state_pass_button(self):
        """
        属性: 审核状态-审核通过
        :return: 审核状态-审核通过
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_examine_state_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_search_button(self):
        """
        属性: 查询按钮
        :return: 查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_search_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_clear_button(self):
        """
        属性: 清楚按钮
        :return: 清楚按钮
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_first_line_button(self):
        """
        属性: 第一行数据按钮（审核/撤销）
        :return: 第一行数据按钮（审核/撤销）
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_first_line_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_unpass_reason_input(self):
        """
        属性: 审核-不通过原因输入框
        :return: 审核-不通过原因输入框
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_unpass_reason_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_examine_pass_button(self):
        """
        属性: 审核-通过按钮
        :return: 审核-通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_examine_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_examine_unpass_button(self):
        """
        属性: 审核-不通过按钮
        :return: 审核-不通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_examine_unpass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_examine_cancel_button(self):
        """
        属性: 审核-取消按钮
        :return: 审核-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_examine_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_revoke_reason_input(self):
        """
        属性: 撤销-撤销原因输入框
        :return: 撤销-撤销原因输入框
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_revoke_reason_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_revoke_confirm_button(self):
        """
        属性: 撤销-确定按钮
        :return: 撤销-确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_revoke_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_revoke_cancel_button(self):
        """
        属性: 撤销-取消按钮
        :return: 撤销-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_revoke_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_revoke_close_button(self):
        """
        属性: 撤销-关闭按钮
        :return: 撤销-关闭按钮
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_revoke_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_batch_revoke_button(self):
        """
        属性: 批量撤销按钮
        :return: 批量撤销按钮
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_batch_revoke_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_first_line_examine_state_text(self):
        """
        属性: 第一行审核状态按钮
        :return: 第一行审核状态按钮
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_first_line_examine_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def get_message_content_text_action(self):
        """
        动作：获取消息通知的文本
        :return: '消息通知'的文本
        """
        control_content = self.project.get_element_text(self.message_content_text)
        return control_content

    def set_person_authentication_real_name_input_action(self, person_authentication_real_name_input):
        """
        动作：设置用户姓名输入框
        :param person_authentication_real_name_input: 用户姓名输入框
        :return: 设置'用户姓名输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.person_authentication_real_name_input, person_authentication_real_name_input)
        return self.project.get_current_page_source()

    def set_person_authentication_mobile_input_action(self, person_authentication_mobile_input):
        """
        动作：设置用户手机输入框
        :param person_authentication_mobile_input: 用户手机输入框
        :return: 设置'用户手机输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.person_authentication_mobile_input, person_authentication_mobile_input)
        return self.project.get_current_page_source()

    def set_person_authentication_id_input_action(self, person_authentication_id_input):
        """
        动作：设置用户ID输入框
        :param person_authentication_id_input: 用户ID输入框
        :return: 设置'用户ID输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.person_authentication_id_input, person_authentication_id_input)
        return self.project.get_current_page_source()

    def click_person_authentication_role_uuid_button_action(self):
        """
        动作：点击用户角色下拉框
        :return: 点击'用户角色下拉框'按钮后的页面
        """
        self.project.click(self.person_authentication_role_uuid_button)
        return self.project.get_current_page_source()

    def click_person_authentication_role_uuid_all_button_action(self):
        """
        动作：点击用户角色-全部
        :return: 点击'用户角色-全部'按钮后的页面
        """
        self.project.click(self.person_authentication_role_uuid_all_button)
        return self.project.get_current_page_source()

    def click_person_authentication_role_uuid_user_button_action(self):
        """
        动作：点击用户角色-普通用户
        :return: 点击'用户角色-普通用户'按钮后的页面
        """
        self.project.click(self.person_authentication_role_uuid_user_button)
        return self.project.get_current_page_source()

    def click_person_authentication_role_uuid_teacher_button_action(self):
        """
        动作：点击用户角色-讲师
        :return: 点击'用户角色-讲师'按钮后的页面
        """
        self.project.click(self.person_authentication_role_uuid_teacher_button)
        return self.project.get_current_page_source()

    def click_person_authentication_role_uuid_adviser_button_action(self):
        """
        动作：点击用户角色-顾问
        :return: 点击'用户角色-顾问'按钮后的页面
        """
        self.project.click(self.person_authentication_role_uuid_adviser_button)
        return self.project.get_current_page_source()

    def click_person_authentication_role_uuid_celebrity_button_action(self):
        """
        动作：点击用户角色-大咖
        :return: 点击'用户角色-大咖'按钮后的页面
        """
        self.project.click(self.person_authentication_role_uuid_celebrity_button)
        return self.project.get_current_page_source()

    def set_person_authentication_person_nickname_input_action(self, person_authentication_person_nickname_input):
        """
        动作：设置用户昵称输入框
        :param person_authentication_person_nickname_input: 用户昵称输入框
        :return: 设置'用户昵称输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.person_authentication_person_nickname_input, person_authentication_person_nickname_input)
        return self.project.get_current_page_source()

    def click_person_authentication_examine_state_button_action(self):
        """
        动作：点击审核状态下拉框
        :return: 点击'审核状态下拉框'按钮后的页面
        """
        self.project.click(self.person_authentication_examine_state_button)
        return self.project.get_current_page_source()

    def click_person_authentication_examine_state_all_button_action(self):
        """
        动作：点击审核状态-全部
        :return: 点击'审核状态-全部'按钮后的页面
        """
        self.project.click(self.person_authentication_examine_state_all_button)
        return self.project.get_current_page_source()

    def click_person_authentication_examine_state_unpass_button_action(self):
        """
        动作：点击审核状态-审核不通过
        :return: 点击'审核状态-审核不通过'按钮后的页面
        """
        self.project.click(self.person_authentication_examine_state_unpass_button)
        return self.project.get_current_page_source()

    def click_person_authentication_examine_state_pending_button_action(self):
        """
        动作：点击审核状态-待审核
        :return: 点击'审核状态-待审核'按钮后的页面
        """
        self.project.click(self.person_authentication_examine_state_pending_button)
        return self.project.get_current_page_source()

    def click_person_authentication_examine_state_revoke_certification_button_action(self):
        """
        动作：点击审核状态-撤销认证
        :return: 点击'审核状态-撤销认证'按钮后的页面
        """
        self.project.click(self.person_authentication_examine_state_revoke_certification_button)
        return self.project.get_current_page_source()

    def click_person_authentication_examine_state_pass_button_action(self):
        """
        动作：点击审核状态-审核通过
        :return: 点击'审核状态-审核通过'按钮后的页面
        """
        self.project.click(self.person_authentication_examine_state_pass_button)
        return self.project.get_current_page_source()

    def click_person_authentication_search_button_action(self):
        """
        动作：点击查询按钮
        :return: 点击'查询按钮'按钮后的页面
        """
        self.project.click(self.person_authentication_search_button)
        return self.project.get_current_page_source()

    def click_person_authentication_clear_button_action(self):
        """
        动作：点击清楚按钮
        :return: 点击'清楚按钮'按钮后的页面
        """
        self.project.click(self.person_authentication_clear_button)
        return self.project.get_current_page_source()

    def click_person_authentication_first_line_button_action(self):
        """
        动作：点击第一行数据按钮（审核/撤销）
        :return: 点击'第一行数据按钮（审核/撤销）'按钮后的页面
        """
        self.project.click(self.person_authentication_first_line_button)
        return self.project.get_current_page_source()

    def set_person_authentication_unpass_reason_input_action(self, person_authentication_unpass_reason_input):
        """
        动作：设置审核-不通过原因输入框
        :param person_authentication_unpass_reason_input: 审核-不通过原因输入框
        :return: 设置'审核-不通过原因输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.person_authentication_unpass_reason_input, person_authentication_unpass_reason_input)
        return self.project.get_current_page_source()

    def click_person_authentication_examine_pass_button_action(self):
        """
        动作：点击审核-通过按钮
        :return: 点击'审核-通过按钮'按钮后的页面
        """
        self.project.click(self.person_authentication_examine_pass_button)
        return self.project.get_current_page_source()

    def click_person_authentication_examine_unpass_button_action(self):
        """
        动作：点击审核-不通过按钮
        :return: 点击'审核-不通过按钮'按钮后的页面
        """
        self.project.click(self.person_authentication_examine_unpass_button)
        return self.project.get_current_page_source()

    def click_person_authentication_examine_cancel_button_action(self):
        """
        动作：点击审核-取消按钮
        :return: 点击'审核-取消按钮'按钮后的页面
        """
        self.project.click(self.person_authentication_examine_cancel_button)
        return self.project.get_current_page_source()

    def set_person_authentication_revoke_reason_input_action(self, person_authentication_revoke_reason_input):
        """
        动作：设置撤销-撤销原因输入框
        :param person_authentication_revoke_reason_input: 撤销-撤销原因输入框
        :return: 设置'撤销-撤销原因输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.person_authentication_revoke_reason_input, person_authentication_revoke_reason_input)
        return self.project.get_current_page_source()

    def click_person_authentication_revoke_confirm_button_action(self):
        """
        动作：点击撤销-确定按钮
        :return: 点击'撤销-确定按钮'按钮后的页面
        """
        self.project.click(self.person_authentication_revoke_confirm_button)
        return self.project.get_current_page_source()

    def click_person_authentication_revoke_cancel_button_action(self):
        """
        动作：点击撤销-取消按钮
        :return: 点击'撤销-取消按钮'按钮后的页面
        """
        self.project.click(self.person_authentication_revoke_cancel_button)
        return self.project.get_current_page_source()

    def click_person_authentication_revoke_close_button_action(self):
        """
        动作：点击撤销-关闭按钮
        :return: 点击'撤销-关闭按钮'按钮后的页面
        """
        self.project.click(self.person_authentication_revoke_close_button)
        return self.project.get_current_page_source()

    def click_person_authentication_batch_revoke_button_action(self):
        """
        动作：点击批量撤销按钮
        :return: 点击'批量撤销按钮'按钮后的页面
        """
        self.project.click(self.person_authentication_batch_revoke_button)
        return self.project.get_current_page_source()

    def get_person_authentication_first_line_examine_state_text_action(self):
        """
        动作：获取第一行审核状态按钮的文本
        :return: '第一行审核状态按钮'的文本
        """
        control_content = self.project.get_element_text(self.person_authentication_first_line_examine_state_text)
        return control_content

    # endregion Actions
