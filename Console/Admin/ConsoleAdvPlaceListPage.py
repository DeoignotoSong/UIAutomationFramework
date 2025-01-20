from Utils.Log import log

"""
后台-运营中心-广告位管理-广告位配置
console_url/advert/adv_place_list
"""

class ConsoleAdvPlaceListPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/advert/adv_place_list'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 禁用确认提示框
        self._message_dialog_content_text_tag = '/html/body/div[2]/div/div[2]/div[1]/div[2]/p'
        # 搜索-广告位名称
        self._search_adv_name_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[2]/div/div/input'
        # 搜索-查询按钮
        self._search_query_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[9]/div/button'
        # 添加广告位按钮
        self._add_adv_place_button_tag = '//*[@id="tableSearch"]/form/div[2]/div[1]/div/button'
        # 添加广告
        self._add_adv_button_tag = '//*[@id="tableSearch"]/form/div[2]/div[3]/div/button'
        # 列表-第一条-广告ID
        self._list_adv_first_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[1]/div'
        # 列表-第一条-名称
        self._list_adv_first_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[2]/div'
        # 列表-第一条-广告位类型
        self._list_adv_first_type_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[3]/div'
        # 列表-第一条-状态
        self._list_adv_first_status_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[4]/div'
        # 列表-第一条-所有权
        self._list_adv_first_authority_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[5]/div'
        # 列表-第一条-位置类型
        self._list_adv_first_mode_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[6]/div'
        # 列表-第一条-频道
        self._list_adv_first_channel_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[8]/div'
        # 列表-第一条-渠道
        self._list_adv_first_source_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[9]/div'
        # 列表-第一条-操作
        self._list_adv_first_operate_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[1]/table/thead/tr/th[10]/div'
        # 列表-第一条-操作-禁用
        self._list_adv_first_operate_forbidden_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/a[1]/span'
        # 列表-第一条-操作-启用
        self._list_adv_first_operate_start_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/a[1]/span'
        # 列表-第一条-操作-删除
        self._list_adv_first_operate_delete_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/a[2]/span'
        # 确认禁用-确定按钮
        self._disable_confirm_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # 确认禁用-取消按钮
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
    def search_adv_name_input(self):
        """
        属性: 搜索-广告位名称
        :return: 搜索-广告位名称
        """
        element = None
        try:
            element = self.project.get_element(self._search_adv_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_query_button(self):
        """
        属性: 搜索-查询按钮
        :return: 搜索-查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_query_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_adv_place_button(self):
        """
        属性: 添加广告位按钮
        :return: 添加广告位按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_adv_place_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_adv_button(self):
        """
        属性: 添加广告
        :return: 添加广告
        """
        element = None
        try:
            element = self.project.get_element(self._add_adv_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_adv_first_id_text(self):
        """
        属性: 列表-第一条-广告ID
        :return: 列表-第一条-广告ID
        """
        element = None
        try:
            element = self.project.get_element(self._list_adv_first_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_adv_first_name_text(self):
        """
        属性: 列表-第一条-名称
        :return: 列表-第一条-名称
        """
        element = None
        try:
            element = self.project.get_element(self._list_adv_first_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_adv_first_type_text(self):
        """
        属性: 列表-第一条-广告位类型
        :return: 列表-第一条-广告位类型
        """
        element = None
        try:
            element = self.project.get_element(self._list_adv_first_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_adv_first_status_text(self):
        """
        属性: 列表-第一条-状态
        :return: 列表-第一条-状态
        """
        element = None
        try:
            element = self.project.get_element(self._list_adv_first_status_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_adv_first_authority_text(self):
        """
        属性: 列表-第一条-所有权
        :return: 列表-第一条-所有权
        """
        element = None
        try:
            element = self.project.get_element(self._list_adv_first_authority_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_adv_first_mode_text(self):
        """
        属性: 列表-第一条-位置类型
        :return: 列表-第一条-位置类型
        """
        element = None
        try:
            element = self.project.get_element(self._list_adv_first_mode_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_adv_first_channel_text(self):
        """
        属性: 列表-第一条-频道
        :return: 列表-第一条-频道
        """
        element = None
        try:
            element = self.project.get_element(self._list_adv_first_channel_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_adv_first_source_text(self):
        """
        属性: 列表-第一条-渠道
        :return: 列表-第一条-渠道
        """
        element = None
        try:
            element = self.project.get_element(self._list_adv_first_source_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_adv_first_operate_text(self):
        """
        属性: 列表-第一条-操作
        :return: 列表-第一条-操作
        """
        element = None
        try:
            element = self.project.get_element(self._list_adv_first_operate_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_adv_first_operate_forbidden_button(self):
        """
        属性: 列表-第一条-操作-禁用
        :return: 列表-第一条-操作-禁用
        """
        element = None
        try:
            element = self.project.get_element(self._list_adv_first_operate_forbidden_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_adv_first_operate_start_button(self):
        """
        属性: 列表-第一条-操作-启用
        :return: 列表-第一条-操作-启用
        """
        element = None
        try:
            element = self.project.get_element(self._list_adv_first_operate_start_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_adv_first_operate_delete_button(self):
        """
        属性: 列表-第一条-操作-删除
        :return: 列表-第一条-操作-删除
        """
        element = None
        try:
            element = self.project.get_element(self._list_adv_first_operate_delete_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def disable_confirm_button(self):
        """
        属性: 确认禁用-确定按钮
        :return: 确认禁用-确定按钮
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
        属性: 确认禁用-取消按钮
        :return: 确认禁用-取消按钮
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

    def set_search_adv_name_input_action(self, search_adv_name_input):
        """
        动作：设置搜索-广告位名称
        :param search_adv_name_input: 搜索-广告位名称
        :return: 设置'搜索-广告位名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_adv_name_input, search_adv_name_input)
        return self.project.get_current_page_source()

    def click_search_query_button_action(self):
        """
        动作：点击搜索-查询按钮
        :return: 点击'搜索-查询按钮'按钮后的页面
        """
        self.project.click(self.search_query_button)
        return self.project.get_current_page_source()

    def click_add_adv_place_button_action(self):
        """
        动作：点击添加广告位按钮
        :return: 点击'添加广告位按钮'按钮后的页面
        """
        self.project.click(self.add_adv_place_button)
        return self.project.get_current_page_source()

    def click_add_adv_button_action(self):
        """
        动作：点击添加广告
        :return: 点击'添加广告'按钮后的页面
        """
        self.project.click(self.add_adv_button)
        return self.project.get_current_page_source()

    def get_list_adv_first_id_text_action(self):
        """
        动作：获取列表-第一条-广告ID的文本
        :return: '列表-第一条-广告ID'的文本
        """
        control_content = self.project.get_element_text(self.list_adv_first_id_text)
        return control_content

    def get_list_adv_first_name_text_action(self):
        """
        动作：获取列表-第一条-名称的文本
        :return: '列表-第一条-名称'的文本
        """
        control_content = self.project.get_element_text(self.list_adv_first_name_text)
        return control_content

    def get_list_adv_first_type_text_action(self):
        """
        动作：获取列表-第一条-广告位类型的文本
        :return: '列表-第一条-广告位类型'的文本
        """
        control_content = self.project.get_element_text(self.list_adv_first_type_text)
        return control_content

    def get_list_adv_first_status_text_action(self):
        """
        动作：获取列表-第一条-状态的文本
        :return: '列表-第一条-状态'的文本
        """
        control_content = self.project.get_element_text(self.list_adv_first_status_text)
        return control_content

    def get_list_adv_first_authority_text_action(self):
        """
        动作：获取列表-第一条-所有权的文本
        :return: '列表-第一条-所有权'的文本
        """
        control_content = self.project.get_element_text(self.list_adv_first_authority_text)
        return control_content

    def get_list_adv_first_mode_text_action(self):
        """
        动作：获取列表-第一条-位置类型的文本
        :return: '列表-第一条-位置类型'的文本
        """
        control_content = self.project.get_element_text(self.list_adv_first_mode_text)
        return control_content

    def get_list_adv_first_channel_text_action(self):
        """
        动作：获取列表-第一条-频道的文本
        :return: '列表-第一条-频道'的文本
        """
        control_content = self.project.get_element_text(self.list_adv_first_channel_text)
        return control_content

    def get_list_adv_first_source_text_action(self):
        """
        动作：获取列表-第一条-渠道的文本
        :return: '列表-第一条-渠道'的文本
        """
        control_content = self.project.get_element_text(self.list_adv_first_source_text)
        return control_content

    def get_list_adv_first_operate_text_action(self):
        """
        动作：获取列表-第一条-操作的文本
        :return: '列表-第一条-操作'的文本
        """
        control_content = self.project.get_element_text(self.list_adv_first_operate_text)
        return control_content

    def click_list_adv_first_operate_forbidden_button_action(self):
        """
        动作：点击列表-第一条-操作-禁用
        :return: 点击'列表-第一条-操作-禁用'按钮后的页面
        """
        self.project.click(self.list_adv_first_operate_forbidden_button)
        return self.project.get_current_page_source()

    def click_list_adv_first_operate_start_button_action(self):
        """
        动作：点击列表-第一条-操作-启用
        :return: 点击'列表-第一条-操作-启用'按钮后的页面
        """
        self.project.click(self.list_adv_first_operate_start_button)
        return self.project.get_current_page_source()

    def click_list_adv_first_operate_delete_button_action(self):
        """
        动作：点击列表-第一条-操作-删除
        :return: 点击'列表-第一条-操作-删除'按钮后的页面
        """
        self.project.click(self.list_adv_first_operate_delete_button)
        return self.project.get_current_page_source()

    def click_disable_confirm_button_action(self):
        """
        动作：点击确认禁用-确定按钮
        :return: 点击'确认禁用-确定按钮'按钮后的页面
        """
        self.project.click(self.disable_confirm_button)
        return self.project.get_current_page_source()

    def click_disable_cancel_button_action(self):
        """
        动作：点击确认禁用-取消按钮
        :return: 点击'确认禁用-取消按钮'按钮后的页面
        """
        self.project.click(self.disable_cancel_button)
        return self.project.get_current_page_source()

    # endregion Actions
