from Utils.Log import log
from poium import Page, Element


'''
学习中心页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class LearningCenterPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 后退按钮
        self._back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        # 页面标题
        self._title_page_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_center_tv"]'
        # 直播课列表-结果标题
        self._result_title_page_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/img"]/following::android.widget.LinearLayout/android.widget.TextView[1]'
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
