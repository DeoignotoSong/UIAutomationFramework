from Utils.Log import log

"""
后台-用户中心-机构院校管理-机构院校信息维护
console_url/university/apply_list_info
"""


class ConsoleInstitutionInfoDefendPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/university/apply_list_info'
        # region Fields
        # 提交成功提示信息
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 联系人电话输入
        self._console_contact_mobile_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 所属国家
        self._console_at_country_button_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/div[1]/input'
        # 联系人姓名输入
        self._console_contact_name_input_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div/input'
        # 机构院校名称输入
        self._console_institution_school_name_input_tag = '//*[@id="tableSearch"]/form/div/div[last()-2]/div/div/input'
        # 查询按钮
        self._console_inquiry_button_tag = '//*[@id="tableSearch"]/form/div/div[last()-1]/div/button'
        # 清除按钮
        self._console_clean_button_tag = '//*[@id="tableSearch"]/form/div/div[last()]/div/button/span'
        # 查询数据名称
        self._console_inquiry_value_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div'
        # 审核操作按钮
        self._console_inquiry_value_review_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[11]/div/a[2]'
        # 审核页面表单名称
        self._console_review_form_name_text_tag = '//*[@id="app"]/div/section/main/div/div[1]/div[2]/ul/li'
        # 不通过原因输入
        self._console_review_not_pass_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[19]/div/div/div/div/textarea'
        # 不通过按钮
        self._console_review_no_pass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[21]/div[1]/div/div/button[2]/span'
        # 通过按钮
        self._console_review_pass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[21]/div[1]/div/div/button[1]'
        # 审核后数据状态
        self._console_review_value_status_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[8]/div'
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
    def console_inquiry_value_review_button(self):
        """
        属性: 审核操作按钮
        :return: 审核操作按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_inquiry_value_review_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_review_form_name_text(self):
        """
        属性: 审核页面表单名称
        :return: 审核页面表单名称
        """
        element = None
        try:
            element = self.project.get_element(self._console_review_form_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_review_not_pass_input(self):
        """
        属性: 不通过原因输入
        :return: 不通过原因输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_review_not_pass_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_review_no_pass_button(self):
        """
        属性: 不通过按钮
        :return: 不通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_review_no_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_review_pass_button(self):
        """
        属性: 通过按钮
        :return: 通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_review_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_review_value_status_text(self):
        """
        属性: 审核后数据状态
        :return: 审核后数据状态
        """
        element = None
        try:
            element = self.project.get_element(self._console_review_value_status_text_tag)
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

    def set_console_contact_mobile_input_action(self, console_contact_mobile_input):
        """
        动作：设置联系人电话输入
        :param console_contact_mobile_input: 联系人电话输入
        :return: 设置'联系人电话输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_contact_mobile_input, console_contact_mobile_input)
        return self.project.get_current_page_source()

    def click_console_at_country_button_action(self):
        """
        动作：点击所属国家
        :return: 点击'所属国家'按钮后的页面
        """
        self.project.click(self.console_at_country_button)
        return self.project.get_current_page_source()

    def set_console_contact_name_input_action(self, console_contact_name_input):
        """
        动作：设置联系人姓名输入
        :param console_contact_name_input: 联系人姓名输入
        :return: 设置'联系人姓名输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_contact_name_input, console_contact_name_input)
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

    def get_console_inquiry_value_name_text_action(self):
        """
        动作：获取查询数据名称的文本
        :return: '查询数据名称'的文本
        """
        control_content = self.project.get_element_text(self.console_inquiry_value_name_text)
        return control_content

    def click_console_inquiry_value_review_button_action(self):
        """
        动作：点击审核操作按钮
        :return: 点击'审核操作按钮'按钮后的页面
        """
        self.project.click(self.console_inquiry_value_review_button)
        return self.project.get_current_page_source()

    def get_console_review_form_name_text_action(self):
        """
        动作：获取审核页面表单名称的文本
        :return: '审核页面表单名称'的文本
        """
        control_content = self.project.get_element_text(self.console_review_form_name_text)
        return control_content

    def set_console_review_not_pass_input_action(self, console_review_not_pass_input):
        """
        动作：设置不通过原因输入
        :param console_review_not_pass_input: 不通过原因输入
        :return: 设置'不通过原因输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_review_not_pass_input, console_review_not_pass_input)
        return self.project.get_current_page_source()

    def click_console_review_no_pass_button_action(self):
        """
        动作：点击不通过按钮
        :return: 点击'不通过按钮'按钮后的页面
        """
        self.project.click(self.console_review_no_pass_button)
        return self.project.get_current_page_source()

    def click_console_review_pass_button_action(self):
        """
        动作：点击通过按钮
        :return: 点击'通过按钮'按钮后的页面
        """
        self.project.click(self.console_review_pass_button)
        return self.project.get_current_page_source()

    def get_console_review_value_status_text_action(self):
        """
        动作：获取审核后数据状态的文本
        :return: '审核后数据状态'的文本
        """
        control_content = self.project.get_element_text(self.console_review_value_status_text)
        return control_content

    # endregion Actions
