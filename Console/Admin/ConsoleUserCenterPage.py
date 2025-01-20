from Utils.Log import log

"""
后台首页-用户中心
console_url/user/dashboard
"""


class ConsoleUserCenterPage:

    def __init__(self, project):
        self.project = project
        self.url = 'console_url/user/dashboard'
        # region Fields
        # 机构院校管理按钮
        self._institute_management_button_tag = '//*[@id="app"]/div/section/aside/ul/li[1]/div'
        # 机构院校列表按钮
        self._institute_list_button_tag = '//*[@id="app"]/div/section/aside/ul/li[1]/ul/li[1]'
        # 机构院校信息维护按钮
        self._institute_info_maintain = '//*[@id="app"]/div/section/aside/ul/li[1]/ul/li[2]'
        # 机构院校审核按钮
        self._institute_examine_button_tag = '//*[@id="app"]/div/section/aside/ul/li[1]/ul/li[3]'
        # 机构院校子账号管理
        self._institute_subaccount_management_button_tag = '//*[@id="app"]/div/section/aside/ul/li[1]/ul/li[4]'
        # 用户管理按钮
        self._person_management_button_tag = '//*[@id="app"]/div/section/aside/ul/li[2]/div'
        # 用户列表按钮
        self._person_list_button_tag = '//*[@id="app"]/div/section/aside/ul/li[2]/ul/li[1]'
        # 平台讲师认证按钮
        self._person_authentication_button_tag = '//*[@id="app"]/div/section/aside/ul/li[2]/ul/li[2]'
        # endregion Fields

    # region Properties
    @property
    def institute_management_button(self):
        """
        属性: 机构院校管理按钮
        :return: 机构院校管理按钮
        """
        element = None
        try:
            element = self.project.get_element(self._institute_management_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def institute_list_button(self):
        """
        属性: 机构院校列表按钮
        :return: 机构院校列表按钮
        """
        element = None
        try:
            element = self.project.get_element(self._institute_list_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def institute_examine_button(self):
        """
        属性: 机构院校审核按钮
        :return: 机构院校审核按钮
        """
        element = None
        try:
            element = self.project.get_element(self._institute_examine_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def institute_subaccount_management_button(self):
        """
        属性: 机构院校子账号管理
        :return: 机构院校子账号管理
        """
        element = None
        try:
            element = self.project.get_element(self._institute_subaccount_management_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_management_button(self):
        """
        属性: 用户管理按钮
        :return: 用户管理按钮
        """
        element = None
        try:
            element = self.project.get_element(self._person_management_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_list_button(self):
        """
        属性: 用户列表按钮
        :return: 用户列表按钮
        """
        element = None
        try:
            element = self.project.get_element(self._person_list_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def person_authentication_button(self):
        """
        属性: 平台讲师认证按钮
        :return: 平台讲师认证按钮
        """
        element = None
        try:
            element = self.project.get_element(self._person_authentication_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_institute_management_button_action(self):
        """
        动作：点击机构院校管理按钮
        :return: 点击'机构院校管理按钮'按钮后的页面
        """
        self.project.click(self.institute_management_button)
        return self.project.get_current_page_source()

    def click_institute_list_button_action(self):
        """
        动作：点击机构院校列表按钮
        :return: 点击'机构院校列表按钮'按钮后的页面
        """
        self.project.click(self.institute_list_button)
        return self.project.get_current_page_source()

    def click_institute_examine_button_action(self):
        """
        动作：点击机构院校审核按钮
        :return: 点击'机构院校审核按钮'按钮后的页面
        """
        self.project.click(self.institute_examine_button)
        return self.project.get_current_page_source()

    def click_institute_subaccount_management_button_action(self):
        """
        动作：点击机构院校子账号管理
        :return: 点击'机构院校子账号管理'按钮后的页面
        """
        self.project.click(self.institute_subaccount_management_button)
        return self.project.get_current_page_source()

    def click_person_management_button_action(self):
        """
        动作：点击用户管理按钮
        :return: 点击'用户管理按钮'按钮后的页面
        """
        self.project.click(self.person_management_button)
        return self.project.get_current_page_source()

    def click_person_list_button_action(self):
        """
        动作：点击用户列表按钮
        :return: 点击'用户列表按钮'按钮后的页面
        """
        self.project.click(self.person_list_button)
        return self.project.get_current_page_source()

    def click_person_authentication_button_action(self):
        """
        动作：点击平台讲师认证按钮
        :return: 点击'平台讲师认证按钮'按钮后的页面
        """
        self.project.click(self.person_authentication_button)
        return self.project.get_current_page_source()

    # endregion Actions
