from Utils.Log import log

"""
后台-用户中心-机构院校管理-机构院校子账号管理
console_url/mechanism/subaccount/administration
"""


class ConsoleInstitutionSubAccountPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/mechanism/subaccount/administration'
        # region Fields
        # 查询数据空信息
        self._message_content_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div/div[3]/div/span/label'
        # 查询出的用户信息
        self._message_user_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[5]/div'
        # 机构院校名称输入
        self._console_institution_name_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 用户账号输入
        self._console_institution_account_input_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 查询按钮
        self._console_institution_select_button_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/button'
        # 清除按钮
        self._console_institution_clean_button_tag = '//*[@id="tableSearch"]/form/div/div[5]/div/button'
        # endregion Fields

    # region Properties
    @property
    def message_content_text(self):
        """
        属性: 查询数据空信息
        :return: 查询数据空信息
        """
        element = None
        try:
            element = self.project.get_element(self._message_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def message_user_name_text(self):
        """
        属性: 查询出的用户信息
        :return: 查询出的用户信息
        """
        element = None
        try:
            element = self.project.get_element(self._message_user_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_institution_name_input(self):
        """
        属性: 机构院校名称输入
        :return: 机构院校名称输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_institution_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_institution_account_input(self):
        """
        属性: 用户账号输入
        :return: 用户账号输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_institution_account_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_institution_select_button(self):
        """
        属性: 查询按钮
        :return: 查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_institution_select_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_institution_clean_button(self):
        """
        属性: 清除按钮
        :return: 清除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_institution_clean_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def get_message_content_text_action(self):
        """
        动作：获取查询数据空信息的文本
        :return: '查询数据空信息'的文本
        """
        control_content = self.project.get_element_text(self.message_content_text)
        return control_content

    def get_message_user_name_text_action(self):
        """
        动作：获取查询出的用户信息的文本
        :return: '查询出的用户信息'的文本
        """
        control_content = self.project.get_element_text(self.message_user_name_text)
        return control_content

    def set_console_institution_name_input_action(self, console_institution_name_input):
        """
        动作：设置机构院校名称输入
        :param console_institution_name_input: 机构院校名称输入
        :return: 设置'机构院校名称输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_institution_name_input, console_institution_name_input)
        return self.project.get_current_page_source()

    def set_console_institution_account_input_action(self, console_institution_account_input):
        """
        动作：设置用户账号输入
        :param console_institution_account_input: 用户账号输入
        :return: 设置'用户账号输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_institution_account_input, console_institution_account_input)
        return self.project.get_current_page_source()

    def click_console_institution_select_button_action(self):
        """
        动作：点击查询按钮
        :return: 点击'查询按钮'按钮后的页面
        """
        self.project.click(self.console_institution_select_button)
        return self.project.get_current_page_source()

    def click_console_institution_clean_button_action(self):
        """
        动作：点击清除按钮
        :return: 点击'清除按钮'按钮后的页面
        """
        self.project.click(self.console_institution_clean_button)
        return self.project.get_current_page_source()

    # endregion Actions
