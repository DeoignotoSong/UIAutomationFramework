from Utils.Log import log
from poium import Page, Element


'''
评价页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class EvaluateWritePage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 后退按钮
        self._back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        # 页面标题
        self._title_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_center_tv"]'
        # 用户星星评分-5
        self._evaluate_user_rating_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/evaluate_user_rating_bar"]/android.widget.ImageView[5]'
        # 课程星星评分-5
        self._evaluate_course_rating_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/evaluate_course_rating_bar"]/android.widget.ImageView[5]'
        # 评价内容
        self._write_evaluate_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/write_evaluate_et"]'
        # 评价按钮
        self._evaluate_write_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/item_evaluate_next"]'
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
    def evaluate_user_rating_button(self):
        """
        属性: 用户星星评分-5
        :return: 用户星星评分-5
        """
        element = None
        try:
            element = self.Android.get_element(self._evaluate_user_rating_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def evaluate_course_rating_button(self):
        """
        属性: 课程星星评分-5
        :return: 课程星星评分-5
        """
        element = None
        try:
            element = self.Android.get_element(self._evaluate_course_rating_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def write_evaluate(self):
        """
        属性: 评价内容
        :return: 评价内容
        """
        element = None
        try:
            element = self.Android.get_element(self._write_evaluate_tag)
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

    def click_evaluate_user_rating_button_action(self):
        """
        动作：点击用户星星评分-5
        :return: 点击'用户星星评分-5'按钮后的页面
        """
        self.Android.click(self.evaluate_user_rating_button)
        return self.Android.get_current_page_source()

    def click_evaluate_course_rating_button_action(self):
        """
        动作：点击课程星星评分-5
        :return: 点击'课程星星评分-5'按钮后的页面
        """
        self.Android.click(self.evaluate_course_rating_button)
        return self.Android.get_current_page_source()

    # endregion Actions
