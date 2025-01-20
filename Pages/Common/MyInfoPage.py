from Utils.Log import log


'''
我的个人信息页面
com.jinjilie.daxuezhang.functions.detail.activity.ArticleActivity
'''


class MyInfoPage:
    def __init__(self, project):
        self.Android = project

        # region Fields
        # 后退按钮
        self._article_detail_back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        # 我的头像
        self._my_head_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/my_head_iv"]'
        # 我的昵称
        self._my_exhibition_nick_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/my_exhibition_nick_tv"]'
        # 位置信息
        self._my_location_map_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/my_location_map"]'
        # 位置信息-value
        self._my_location_map_value_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/my_location_map"]/following::android.widget.TextView[1]'
        # 绑定银行卡
        self._my_bind_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/my_bind_tv"]'
        # 设置密码
        self._my_psw_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/my_psw_tv"]'
        # 三方绑定
        self._my_bind_third_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/my_bind_third_tv"]'
        # 退出登录

        # endregion Fields

    # region Properties
    @property
    def article_detail_back_button(self):
        """
        属性: 后退按钮
        :return: 后退按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._article_detail_back_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def my_head_button(self):
        """
        属性: 我的头像
        :return: 我的头像
        """
        element = None
        try:
            element = self.Android.get_element(self._my_head_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def my_exhibition_nick_button(self):
        """
        属性: 我的昵称
        :return: 我的昵称
        """
        element = None
        try:
            element = self.Android.get_element(self._my_exhibition_nick_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def my_location_map_button(self):
        """
        属性: 位置信息
        :return: 位置信息
        """
        element = None
        try:
            element = self.Android.get_element(self._my_location_map_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def my_location_map_value(self):
        """
        属性: 位置信息-value
        :return: 位置信息-value
        """
        element = None
        try:
            element = self.Android.get_element(self._my_location_map_value_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def my_bind_button(self):
        """
        属性: 绑定银行卡
        :return: 绑定银行卡
        """
        element = None
        try:
            element = self.Android.get_element(self._my_bind_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def my_psw_button(self):
        """
        属性: 设置密码
        :return: 设置密码
        """
        element = None
        try:
            element = self.Android.get_element(self._my_psw_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def my_bind_third_button(self):
        """
        属性: 三方绑定
        :return: 三方绑定
        """
        element = None
        try:
            element = self.Android.get_element(self._my_bind_third_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_article_detail_back_button_action(self):
        """
        动作：点击后退按钮
        :return: 点击'后退按钮'按钮后的页面
        """
        self.Android.click(self.article_detail_back_button)
        return self.Android.get_current_page_source()

    def click_my_head_button_action(self):
        """
        动作：点击我的头像
        :return: 点击'我的头像'按钮后的页面
        """
        self.Android.click(self.my_head_button)
        return self.Android.get_current_page_source()

    def click_my_exhibition_nick_button_action(self):
        """
        动作：点击我的昵称
        :return: 点击'我的昵称'按钮后的页面
        """
        self.Android.click(self.my_exhibition_nick_button)
        return self.Android.get_current_page_source()

    def click_my_location_map_button_action(self):
        """
        动作：点击位置信息
        :return: 点击'位置信息'按钮后的页面
        """
        self.Android.click(self.my_location_map_button)
        return self.Android.get_current_page_source()

    def click_my_bind_button_action(self):
        """
        动作：点击绑定银行卡
        :return: 点击'绑定银行卡'按钮后的页面
        """
        self.Android.click(self.my_bind_button)
        return self.Android.get_current_page_source()

    def click_my_psw_button_action(self):
        """
        动作：点击设置密码
        :return: 点击'设置密码'按钮后的页面
        """
        self.Android.click(self.my_psw_button)
        return self.Android.get_current_page_source()

    def click_my_bind_third_button_action(self):
        """
        动作：点击三方绑定
        :return: 点击'三方绑定'按钮后的页面
        """
        self.Android.click(self.my_bind_third_button)
        return self.Android.get_current_page_source()

    # endregion Actions
