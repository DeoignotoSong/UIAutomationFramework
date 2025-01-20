from Utils.Log import log


'''
登录页面
com.jinjilie.daxuezhang.model.login.activity.LoginActivity
'''


class UserLoginRegisterPage:
    def __init__(self, project):
        self.Android = project

        # region Fields
        # 密码登录按钮
        self._password_login_button_tag = '//android.widget.TextView[@resource-id="com.jinjilie.daxuezhang.debug:id/login_psw_ll"]'
        # 关闭按钮
        self._closed_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        # 验证码登录按钮
        self._verification_code_login_button_tag = '//android.widget.TextView[@resource-id="com.jinjilie.daxuezhang.debug:id/login_code_ll"]'
        # 账户登录-手机号输入框
        self._mobile_input_tag = '//android.widget.EditText[@resource-id="com.jinjilie.daxuezhang.debug:id/login_phone_et"]'
        # 账户登录-密码输入框
        self._password_input_tag = '//android.widget.EditText[@resource-id="com.jinjilie.daxuezhang.debug:id/login_code_or_psw_et"]'
        # 登录按钮
        self._login_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/login_tv"]'
        # 协议同意复选框
        self._agree_checkbox_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/login_protocol_iv"]'
        # endregion Fields

    # region Properties
    @property
    def password_login_button(self):
        """
        属性: 密码登录按钮
        :return: 密码登录按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._password_login_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def closed_button(self):
        """
        属性: 关闭按钮
        :return: 关闭按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._closed_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def verification_code_login_button(self):
        """
        属性: 验证码登录按钮
        :return: 验证码登录按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._verification_code_login_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def mobile_input(self):
        """
        属性: 账户登录-手机号输入框
        :return: 账户登录-手机号输入框
        """
        element = None
        try:
            element = self.Android.get_element(self._mobile_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def password_input(self):
        """
        属性: 账户登录-密码输入框
        :return: 账户登录-密码输入框
        """
        element = None
        try:
            element = self.Android.get_element(self._password_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def login_button(self):
        """
        属性: 登录按钮
        :return: 登录按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._login_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def agree_checkbox_button(self):
        """
        属性: 协议同意复选框
        :return: 协议同意复选框
        """
        element = None
        try:
            element = self.Android.get_element(self._agree_checkbox_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_password_login_button_action(self):
        """
        动作：点击密码登录按钮
        :return: 点击'密码登录按钮'按钮后的页面
        """
        self.Android.click(self.password_login_button)
        return self.Android.get_current_page_source()

    def click_closed_button_action(self):
        """
        动作：点击关闭按钮
        :return: 点击'关闭按钮'按钮后的页面
        """
        self.Android.click(self.closed_button)
        return self.Android.get_current_page_source()

    def click_verification_code_login_button_action(self):
        """
        动作：点击验证码登录按钮
        :return: 点击'验证码登录按钮'按钮后的页面
        """
        self.Android.click(self.verification_code_login_button)
        return self.Android.get_current_page_source()

    def set_mobile_input_action(self, mobile_input):
        """
        动作：设置账户登录-手机号输入框
        :param mobile_input: 账户登录-手机号输入框
        :return: 设置'账户登录-手机号输入框'文本后的页面
        """
        self.Android.clear_and_send_keys(self.mobile_input, mobile_input)
        return self.Android.get_current_page_source()

    def set_password_input_action(self, password_input):
        """
        动作：设置账户登录-密码输入框
        :param password_input: 账户登录-密码输入框
        :return: 设置'账户登录-密码输入框'文本后的页面
        """
        self.Android.clear_and_send_keys(self.password_input, password_input)
        return self.Android.get_current_page_source()

    def click_login_button_action(self):
        """
        动作：点击登录按钮
        :return: 点击'登录按钮'按钮后的页面
        """
        self.Android.click(self.login_button)
        return self.Android.get_current_page_source()

    def click_agree_checkbox_button_action(self):
        """
        动作：点击协议同意复选框
        :return: 点击'协议同意复选框'按钮后的页面
        """
        self.Android.click(self.agree_checkbox_button)
        return self.Android.get_current_page_source()

    # endregion Actions
