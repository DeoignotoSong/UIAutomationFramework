from Utils.Log import log
from poium import Page, Element


'''
订单支付成功页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class OrderPaySuccessPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 后退按钮
        self._back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        # 标题
        self._header_center_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_center_tv"]'
        # 提示内容
        self._pay_text_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/course_ll"]/preceding-sibling::android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView'
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
    def header_center(self):
        """
        属性: 标题
        :return: 标题
        """
        element = None
        try:
            element = self.Android.get_element(self._header_center_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def pay_text(self):
        """
        属性: 提示内容
        :return: 提示内容
        """
        element = None
        try:
            element = self.Android.get_element(self._pay_text_tag)
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

    def get_pay_text_action(self):
        """
        动作：获取提示内容的文本
        :return: '提示内容'的文本
        """
        control_content = self.pay_text.text.strip()
        return control_content

    # endregion Actions
