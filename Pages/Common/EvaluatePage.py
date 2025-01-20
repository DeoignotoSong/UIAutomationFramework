from Utils.Log import log
from poium import Page, Element


'''
评价页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class EvaluatePage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 后退按钮
        self._back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        # 页面标题
        self._title_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_center_tv"]'
        # 待评价
        self._evaluatelist_no_text_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/evaluatelist_no_text_ly"]'
        # 已评价
        self._evaluatelist_also_text_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/evaluatelist_also_text_tv"]'
        # 评价按钮
        self._evaluate_write_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/evaluate_witre_tv"]'
        # endregion Fields

    # region Properties
    @property
    def back_button(self):
        """
        属性: 后退按钮
        :return: 后退按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._back_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def title(self):
        """
        属性: 页面标题
        :return: 页面标题
        """
        element = None
        try:
            element = self.Android.get_element(self._title_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def evaluatelist_no_text_button(self):
        """
        属性: 待评价
        :return: 待评价
        """
        element = None
        try:
            element = self.Android.get_element(self._evaluatelist_no_text_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def evaluatelist_also_text_button(self):
        """
        属性: 已评价
        :return: 已评价
        """
        element = None
        try:
            element = self.Android.get_element(self._evaluatelist_also_text_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def evaluate_write(self):
        """
        属性: 评价按钮
        :return: 评价按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._evaluate_write_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_back_button_action(self):
        """
        动作：点击后退按钮
        :return: 点击'后退按钮'按钮后的页面
        """
        self.Android.click(self.back_button)
        return self.Android.get_current_page_source()

    def click_evaluatelist_no_text_button_action(self):
        """
        动作：点击待评价
        :return: 点击'待评价'按钮后的页面
        """
        self.Android.click(self.evaluatelist_no_text_button)
        return self.Android.get_current_page_source()

    def click_evaluatelist_also_text_button_action(self):
        """
        动作：点击已评价
        :return: 点击'已评价'按钮后的页面
        """
        self.Android.click(self.evaluatelist_also_text_button)
        return self.Android.get_current_page_source()

    # endregion Actions
