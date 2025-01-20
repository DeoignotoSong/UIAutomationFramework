from Utils.Log import log

"""
后台-运营中心-广告位管理-添加广告页面
console_url/advert/advert-add/add/0
"""

class ConsoleAdvAddPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/advert/advert-add/add/0'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 选择广告位按钮
        self._choice_advert_place_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/button/span'
        # 选择广告_广告名称
        self._choice_advert_name_input_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 选择广告_查询按钮
        self._choice_advert_select_button_tag = '//*[@id="tableSearch"]/form/div/div[9]/div/button'
        # 选择广告_列表_第一个结果_操作_选择
        self._choice_advert_list_first_choice_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/a/span'
        # 顺序输入文本框
        self._advert_add_order_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div/div[2]/div/div/div[1]/input'
        # 购买人输入文本框
        self._advert_add_buy_user_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div/div[3]/div/div/div/input'
        # 联系方式输入文本框
        self._advert_add_buy_user_contact_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div/div[4]/div/div/div/input'
        # 广告名输入本文框
        self._advert_add_advert_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div/div[5]/div/div/div/input'
        # 广告费用输入文本框
        self._advert_add_adprice_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div/div[6]/div/div/div/input'
        # 广告语输入文本框
        self._advert_add_slogan_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div/div[7]/div/div/div[1]/input'
        # 广告图片上传文本框
        self._advert_add_advert_image_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div/div[11]/div/div/span/div/input'
        # 广告开始时间段
        self._advert_add_advert_begin_datetime_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div/div[9]/div/div/div/input[1]'
        # 广告结束时间段
        self._advert_add_advert_over_datetime_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div/div[9]/div/div/div/input[2]'
        # 提交按钮
        self._advert_add_submit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[3]/button/span'
        # endregion Fields

    # region Properties
    @property
    def message_content_text(self):
        """
        属性: 消息提示
        :return: 消息提示
        """
        element = None
        try:
            element = self.project.get_element(self._message_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def choice_advert_place_button(self):
        """
        属性: 选择广告位按钮
        :return: 选择广告位按钮
        """
        element = None
        try:
            element = self.project.get_element(self._choice_advert_place_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def choice_advert_name_input(self):
        """
        属性: 选择广告_广告名称
        :return: 选择广告_广告名称
        """
        element = None
        try:
            element = self.project.get_element(self._choice_advert_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def choice_advert_select_button(self):
        """
        属性: 选择广告_查询按钮
        :return: 选择广告_查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._choice_advert_select_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def choice_advert_list_first_choice_button(self):
        """
        属性: 选择广告_列表_第一个结果_操作_选择
        :return: 选择广告_列表_第一个结果_操作_选择
        """
        element = None
        try:
            element = self.project.get_element(self._choice_advert_list_first_choice_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def advert_add_order_input(self):
        """
        属性: 顺序输入文本框
        :return: 顺序输入文本框
        """
        element = None
        try:
            element = self.project.get_element(self._advert_add_order_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def advert_add_buy_user_name_input(self):
        """
        属性: 购买人输入文本框
        :return: 购买人输入文本框
        """
        element = None
        try:
            element = self.project.get_element(self._advert_add_buy_user_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def advert_add_buy_user_contact_input(self):
        """
        属性: 联系方式输入文本框
        :return: 联系方式输入文本框
        """
        element = None
        try:
            element = self.project.get_element(self._advert_add_buy_user_contact_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def advert_add_advert_name_input(self):
        """
        属性: 广告名输入本文框
        :return: 广告名输入本文框
        """
        element = None
        try:
            element = self.project.get_element(self._advert_add_advert_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def advert_add_adprice_input(self):
        """
        属性: 广告费用输入文本框
        :return: 广告费用输入文本框
        """
        element = None
        try:
            element = self.project.get_element(self._advert_add_adprice_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def advert_add_slogan_input(self):
        """
        属性: 广告语输入文本框
        :return: 广告语输入文本框
        """
        element = None
        try:
            element = self.project.get_element(self._advert_add_slogan_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def advert_add_advert_image_input(self):
        """
        属性: 广告图片上传文本框
        :return: 广告图片上传文本框
        """
        element = None
        try:
            element = self.project.get_element(self._advert_add_advert_image_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def advert_add_advert_begin_datetime_input(self):
        """
        属性: 广告开始时间段
        :return: 广告开始时间段
        """
        element = None
        try:
            element = self.project.get_element(self._advert_add_advert_begin_datetime_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def advert_add_advert_over_datetime_input(self):
        """
        属性: 广告结束时间段
        :return: 广告结束时间段
        """
        element = None
        try:
            element = self.project.get_element(self._advert_add_advert_over_datetime_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def advert_add_submit_button(self):
        """
        属性: 提交按钮
        :return: 提交按钮
        """
        element = None
        try:
            element = self.project.get_element(self._advert_add_submit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def get_message_content_text_action(self):
        """
        动作：获取消息提示的文本
        :return: '消息提示'的文本
        """
        control_content = self.project.get_element_text(self.message_content_text)
        return control_content

    def click_choice_advert_place_button_action(self):
        """
        动作：点击选择广告位按钮
        :return: 点击'选择广告位按钮'按钮后的页面
        """
        self.project.click(self.choice_advert_place_button)
        return self.project.get_current_page_source()

    def set_choice_advert_name_input_action(self, choice_advert_name_input):
        """
        动作：设置选择广告_广告名称
        :param choice_advert_name_input: 选择广告_广告名称
        :return: 设置'选择广告_广告名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.choice_advert_name_input, choice_advert_name_input)
        return self.project.get_current_page_source()

    def click_choice_advert_select_button_action(self):
        """
        动作：点击选择广告_查询按钮
        :return: 点击'选择广告_查询按钮'按钮后的页面
        """
        self.project.click(self.choice_advert_select_button)
        return self.project.get_current_page_source()

    def click_choice_advert_list_first_choice_button_action(self):
        """
        动作：点击选择广告_列表_第一个结果_操作_选择
        :return: 点击'选择广告_列表_第一个结果_操作_选择'按钮后的页面
        """
        self.project.click(self.choice_advert_list_first_choice_button)
        return self.project.get_current_page_source()

    def set_advert_add_order_input_action(self, advert_add_order_input):
        """
        动作：设置顺序输入文本框
        :param advert_add_order_input: 顺序输入文本框
        :return: 设置'顺序输入文本框'文本后的页面
        """
        self.project.clear_and_send_keys(self.advert_add_order_input, advert_add_order_input)
        return self.project.get_current_page_source()

    def set_advert_add_buy_user_name_input_action(self, advert_add_buy_user_name_input):
        """
        动作：设置购买人输入文本框
        :param advert_add_buy_user_name_input: 购买人输入文本框
        :return: 设置'购买人输入文本框'文本后的页面
        """
        self.project.clear_and_send_keys(self.advert_add_buy_user_name_input, advert_add_buy_user_name_input)
        return self.project.get_current_page_source()

    def set_advert_add_buy_user_contact_input_action(self, advert_add_buy_user_contact_input):
        """
        动作：设置联系方式输入文本框
        :param advert_add_buy_user_contact_input: 联系方式输入文本框
        :return: 设置'联系方式输入文本框'文本后的页面
        """
        self.project.clear_and_send_keys(self.advert_add_buy_user_contact_input, advert_add_buy_user_contact_input)
        return self.project.get_current_page_source()

    def set_advert_add_advert_name_input_action(self, advert_add_advert_name_input):
        """
        动作：设置广告名输入本文框
        :param advert_add_advert_name_input: 广告名输入本文框
        :return: 设置'广告名输入本文框'文本后的页面
        """
        self.project.clear_and_send_keys(self.advert_add_advert_name_input, advert_add_advert_name_input)
        return self.project.get_current_page_source()

    def set_advert_add_adprice_input_action(self, advert_add_adprice_input):
        """
        动作：设置广告费用输入文本框
        :param advert_add_adprice_input: 广告费用输入文本框
        :return: 设置'广告费用输入文本框'文本后的页面
        """
        self.project.clear_and_send_keys(self.advert_add_adprice_input, advert_add_adprice_input)
        return self.project.get_current_page_source()

    def set_advert_add_slogan_input_action(self, advert_add_slogan_input):
        """
        动作：设置广告语输入文本框
        :param advert_add_slogan_input: 广告语输入文本框
        :return: 设置'广告语输入文本框'文本后的页面
        """
        self.project.clear_and_send_keys(self.advert_add_slogan_input, advert_add_slogan_input)
        return self.project.get_current_page_source()

    def set_advert_add_advert_image_input_action(self, advert_add_advert_image_input):
        """
        动作：设置广告图片上传文本框
        :param advert_add_advert_image_input: 广告图片上传文本框
        :return: 设置'广告图片上传文本框'文本后的页面
        """
        self.project.clear_and_send_keys(self.advert_add_advert_image_input, advert_add_advert_image_input)
        return self.project.get_current_page_source()

    def set_advert_add_advert_begin_datetime_input_action(self, advert_add_advert_begin_datetime_input):
        """
        动作：设置广告开始时间段
        :param advert_add_advert_begin_datetime_input: 广告开始时间段
        :return: 设置'广告开始时间段'文本后的页面
        """
        self.project.clear_and_send_keys(self.advert_add_advert_begin_datetime_input, advert_add_advert_begin_datetime_input)
        return self.project.get_current_page_source()

    def set_advert_add_advert_over_datetime_input_action(self, advert_add_advert_over_datetime_input):
        """
        动作：设置广告结束时间段
        :param advert_add_advert_over_datetime_input: 广告结束时间段
        :return: 设置'广告结束时间段'文本后的页面
        """
        self.project.clear_and_send_keys(self.advert_add_advert_over_datetime_input, advert_add_advert_over_datetime_input)
        return self.project.get_current_page_source()

    def click_advert_add_submit_button_action(self):
        """
        动作：点击提交按钮
        :return: 点击'提交按钮'按钮后的页面
        """
        self.project.click(self.advert_add_submit_button)
        return self.project.get_current_page_source()

    # endregion Actions
