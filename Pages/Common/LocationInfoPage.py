from Utils.Log import log


'''
我的昵称设置页面
com.jinjilie.daxuezhang.functions.detail.activity.ArticleActivity
'''


class LocationInfoPage:
    def __init__(self, project):
        self.Android = project

        # region Fields
        # 后退按钮
        self._college_detail_back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        # 国家/地区修改按钮
        self._location_country_modify_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/location_country_tv"]'
        # 详细地址输入框
        self._location_name_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/location_name_et"]'
        # 提交按钮
        self._submit_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_right_tv"]'
        # 阿尔巴尼亚
        self._arbny_button_tag = '//*[@text="阿尔巴尼亚"]'
        # 阿富汗
        self._afh_button_tag = '//*[@text="阿富汗"]'
        # endregion Fields

    # region Properties
    @property
    def college_detail_back_button(self):
        """
        属性: 后退按钮
        :return: 后退按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._college_detail_back_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def location_country_modify_button(self):
        """
        属性: 国家/地区修改按钮
        :return: 国家/地区修改按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._location_country_modify_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def location_name(self):
        """
        属性: 详细地址输入框
        :return: 详细地址输入框
        """
        element = None
        try:
            element = self.Android.get_element(self._location_name_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def submit_button(self):
        """
        属性: 提交按钮
        :return: 提交按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._submit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def arbny_button(self):
        """
        属性: 阿尔巴尼亚
        :return: 阿尔巴尼亚
        """
        element = None
        try:
            element = self.Android.get_element(self._arbny_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def afh_button(self):
        """
        属性: 阿富汗
        :return: 阿富汗
        """
        element = None
        try:
            element = self.Android.get_element(self._afh_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_college_detail_back_button_action(self):
        """
        动作：点击后退按钮
        :return: 点击'后退按钮'按钮后的页面
        """
        self.Android.click(self.college_detail_back_button)
        return self.Android.get_current_page_source()

    def click_location_country_modify_button_action(self):
        """
        动作：点击国家/地区修改按钮
        :return: 点击'国家/地区修改按钮'按钮后的页面
        """
        self.Android.click(self.location_country_modify_button)
        return self.Android.get_current_page_source()

    def click_submit_button_action(self):
        """
        动作：点击提交按钮
        :return: 点击'提交按钮'按钮后的页面
        """
        self.Android.click(self.submit_button)
        return self.Android.get_current_page_source()

    def click_arbny_button_action(self):
        """
        动作：点击阿尔巴尼亚
        :return: 点击'阿尔巴尼亚'按钮后的页面
        """
        self.Android.click(self.arbny_button)
        return self.Android.get_current_page_source()

    def click_afh_button_action(self):
        """
        动作：点击阿富汗
        :return: 点击'阿富汗'按钮后的页面
        """
        self.Android.click(self.afh_button)
        return self.Android.get_current_page_source()

    # endregion Actions
