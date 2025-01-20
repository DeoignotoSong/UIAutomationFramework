from Utils.Log import log
from poium import Page, Element


'''
APP内部通用对话框
com.jinjilie.daxuezhang.functions.MainActivity
'''


class HomePage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 城市
        self._city_address_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/address_tv']"
        # 搜索栏
        self._search_bar_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/search_rl']"
        # 底部导首页ICON
        self._footer_nav_home_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/bbl']/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView"
        # 底部导问答ICON
        self._footer_nav_qa_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/bbl']/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView"
        # 底部导课程ICON
        self._footer_nav_course_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/bbl']/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView"
        # 底部导微聊ICON
        self._footer_nav_chat_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/bbl']/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView"
        # 底部导我的ICON
        self._footer_nav_my_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/bbl']/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView"
        # endregion Fields

    # region Properties
    @property
    def city_address_button(self):
        """
        属性: 城市
        :return: 城市
        """
        element = None
        try:
            element = self.Android.get_element(self._city_address_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_bar_button(self):
        """
        属性: 搜索栏
        :return: 搜索栏
        """
        element = None
        try:
            element = self.Android.get_element(self._search_bar_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def footer_nav_home_button(self):
        """
        属性: 底部导首页ICON
        :return: 底部导首页ICON
        """
        element = None
        try:
            element = self.Android.get_element(self._footer_nav_home_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def footer_nav_qa_button(self):
        """
        属性: 底部导问答ICON
        :return: 底部导问答ICON
        """
        element = None
        try:
            element = self.Android.get_element(self._footer_nav_qa_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def footer_nav_course_button(self):
        """
        属性: 底部导课程ICON
        :return: 底部导课程ICON
        """
        element = None
        try:
            element = self.Android.get_element(self._footer_nav_course_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def footer_nav_chat_button(self):
        """
        属性: 底部导微聊ICON
        :return: 底部导微聊ICON
        """
        element = None
        try:
            element = self.Android.get_element(self._footer_nav_chat_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def footer_nav_my_button(self):
        """
        属性: 底部导我的ICON
        :return: 底部导我的ICON
        """
        element = None
        try:
            element = self.Android.get_element(self._footer_nav_my_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_city_address_button_action(self):
        """
        动作：点击城市
        :return: 点击'城市'按钮后的页面
        """
        self.Android.click(self.city_address_button)
        return self.Android.get_current_page_source()

    def click_search_bar_button_action(self):
        """
        动作：点击搜索栏
        :return: 点击'搜索栏'按钮后的页面
        """
        self.Android.click(self.search_bar_button)
        return self.Android.get_current_page_source()

    def click_footer_nav_home_button_action(self):
        """
        动作：点击底部导首页ICON
        :return: 点击'底部导首页ICON'按钮后的页面
        """
        self.Android.click(self.footer_nav_home_button)
        return self.Android.get_current_page_source()

    def click_footer_nav_qa_button_action(self):
        """
        动作：点击底部导问答ICON
        :return: 点击'底部导问答ICON'按钮后的页面
        """
        self.Android.click(self.footer_nav_qa_button)
        return self.Android.get_current_page_source()

    def click_footer_nav_course_button_action(self):
        """
        动作：点击底部导课程ICON
        :return: 点击'底部导课程ICON'按钮后的页面
        """
        self.Android.click(self.footer_nav_course_button)
        return self.Android.get_current_page_source()

    def click_footer_nav_chat_button_action(self):
        """
        动作：点击底部导微聊ICON
        :return: 点击'底部导微聊ICON'按钮后的页面
        """
        self.Android.click(self.footer_nav_chat_button)
        return self.Android.get_current_page_source()

    def click_footer_nav_my_button_action(self):
        """
        动作：点击底部导我的ICON
        :return: 点击'底部导我的ICON'按钮后的页面
        """
        self.Android.click(self.footer_nav_my_button)
        return self.Android.get_current_page_source()

    # endregion Actions
