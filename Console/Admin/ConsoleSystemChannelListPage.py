from Utils.Log import log

"""
后台-基础维护-系统管理-频道管理
console_url/system/channel-list
"""


class ConsoleSystemChannelListPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/system/channel-list'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 搜索-频道名称
        self._search_channel_name_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[1]/div/div/input'
        # 搜索-查询按钮
        self._search_query_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[2]/div/button'
        # 搜索-清除按钮
        self._search_clear_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[3]/div/button'
        # 频道添加按钮
        self._channel_add_button_tag = '//*[@id="tableSearch"]/form/div[2]/div/div/button'
        # 频道添加-频道编码
        self._channel_add_channel_code_input_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[1]/div/div[1]/input'
        # 频道添加-频道名称
        self._channel_add_channel_name_input_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[2]/div/div[1]/input'
        # 频道添加-英文缩写
        self._channel_add_en_abbr_input_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[3]/div/div[1]/input'
        # 频道添加-在首页显示-是
        self._channel_add_is_show_yes_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[4]/div/label[1]'
        # 频道添加-在首页显示-否
        self._channel_add_is_show_no_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[4]/div/label[2]'
        # 频道添加-是否启用-是
        self._channel_add_is_enable_yes_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[5]/div/label[1]'
        # 频道添加-是否启用-否
        self._channel_add_is_enable_no_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[5]/div/label[2]'
        # 频道添加-是否显示资源-是
        self._channel_add_is_show_source_yes_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[6]/div/label[1]'
        # 频道添加-是否显示资源-否
        self._channel_add_is_show_source_no_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[6]/div/label[2]'
        # 频道添加-显示颜色
        self._channel_add_color_input_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[7]/div/div[1]/input'
        # 频道添加-排序
        self._channel_add_sort_input_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[8]/div/div[1]/input'
        # 频道添加-楼层名称
        self._channel_add_floor_name_input_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[9]/div/div[1]/input'
        # 频道添加-是否可配置楼层-是
        self._channel_add_is_config_floor_yes_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[10]/div/label[1]'
        # 频道添加-是否可配置楼层-否
        self._channel_add_is_config_floor_no_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[10]/div/label[2]'
        # 频道添加-频道描述
        self._channel_add_description_input_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[11]/div/div/textarea'
        # 频道添加-频道描述字数统计
        self._channel_add_channel_description_input_count_text_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[11]/div/div/span'
        # 频道添加-确定按钮
        self._channel_add_confirm_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[3]/span/button[2]'
        # 频道添加-取消按钮
        self._channel_add_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[3]/span/button[1]'
        # 频道添加-关闭按钮
        self._channel_add_close_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[1]/button'
        # 列表-第一个频道-ID
        self._list_first_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 列表-第一个频道-频道编码
        self._list_first_channel_code_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 列表-第一个频道-频道名称
        self._list_first_channel_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 列表-第一个频道-英文缩写
        self._list_first_en_addr_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 列表-第一个频道-创建时间
        self._list_first_created_at_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 列表-第一个频道-是否在首页显示
        self._list_first_is_show_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div'
        # 列表-第一个频道-排序-向上
        self._list_first_sort_up_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/i[1]'
        # 列表-第一个频道-排序-向下
        self._list_first_sort_down_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/i[2]'
        # 列表-第一个频道-操作-编辑按钮
        self._list_first_edit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/a[1]'
        # 列表-第一个频道-操作-删除按钮
        self._list_first_delete_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/a[2]'
        # 列表-第一个频道-操作-删除-确定按钮
        self._list_first_delete_confirm_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # 列表-第一个频道-操作-删除-取消按钮
        self._list_first_delete_cancel_button_tag = '/html/body/div[2]/div/div[3]/button[1]'
        # 列表-第一个频道-操作-删除-关闭按钮
        self._list_first_delete_close_button_tag = '/html/body/div[2]/div/div[1]/button/i'
        # 频道编辑-频道编码
        self._channel_edit_channel_code_input_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[1]/div/div/input'
        # 频道编辑-频道名称
        self._channel_edit_channel_name_input_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[2]/div/div/input'
        # 频道编辑-英文缩写
        self._channel_edit_en_addr_input_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[3]/div/div/input'
        # 频道编辑-在首页显示-是
        self._channel_edit_is_show_yes_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[4]/div/label[1]'
        # 频道编辑-在首页显示-否
        self._channel_edit_is_show_no_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[4]/div/label[2]'
        # 频道编辑-是否启用-是
        self._channel_edit_is_enable_yes_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[5]/div/label[1]'
        # 频道编辑-是否启用-否
        self._channel_edit_is_enable_no_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[5]/div/label[2]'
        # 频道编辑-是否显示资源-是
        self._channel_edit_is_show_source_yes_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[6]/div/label[1]'
        # 频道编辑-是否显示资源-否
        self._channel_edit_is_show_source_no_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[6]/div/label[2]'
        # 频道编辑-显示颜色
        self._channel_edit_color_input_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[7]/div/div/input'
        # 频道编辑-排序
        self._channel_edit_sort_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[8]/div/div/input'
        # 频道编辑-楼层名称
        self._channel_edit_floor_name_input_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[9]/div/div/input'
        # 频道编辑-是否可配置楼层-是
        self._channel_edit_is_config_floor_yes_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[10]/div/label[1]'
        # 频道编辑-是否可配置楼层-否
        self._channel_edit_is_config_floor_no_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[10]/div/label[2]'
        # 频道编辑-频道描述
        self._channel_edit_channel_description_input_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[11]/div/div/textarea'
        # 频道编辑-确定按钮
        self._channel_edit_confirm_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[3]/span/button[2]'
        # 频道编辑-取消按钮
        self._channel_edit_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[3]/span/button[1]'
        # 频道编辑-关闭按钮
        self._channel_edit_close_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[1]/button/i'
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
    def search_channel_name_input(self):
        """
        属性: 搜索-频道名称
        :return: 搜索-频道名称
        """
        element = None
        try:
            element = self.project.get_element(self._search_channel_name_input_tag)
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
    def search_clear_button(self):
        """
        属性: 搜索-清除按钮
        :return: 搜索-清除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_button(self):
        """
        属性: 频道添加按钮
        :return: 频道添加按钮
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_channel_code_input(self):
        """
        属性: 频道添加-频道编码
        :return: 频道添加-频道编码
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_channel_code_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_channel_name_input(self):
        """
        属性: 频道添加-频道名称
        :return: 频道添加-频道名称
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_channel_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_en_abbr_input(self):
        """
        属性: 频道添加-英文缩写
        :return: 频道添加-英文缩写
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_en_abbr_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_is_show_yes_button(self):
        """
        属性: 频道添加-在首页显示-是
        :return: 频道添加-在首页显示-是
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_is_show_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_is_show_no_button(self):
        """
        属性: 频道添加-在首页显示-否
        :return: 频道添加-在首页显示-否
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_is_show_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_is_enable_yes_button(self):
        """
        属性: 频道添加-是否启用-是
        :return: 频道添加-是否启用-是
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_is_enable_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_is_enable_no_button(self):
        """
        属性: 频道添加-是否启用-否
        :return: 频道添加-是否启用-否
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_is_enable_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_is_show_source_yes_button(self):
        """
        属性: 频道添加-是否显示资源-是
        :return: 频道添加-是否显示资源-是
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_is_show_source_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_is_show_source_no_button(self):
        """
        属性: 频道添加-是否显示资源-否
        :return: 频道添加-是否显示资源-否
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_is_show_source_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_color_input(self):
        """
        属性: 频道添加-显示颜色
        :return: 频道添加-显示颜色
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_color_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_sort_input(self):
        """
        属性: 频道添加-排序
        :return: 频道添加-排序
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_sort_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_floor_name_input(self):
        """
        属性: 频道添加-楼层名称
        :return: 频道添加-楼层名称
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_floor_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_is_config_floor_yes_button(self):
        """
        属性: 频道添加-是否可配置楼层-是
        :return: 频道添加-是否可配置楼层-是
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_is_config_floor_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_is_config_floor_no_button(self):
        """
        属性: 频道添加-是否可配置楼层-否
        :return: 频道添加-是否可配置楼层-否
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_is_config_floor_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_description_input(self):
        """
        属性: 频道添加-频道描述
        :return: 频道添加-频道描述
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_description_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_channel_description_input_count_text(self):
        """
        属性: 频道添加-频道描述字数统计
        :return: 频道添加-频道描述字数统计
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_channel_description_input_count_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_confirm_button(self):
        """
        属性: 频道添加-确定按钮
        :return: 频道添加-确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_cancel_button(self):
        """
        属性: 频道添加-取消按钮
        :return: 频道添加-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_add_close_button(self):
        """
        属性: 频道添加-关闭按钮
        :return: 频道添加-关闭按钮
        """
        element = None
        try:
            element = self.project.get_element(self._channel_add_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_id_text(self):
        """
        属性: 列表-第一个频道-ID
        :return: 列表-第一个频道-ID
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_channel_code_text(self):
        """
        属性: 列表-第一个频道-频道编码
        :return: 列表-第一个频道-频道编码
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_channel_code_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_channel_name_text(self):
        """
        属性: 列表-第一个频道-频道名称
        :return: 列表-第一个频道-频道名称
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_channel_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_en_addr_text(self):
        """
        属性: 列表-第一个频道-英文缩写
        :return: 列表-第一个频道-英文缩写
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_en_addr_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_created_at_text(self):
        """
        属性: 列表-第一个频道-创建时间
        :return: 列表-第一个频道-创建时间
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_created_at_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_is_show_text(self):
        """
        属性: 列表-第一个频道-是否在首页显示
        :return: 列表-第一个频道-是否在首页显示
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_is_show_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_sort_up_button(self):
        """
        属性: 列表-第一个频道-排序-向上
        :return: 列表-第一个频道-排序-向上
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_sort_up_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_sort_down_button(self):
        """
        属性: 列表-第一个频道-排序-向下
        :return: 列表-第一个频道-排序-向下
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_sort_down_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_edit_button(self):
        """
        属性: 列表-第一个频道-操作-编辑按钮
        :return: 列表-第一个频道-操作-编辑按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_edit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_delete_button(self):
        """
        属性: 列表-第一个频道-操作-删除按钮
        :return: 列表-第一个频道-操作-删除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_delete_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_delete_confirm_button(self):
        """
        属性: 列表-第一个频道-操作-删除-确定按钮
        :return: 列表-第一个频道-操作-删除-确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_delete_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_delete_cancel_button(self):
        """
        属性: 列表-第一个频道-操作-删除-取消按钮
        :return: 列表-第一个频道-操作-删除-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_delete_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_delete_close_button(self):
        """
        属性: 列表-第一个频道-操作-删除-关闭按钮
        :return: 列表-第一个频道-操作-删除-关闭按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_delete_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_channel_code_input(self):
        """
        属性: 频道编辑-频道编码
        :return: 频道编辑-频道编码
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_channel_code_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_channel_name_input(self):
        """
        属性: 频道编辑-频道名称
        :return: 频道编辑-频道名称
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_channel_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_en_addr_input(self):
        """
        属性: 频道编辑-英文缩写
        :return: 频道编辑-英文缩写
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_en_addr_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_is_show_yes_button(self):
        """
        属性: 频道编辑-在首页显示-是
        :return: 频道编辑-在首页显示-是
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_is_show_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_is_show_no_button(self):
        """
        属性: 频道编辑-在首页显示-否
        :return: 频道编辑-在首页显示-否
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_is_show_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_is_enable_yes_button(self):
        """
        属性: 频道编辑-是否启用-是
        :return: 频道编辑-是否启用-是
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_is_enable_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_is_enable_no_button(self):
        """
        属性: 频道编辑-是否启用-否
        :return: 频道编辑-是否启用-否
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_is_enable_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_is_show_source_yes_button(self):
        """
        属性: 频道编辑-是否显示资源-是
        :return: 频道编辑-是否显示资源-是
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_is_show_source_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_is_show_source_no_button(self):
        """
        属性: 频道编辑-是否显示资源-否
        :return: 频道编辑-是否显示资源-否
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_is_show_source_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_color_input(self):
        """
        属性: 频道编辑-显示颜色
        :return: 频道编辑-显示颜色
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_color_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_sort(self):
        """
        属性: 频道编辑-排序
        :return: 频道编辑-排序
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_sort_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_floor_name_input(self):
        """
        属性: 频道编辑-楼层名称
        :return: 频道编辑-楼层名称
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_floor_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_is_config_floor_yes_button(self):
        """
        属性: 频道编辑-是否可配置楼层-是
        :return: 频道编辑-是否可配置楼层-是
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_is_config_floor_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_is_config_floor_no_button(self):
        """
        属性: 频道编辑-是否可配置楼层-否
        :return: 频道编辑-是否可配置楼层-否
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_is_config_floor_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_channel_description_input(self):
        """
        属性: 频道编辑-频道描述
        :return: 频道编辑-频道描述
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_channel_description_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_confirm_button(self):
        """
        属性: 频道编辑-确定按钮
        :return: 频道编辑-确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_cancel_button(self):
        """
        属性: 频道编辑-取消按钮
        :return: 频道编辑-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def channel_edit_close_button(self):
        """
        属性: 频道编辑-关闭按钮
        :return: 频道编辑-关闭按钮
        """
        element = None
        try:
            element = self.project.get_element(self._channel_edit_close_button_tag)
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

    def set_search_channel_name_input_action(self, search_channel_name_input):
        """
        动作：设置搜索-频道名称
        :param search_channel_name_input: 搜索-频道名称
        :return: 设置'搜索-频道名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_channel_name_input, search_channel_name_input)
        return self.project.get_current_page_source()

    def click_search_query_button_action(self):
        """
        动作：点击搜索-查询按钮
        :return: 点击'搜索-查询按钮'按钮后的页面
        """
        self.project.click(self.search_query_button)
        return self.project.get_current_page_source()

    def click_search_clear_button_action(self):
        """
        动作：点击搜索-清除按钮
        :return: 点击'搜索-清除按钮'按钮后的页面
        """
        self.project.click(self.search_clear_button)
        return self.project.get_current_page_source()

    def click_channel_add_button_action(self):
        """
        动作：点击频道添加按钮
        :return: 点击'频道添加按钮'按钮后的页面
        """
        self.project.click(self.channel_add_button)
        return self.project.get_current_page_source()

    def set_channel_add_channel_code_input_action(self, channel_add_channel_code_input):
        """
        动作：设置频道添加-频道编码
        :param channel_add_channel_code_input: 频道添加-频道编码
        :return: 设置'频道添加-频道编码'文本后的页面
        """
        self.project.clear_and_send_keys(self.channel_add_channel_code_input, channel_add_channel_code_input)
        return self.project.get_current_page_source()

    def set_channel_add_channel_name_input_action(self, channel_add_channel_name_input):
        """
        动作：设置频道添加-频道名称
        :param channel_add_channel_name_input: 频道添加-频道名称
        :return: 设置'频道添加-频道名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.channel_add_channel_name_input, channel_add_channel_name_input)
        return self.project.get_current_page_source()

    def set_channel_add_en_abbr_input_action(self, channel_add_en_abbr_input):
        """
        动作：设置频道添加-英文缩写
        :param channel_add_en_abbr_input: 频道添加-英文缩写
        :return: 设置'频道添加-英文缩写'文本后的页面
        """
        self.project.clear_and_send_keys(self.channel_add_en_abbr_input, channel_add_en_abbr_input)
        return self.project.get_current_page_source()

    def click_channel_add_is_show_yes_button_action(self):
        """
        动作：点击频道添加-在首页显示-是
        :return: 点击'频道添加-在首页显示-是'按钮后的页面
        """
        self.project.click(self.channel_add_is_show_yes_button)
        return self.project.get_current_page_source()

    def click_channel_add_is_show_no_button_action(self):
        """
        动作：点击频道添加-在首页显示-否
        :return: 点击'频道添加-在首页显示-否'按钮后的页面
        """
        self.project.click(self.channel_add_is_show_no_button)
        return self.project.get_current_page_source()

    def click_channel_add_is_enable_yes_button_action(self):
        """
        动作：点击频道添加-是否启用-是
        :return: 点击'频道添加-是否启用-是'按钮后的页面
        """
        self.project.click(self.channel_add_is_enable_yes_button)
        return self.project.get_current_page_source()

    def click_channel_add_is_enable_no_button_action(self):
        """
        动作：点击频道添加-是否启用-否
        :return: 点击'频道添加-是否启用-否'按钮后的页面
        """
        self.project.click(self.channel_add_is_enable_no_button)
        return self.project.get_current_page_source()

    def click_channel_add_is_show_source_yes_button_action(self):
        """
        动作：点击频道添加-是否显示资源-是
        :return: 点击'频道添加-是否显示资源-是'按钮后的页面
        """
        self.project.click(self.channel_add_is_show_source_yes_button)
        return self.project.get_current_page_source()

    def click_channel_add_is_show_source_no_button_action(self):
        """
        动作：点击频道添加-是否显示资源-否
        :return: 点击'频道添加-是否显示资源-否'按钮后的页面
        """
        self.project.click(self.channel_add_is_show_source_no_button)
        return self.project.get_current_page_source()

    def set_channel_add_color_input_action(self, channel_add_color_input):
        """
        动作：设置频道添加-显示颜色
        :param channel_add_color_input: 频道添加-显示颜色
        :return: 设置'频道添加-显示颜色'文本后的页面
        """
        self.project.clear_and_send_keys(self.channel_add_color_input, channel_add_color_input)
        return self.project.get_current_page_source()

    def set_channel_add_sort_input_action(self, channel_add_sort_input):
        """
        动作：设置频道添加-排序
        :param channel_add_sort_input: 频道添加-排序
        :return: 设置'频道添加-排序'文本后的页面
        """
        self.project.clear_and_send_keys(self.channel_add_sort_input, channel_add_sort_input)
        return self.project.get_current_page_source()

    def set_channel_add_floor_name_input_action(self, channel_add_floor_name_input):
        """
        动作：设置频道添加-楼层名称
        :param channel_add_floor_name_input: 频道添加-楼层名称
        :return: 设置'频道添加-楼层名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.channel_add_floor_name_input, channel_add_floor_name_input)
        return self.project.get_current_page_source()

    def click_channel_add_is_config_floor_yes_button_action(self):
        """
        动作：点击频道添加-是否可配置楼层-是
        :return: 点击'频道添加-是否可配置楼层-是'按钮后的页面
        """
        self.project.click(self.channel_add_is_config_floor_yes_button)
        return self.project.get_current_page_source()

    def click_channel_add_is_config_floor_no_button_action(self):
        """
        动作：点击频道添加-是否可配置楼层-否
        :return: 点击'频道添加-是否可配置楼层-否'按钮后的页面
        """
        self.project.click(self.channel_add_is_config_floor_no_button)
        return self.project.get_current_page_source()

    def set_channel_add_description_input_action(self, channel_add_description_input):
        """
        动作：设置频道添加-频道描述
        :param channel_add_description_input: 频道添加-频道描述
        :return: 设置'频道添加-频道描述'文本后的页面
        """
        self.project.clear_and_send_keys(self.channel_add_description_input, channel_add_description_input)
        return self.project.get_current_page_source()

    def get_channel_add_channel_description_input_count_text_action(self):
        """
        动作：获取频道添加-频道描述字数统计的文本
        :return: '频道添加-频道描述字数统计'的文本
        """
        control_content = self.project.get_element_text(self.channel_add_channel_description_input_count_text)
        return control_content

    def click_channel_add_confirm_button_action(self):
        """
        动作：点击频道添加-确定按钮
        :return: 点击'频道添加-确定按钮'按钮后的页面
        """
        self.project.click(self.channel_add_confirm_button)
        return self.project.get_current_page_source()

    def click_channel_add_cancel_button_action(self):
        """
        动作：点击频道添加-取消按钮
        :return: 点击'频道添加-取消按钮'按钮后的页面
        """
        self.project.click(self.channel_add_cancel_button)
        return self.project.get_current_page_source()

    def click_channel_add_close_button_action(self):
        """
        动作：点击频道添加-关闭按钮
        :return: 点击'频道添加-关闭按钮'按钮后的页面
        """
        self.project.click(self.channel_add_close_button)
        return self.project.get_current_page_source()

    def get_list_first_id_text_action(self):
        """
        动作：获取列表-第一个频道-ID的文本
        :return: '列表-第一个频道-ID'的文本
        """
        control_content = self.project.get_element_text(self.list_first_id_text)
        return control_content

    def get_list_first_channel_code_text_action(self):
        """
        动作：获取列表-第一个频道-频道编码的文本
        :return: '列表-第一个频道-频道编码'的文本
        """
        control_content = self.project.get_element_text(self.list_first_channel_code_text)
        return control_content

    def get_list_first_channel_name_text_action(self):
        """
        动作：获取列表-第一个频道-频道名称的文本
        :return: '列表-第一个频道-频道名称'的文本
        """
        control_content = self.project.get_element_text(self.list_first_channel_name_text)
        return control_content

    def get_list_first_en_addr_text_action(self):
        """
        动作：获取列表-第一个频道-英文缩写的文本
        :return: '列表-第一个频道-英文缩写'的文本
        """
        control_content = self.project.get_element_text(self.list_first_en_addr_text)
        return control_content

    def get_list_first_created_at_text_action(self):
        """
        动作：获取列表-第一个频道-创建时间的文本
        :return: '列表-第一个频道-创建时间'的文本
        """
        control_content = self.project.get_element_text(self.list_first_created_at_text)
        return control_content

    def get_list_first_is_show_text_action(self):
        """
        动作：获取列表-第一个频道-是否在首页显示的文本
        :return: '列表-第一个频道-是否在首页显示'的文本
        """
        control_content = self.project.get_element_text(self.list_first_is_show_text)
        return control_content

    def click_list_first_sort_up_button_action(self):
        """
        动作：点击列表-第一个频道-排序-向上
        :return: 点击'列表-第一个频道-排序-向上'按钮后的页面
        """
        self.project.click(self.list_first_sort_up_button)
        return self.project.get_current_page_source()

    def click_list_first_sort_down_button_action(self):
        """
        动作：点击列表-第一个频道-排序-向下
        :return: 点击'列表-第一个频道-排序-向下'按钮后的页面
        """
        self.project.click(self.list_first_sort_down_button)
        return self.project.get_current_page_source()

    def click_list_first_edit_button_action(self):
        """
        动作：点击列表-第一个频道-操作-编辑按钮
        :return: 点击'列表-第一个频道-操作-编辑按钮'按钮后的页面
        """
        self.project.click(self.list_first_edit_button)
        return self.project.get_current_page_source()

    def click_list_first_delete_button_action(self):
        """
        动作：点击列表-第一个频道-操作-删除按钮
        :return: 点击'列表-第一个频道-操作-删除按钮'按钮后的页面
        """
        self.project.click(self.list_first_delete_button)
        return self.project.get_current_page_source()

    def click_list_first_delete_confirm_button_action(self):
        """
        动作：点击列表-第一个频道-操作-删除-确定按钮
        :return: 点击'列表-第一个频道-操作-删除-确定按钮'按钮后的页面
        """
        self.project.click(self.list_first_delete_confirm_button)
        return self.project.get_current_page_source()

    def click_list_first_delete_cancel_button_action(self):
        """
        动作：点击列表-第一个频道-操作-删除-取消按钮
        :return: 点击'列表-第一个频道-操作-删除-取消按钮'按钮后的页面
        """
        self.project.click(self.list_first_delete_cancel_button)
        return self.project.get_current_page_source()

    def click_list_first_delete_close_button_action(self):
        """
        动作：点击列表-第一个频道-操作-删除-关闭按钮
        :return: 点击'列表-第一个频道-操作-删除-关闭按钮'按钮后的页面
        """
        self.project.click(self.list_first_delete_close_button)
        return self.project.get_current_page_source()

    def set_channel_edit_channel_code_input_action(self, channel_edit_channel_code_input):
        """
        动作：设置频道编辑-频道编码
        :param channel_edit_channel_code_input: 频道编辑-频道编码
        :return: 设置'频道编辑-频道编码'文本后的页面
        """
        self.project.clear_and_send_keys(self.channel_edit_channel_code_input, channel_edit_channel_code_input)
        return self.project.get_current_page_source()

    def set_channel_edit_channel_name_input_action(self, channel_edit_channel_name_input):
        """
        动作：设置频道编辑-频道名称
        :param channel_edit_channel_name_input: 频道编辑-频道名称
        :return: 设置'频道编辑-频道名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.channel_edit_channel_name_input, channel_edit_channel_name_input)
        return self.project.get_current_page_source()

    def set_channel_edit_en_addr_input_action(self, channel_edit_en_addr_input):
        """
        动作：设置频道编辑-英文缩写
        :param channel_edit_en_addr_input: 频道编辑-英文缩写
        :return: 设置'频道编辑-英文缩写'文本后的页面
        """
        self.project.clear_and_send_keys(self.channel_edit_en_addr_input, channel_edit_en_addr_input)
        return self.project.get_current_page_source()

    def click_channel_edit_is_show_yes_button_action(self):
        """
        动作：点击频道编辑-在首页显示-是
        :return: 点击'频道编辑-在首页显示-是'按钮后的页面
        """
        self.project.click(self.channel_edit_is_show_yes_button)
        return self.project.get_current_page_source()

    def click_channel_edit_is_show_no_button_action(self):
        """
        动作：点击频道编辑-在首页显示-否
        :return: 点击'频道编辑-在首页显示-否'按钮后的页面
        """
        self.project.click(self.channel_edit_is_show_no_button)
        return self.project.get_current_page_source()

    def click_channel_edit_is_enable_yes_button_action(self):
        """
        动作：点击频道编辑-是否启用-是
        :return: 点击'频道编辑-是否启用-是'按钮后的页面
        """
        self.project.click(self.channel_edit_is_enable_yes_button)
        return self.project.get_current_page_source()

    def click_channel_edit_is_enable_no_button_action(self):
        """
        动作：点击频道编辑-是否启用-否
        :return: 点击'频道编辑-是否启用-否'按钮后的页面
        """
        self.project.click(self.channel_edit_is_enable_no_button)
        return self.project.get_current_page_source()

    def click_channel_edit_is_show_source_yes_button_action(self):
        """
        动作：点击频道编辑-是否显示资源-是
        :return: 点击'频道编辑-是否显示资源-是'按钮后的页面
        """
        self.project.click(self.channel_edit_is_show_source_yes_button)
        return self.project.get_current_page_source()

    def click_channel_edit_is_show_source_no_button_action(self):
        """
        动作：点击频道编辑-是否显示资源-否
        :return: 点击'频道编辑-是否显示资源-否'按钮后的页面
        """
        self.project.click(self.channel_edit_is_show_source_no_button)
        return self.project.get_current_page_source()

    def set_channel_edit_color_input_action(self, channel_edit_color_input):
        """
        动作：设置频道编辑-显示颜色
        :param channel_edit_color_input: 频道编辑-显示颜色
        :return: 设置'频道编辑-显示颜色'文本后的页面
        """
        self.project.clear_and_send_keys(self.channel_edit_color_input, channel_edit_color_input)
        return self.project.get_current_page_source()

    def set_channel_edit_floor_name_input_action(self, channel_edit_floor_name_input):
        """
        动作：设置频道编辑-楼层名称
        :param channel_edit_floor_name_input: 频道编辑-楼层名称
        :return: 设置'频道编辑-楼层名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.channel_edit_floor_name_input, channel_edit_floor_name_input)
        return self.project.get_current_page_source()

    def click_channel_edit_is_config_floor_yes_button_action(self):
        """
        动作：点击频道编辑-是否可配置楼层-是
        :return: 点击'频道编辑-是否可配置楼层-是'按钮后的页面
        """
        self.project.click(self.channel_edit_is_config_floor_yes_button)
        return self.project.get_current_page_source()

    def click_channel_edit_is_config_floor_no_button_action(self):
        """
        动作：点击频道编辑-是否可配置楼层-否
        :return: 点击'频道编辑-是否可配置楼层-否'按钮后的页面
        """
        self.project.click(self.channel_edit_is_config_floor_no_button)
        return self.project.get_current_page_source()

    def set_channel_edit_channel_description_input_action(self, channel_edit_channel_description_input):
        """
        动作：设置频道编辑-频道描述
        :param channel_edit_channel_description_input: 频道编辑-频道描述
        :return: 设置'频道编辑-频道描述'文本后的页面
        """
        self.project.clear_and_send_keys(self.channel_edit_channel_description_input, channel_edit_channel_description_input)
        return self.project.get_current_page_source()

    def click_channel_edit_confirm_button_action(self):
        """
        动作：点击频道编辑-确定按钮
        :return: 点击'频道编辑-确定按钮'按钮后的页面
        """
        self.project.click(self.channel_edit_confirm_button)
        return self.project.get_current_page_source()

    def click_channel_edit_cancel_button_action(self):
        """
        动作：点击频道编辑-取消按钮
        :return: 点击'频道编辑-取消按钮'按钮后的页面
        """
        self.project.click(self.channel_edit_cancel_button)
        return self.project.get_current_page_source()

    def click_channel_edit_close_button_action(self):
        """
        动作：点击频道编辑-关闭按钮
        :return: 点击'频道编辑-关闭按钮'按钮后的页面
        """
        self.project.click(self.channel_edit_close_button)
        return self.project.get_current_page_source()

    # endregion Actions
