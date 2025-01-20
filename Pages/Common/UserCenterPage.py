from Utils.Log import log


'''
用户中心页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class UserCenterPage:
    def __init__(self, project):
        self.Android = project

        # region Fields
        # 已登录用户名
        self._login_username_text_tag = '//android.widget.TextView[@resource-id="com.jinjilie.daxuezhang.debug:id/my_name_tv"]'
        # 学习中心按钮
        self._learning_center_button_tag = '//android.widget.LinearLayout[@resource-id="com.jinjilie.daxuezhang.debug:id/my_learning_ll"]/android.widget.ImageView[1]'
        # 学习中心文本按钮
        self._learning_center_text_button_tag = '//*[@text="学习中心"]'
        # 登录注册文本按钮
        self._login_register_button_tag = "//*[@text='登录/注册']"
        # 签到按钮
        self._sign_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/my_sign_ll"]'
        # 签到按钮文字
        self._sign_text_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/my_sign_ll"]/android.widget.TextView'
        # 编辑资料
        self._edit_info_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/my_head_rl"]'
        # 设置icon
        self._setting_icon_button_tag = '//*[@text="设置"]'
        # 我的订单
        self._order_icon_button_tag = '//*[@text="我的订单"]'
        # 我的评价
        self._evaluate_icon_button_tag = '//*[@text="我的评价"]'
        # endregion Fields

    # region Properties
    @property
    def login_username_text(self):
        """
        属性: 已登录用户名
        :return: 已登录用户名
        """
        element = None
        try:
            element = self.Android.get_element(self._login_username_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def learning_center_button(self):
        """
        属性: 学习中心按钮
        :return: 学习中心按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._learning_center_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def learning_center_text_button(self):
        """
        属性: 学习中心文本按钮
        :return: 学习中心文本按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._learning_center_text_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def login_register_button(self):
        """
        属性: 登录注册文本按钮
        :return: 登录注册文本按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._login_register_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def sign_button(self):
        """
        属性: 签到按钮
        :return: 签到按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._sign_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def sign_text(self):
        """
        属性: 签到按钮文字
        :return: 签到按钮文字
        """
        element = None
        try:
            element = self.Android.get_element(self._sign_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def edit_info_button(self):
        """
        属性: 编辑资料
        :return: 编辑资料
        """
        element = None
        try:
            element = self.Android.get_element(self._edit_info_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def setting_icon_button(self):
        """
        属性: 设置icon
        :return: 设置icon
        """
        element = None
        try:
            element = self.Android.get_element(self._setting_icon_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def order_icon_button(self):
        """
        属性: 我的订单
        :return: 我的订单
        """
        element = None
        try:
            element = self.Android.get_element(self._order_icon_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def evaluate_icon_button(self):
        """
        属性: 我的评价
        :return: 我的评价
        """
        element = None
        try:
            element = self.Android.get_element(self._evaluate_icon_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def get_login_username_text_action(self):
        """
        动作：获取已登录用户名的文本
        :return: '已登录用户名'的文本
        """
        control_content = self.login_username_text.text.strip()
        return control_content

    def click_learning_center_button_action(self):
        """
        动作：点击学习中心按钮
        :return: 点击'学习中心按钮'按钮后的页面
        """
        self.Android.click(self.learning_center_button)
        return self.Android.get_current_page_source()

    def click_learning_center_text_button_action(self):
        """
        动作：点击学习中心文本按钮
        :return: 点击'学习中心文本按钮'按钮后的页面
        """
        self.Android.click(self.learning_center_text_button)
        return self.Android.get_current_page_source()

    def click_login_register_button_action(self):
        """
        动作：点击登录注册文本按钮
        :return: 点击'登录注册文本按钮'按钮后的页面
        """
        self.Android.click(self.login_register_button)
        return self.Android.get_current_page_source()

    def click_sign_button_action(self):
        """
        动作：点击签到按钮
        :return: 点击'签到按钮'按钮后的页面
        """
        self.Android.click(self.sign_button)
        return self.Android.get_current_page_source()

    def get_sign_text_action(self):
        """
        动作：获取签到按钮文字的文本
        :return: '签到按钮文字'的文本
        """
        control_content = self.sign_text.text.strip()
        return control_content

    def click_edit_info_button_action(self):
        """
        动作：点击编辑资料
        :return: 点击'编辑资料'按钮后的页面
        """
        self.Android.click(self.edit_info_button)
        return self.Android.get_current_page_source()

    def click_setting_icon_button_action(self):
        """
        动作：点击设置icon
        :return: 点击'设置icon'按钮后的页面
        """
        self.Android.click(self.setting_icon_button)
        return self.Android.get_current_page_source()

    def click_order_icon_button_action(self):
        """
        动作：点击我的订单
        :return: 点击'我的订单'按钮后的页面
        """
        self.Android.click(self.order_icon_button)
        return self.Android.get_current_page_source()

    def click_evaluate_icon_button_action(self):
        """
        动作：点击我的评价
        :return: 点击'我的评价'按钮后的页面
        """
        self.Android.click(self.evaluate_icon_button)
        return self.Android.get_current_page_source()

    # endregion Actions
