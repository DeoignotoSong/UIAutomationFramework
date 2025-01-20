from Utils.Log import log
from poium import Page, Element


'''
首页综合搜索页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class SearchPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 搜索按钮
        self._search_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/search_tv']"
        # 搜索栏
        self._search_bar_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/search_et']"
        # endregion Fields

    # region Properties
    @property
    def search_button(self):
        """
        属性: 搜索按钮
        :return: 搜索按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._search_button_tag)
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

    # endregion Properties

    # region Actions
    def click_search_button_action(self):
        """
        动作：点击搜索按钮
        :return: 点击'搜索按钮'按钮后的页面
        """
        self.Android.click(self.search_button)
        return self.Android.get_current_page_source()

    def click_search_bar_button_action(self):
        """
        动作：点击搜索栏
        :return: 点击'搜索栏'按钮后的页面
        """
        self.Android.click(self.search_bar_button)
        return self.Android.get_current_page_source()

    # endregion Actions
