from Utils.Log import log
from poium import Page, Element


'''
选择标签页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class QuestionChoiceTabPage:
    def __init__(self, project):
        self.Android = project
        # region Fields
        # 选择标签-标题-留学
        self._tv_tab_title_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/topTab_tl']/android.widget.LinearLayout/android.widget.RelativeLayout[2]"
        # 一级标签-第一项
        self._one_level_first_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/top_rv']/android.widget.LinearLayout[1]"
        # 二级级标签-第二项
        self._two_level_second_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/bottom_rv']/android.widget.LinearLayout[1]/android.widget.TextView"
        # 选择主题标签-第二列-第一个
        self._theme_level_second_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/top_rv']/android.widget.LinearLayout[1]"
        # 下一步
        self._next_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/next_tv']"
        # endregion Fields

    # region Properties
    @property
    def tv_tab_title_button(self):
        """
        属性: 选择标签-标题-留学
        :return: 选择标签-标题-留学
        """
        element = None
        try:
            element = self.Android.get_element(self._tv_tab_title_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def one_level_first_button(self):
        """
        属性: 一级标签-第一项
        :return: 一级标签-第一项
        """
        element = None
        try:
            element = self.Android.get_element(self._one_level_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def two_level_second_button(self):
        """
        属性: 二级级标签-第二项
        :return: 二级级标签-第二项
        """
        element = None
        try:
            element = self.Android.get_element(self._two_level_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def theme_level_second_button(self):
        """
        属性: 选择主题标签-第二列-第一个
        :return: 选择主题标签-第二列-第一个
        """
        element = None
        try:
            element = self.Android.get_element(self._theme_level_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def next_button(self):
        """
        属性: 下一步
        :return: 下一步
        """
        element = None
        try:
            element = self.Android.get_element(self._next_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_tv_tab_title_button_action(self):
        """
        动作：点击选择标签-标题-留学
        :return: 点击'选择标签-标题-留学'按钮后的页面
        """
        self.Android.click(self.tv_tab_title_button)
        return self.Android.get_current_page_source()

    def click_one_level_first_button_action(self):
        """
        动作：点击一级标签-第一项
        :return: 点击'一级标签-第一项'按钮后的页面
        """
        self.Android.click(self.one_level_first_button)
        return self.Android.get_current_page_source()

    def click_two_level_second_button_action(self):
        """
        动作：点击二级级标签-第二项
        :return: 点击'二级级标签-第二项'按钮后的页面
        """
        self.Android.click(self.two_level_second_button)
        return self.Android.get_current_page_source()

    def click_theme_level_second_button_action(self):
        """
        动作：点击选择主题标签-第二列-第一个
        :return: 点击'选择主题标签-第二列-第一个'按钮后的页面
        """
        self.Android.click(self.theme_level_second_button)
        return self.Android.get_current_page_source()

    def click_next_button_action(self):
        """
        动作：点击下一步
        :return: 点击'下一步'按钮后的页面
        """
        self.Android.click(self.next_button)
        return self.Android.get_current_page_source()

    # endregion Actions
