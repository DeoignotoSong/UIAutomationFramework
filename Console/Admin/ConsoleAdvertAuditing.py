from Utils.Log import log

"""
后台-运营中心-广告位管理-广告审核页面
console_url/advert/advert-add/add/0
"""

class ConsoleAdvertAuditing:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/advert/advert-add/add/0'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 禁用确认提示框
        self._message_dialog_content_text_tag = '/html/body/div[2]/div/div[2]/div[1]/div[2]/p'
        # 搜索-广告名称
        self._advert_auditing_advert_name_input_tag = '//*[@id="tableSearch"]/form/div/div[7]/div/div/input'
        # 搜索-广告id
        self._advert_auditing_advert_id_input_tag = '//*[@id="tableSearch"]/form/div/div[6]/div/div/input'
        # 搜索-查询按钮
        self._advert_auditing_advert_search_button_tag = '//*[@id="tableSearch"]/form/div/div[9]/div/button'
        # 列表-第一条结果-操作-通过
        self._advert_auditing_list_first_pass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[15]/div/a[1]/span'
        # 列表-第一条结果-操作-不通过
        self._advert_auditing_advert_first_fail_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[15]/div/a[2]/span'
        # 提交按钮
        self._advert_add_submit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[3]/button/span'
        # 确认对话框-确定按钮
        self._disable_confirm_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # 确认对话框-取消按钮
        self._disable_cancel_button_tag = '/html/body/div[3]/div/div[3]/button[1]'
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
    def message_dialog_content_text(self):
        """
        属性: 禁用确认提示框
        :return: 禁用确认提示框
        """
        element = None
        try:
            element = self.project.get_element(self._message_dialog_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def advert_auditing_advert_name_input(self):
        """
        属性: 搜索-广告名称
        :return: 搜索-广告名称
        """
        element = None
        try:
            element = self.project.get_element(self._advert_auditing_advert_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def advert_auditing_advert_id_input(self):
        """
        属性: 搜索-广告id
        :return: 搜索-广告id
        """
        element = None
        try:
            element = self.project.get_element(self._advert_auditing_advert_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def advert_auditing_advert_search_button(self):
        """
        属性: 搜索-查询按钮
        :return: 搜索-查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._advert_auditing_advert_search_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def advert_auditing_list_first_pass_button(self):
        """
        属性: 列表-第一条结果-操作-通过
        :return: 列表-第一条结果-操作-通过
        """
        element = None
        try:
            element = self.project.get_element(self._advert_auditing_list_first_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def advert_auditing_advert_first_fail_button(self):
        """
        属性: 列表-第一条结果-操作-不通过
        :return: 列表-第一条结果-操作-不通过
        """
        element = None
        try:
            element = self.project.get_element(self._advert_auditing_advert_first_fail_button_tag)
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

    @property
    def disable_confirm_button(self):
        """
        属性: 确认对话框-确定按钮
        :return: 确认对话框-确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._disable_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def disable_cancel_button(self):
        """
        属性: 确认对话框-取消按钮
        :return: 确认对话框-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._disable_cancel_button_tag)
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

    def get_message_dialog_content_text_action(self):
        """
        动作：获取禁用确认提示框的文本
        :return: '禁用确认提示框'的文本
        """
        control_content = self.project.get_element_text(self.message_dialog_content_text)
        return control_content

    def set_advert_auditing_advert_name_input_action(self, advert_auditing_advert_name_input):
        """
        动作：设置搜索-广告名称
        :param advert_auditing_advert_name_input: 搜索-广告名称
        :return: 设置'搜索-广告名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.advert_auditing_advert_name_input, advert_auditing_advert_name_input)
        return self.project.get_current_page_source()

    def set_advert_auditing_advert_id_input_action(self, advert_auditing_advert_id_input):
        """
        动作：设置搜索-广告id
        :param advert_auditing_advert_id_input: 搜索-广告id
        :return: 设置'搜索-广告id'文本后的页面
        """
        self.project.clear_and_send_keys(self.advert_auditing_advert_id_input, advert_auditing_advert_id_input)
        return self.project.get_current_page_source()

    def click_advert_auditing_advert_search_button_action(self):
        """
        动作：点击搜索-查询按钮
        :return: 点击'搜索-查询按钮'按钮后的页面
        """
        self.project.click(self.advert_auditing_advert_search_button)
        return self.project.get_current_page_source()

    def click_advert_auditing_list_first_pass_button_action(self):
        """
        动作：点击列表-第一条结果-操作-通过
        :return: 点击'列表-第一条结果-操作-通过'按钮后的页面
        """
        self.project.click(self.advert_auditing_list_first_pass_button)
        return self.project.get_current_page_source()

    def click_advert_auditing_advert_first_fail_button_action(self):
        """
        动作：点击列表-第一条结果-操作-不通过
        :return: 点击'列表-第一条结果-操作-不通过'按钮后的页面
        """
        self.project.click(self.advert_auditing_advert_first_fail_button)
        return self.project.get_current_page_source()

    def click_advert_add_submit_button_action(self):
        """
        动作：点击提交按钮
        :return: 点击'提交按钮'按钮后的页面
        """
        self.project.click(self.advert_add_submit_button)
        return self.project.get_current_page_source()

    def click_disable_confirm_button_action(self):
        """
        动作：点击确认对话框-确定按钮
        :return: 点击'确认对话框-确定按钮'按钮后的页面
        """
        self.project.click(self.disable_confirm_button)
        return self.project.get_current_page_source()

    def click_disable_cancel_button_action(self):
        """
        动作：点击确认对话框-取消按钮
        :return: 点击'确认对话框-取消按钮'按钮后的页面
        """
        self.project.click(self.disable_cancel_button)
        return self.project.get_current_page_source()

    # endregion Actions
