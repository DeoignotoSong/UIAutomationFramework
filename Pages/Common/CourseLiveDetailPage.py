from Utils.Log import log
from poium import Page, Element


'''
直播课程详情页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class CourseLiveDetailPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 后退按钮
        self._back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/back_iv"]'
        # 页面标题
        self._title_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/title_tv"]'
        # 进入教室
        self._in_class_room_tag = '//*[@text="进入教室"]'
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
    def in_class_room(self):
        """
        属性: 进入教室
        :return: 进入教室
        """
        element = None
        try:
            element = self.Android.get_element(self._in_class_room_tag)
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

    # endregion Actions
