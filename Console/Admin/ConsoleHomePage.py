from Utils.Log import log

"""
后台首页
console_url/home/dashboard
"""


class ConsoleHomePage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/home/dashboard'
        # region Fields
        # 登录人名称
        self._console_name_text_tag = '//*[@id="app"]/div/header/div[1]/div[2]/div/span'
        # 安全退出按钮
        self._console_logout_button_tag = '//*[@id="app"]/div/header/div[1]/div[2]/span'
        # 后台基础维护菜单按钮
        self._console_basic_maintain_button_tag = '//*[@id="app"]/div/header/div[2]/ul/li[2]'
        # 后台基础维护_运维管理按钮
        self._console_basic_maintain_devops_management_button_tag = '//*[@id="app"]/div/section/main/div/div/div[2]/div[2]/button[1]'
        # 后台基础维护_MQ管理
        self._console_basic_maintain_MQ_management_button_tag = '//*[@id="app"]/div/section/main/div/div/div[2]/div[2]/button[2]'
        # 后台用户中心菜单按钮
        self._console_user_center_button_tag = '//*[@id="app"]/div/header/div[2]/ul/li[3]'
        # 后台订单中心菜单按钮
        self._console_order_center_button_tag = '//*[@id="app"]/div/header/div[2]/ul/li[4]'
        # 后台财务中心按钮
        self._console_finance_center_button_tag = '//*[@id="app"]/div/header/div[2]/ul/li[5]'
        # 后台内容监控中心按钮
        self._console_content_monitor_center_button_tag = '//*[@id="app"]/div/header/div[2]/ul/li[6]'
        # 后台运营中心按钮
        self._operation_center_button_tag = '//*[@id="app"]/div/header/div[2]/ul/li[7]'
        # 后台社交中心按钮
        self._console_social_center_button_tag = '//*[@id="app"]/div/header/div[2]/ul/li[8]'
        # 后台消息中心按钮
        self._console_message_center_button_tag = '//*[@id="app"]/div/header/div[2]/ul/li[9]'
        # 后台客服中心
        self._console_service_center_button_tag = '//*[@id="app"]/div/header/div[2]/ul/li[10]'
        # 后台帮助中心
        self._console_help_center_button_tag = '//*[@id="app"]/div/header/div[2]/ul/li[11]'
        # endregion Fields

    # region Properties
    @property
    def console_name_text(self):
        """
        属性: 登录人名称
        :return: 登录人名称
        """
        element = None
        try:
            element = self.project.get_element(self._console_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_logout_button(self):
        """
        属性: 安全退出按钮
        :return: 安全退出按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_logout_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_basic_maintain_button(self):
        """
        属性: 后台基础维护菜单按钮
        :return: 后台基础维护菜单按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_basic_maintain_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_basic_maintain_devops_management_button(self):
        """
        属性: 后台基础维护_运维管理按钮
        :return: 后台基础维护_运维管理按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_basic_maintain_devops_management_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_basic_maintain_MQ_management_button(self):
        """
        属性: 后台基础维护_MQ管理
        :return: 后台基础维护_MQ管理
        """
        element = None
        try:
            element = self.project.get_element(self._console_basic_maintain_MQ_management_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_user_center_button(self):
        """
        属性: 后台用户中心菜单按钮
        :return: 后台用户中心菜单按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_user_center_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_order_center_button(self):
        """
        属性: 后台订单中心菜单按钮
        :return: 后台订单中心菜单按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_order_center_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_finance_center_button(self):
        """
        属性: 后台财务中心按钮
        :return: 后台财务中心按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_finance_center_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_content_monitor_center_button(self):
        """
        属性: 后台内容监控中心按钮
        :return: 后台内容监控中心按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_content_monitor_center_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def operation_center_button(self):
        """
        属性: 后台运营中心按钮
        :return: 后台运营中心按钮
        """
        element = None
        try:
            element = self.project.get_element(self._operation_center_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_social_center_button(self):
        """
        属性: 后台社交中心按钮
        :return: 后台社交中心按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_social_center_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_message_center_button(self):
        """
        属性: 后台消息中心按钮
        :return: 后台消息中心按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_message_center_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_service_center_button(self):
        """
        属性: 后台客服中心
        :return: 后台客服中心
        """
        element = None
        try:
            element = self.project.get_element(self._console_service_center_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_help_center_button(self):
        """
        属性: 后台帮助中心
        :return: 后台帮助中心
        """
        element = None
        try:
            element = self.project.get_element(self._console_help_center_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def get_console_name_text_action(self):
        """
        动作：获取登录人名称的文本
        :return: '登录人名称'的文本
        """
        control_content = self.project.get_element_text(self.console_name_text)
        return control_content

    def click_console_logout_button_action(self):
        """
        动作：点击安全退出按钮
        :return: 点击'安全退出按钮'按钮后的页面
        """
        self.project.click(self.console_logout_button)
        return self.project.get_current_page_source()

    def click_console_basic_maintain_button_action(self):
        """
        动作：点击后台基础维护菜单按钮
        :return: 点击'后台基础维护菜单按钮'按钮后的页面
        """
        self.project.click(self.console_basic_maintain_button)
        return self.project.get_current_page_source()

    def click_console_basic_maintain_devops_management_button_action(self):
        """
        动作：点击后台基础维护_运维管理按钮
        :return: 点击'后台基础维护_运维管理按钮'按钮后的页面
        """
        self.project.click(self.console_basic_maintain_devops_management_button)
        return self.project.get_current_page_source()

    def click_console_basic_maintain_MQ_management_button_action(self):
        """
        动作：点击后台基础维护_MQ管理
        :return: 点击'后台基础维护_MQ管理'按钮后的页面
        """
        self.project.click(self.console_basic_maintain_MQ_management_button)
        return self.project.get_current_page_source()

    def click_console_user_center_button_action(self):
        """
        动作：点击后台用户中心菜单按钮
        :return: 点击'后台用户中心菜单按钮'按钮后的页面
        """
        self.project.click(self.console_user_center_button)
        return self.project.get_current_page_source()

    def click_console_order_center_button_action(self):
        """
        动作：点击后台订单中心菜单按钮
        :return: 点击'后台订单中心菜单按钮'按钮后的页面
        """
        self.project.click(self.console_order_center_button)
        return self.project.get_current_page_source()

    def click_console_finance_center_button_action(self):
        """
        动作：点击后台财务中心按钮
        :return: 点击'后台财务中心按钮'按钮后的页面
        """
        self.project.click(self.console_finance_center_button)
        return self.project.get_current_page_source()

    def click_console_content_monitor_center_button_action(self):
        """
        动作：点击后台内容监控中心按钮
        :return: 点击'后台内容监控中心按钮'按钮后的页面
        """
        self.project.click(self.console_content_monitor_center_button)
        return self.project.get_current_page_source()

    def click_operation_center_button_action(self):
        """
        动作：点击后台运营中心按钮
        :return: 点击'后台运营中心按钮'按钮后的页面
        """
        self.project.click(self.operation_center_button)
        return self.project.get_current_page_source()

    def click_console_social_center_button_action(self):
        """
        动作：点击后台社交中心按钮
        :return: 点击'后台社交中心按钮'按钮后的页面
        """
        self.project.click(self.console_social_center_button)
        return self.project.get_current_page_source()

    def click_console_message_center_button_action(self):
        """
        动作：点击后台消息中心按钮
        :return: 点击'后台消息中心按钮'按钮后的页面
        """
        self.project.click(self.console_message_center_button)
        return self.project.get_current_page_source()

    def click_console_service_center_button_action(self):
        """
        动作：点击后台客服中心
        :return: 点击'后台客服中心'按钮后的页面
        """
        self.project.click(self.console_service_center_button)
        return self.project.get_current_page_source()

    def click_console_help_center_button_action(self):
        """
        动作：点击后台帮助中心
        :return: 点击'后台帮助中心'按钮后的页面
        """
        self.project.click(self.console_help_center_button)
        return self.project.get_current_page_source()

    # endregion Actions
