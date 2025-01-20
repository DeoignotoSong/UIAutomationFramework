from Utils.Log import log
from poium import Page, Element


'''
订单确认页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class OrderEnsurePage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 后退按钮
        self._back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        # 协议连接
        self._protocol_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/btn_protocol"]'
        # 直播讲座-协议连接
        self._live_exhibition_protocol_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/btn_protocol_no"]'
        # 我知晓并同意
        self._register_agree_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/register_agree_tv"]'
        # 预约按钮
        self._appointment_button_tag = '//*[@text="预约"]'
        # 立即支付
        self._pay_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/btn_pay"]'
        # 付款金额
        self._pay_text_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/pay"]'
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
    def protocol_button(self):
        """
        属性: 协议连接
        :return: 协议连接
        """
        element = None
        try:
            element = self.Android.get_element(self._protocol_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def live_exhibition_protocol_button(self):
        """
        属性: 直播讲座-协议连接
        :return: 直播讲座-协议连接
        """
        element = None
        try:
            element = self.Android.get_element(self._live_exhibition_protocol_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def register_agree_button(self):
        """
        属性: 我知晓并同意
        :return: 我知晓并同意
        """
        element = None
        try:
            element = self.Android.get_element(self._register_agree_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def appointment_button(self):
        """
        属性: 预约按钮
        :return: 预约按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._appointment_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def pay_button(self):
        """
        属性: 立即支付
        :return: 立即支付
        """
        element = None
        try:
            element = self.Android.get_element(self._pay_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def pay_text(self):
        """
        属性: 付款金额
        :return: 付款金额
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

    def click_protocol_button_action(self):
        """
        动作：点击协议连接
        :return: 点击'协议连接'按钮后的页面
        """
        self.Android.click(self.protocol_button)
        return self.Android.get_current_page_source()

    def click_live_exhibition_protocol_button_action(self):
        """
        动作：点击直播讲座-协议连接
        :return: 点击'直播讲座-协议连接'按钮后的页面
        """
        self.Android.click(self.live_exhibition_protocol_button)
        return self.Android.get_current_page_source()

    def click_register_agree_button_action(self):
        """
        动作：点击我知晓并同意
        :return: 点击'我知晓并同意'按钮后的页面
        """
        self.Android.click(self.register_agree_button)
        return self.Android.get_current_page_source()

    def click_appointment_button_action(self):
        """
        动作：点击预约按钮
        :return: 点击'预约按钮'按钮后的页面
        """
        self.Android.click(self.appointment_button)
        return self.Android.get_current_page_source()

    def click_pay_button_action(self):
        """
        动作：点击立即支付
        :return: 点击'立即支付'按钮后的页面
        """
        self.Android.click(self.pay_button)
        return self.Android.get_current_page_source()

    def get_pay_text_action(self):
        """
        动作：获取付款金额的文本
        :return: '付款金额'的文本
        """
        control_content = self.pay_text.text.strip()
        return control_content

    # endregion Actions
