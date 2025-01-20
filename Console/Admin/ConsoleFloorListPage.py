from Utils.Log import log

"""
后台-运营中心-楼层栏目管理-楼层栏目管理
console_url/floor/list
"""


class ConsoleFloorListPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/floor/list'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 下拉列表
        self._drop_down_list_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 搜索-楼层栏目ID
        self._search_floor_column_id_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[1]/div/div/input'
        # 搜索-楼层栏目名称
        self._search_floor_column_name_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[2]/div/div/input'
        # 搜索-所属楼层
        self._search_floor_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[3]/div/div/div'
        # 搜索-查询按钮
        self._search_query_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[6]/div/button'
        # 搜索-清除按钮
        self._search_clear_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[7]/div/button'
        # 列表-第一个-楼层栏目ID
        self._list_first_floor_column_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div'
        # 列表-第一个-楼层栏目名称
        self._list_first_floor_column_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 列表-第一个-所属楼层
        self._list_first_floor_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 列表-第一个-地域
        self._list_first_address_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 列表-第一个-创建时间
        self._list_first_create_time_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 列表-第一个-当前状态
        self._list_first_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 列表-第一个-操作-编辑按钮
        self._list_first_edit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[7]/div/a[1]'
        # 列表-第一个-禁用/启用按钮
        self._list_first_is_enable_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[7]/div/a[2]'
        # 楼层栏目创建按钮
        self._floor_column_create_button_tag = '//*[@id="tableSearch"]/form/div[2]/div[1]/div/button'
        # 楼层栏目创建-所属楼层
        self._floor_column_create_floor_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[1]/div/div/div/div/div[1]'
        # 楼层栏目创建-地域
        self._floor_column_create_address_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[2]/div/div/div/div/div'
        # 楼层栏目创建-楼层栏目名称
        self._floor_column_create_floor_column_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[3]/div/div/div/div[1]/input'
        # 楼层栏目创建-保存按钮
        self._floor_column_create_save_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[3]/span/button[1]'
        # 楼层栏目创建-取消按钮
        self._floor_column_create_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[3]/span/button[2]'
        # 楼层栏目编辑-楼层栏目名称
        self._floor_column_edit_floor_column_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div[3]/div/div/div/div/input'
        # 楼层栏目编辑-保存按钮
        self._floor_column_edit_save_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[3]/span/button[1]'
        # 楼层栏目编辑-取消按钮
        self._floor_column_edit_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[3]/span/button[2]'
        # 确认禁用-确定
        self._disable_confirm_button_tag = '/html/body/div[last()-1]/div/div[3]/button[2]'
        # 确认禁用-取消
        self._disable_cancel_button_tag = '/html/body/div[last()-1]/div/div[3]/button[1]'
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
    def drop_down_list_select(self):
        """
        属性: 下拉列表
        :return: 下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._drop_down_list_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_floor_column_id_input(self):
        """
        属性: 搜索-楼层栏目ID
        :return: 搜索-楼层栏目ID
        """
        element = None
        try:
            element = self.project.get_element(self._search_floor_column_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_floor_column_name_input(self):
        """
        属性: 搜索-楼层栏目名称
        :return: 搜索-楼层栏目名称
        """
        element = None
        try:
            element = self.project.get_element(self._search_floor_column_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_floor_button(self):
        """
        属性: 搜索-所属楼层
        :return: 搜索-所属楼层
        """
        element = None
        try:
            element = self.project.get_element(self._search_floor_button_tag)
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
    def list_first_floor_column_id_text(self):
        """
        属性: 列表-第一个-楼层栏目ID
        :return: 列表-第一个-楼层栏目ID
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_floor_column_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_floor_column_name_text(self):
        """
        属性: 列表-第一个-楼层栏目名称
        :return: 列表-第一个-楼层栏目名称
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_floor_column_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_floor_name_text(self):
        """
        属性: 列表-第一个-所属楼层
        :return: 列表-第一个-所属楼层
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_floor_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_address_text(self):
        """
        属性: 列表-第一个-地域
        :return: 列表-第一个-地域
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_address_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_create_time_text(self):
        """
        属性: 列表-第一个-创建时间
        :return: 列表-第一个-创建时间
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_create_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_state_text(self):
        """
        属性: 列表-第一个-当前状态
        :return: 列表-第一个-当前状态
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_edit_button(self):
        """
        属性: 列表-第一个-操作-编辑按钮
        :return: 列表-第一个-操作-编辑按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_edit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_is_enable_button(self):
        """
        属性: 列表-第一个-禁用/启用按钮
        :return: 列表-第一个-禁用/启用按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_is_enable_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def floor_column_create_button(self):
        """
        属性: 楼层栏目创建按钮
        :return: 楼层栏目创建按钮
        """
        element = None
        try:
            element = self.project.get_element(self._floor_column_create_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def floor_column_create_floor_button(self):
        """
        属性: 楼层栏目创建-所属楼层
        :return: 楼层栏目创建-所属楼层
        """
        element = None
        try:
            element = self.project.get_element(self._floor_column_create_floor_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def floor_column_create_address_button(self):
        """
        属性: 楼层栏目创建-地域
        :return: 楼层栏目创建-地域
        """
        element = None
        try:
            element = self.project.get_element(self._floor_column_create_address_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def floor_column_create_floor_column_name_input(self):
        """
        属性: 楼层栏目创建-楼层栏目名称
        :return: 楼层栏目创建-楼层栏目名称
        """
        element = None
        try:
            element = self.project.get_element(self._floor_column_create_floor_column_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def floor_column_create_save_button(self):
        """
        属性: 楼层栏目创建-保存按钮
        :return: 楼层栏目创建-保存按钮
        """
        element = None
        try:
            element = self.project.get_element(self._floor_column_create_save_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def floor_column_create_cancel_button(self):
        """
        属性: 楼层栏目创建-取消按钮
        :return: 楼层栏目创建-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._floor_column_create_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def floor_column_edit_floor_column_name_input(self):
        """
        属性: 楼层栏目编辑-楼层栏目名称
        :return: 楼层栏目编辑-楼层栏目名称
        """
        element = None
        try:
            element = self.project.get_element(self._floor_column_edit_floor_column_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def floor_column_edit_save_button(self):
        """
        属性: 楼层栏目编辑-保存按钮
        :return: 楼层栏目编辑-保存按钮
        """
        element = None
        try:
            element = self.project.get_element(self._floor_column_edit_save_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def floor_column_edit_cancel_button(self):
        """
        属性: 楼层栏目编辑-取消按钮
        :return: 楼层栏目编辑-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._floor_column_edit_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def disable_confirm_button(self):
        """
        属性: 确认禁用-确定
        :return: 确认禁用-确定
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
        属性: 确认禁用-取消
        :return: 确认禁用-取消
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

    def get_select_drop_down_list_action(self, drop_down_list_select):
        """
        动作：获取下拉列表列表选中的文本
        :param drop_down_list_select: 下拉列表列表索引或文本
        :return: '下拉列表'的文本
        """
        control_content = self.project.get_select_content(self.drop_down_list_select, drop_down_list_select)
        return control_content

    def select_drop_down_list_action(self, drop_down_list_select):
        """
        动作：选择下拉列表
        :param drop_down_list_select: 下拉列表列表索引或文本
        :return: 选择'下拉列表'选择器后的页面
        """
        self.project.select_control(self.drop_down_list_select, drop_down_list_select)
        return self.project.get_current_page_source()

    def set_search_floor_column_id_input_action(self, search_floor_column_id_input):
        """
        动作：设置搜索-楼层栏目ID
        :param search_floor_column_id_input: 搜索-楼层栏目ID
        :return: 设置'搜索-楼层栏目ID'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_floor_column_id_input, search_floor_column_id_input)
        return self.project.get_current_page_source()

    def set_search_floor_column_name_input_action(self, search_floor_column_name_input):
        """
        动作：设置搜索-楼层栏目名称
        :param search_floor_column_name_input: 搜索-楼层栏目名称
        :return: 设置'搜索-楼层栏目名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_floor_column_name_input, search_floor_column_name_input)
        return self.project.get_current_page_source()

    def click_search_floor_button_action(self):
        """
        动作：点击搜索-所属楼层
        :return: 点击'搜索-所属楼层'按钮后的页面
        """
        self.project.click(self.search_floor_button)
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

    def get_list_first_floor_column_id_text_action(self):
        """
        动作：获取列表-第一个-楼层栏目ID的文本
        :return: '列表-第一个-楼层栏目ID'的文本
        """
        control_content = self.project.get_element_text(self.list_first_floor_column_id_text)
        return control_content

    def get_list_first_floor_column_name_text_action(self):
        """
        动作：获取列表-第一个-楼层栏目名称的文本
        :return: '列表-第一个-楼层栏目名称'的文本
        """
        control_content = self.project.get_element_text(self.list_first_floor_column_name_text)
        return control_content

    def get_list_first_floor_name_text_action(self):
        """
        动作：获取列表-第一个-所属楼层的文本
        :return: '列表-第一个-所属楼层'的文本
        """
        control_content = self.project.get_element_text(self.list_first_floor_name_text)
        return control_content

    def get_list_first_address_text_action(self):
        """
        动作：获取列表-第一个-地域的文本
        :return: '列表-第一个-地域'的文本
        """
        control_content = self.project.get_element_text(self.list_first_address_text)
        return control_content

    def get_list_first_create_time_text_action(self):
        """
        动作：获取列表-第一个-创建时间的文本
        :return: '列表-第一个-创建时间'的文本
        """
        control_content = self.project.get_element_text(self.list_first_create_time_text)
        return control_content

    def get_list_first_state_text_action(self):
        """
        动作：获取列表-第一个-当前状态的文本
        :return: '列表-第一个-当前状态'的文本
        """
        control_content = self.project.get_element_text(self.list_first_state_text)
        return control_content

    def click_list_first_edit_button_action(self):
        """
        动作：点击列表-第一个-操作-编辑按钮
        :return: 点击'列表-第一个-操作-编辑按钮'按钮后的页面
        """
        self.project.click(self.list_first_edit_button)
        return self.project.get_current_page_source()

    def click_list_first_is_enable_button_action(self):
        """
        动作：点击列表-第一个-禁用/启用按钮
        :return: 点击'列表-第一个-禁用/启用按钮'按钮后的页面
        """
        self.project.click(self.list_first_is_enable_button)
        return self.project.get_current_page_source()

    def click_floor_column_create_button_action(self):
        """
        动作：点击楼层栏目创建按钮
        :return: 点击'楼层栏目创建按钮'按钮后的页面
        """
        self.project.click(self.floor_column_create_button)
        return self.project.get_current_page_source()

    def click_floor_column_create_floor_button_action(self):
        """
        动作：点击楼层栏目创建-所属楼层
        :return: 点击'楼层栏目创建-所属楼层'按钮后的页面
        """
        self.project.click(self.floor_column_create_floor_button)
        return self.project.get_current_page_source()

    def click_floor_column_create_address_button_action(self):
        """
        动作：点击楼层栏目创建-地域
        :return: 点击'楼层栏目创建-地域'按钮后的页面
        """
        self.project.click(self.floor_column_create_address_button)
        return self.project.get_current_page_source()

    def set_floor_column_create_floor_column_name_input_action(self, floor_column_create_floor_column_name_input):
        """
        动作：设置楼层栏目创建-楼层栏目名称
        :param floor_column_create_floor_column_name_input: 楼层栏目创建-楼层栏目名称
        :return: 设置'楼层栏目创建-楼层栏目名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.floor_column_create_floor_column_name_input, floor_column_create_floor_column_name_input)
        return self.project.get_current_page_source()

    def click_floor_column_create_save_button_action(self):
        """
        动作：点击楼层栏目创建-保存按钮
        :return: 点击'楼层栏目创建-保存按钮'按钮后的页面
        """
        self.project.click(self.floor_column_create_save_button)
        return self.project.get_current_page_source()

    def click_floor_column_create_cancel_button_action(self):
        """
        动作：点击楼层栏目创建-取消按钮
        :return: 点击'楼层栏目创建-取消按钮'按钮后的页面
        """
        self.project.click(self.floor_column_create_cancel_button)
        return self.project.get_current_page_source()

    def set_floor_column_edit_floor_column_name_input_action(self, floor_column_edit_floor_column_name_input):
        """
        动作：设置楼层栏目编辑-楼层栏目名称
        :param floor_column_edit_floor_column_name_input: 楼层栏目编辑-楼层栏目名称
        :return: 设置'楼层栏目编辑-楼层栏目名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.floor_column_edit_floor_column_name_input, floor_column_edit_floor_column_name_input)
        return self.project.get_current_page_source()

    def click_floor_column_edit_save_button_action(self):
        """
        动作：点击楼层栏目编辑-保存按钮
        :return: 点击'楼层栏目编辑-保存按钮'按钮后的页面
        """
        self.project.click(self.floor_column_edit_save_button)
        return self.project.get_current_page_source()

    def click_floor_column_edit_cancel_button_action(self):
        """
        动作：点击楼层栏目编辑-取消按钮
        :return: 点击'楼层栏目编辑-取消按钮'按钮后的页面
        """
        self.project.click(self.floor_column_edit_cancel_button)
        return self.project.get_current_page_source()

    def click_disable_confirm_button_action(self):
        """
        动作：点击确认禁用-确定
        :return: 点击'确认禁用-确定'按钮后的页面
        """
        self.project.click(self.disable_confirm_button)
        return self.project.get_current_page_source()

    def click_disable_cancel_button_action(self):
        """
        动作：点击确认禁用-取消
        :return: 点击'确认禁用-取消'按钮后的页面
        """
        self.project.click(self.disable_cancel_button)
        return self.project.get_current_page_source()

    # endregion Actions
