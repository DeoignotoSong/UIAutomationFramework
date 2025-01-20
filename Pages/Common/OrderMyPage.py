from Utils.Log import log


'''
我的订单页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class OrderMyPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 后退按钮
        self._back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        # 已完成标签
        self._finished_button_tag = '//*[@text="已完成"]'
        # 订单产品名称
        self._order_goods_name_text_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/order_goods_name_tv"]'
        # 订单号
        self._order_nun_text_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/order_nun_tv"]'
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
    def finished_button(self):
        """
        属性: 已完成标签
        :return: 已完成标签
        """
        element = None
        try:
            element = self.Android.get_element(self._finished_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def order_goods_name_text(self):
        """
        属性: 订单产品名称
        :return: 订单产品名称
        """
        element = None
        try:
            element = self.Android.get_element(self._order_goods_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def order_nun_text(self):
        """
        属性: 订单号
        :return: 订单号
        """
        element = None
        try:
            element = self.Android.get_element(self._order_nun_text_tag)
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

    def click_finished_button_action(self):
        """
        动作：点击已完成标签
        :return: 点击'已完成标签'按钮后的页面
        """
        self.Android.click(self.finished_button)
        return self.Android.get_current_page_source()

    def get_order_goods_name_text_action(self):
        """
        动作：获取订单产品名称的文本
        :return: '订单产品名称'的文本
        """
        control_content = self.order_goods_name_text.text.strip()
        return control_content

    def get_order_nun_text_action(self):
        """
        动作：获取订单号的文本
        :return: '订单号'的文本
        """
        control_content = self.order_nun_text.text.strip()
        return control_content

    # endregion Actions
