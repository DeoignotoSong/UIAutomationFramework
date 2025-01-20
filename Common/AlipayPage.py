from Utils.Log import log

"""
支付宝支付页面
"""


class AlipayPage:
    def __init__(self, project):
        self.project = project

        # region Fields
        # 扫一扫付款/登录账户付款
        self._ali_login_style_button_tag = '//*[@id="J_tip_qr"]/a'
        # 账户名输入框
        self._ali_account_login_username_input_tag = '//*[@id="J_tLoginId"]'
        # 账户密码输入框
        self._ali_account_login_password_input_tag = '//*[@id="payPasswd_rsainput"]'
        # 验证码输入框
        self._ali_account_login_check_code_input_tag = '/html/body/div[4]/div[3]/div[2]/div/div[3]/form/div/div[2]/div/div[4]/div/div/div/span/input'
        # 验证码图片
        self._ali_account_login_check_code_image_button_tag = '/html/body/div[4]/div[3]/div[2]/div/div[3]/form/div/div[2]/div/div[4]/div/div/div/span/img'
        # 登录账户-下一步按钮
        self._ali_account_login_next_step_button_tag = '//*[@id="J_newBtn"]'
        # 支付密码输入框
        self._pay_password_input_tag = '//*[@id="payPassword_rsainput"]'
        # 确认付款按钮
        self._pay_confirm_button_tag = '//*[@id="J_authSubmit"]'
        # 付款成功文本
        self._pay_success_text_tag = '//*[@id="main"]/div/div[1]/h3'
        # endregion Fields

    # region Properties
    @property
    def ali_login_style_button(self):
        """
        属性: 扫一扫付款/登录账户付款
        :return: 扫一扫付款/登录账户付款
        """
        element = None
        try:
            element = self.project.get_element(self._ali_login_style_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def ali_account_login_username_input(self):
        """
        属性: 账户名输入框
        :return: 账户名输入框
        """
        element = None
        try:
            element = self.project.get_element(self._ali_account_login_username_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def ali_account_login_password_input(self):
        """
        属性: 账户密码输入框
        :return: 账户密码输入框
        """
        element = None
        try:
            element = self.project.get_element(self._ali_account_login_password_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def ali_account_login_check_code_input(self):
        """
        属性: 验证码输入框
        :return: 验证码输入框
        """
        element = None
        try:
            element = self.project.get_element(self._ali_account_login_check_code_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def ali_account_login_check_code_image_button(self):
        """
        属性: 验证码图片
        :return: 验证码图片
        """
        element = None
        try:
            element = self.project.get_element(self._ali_account_login_check_code_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def ali_account_login_next_step_button(self):
        """
        属性: 登录账户-下一步按钮
        :return: 登录账户-下一步按钮
        """
        element = None
        try:
            element = self.project.get_element(self._ali_account_login_next_step_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def pay_password_input(self):
        """
        属性: 支付密码输入框
        :return: 支付密码输入框
        """
        element = None
        try:
            element = self.project.get_element(self._pay_password_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def pay_confirm_button(self):
        """
        属性: 确认付款按钮
        :return: 确认付款按钮
        """
        element = None
        try:
            element = self.project.get_element(self._pay_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def pay_success_text(self):
        """
        属性: 付款成功文本
        :return: 付款成功文本
        """
        element = None
        try:
            element = self.project.get_element(self._pay_success_text_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_ali_login_style_button_action(self):
        """
        动作：点击扫一扫付款/登录账户付款
        :return: 点击'扫一扫付款/登录账户付款'按钮后的页面
        """
        self.project.click(self.ali_login_style_button)
        return self.project.get_current_page_source()

    def set_ali_account_login_username_input_action(self, ali_account_login_username_input):
        """
        动作：设置账户名输入框
        :param ali_account_login_username_input: 账户名输入框
        :return: 设置'账户名输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.ali_account_login_username_input, ali_account_login_username_input)
        return self.project.get_current_page_source()

    def set_ali_account_login_password_input_action(self, ali_account_login_password_input):
        """
        动作：设置账户密码输入框
        :param ali_account_login_password_input: 账户密码输入框
        :return: 设置'账户密码输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.ali_account_login_password_input, ali_account_login_password_input)
        return self.project.get_current_page_source()

    def set_ali_account_login_check_code_input_action(self, ali_account_login_check_code_input):
        """
        动作：设置验证码输入框
        :param ali_account_login_check_code_input: 验证码输入框
        :return: 设置'验证码输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.ali_account_login_check_code_input, ali_account_login_check_code_input)
        return self.project.get_current_page_source()

    def click_ali_account_login_check_code_image_button_action(self):
        """
        动作：点击验证码图片
        :return: 点击'验证码图片'按钮后的页面
        """
        self.project.click(self.ali_account_login_check_code_image_button)
        return self.project.get_current_page_source()

    def click_ali_account_login_next_step_button_action(self):
        """
        动作：点击登录账户-下一步按钮
        :return: 点击'登录账户-下一步按钮'按钮后的页面
        """
        self.project.click(self.ali_account_login_next_step_button)
        return self.project.get_current_page_source()

    def set_pay_password_input_action(self, pay_password_input):
        """
        动作：设置支付密码输入框
        :param pay_password_input: 支付密码输入框
        :return: 设置'支付密码输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.pay_password_input, pay_password_input)
        return self.project.get_current_page_source()

    def click_pay_confirm_button_action(self):
        """
        动作：点击确认付款按钮
        :return: 点击'确认付款按钮'按钮后的页面
        """
        self.project.click(self.pay_confirm_button)
        return self.project.get_current_page_source()

    def get_pay_success_text_action(self):
        """
        动作：获取付款成功文本的文本
        :return: '付款成功文本'的文本
        """
        control_content = self.project.get_element_text(self.pay_success_text)
        return control_content

    # endregion Actions
