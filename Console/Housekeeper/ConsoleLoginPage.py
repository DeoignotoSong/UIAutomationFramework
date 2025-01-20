from Utils.Log import log

"""
后台登录页
console_url
"""


class ConsoleLoginPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url'
        # region Fields
        # 消息提示信息
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 账号输入框
        self._console_username_input_tag = '/html/body/div/div/form/div[3]/div/div[1]/input'
        # 密码输入框
        self._console_passwd_input_tag = '/html/body/div/div/form/div[4]/div/div[1]/input'
        # 验证码输入框
        self._console_slider_check_input_tag = '/html/body/div/div/form/div[4]/div/div[1]/input'
        # 万能验证码输入框
        self._console_universal_code_input_tag = '//*[@id="app"]/div/div/form/div[4]/div/input'
        # 登录按钮
        self._console_login_button_tag = '/html/body/div/div/form/div[5]/div/button'
        # 登录按钮文本
        self._console_login_text_tag = '/html/body/div/div/form/div[5]/div/button/span/span'
        # endregion Fields

    # region Properties
    @property
    def message_content_text(self):
        """
        属性: 消息提示信息
        :return: 消息提示信息
        """
        element = None
        try:
            element = self.project.get_element(self._message_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_username_input(self):
        """
        属性: 账号输入框
        :return: 账号输入框
        """
        element = None
        try:
            element = self.project.get_element(self._console_username_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_passwd_input(self):
        """
        属性: 密码输入框
        :return: 密码输入框
        """
        element = None
        try:
            element = self.project.get_element(self._console_passwd_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_slider_check_input(self):
        """
        属性: 验证码输入框
        :return: 验证码输入框
        """
        element = None
        try:
            element = self.project.get_element(self._console_slider_check_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_universal_code_input(self):
        """
        属性: 万能验证码输入框
        :return: 万能验证码输入框
        """
        element = None
        try:
            element = self.project.get_element(self._console_universal_code_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_login_button(self):
        """
        属性: 登录按钮
        :return: 登录按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_login_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_login_text(self):
        """
        属性: 登录按钮文本
        :return: 登录按钮文本
        """
        element = None
        try:
            element = self.project.get_element(self._console_login_text_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def get_message_content_text_action(self):
        """
        动作：获取消息提示信息的文本
        :return: '消息提示信息'的文本
        """
        control_content = self.project.get_element_text(self.message_content_text)
        return control_content

    def set_console_username_input_action(self, console_username_input):
        """
        动作：设置账号输入框
        :param console_username_input: 账号输入框
        :return: 设置'账号输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_username_input, console_username_input)
        return self.project.get_current_page_source()

    def set_console_passwd_input_action(self, console_passwd_input):
        """
        动作：设置密码输入框
        :param console_passwd_input: 密码输入框
        :return: 设置'密码输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_passwd_input, console_passwd_input)
        return self.project.get_current_page_source()

    def set_console_slider_check_input_action(self, console_slider_check_input):
        """
        动作：设置验证码输入框
        :param console_slider_check_input: 验证码输入框
        :return: 设置'验证码输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_slider_check_input, console_slider_check_input)
        return self.project.get_current_page_source()

    def set_console_universal_code_input_action(self, console_universal_code_input):
        """
        动作：设置万能验证码输入框
        :param console_universal_code_input: 万能验证码输入框
        :return: 设置'万能验证码输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_universal_code_input, console_universal_code_input)
        return self.project.get_current_page_source()

    def click_console_login_button_action(self):
        """
        动作：点击登录按钮
        :return: 点击'登录按钮'按钮后的页面
        """
        self.project.click(self.console_login_button)
        return self.project.get_current_page_source()

    def get_console_login_text_action(self):
        """
        动作：获取登录按钮文本的文本
        :return: '登录按钮文本'的文本
        """
        control_content = self.project.get_element_text(self.console_login_text)
        return control_content

    # endregion Actions
