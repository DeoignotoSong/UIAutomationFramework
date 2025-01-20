from Utils.Log import log


'''
我的昵称设置页面
com.jinjilie.daxuezhang.functions.detail.activity.ArticleActivity
'''


class MyNickSetingPage:
    def __init__(self, project):
        self.Android = project

        # region Fields
        # 后退按钮
        self._college_detail_back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        # 我的昵称input
        self._my_nick_input_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/my_input_et"]'
        # 确定按钮
        self._my_next_button_tag = '//*[@text="确定"]'
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
    def my_nick_input(self):
        """
        属性: 我的昵称input
        :return: 我的昵称input
        """
        element = None
        try:
            element = self.Android.get_element(self._my_nick_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def my_next_button(self):
        """
        属性: 确定按钮
        :return: 确定按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._my_next_button_tag)
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

    def set_my_nick_input_action(self, my_nick_input):
        """
        动作：设置我的昵称input
        :param my_nick_input: 我的昵称input
        :return: 设置'我的昵称input'文本后的页面
        """
        self.Android.clear_and_send_keys(self.my_nick_input, my_nick_input)
        return self.Android.get_current_page_source()

    def click_my_next_button_action(self):
        """
        动作：点击确定按钮
        :return: 点击'确定按钮'按钮后的页面
        """
        self.Android.click(self.my_next_button)
        return self.Android.get_current_page_source()

    # endregion Actions
