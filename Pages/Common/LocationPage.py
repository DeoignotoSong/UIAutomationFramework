from Utils.Log import log
from poium import Page, Element


'''
位置选择页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class LocationPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 当前城市名称
        self._current_city_text_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/tvCurrentCity']"
        # 搜索栏
        self._search_bar_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/etSearchBar']"
        # 搜索结果第一个位置元素
        self._search_result_first_element_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/tv_city_name']"
        # 热门城市列表
        self._hot_city_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/rvHotCityList']"
        # endregion Fields

    # region Properties
    @property
    def current_city_text(self):
        """
        属性: 当前城市名称
        :return: 当前城市名称
        """
        element = None
        try:
            element = self.Android.get_element(self._current_city_text_tag)
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
    def search_result_first_element(self):
        """
        属性: 搜索结果第一个位置元素
        :return: 搜索结果第一个位置元素
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_first_element_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def hot_city(self):
        """
        属性: 热门城市列表
        :return: 热门城市列表
        """
        element = None
        try:
            element = self.Android.get_element(self._hot_city_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def get_current_city_text_action(self):
        """
        动作：获取当前城市名称的文本
        :return: '当前城市名称'的文本
        """
        control_content = self.current_city_text.text.strip()
        return control_content

    def click_search_bar_button_action(self):
        """
        动作：点击搜索栏
        :return: 点击'搜索栏'按钮后的页面
        """
        self.Android.click(self.search_bar_button)
        return self.Android.get_current_page_source()

    # endregion Actions
