from Utils.Log import log

"""
后台-运营中心-推荐位管理-推荐位列表
console_url/recommend/list
"""


class ConsoleRecommendListPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/recommend/list'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 搜索-推荐位ID
        self._search_recommend_id_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[1]/div/div/input'
        # 搜索-推荐位名称
        self._search_recommend_name_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[2]/div/div/input'
        # 搜索-查询按钮
        self._search_query_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[8]/div/button'
        # 搜索-清除按钮
        self._search_clear_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[9]/div/button'
        # 列表-第一个-推荐位ID
        self._list_first_recommend_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div'
        # 列表-第一个-推荐位名称
        self._list_first_recommend_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 列表-第一个-所属渠道
        self._list_first_source_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 列表-第一个-所属楼层
        self._list_first_floor_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 列表-第一个-地域
        self._list_first_address_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 列表-第一个-推荐位类型
        self._list_first_recommend_type_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 列表-第一个-内容展示数
        self._list_first_max_display_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div'
        # 列表-第一个-状态
        self._list_first_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div'
        # 列表-第一个-操作-编辑按钮
        self._list_first_edit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/a[1]'
        # 列表-第一个-操作-禁用/启用按钮
        self._list_first_is_enable_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/a[2]'
        # 确认启用-确定按钮
        self._enable_confirm_button_tag = '/html/body/div[last()-1]/div/div[3]/button[2]'
        # 确认启用-取消按钮
        self._enable_cancel_button_tag = '/html/body/div[last()-1]/div/div[3]/button[1]'
        # 确认禁用-确定按钮
        self._disable_confirm_button_tag = '/html/body/div[last()-1]/div/div[3]/button[2]'
        # 确认禁用-取消按钮
        self._disable_cancel_button_tag = '/html/body/div[last()-1]/div/div[3]/button[1]'
        # 创建推荐位按钮
        self._recommend_create_button_tag = '//*[@id="tableSearch"]/form/div[2]/div/div/button'
        # 创建推荐位-推荐位名称
        self._recommend_create_recommend_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[1]/div[2]/div/div[1]/div/div/div[1]/input'
        # 创建推荐位-所属渠道
        self._recommend_create_source_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[1]/div[2]/div/div[2]/div/div/div/div'
        # 创建推荐位-所属渠道-列表
        self._recommend_create_source_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 创建推荐位-推荐位类型
        self._recommend_create_recommend_type_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[1]/div[1]/div/div/div/div'
        # 创建推荐位-推荐位类型-列表
        self._recommend_create_recommend_type_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 创建推荐位-所属楼层
        self._recommend_create_floor_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[1]/div/div/div/div'
        # 创建推荐位-所属楼层-列表
        self._recommend_create_floor_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 创建推荐位-地域
        self._recommend_create_address_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[2]/div/div/div/div'
        # 创建推荐位-地域-列表
        self._recommend_create_address_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 创建推荐位-楼层栏目名称
        self._recommend_create_floor_column_name_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[3]/div/div/div/div'
        # 创建推荐位-楼层栏目名称-列表
        self._recommend_create_floor_column_name_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 创建推荐位-推荐内容-第一个-排序
        self._recommend_create_recommend_content_first_sort_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[3]/table/tbody/tr[1]/td[1]/div'
        # 创建推荐位-推荐内容-第一个-内容ID
        self._recommend_create_recommend_content_first_content_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[3]/table/tbody/tr[1]/td[2]/div'
        # 创建推荐位-推荐内容-第一个-内容名称
        self._recommend_create_recommend_content_first_content_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[3]/table/tbody/tr[1]/td[3]/div'
        # 创建推荐位-推荐内容-第一个-用户名称
        self._recommend_create_recommend_content_first_user_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[3]/table/tbody/tr[1]/td[4]/div'
        # 创建推荐位-推荐内容-第一个-内容类型
        self._recommend_create_recommend_content_first_content_type_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[3]/table/tbody/tr[1]/td[5]/div'
        # 创建推荐位-推荐内容-第一个-操作-替换按钮
        self._recommend_create_recommend_content_first_replace_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/a'
        # 创建推荐位-推荐内容-第二个-排序
        self._recommend_create_recommend_content_second_sort_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[3]/table/tbody/tr[2]/td[1]/div'
        # 创建推荐位-推荐内容-第二个-内容ID
        self._recommend_create_recommend_content_second_content_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[3]/table/tbody/tr[2]/td[2]/div'
        # 创建推荐位-推荐内容-第二个-内容名称
        self._recommend_create_recommend_content_second_content_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[3]/table/tbody/tr[2]/td[3]/div'
        # 创建推荐位-推荐内容-第二个-用户名称
        self._recommend_create_recommend_content_second_user_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[3]/table/tbody/tr[2]/td[4]/div'
        # 创建推荐位-推荐内容-第二个-内容类型
        self._recommend_create_recommend_content_second_content_type_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[3]/table/tbody/tr[2]/td[5]/div'
        # 创建推荐位-推荐内容-第二个-操作-替换按钮
        self._recommend_create_recommend_content_second_replace_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[4]/div[2]/table/tbody/tr[2]/td[6]/div/a'
        # 创建推荐位-内容选择页-搜索-内容名称
        self._recommend_create_content_select_search_content_name_input_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div/input'
        # 创建推荐位-内容选择页-搜索-查询按钮
        self._recommend_create_content_select_search_query_button_tag = '//*[@id="tableSearch"]/form/div/div[5]/div/button'
        # 创建推荐位-内容选择页-列表-第一个-复选框
        self._recommend_create_content_select_list_first_select_button_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label'
        # 创建推荐位-内容选择页-列表-第一个-内容ID
        self._recommend_create_content_select_list_first_content_id_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 创建推荐位-内容选择页-列表-第一个-内容名称
        self._recommend_create_content_select_list_first_content_name_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 创建推荐位-内容选择页-列表-第一个-用户名称
        self._recommend_create_content_select_list_first_user_name_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 创建推荐位-内容选择页-列表-第一个-内容类型
        self._recommend_create_content_select_list_first_content_type_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 创建推荐位-内容选择页-列表-第二个-复选框
        self._recommend_create_content_select_list_second_select_button_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[1]/div/label'
        # 创建推荐位-内容选择页-列表-第二个-内容ID
        self._recommend_create_content_select_list_second_content_id_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[2]/div'
        # 创建推荐位-内容选择页-列表-第二个-内容名称
        self._recommend_create_content_select_list_second_content_name_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[3]/div'
        # 创建推荐位-内容选择页-列表-第二个-用户名称
        self._recommend_create_content_select_list_second_user_name_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[4]/div'
        # 创建推荐位-内容选择页-列表-第二个-内容类型
        self._recommend_create_content_select_list_second_content_type_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[5]/div'
        # 创建推荐位-内容选择页-确定按钮
        self._recommend_create_content_select_confirm_button_tag = '/html/body/div[last()-1]/div/div[3]/span/button[1]'
        # 创建推荐位-内容选择页-取消按钮
        self._recommend_create_content_select_cancel_button_tag = '/html/body/div[last()-1]/div/div[3]/span/button[2]'
        # 创建推荐位-保存按钮
        self._recommend_create_save_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[3]/button[1]'
        # 创建推荐位-返回按钮
        self._recommend_create_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[3]/button[2]'
        # 编辑推荐位-推荐位名称
        self._recommend_edit_recommend_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[1]/div[2]/div/div[1]/div/div/div/input'
        # 编辑推荐位-所属渠道
        self._recommend_edit_source_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[1]/div[2]/div/div[2]/div/div/div/div'
        # 编辑推荐位-所属渠道-第一个
        self._recommend_edit_source_first_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 编辑推荐位-所属渠道-第一个文本
        self._recommend_edit_source_first_text_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]/span'
        # 编辑推荐位-所属渠道-第二个
        self._recommend_edit_source_second_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]'
        # 编辑推荐位-所属渠道-第二个文本
        self._recommend_edit_source_second_text_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]/span'
        # 编辑推荐位-推荐内容-第一个-排序
        self._recommend_edit_recommend_content_first_sort_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[3]/table/tbody/tr/td[1]/div'
        # 编辑推荐位-推荐内容-第一个-内容ID
        self._recommend_edit_recommend_content_first_content_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[3]/table/tbody/tr/td[2]/div'
        # 编辑推荐位-推荐内容-第一个-内容名称
        self._recommend_edit_recommend_content_first_content_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[3]/table/tbody/tr/td[3]/div'
        # 编辑推荐位-推荐内容-第一个-用户名称
        self._recommend_edit_recommend_content_first_user_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[3]/table/tbody/tr[1]/td[4]/div'
        # 编辑推荐位-推荐内容-第一个-内容类型
        self._recommend_edit_recommend_content_first_content_type_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[3]/table/tbody/tr[1]/td[5]/div'
        # 编辑推荐位-推荐内容-第一个-操作-替换
        self._recommend_edit_recommend_content_first_replace_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[last()]/div/div/div/div/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/a'
        # 编辑推荐位-内容选择页-搜索-内容名称
        self._recommend_edit_content_select_search_content_name_input_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div/input'
        # 编辑推荐位-内容选择页-搜索-查询按钮
        self._recommend_edit_content_select_search_query_button_tag = '//*[@id="tableSearch"]/form/div/div[5]/div/button'
        # 编辑推荐位-内容选择页-列表-第一个-复选框
        self._recommend_edit_content_select_list_first_select_button_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label'
        # 编辑推荐位-内容选择页-列表-第一个-内容ID
        self._recommend_edit_content_select_list_first_content_id_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 编辑推荐位-内容选择页-列表-第一个-内容名称
        self._recommend_edit_content_select_list_first_content_name_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 编辑推荐位-内容选择页-列表-第一个-用户名称
        self._recommend_edit_content_select_list_first_user_name_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 编辑推荐位-内容选择页-列表-第一个-内容类型
        self._recommend_edit_content_select_list_first_content_type_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 编辑推荐位-内容选择页-列表-第二个-复选框
        self._recommend_edit_content_select_list_second_select_button_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[1]/div/label'
        # 编辑推荐位-内容选择页-列表-第二个-内容ID
        self._recommend_edit_content_select_list_second_content_id_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[2]/div'
        # 编辑推荐位-内容选择页-列表-第二个-内容名称
        self._recommend_edit_content_select_list_second_content_name_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[3]/div'
        # 编辑推荐位-内容选择页-列表-第二个-用户名称
        self._recommend_edit_content_select_list_second_user_name_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[4]/div'
        # 编辑推荐位-内容选择页-列表-第二个-内容类型
        self._recommend_edit_content_select_list_second_content_type_text_tag = '/html/body/div[last()-1]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[5]/div'
        # 编辑推荐位-内容选择页-确定按钮
        self._recommend_edit_content_select_confirm_button_tag = '/html/body/div[last()-1]/div/div[3]/span/button[1]'
        # 编辑推荐位-内容选择页-关闭按钮
        self._recommend_edit_content_select_cancel_button_tag = '/html/body/div[last()-1]/div/div[3]/span/button[2]'
        # 编辑推荐位-保存按钮
        self._recommend_edit_save_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[3]/button[1]'
        # 编辑推荐位-返回按钮
        self._recommend_edit_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[3]/button[2]'
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
    def search_recommend_id_input(self):
        """
        属性: 搜索-推荐位ID
        :return: 搜索-推荐位ID
        """
        element = None
        try:
            element = self.project.get_element(self._search_recommend_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_recommend_name_input(self):
        """
        属性: 搜索-推荐位名称
        :return: 搜索-推荐位名称
        """
        element = None
        try:
            element = self.project.get_element(self._search_recommend_name_input_tag)
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
    def list_first_recommend_id_text(self):
        """
        属性: 列表-第一个-推荐位ID
        :return: 列表-第一个-推荐位ID
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_recommend_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_recommend_name_text(self):
        """
        属性: 列表-第一个-推荐位名称
        :return: 列表-第一个-推荐位名称
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_recommend_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_source_text(self):
        """
        属性: 列表-第一个-所属渠道
        :return: 列表-第一个-所属渠道
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_source_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_floor_text(self):
        """
        属性: 列表-第一个-所属楼层
        :return: 列表-第一个-所属楼层
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_floor_text_tag)
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
    def list_first_recommend_type_text(self):
        """
        属性: 列表-第一个-推荐位类型
        :return: 列表-第一个-推荐位类型
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_recommend_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_max_display_text(self):
        """
        属性: 列表-第一个-内容展示数
        :return: 列表-第一个-内容展示数
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_max_display_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_state_text(self):
        """
        属性: 列表-第一个-状态
        :return: 列表-第一个-状态
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
        属性: 列表-第一个-操作-禁用/启用按钮
        :return: 列表-第一个-操作-禁用/启用按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_is_enable_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def enable_confirm_button(self):
        """
        属性: 确认启用-确定按钮
        :return: 确认启用-确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._enable_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def enable_cancel_button(self):
        """
        属性: 确认启用-取消按钮
        :return: 确认启用-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._enable_cancel_button_tag)
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

    @property
    def recommend_create_button(self):
        """
        属性: 创建推荐位按钮
        :return: 创建推荐位按钮
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_recommend_name_input(self):
        """
        属性: 创建推荐位-推荐位名称
        :return: 创建推荐位-推荐位名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_recommend_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_source_button(self):
        """
        属性: 创建推荐位-所属渠道
        :return: 创建推荐位-所属渠道
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_source_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_source_select(self):
        """
        属性: 创建推荐位-所属渠道-列表
        :return: 创建推荐位-所属渠道-列表
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_source_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_recommend_type_button(self):
        """
        属性: 创建推荐位-推荐位类型
        :return: 创建推荐位-推荐位类型
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_recommend_type_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_recommend_type_select(self):
        """
        属性: 创建推荐位-推荐位类型-列表
        :return: 创建推荐位-推荐位类型-列表
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_recommend_type_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_floor_button(self):
        """
        属性: 创建推荐位-所属楼层
        :return: 创建推荐位-所属楼层
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_floor_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_floor_select(self):
        """
        属性: 创建推荐位-所属楼层-列表
        :return: 创建推荐位-所属楼层-列表
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_floor_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_address_button(self):
        """
        属性: 创建推荐位-地域
        :return: 创建推荐位-地域
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_address_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_address_select(self):
        """
        属性: 创建推荐位-地域-列表
        :return: 创建推荐位-地域-列表
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_address_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_floor_column_name_button(self):
        """
        属性: 创建推荐位-楼层栏目名称
        :return: 创建推荐位-楼层栏目名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_floor_column_name_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_floor_column_name_select(self):
        """
        属性: 创建推荐位-楼层栏目名称-列表
        :return: 创建推荐位-楼层栏目名称-列表
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_floor_column_name_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_recommend_content_first_sort_text(self):
        """
        属性: 创建推荐位-推荐内容-第一个-排序
        :return: 创建推荐位-推荐内容-第一个-排序
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_recommend_content_first_sort_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_recommend_content_first_content_id_text(self):
        """
        属性: 创建推荐位-推荐内容-第一个-内容ID
        :return: 创建推荐位-推荐内容-第一个-内容ID
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_recommend_content_first_content_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_recommend_content_first_content_name_text(self):
        """
        属性: 创建推荐位-推荐内容-第一个-内容名称
        :return: 创建推荐位-推荐内容-第一个-内容名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_recommend_content_first_content_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_recommend_content_first_user_name_text(self):
        """
        属性: 创建推荐位-推荐内容-第一个-用户名称
        :return: 创建推荐位-推荐内容-第一个-用户名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_recommend_content_first_user_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_recommend_content_first_content_type_text(self):
        """
        属性: 创建推荐位-推荐内容-第一个-内容类型
        :return: 创建推荐位-推荐内容-第一个-内容类型
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_recommend_content_first_content_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_recommend_content_first_replace_button(self):
        """
        属性: 创建推荐位-推荐内容-第一个-操作-替换按钮
        :return: 创建推荐位-推荐内容-第一个-操作-替换按钮
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_recommend_content_first_replace_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_recommend_content_second_sort_text(self):
        """
        属性: 创建推荐位-推荐内容-第二个-排序
        :return: 创建推荐位-推荐内容-第二个-排序
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_recommend_content_second_sort_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_recommend_content_second_content_id_text(self):
        """
        属性: 创建推荐位-推荐内容-第二个-内容ID
        :return: 创建推荐位-推荐内容-第二个-内容ID
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_recommend_content_second_content_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_recommend_content_second_content_name_text(self):
        """
        属性: 创建推荐位-推荐内容-第二个-内容名称
        :return: 创建推荐位-推荐内容-第二个-内容名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_recommend_content_second_content_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_recommend_content_second_user_name_text(self):
        """
        属性: 创建推荐位-推荐内容-第二个-用户名称
        :return: 创建推荐位-推荐内容-第二个-用户名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_recommend_content_second_user_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_recommend_content_second_content_type_text(self):
        """
        属性: 创建推荐位-推荐内容-第二个-内容类型
        :return: 创建推荐位-推荐内容-第二个-内容类型
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_recommend_content_second_content_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_recommend_content_second_replace_button(self):
        """
        属性: 创建推荐位-推荐内容-第二个-操作-替换按钮
        :return: 创建推荐位-推荐内容-第二个-操作-替换按钮
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_recommend_content_second_replace_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_content_select_search_content_name_input(self):
        """
        属性: 创建推荐位-内容选择页-搜索-内容名称
        :return: 创建推荐位-内容选择页-搜索-内容名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_content_select_search_content_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_content_select_search_query_button(self):
        """
        属性: 创建推荐位-内容选择页-搜索-查询按钮
        :return: 创建推荐位-内容选择页-搜索-查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_content_select_search_query_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_content_select_list_first_select_button(self):
        """
        属性: 创建推荐位-内容选择页-列表-第一个-复选框
        :return: 创建推荐位-内容选择页-列表-第一个-复选框
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_content_select_list_first_select_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_content_select_list_first_content_id_text(self):
        """
        属性: 创建推荐位-内容选择页-列表-第一个-内容ID
        :return: 创建推荐位-内容选择页-列表-第一个-内容ID
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_content_select_list_first_content_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_content_select_list_first_content_name_text(self):
        """
        属性: 创建推荐位-内容选择页-列表-第一个-内容名称
        :return: 创建推荐位-内容选择页-列表-第一个-内容名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_content_select_list_first_content_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_content_select_list_first_user_name_text(self):
        """
        属性: 创建推荐位-内容选择页-列表-第一个-用户名称
        :return: 创建推荐位-内容选择页-列表-第一个-用户名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_content_select_list_first_user_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_content_select_list_first_content_type_text(self):
        """
        属性: 创建推荐位-内容选择页-列表-第一个-内容类型
        :return: 创建推荐位-内容选择页-列表-第一个-内容类型
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_content_select_list_first_content_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_content_select_list_second_select_button(self):
        """
        属性: 创建推荐位-内容选择页-列表-第二个-复选框
        :return: 创建推荐位-内容选择页-列表-第二个-复选框
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_content_select_list_second_select_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_content_select_list_second_content_id_text(self):
        """
        属性: 创建推荐位-内容选择页-列表-第二个-内容ID
        :return: 创建推荐位-内容选择页-列表-第二个-内容ID
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_content_select_list_second_content_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_content_select_list_second_content_name_text(self):
        """
        属性: 创建推荐位-内容选择页-列表-第二个-内容名称
        :return: 创建推荐位-内容选择页-列表-第二个-内容名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_content_select_list_second_content_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_content_select_list_second_user_name_text(self):
        """
        属性: 创建推荐位-内容选择页-列表-第二个-用户名称
        :return: 创建推荐位-内容选择页-列表-第二个-用户名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_content_select_list_second_user_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_content_select_list_second_content_type_text(self):
        """
        属性: 创建推荐位-内容选择页-列表-第二个-内容类型
        :return: 创建推荐位-内容选择页-列表-第二个-内容类型
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_content_select_list_second_content_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_content_select_confirm_button(self):
        """
        属性: 创建推荐位-内容选择页-确定按钮
        :return: 创建推荐位-内容选择页-确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_content_select_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_content_select_cancel_button(self):
        """
        属性: 创建推荐位-内容选择页-取消按钮
        :return: 创建推荐位-内容选择页-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_content_select_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_save_button(self):
        """
        属性: 创建推荐位-保存按钮
        :return: 创建推荐位-保存按钮
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_save_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_create_cancel_button(self):
        """
        属性: 创建推荐位-返回按钮
        :return: 创建推荐位-返回按钮
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_create_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_recommend_name_input(self):
        """
        属性: 编辑推荐位-推荐位名称
        :return: 编辑推荐位-推荐位名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_recommend_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_source_button(self):
        """
        属性: 编辑推荐位-所属渠道
        :return: 编辑推荐位-所属渠道
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_source_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_source_first_button(self):
        """
        属性: 编辑推荐位-所属渠道-第一个
        :return: 编辑推荐位-所属渠道-第一个
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_source_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_source_first_text(self):
        """
        属性: 编辑推荐位-所属渠道-第一个文本
        :return: 编辑推荐位-所属渠道-第一个文本
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_source_first_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_source_second_button(self):
        """
        属性: 编辑推荐位-所属渠道-第二个
        :return: 编辑推荐位-所属渠道-第二个
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_source_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_source_second_text(self):
        """
        属性: 编辑推荐位-所属渠道-第二个文本
        :return: 编辑推荐位-所属渠道-第二个文本
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_source_second_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_recommend_content_first_sort_text(self):
        """
        属性: 编辑推荐位-推荐内容-第一个-排序
        :return: 编辑推荐位-推荐内容-第一个-排序
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_recommend_content_first_sort_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_recommend_content_first_content_id_text(self):
        """
        属性: 编辑推荐位-推荐内容-第一个-内容ID
        :return: 编辑推荐位-推荐内容-第一个-内容ID
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_recommend_content_first_content_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_recommend_content_first_content_name_text(self):
        """
        属性: 编辑推荐位-推荐内容-第一个-内容名称
        :return: 编辑推荐位-推荐内容-第一个-内容名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_recommend_content_first_content_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_recommend_content_first_user_name_text(self):
        """
        属性: 编辑推荐位-推荐内容-第一个-用户名称
        :return: 编辑推荐位-推荐内容-第一个-用户名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_recommend_content_first_user_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_recommend_content_first_content_type_text(self):
        """
        属性: 编辑推荐位-推荐内容-第一个-内容类型
        :return: 编辑推荐位-推荐内容-第一个-内容类型
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_recommend_content_first_content_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_recommend_content_first_replace_button(self):
        """
        属性: 编辑推荐位-推荐内容-第一个-操作-替换
        :return: 编辑推荐位-推荐内容-第一个-操作-替换
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_recommend_content_first_replace_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_content_select_search_content_name_input(self):
        """
        属性: 编辑推荐位-内容选择页-搜索-内容名称
        :return: 编辑推荐位-内容选择页-搜索-内容名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_content_select_search_content_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_content_select_search_query_button(self):
        """
        属性: 编辑推荐位-内容选择页-搜索-查询按钮
        :return: 编辑推荐位-内容选择页-搜索-查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_content_select_search_query_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_content_select_list_first_select_button(self):
        """
        属性: 编辑推荐位-内容选择页-列表-第一个-复选框
        :return: 编辑推荐位-内容选择页-列表-第一个-复选框
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_content_select_list_first_select_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_content_select_list_first_content_id_text(self):
        """
        属性: 编辑推荐位-内容选择页-列表-第一个-内容ID
        :return: 编辑推荐位-内容选择页-列表-第一个-内容ID
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_content_select_list_first_content_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_content_select_list_first_content_name_text(self):
        """
        属性: 编辑推荐位-内容选择页-列表-第一个-内容名称
        :return: 编辑推荐位-内容选择页-列表-第一个-内容名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_content_select_list_first_content_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_content_select_list_first_user_name_text(self):
        """
        属性: 编辑推荐位-内容选择页-列表-第一个-用户名称
        :return: 编辑推荐位-内容选择页-列表-第一个-用户名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_content_select_list_first_user_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_content_select_list_first_content_type_text(self):
        """
        属性: 编辑推荐位-内容选择页-列表-第一个-内容类型
        :return: 编辑推荐位-内容选择页-列表-第一个-内容类型
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_content_select_list_first_content_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_content_select_list_second_select_button(self):
        """
        属性: 编辑推荐位-内容选择页-列表-第二个-复选框
        :return: 编辑推荐位-内容选择页-列表-第二个-复选框
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_content_select_list_second_select_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_content_select_list_second_content_id_text(self):
        """
        属性: 编辑推荐位-内容选择页-列表-第二个-内容ID
        :return: 编辑推荐位-内容选择页-列表-第二个-内容ID
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_content_select_list_second_content_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_content_select_list_second_content_name_text(self):
        """
        属性: 编辑推荐位-内容选择页-列表-第二个-内容名称
        :return: 编辑推荐位-内容选择页-列表-第二个-内容名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_content_select_list_second_content_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_content_select_list_second_user_name_text(self):
        """
        属性: 编辑推荐位-内容选择页-列表-第二个-用户名称
        :return: 编辑推荐位-内容选择页-列表-第二个-用户名称
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_content_select_list_second_user_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_content_select_list_second_content_type_text(self):
        """
        属性: 编辑推荐位-内容选择页-列表-第二个-内容类型
        :return: 编辑推荐位-内容选择页-列表-第二个-内容类型
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_content_select_list_second_content_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_content_select_confirm_button(self):
        """
        属性: 编辑推荐位-内容选择页-确定按钮
        :return: 编辑推荐位-内容选择页-确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_content_select_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_content_select_cancel_button(self):
        """
        属性: 编辑推荐位-内容选择页-关闭按钮
        :return: 编辑推荐位-内容选择页-关闭按钮
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_content_select_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_save_button(self):
        """
        属性: 编辑推荐位-保存按钮
        :return: 编辑推荐位-保存按钮
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_save_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recommend_edit_cancel_button(self):
        """
        属性: 编辑推荐位-返回按钮
        :return: 编辑推荐位-返回按钮
        """
        element = None
        try:
            element = self.project.get_element(self._recommend_edit_cancel_button_tag)
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

    def set_search_recommend_id_input_action(self, search_recommend_id_input):
        """
        动作：设置搜索-推荐位ID
        :param search_recommend_id_input: 搜索-推荐位ID
        :return: 设置'搜索-推荐位ID'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_recommend_id_input, search_recommend_id_input)
        return self.project.get_current_page_source()

    def set_search_recommend_name_input_action(self, search_recommend_name_input):
        """
        动作：设置搜索-推荐位名称
        :param search_recommend_name_input: 搜索-推荐位名称
        :return: 设置'搜索-推荐位名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_recommend_name_input, search_recommend_name_input)
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

    def get_list_first_recommend_id_text_action(self):
        """
        动作：获取列表-第一个-推荐位ID的文本
        :return: '列表-第一个-推荐位ID'的文本
        """
        control_content = self.project.get_element_text(self.list_first_recommend_id_text)
        return control_content

    def get_list_first_recommend_name_text_action(self):
        """
        动作：获取列表-第一个-推荐位名称的文本
        :return: '列表-第一个-推荐位名称'的文本
        """
        control_content = self.project.get_element_text(self.list_first_recommend_name_text)
        return control_content

    def get_list_first_source_text_action(self):
        """
        动作：获取列表-第一个-所属渠道的文本
        :return: '列表-第一个-所属渠道'的文本
        """
        control_content = self.project.get_element_text(self.list_first_source_text)
        return control_content

    def get_list_first_floor_text_action(self):
        """
        动作：获取列表-第一个-所属楼层的文本
        :return: '列表-第一个-所属楼层'的文本
        """
        control_content = self.project.get_element_text(self.list_first_floor_text)
        return control_content

    def get_list_first_address_text_action(self):
        """
        动作：获取列表-第一个-地域的文本
        :return: '列表-第一个-地域'的文本
        """
        control_content = self.project.get_element_text(self.list_first_address_text)
        return control_content

    def get_list_first_recommend_type_text_action(self):
        """
        动作：获取列表-第一个-推荐位类型的文本
        :return: '列表-第一个-推荐位类型'的文本
        """
        control_content = self.project.get_element_text(self.list_first_recommend_type_text)
        return control_content

    def get_list_first_max_display_text_action(self):
        """
        动作：获取列表-第一个-内容展示数的文本
        :return: '列表-第一个-内容展示数'的文本
        """
        control_content = self.project.get_element_text(self.list_first_max_display_text)
        return control_content

    def get_list_first_state_text_action(self):
        """
        动作：获取列表-第一个-状态的文本
        :return: '列表-第一个-状态'的文本
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
        动作：点击列表-第一个-操作-禁用/启用按钮
        :return: 点击'列表-第一个-操作-禁用/启用按钮'按钮后的页面
        """
        self.project.click(self.list_first_is_enable_button)
        return self.project.get_current_page_source()

    def click_enable_confirm_button_action(self):
        """
        动作：点击确认启用-确定按钮
        :return: 点击'确认启用-确定按钮'按钮后的页面
        """
        self.project.click(self.enable_confirm_button)
        return self.project.get_current_page_source()

    def click_enable_cancel_button_action(self):
        """
        动作：点击确认启用-取消按钮
        :return: 点击'确认启用-取消按钮'按钮后的页面
        """
        self.project.click(self.enable_cancel_button)
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

    def click_recommend_create_button_action(self):
        """
        动作：点击创建推荐位按钮
        :return: 点击'创建推荐位按钮'按钮后的页面
        """
        self.project.click(self.recommend_create_button)
        return self.project.get_current_page_source()

    def set_recommend_create_recommend_name_input_action(self, recommend_create_recommend_name_input):
        """
        动作：设置创建推荐位-推荐位名称
        :param recommend_create_recommend_name_input: 创建推荐位-推荐位名称
        :return: 设置'创建推荐位-推荐位名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.recommend_create_recommend_name_input, recommend_create_recommend_name_input)
        return self.project.get_current_page_source()

    def click_recommend_create_source_button_action(self):
        """
        动作：点击创建推荐位-所属渠道
        :return: 点击'创建推荐位-所属渠道'按钮后的页面
        """
        self.project.click(self.recommend_create_source_button)
        return self.project.get_current_page_source()

    def get_select_recommend_create_source_action(self, recommend_create_source_select):
        """
        动作：获取创建推荐位-所属渠道-列表列表选中的文本
        :param recommend_create_source_select: 创建推荐位-所属渠道-列表列表索引或文本
        :return: '创建推荐位-所属渠道-列表'的文本
        """
        control_content = self.project.get_select_content(self.recommend_create_source_select, recommend_create_source_select)
        return control_content

    def select_recommend_create_source_action(self, recommend_create_source_select):
        """
        动作：选择创建推荐位-所属渠道-列表
        :param recommend_create_source_select: 创建推荐位-所属渠道-列表列表索引或文本
        :return: 选择'创建推荐位-所属渠道-列表'选择器后的页面
        """
        self.project.select_control(self.recommend_create_source_select, recommend_create_source_select)
        return self.project.get_current_page_source()

    def click_recommend_create_recommend_type_button_action(self):
        """
        动作：点击创建推荐位-推荐位类型
        :return: 点击'创建推荐位-推荐位类型'按钮后的页面
        """
        self.project.click(self.recommend_create_recommend_type_button)
        return self.project.get_current_page_source()

    def get_select_recommend_create_recommend_type_action(self, recommend_create_recommend_type_select):
        """
        动作：获取创建推荐位-推荐位类型-列表列表选中的文本
        :param recommend_create_recommend_type_select: 创建推荐位-推荐位类型-列表列表索引或文本
        :return: '创建推荐位-推荐位类型-列表'的文本
        """
        control_content = self.project.get_select_content(self.recommend_create_recommend_type_select, recommend_create_recommend_type_select)
        return control_content

    def select_recommend_create_recommend_type_action(self, recommend_create_recommend_type_select):
        """
        动作：选择创建推荐位-推荐位类型-列表
        :param recommend_create_recommend_type_select: 创建推荐位-推荐位类型-列表列表索引或文本
        :return: 选择'创建推荐位-推荐位类型-列表'选择器后的页面
        """
        self.project.select_control(self.recommend_create_recommend_type_select, recommend_create_recommend_type_select)
        return self.project.get_current_page_source()

    def click_recommend_create_floor_button_action(self):
        """
        动作：点击创建推荐位-所属楼层
        :return: 点击'创建推荐位-所属楼层'按钮后的页面
        """
        self.project.click(self.recommend_create_floor_button)
        return self.project.get_current_page_source()

    def get_select_recommend_create_floor_action(self, recommend_create_floor_select):
        """
        动作：获取创建推荐位-所属楼层-列表列表选中的文本
        :param recommend_create_floor_select: 创建推荐位-所属楼层-列表列表索引或文本
        :return: '创建推荐位-所属楼层-列表'的文本
        """
        control_content = self.project.get_select_content(self.recommend_create_floor_select, recommend_create_floor_select)
        return control_content

    def select_recommend_create_floor_action(self, recommend_create_floor_select):
        """
        动作：选择创建推荐位-所属楼层-列表
        :param recommend_create_floor_select: 创建推荐位-所属楼层-列表列表索引或文本
        :return: 选择'创建推荐位-所属楼层-列表'选择器后的页面
        """
        self.project.select_control(self.recommend_create_floor_select, recommend_create_floor_select)
        return self.project.get_current_page_source()

    def click_recommend_create_address_button_action(self):
        """
        动作：点击创建推荐位-地域
        :return: 点击'创建推荐位-地域'按钮后的页面
        """
        self.project.click(self.recommend_create_address_button)
        return self.project.get_current_page_source()

    def get_select_recommend_create_address_action(self, recommend_create_address_select):
        """
        动作：获取创建推荐位-地域-列表列表选中的文本
        :param recommend_create_address_select: 创建推荐位-地域-列表列表索引或文本
        :return: '创建推荐位-地域-列表'的文本
        """
        control_content = self.project.get_select_content(self.recommend_create_address_select, recommend_create_address_select)
        return control_content

    def select_recommend_create_address_action(self, recommend_create_address_select):
        """
        动作：选择创建推荐位-地域-列表
        :param recommend_create_address_select: 创建推荐位-地域-列表列表索引或文本
        :return: 选择'创建推荐位-地域-列表'选择器后的页面
        """
        self.project.select_control(self.recommend_create_address_select, recommend_create_address_select)
        return self.project.get_current_page_source()

    def click_recommend_create_floor_column_name_button_action(self):
        """
        动作：点击创建推荐位-楼层栏目名称
        :return: 点击'创建推荐位-楼层栏目名称'按钮后的页面
        """
        self.project.click(self.recommend_create_floor_column_name_button)
        return self.project.get_current_page_source()

    def get_select_recommend_create_floor_column_name_action(self, recommend_create_floor_column_name_select):
        """
        动作：获取创建推荐位-楼层栏目名称-列表列表选中的文本
        :param recommend_create_floor_column_name_select: 创建推荐位-楼层栏目名称-列表列表索引或文本
        :return: '创建推荐位-楼层栏目名称-列表'的文本
        """
        control_content = self.project.get_select_content(self.recommend_create_floor_column_name_select, recommend_create_floor_column_name_select)
        return control_content

    def select_recommend_create_floor_column_name_action(self, recommend_create_floor_column_name_select):
        """
        动作：选择创建推荐位-楼层栏目名称-列表
        :param recommend_create_floor_column_name_select: 创建推荐位-楼层栏目名称-列表列表索引或文本
        :return: 选择'创建推荐位-楼层栏目名称-列表'选择器后的页面
        """
        self.project.select_control(self.recommend_create_floor_column_name_select, recommend_create_floor_column_name_select)
        return self.project.get_current_page_source()

    def get_recommend_create_recommend_content_first_sort_text_action(self):
        """
        动作：获取创建推荐位-推荐内容-第一个-排序的文本
        :return: '创建推荐位-推荐内容-第一个-排序'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_recommend_content_first_sort_text)
        return control_content

    def get_recommend_create_recommend_content_first_content_id_text_action(self):
        """
        动作：获取创建推荐位-推荐内容-第一个-内容ID的文本
        :return: '创建推荐位-推荐内容-第一个-内容ID'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_recommend_content_first_content_id_text)
        return control_content

    def get_recommend_create_recommend_content_first_content_name_text_action(self):
        """
        动作：获取创建推荐位-推荐内容-第一个-内容名称的文本
        :return: '创建推荐位-推荐内容-第一个-内容名称'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_recommend_content_first_content_name_text)
        return control_content

    def get_recommend_create_recommend_content_first_user_name_text_action(self):
        """
        动作：获取创建推荐位-推荐内容-第一个-用户名称的文本
        :return: '创建推荐位-推荐内容-第一个-用户名称'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_recommend_content_first_user_name_text)
        return control_content

    def get_recommend_create_recommend_content_first_content_type_text_action(self):
        """
        动作：获取创建推荐位-推荐内容-第一个-内容类型的文本
        :return: '创建推荐位-推荐内容-第一个-内容类型'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_recommend_content_first_content_type_text)
        return control_content

    def click_recommend_create_recommend_content_first_replace_button_action(self):
        """
        动作：点击创建推荐位-推荐内容-第一个-操作-替换按钮
        :return: 点击'创建推荐位-推荐内容-第一个-操作-替换按钮'按钮后的页面
        """
        self.project.click(self.recommend_create_recommend_content_first_replace_button)
        return self.project.get_current_page_source()

    def get_recommend_create_recommend_content_second_sort_text_action(self):
        """
        动作：获取创建推荐位-推荐内容-第二个-排序的文本
        :return: '创建推荐位-推荐内容-第二个-排序'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_recommend_content_second_sort_text)
        return control_content

    def get_recommend_create_recommend_content_second_content_id_text_action(self):
        """
        动作：获取创建推荐位-推荐内容-第二个-内容ID的文本
        :return: '创建推荐位-推荐内容-第二个-内容ID'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_recommend_content_second_content_id_text)
        return control_content

    def get_recommend_create_recommend_content_second_content_name_text_action(self):
        """
        动作：获取创建推荐位-推荐内容-第二个-内容名称的文本
        :return: '创建推荐位-推荐内容-第二个-内容名称'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_recommend_content_second_content_name_text)
        return control_content

    def get_recommend_create_recommend_content_second_user_name_text_action(self):
        """
        动作：获取创建推荐位-推荐内容-第二个-用户名称的文本
        :return: '创建推荐位-推荐内容-第二个-用户名称'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_recommend_content_second_user_name_text)
        return control_content

    def get_recommend_create_recommend_content_second_content_type_text_action(self):
        """
        动作：获取创建推荐位-推荐内容-第二个-内容类型的文本
        :return: '创建推荐位-推荐内容-第二个-内容类型'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_recommend_content_second_content_type_text)
        return control_content

    def click_recommend_create_recommend_content_second_replace_button_action(self):
        """
        动作：点击创建推荐位-推荐内容-第二个-操作-替换按钮
        :return: 点击'创建推荐位-推荐内容-第二个-操作-替换按钮'按钮后的页面
        """
        self.project.click(self.recommend_create_recommend_content_second_replace_button)
        return self.project.get_current_page_source()

    def set_recommend_create_content_select_search_content_name_input_action(self, recommend_create_content_select_search_content_name_input):
        """
        动作：设置创建推荐位-内容选择页-搜索-内容名称
        :param recommend_create_content_select_search_content_name_input: 创建推荐位-内容选择页-搜索-内容名称
        :return: 设置'创建推荐位-内容选择页-搜索-内容名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.recommend_create_content_select_search_content_name_input, recommend_create_content_select_search_content_name_input)
        return self.project.get_current_page_source()

    def click_recommend_create_content_select_search_query_button_action(self):
        """
        动作：点击创建推荐位-内容选择页-搜索-查询按钮
        :return: 点击'创建推荐位-内容选择页-搜索-查询按钮'按钮后的页面
        """
        self.project.click(self.recommend_create_content_select_search_query_button)
        return self.project.get_current_page_source()

    def click_recommend_create_content_select_list_first_select_button_action(self):
        """
        动作：点击创建推荐位-内容选择页-列表-第一个-复选框
        :return: 点击'创建推荐位-内容选择页-列表-第一个-复选框'按钮后的页面
        """
        self.project.click(self.recommend_create_content_select_list_first_select_button)
        return self.project.get_current_page_source()

    def get_recommend_create_content_select_list_first_content_id_text_action(self):
        """
        动作：获取创建推荐位-内容选择页-列表-第一个-内容ID的文本
        :return: '创建推荐位-内容选择页-列表-第一个-内容ID'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_content_select_list_first_content_id_text)
        return control_content

    def get_recommend_create_content_select_list_first_content_name_text_action(self):
        """
        动作：获取创建推荐位-内容选择页-列表-第一个-内容名称的文本
        :return: '创建推荐位-内容选择页-列表-第一个-内容名称'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_content_select_list_first_content_name_text)
        return control_content

    def get_recommend_create_content_select_list_first_user_name_text_action(self):
        """
        动作：获取创建推荐位-内容选择页-列表-第一个-用户名称的文本
        :return: '创建推荐位-内容选择页-列表-第一个-用户名称'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_content_select_list_first_user_name_text)
        return control_content

    def get_recommend_create_content_select_list_first_content_type_text_action(self):
        """
        动作：获取创建推荐位-内容选择页-列表-第一个-内容类型的文本
        :return: '创建推荐位-内容选择页-列表-第一个-内容类型'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_content_select_list_first_content_type_text)
        return control_content

    def click_recommend_create_content_select_list_second_select_button_action(self):
        """
        动作：点击创建推荐位-内容选择页-列表-第二个-复选框
        :return: 点击'创建推荐位-内容选择页-列表-第二个-复选框'按钮后的页面
        """
        self.project.click(self.recommend_create_content_select_list_second_select_button)
        return self.project.get_current_page_source()

    def get_recommend_create_content_select_list_second_content_id_text_action(self):
        """
        动作：获取创建推荐位-内容选择页-列表-第二个-内容ID的文本
        :return: '创建推荐位-内容选择页-列表-第二个-内容ID'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_content_select_list_second_content_id_text)
        return control_content

    def get_recommend_create_content_select_list_second_content_name_text_action(self):
        """
        动作：获取创建推荐位-内容选择页-列表-第二个-内容名称的文本
        :return: '创建推荐位-内容选择页-列表-第二个-内容名称'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_content_select_list_second_content_name_text)
        return control_content

    def get_recommend_create_content_select_list_second_user_name_text_action(self):
        """
        动作：获取创建推荐位-内容选择页-列表-第二个-用户名称的文本
        :return: '创建推荐位-内容选择页-列表-第二个-用户名称'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_content_select_list_second_user_name_text)
        return control_content

    def get_recommend_create_content_select_list_second_content_type_text_action(self):
        """
        动作：获取创建推荐位-内容选择页-列表-第二个-内容类型的文本
        :return: '创建推荐位-内容选择页-列表-第二个-内容类型'的文本
        """
        control_content = self.project.get_element_text(self.recommend_create_content_select_list_second_content_type_text)
        return control_content

    def click_recommend_create_content_select_confirm_button_action(self):
        """
        动作：点击创建推荐位-内容选择页-确定按钮
        :return: 点击'创建推荐位-内容选择页-确定按钮'按钮后的页面
        """
        self.project.click(self.recommend_create_content_select_confirm_button)
        return self.project.get_current_page_source()

    def click_recommend_create_content_select_cancel_button_action(self):
        """
        动作：点击创建推荐位-内容选择页-取消按钮
        :return: 点击'创建推荐位-内容选择页-取消按钮'按钮后的页面
        """
        self.project.click(self.recommend_create_content_select_cancel_button)
        return self.project.get_current_page_source()

    def click_recommend_create_save_button_action(self):
        """
        动作：点击创建推荐位-保存按钮
        :return: 点击'创建推荐位-保存按钮'按钮后的页面
        """
        self.project.click(self.recommend_create_save_button)
        return self.project.get_current_page_source()

    def click_recommend_create_cancel_button_action(self):
        """
        动作：点击创建推荐位-返回按钮
        :return: 点击'创建推荐位-返回按钮'按钮后的页面
        """
        self.project.click(self.recommend_create_cancel_button)
        return self.project.get_current_page_source()

    def set_recommend_edit_recommend_name_input_action(self, recommend_edit_recommend_name_input):
        """
        动作：设置编辑推荐位-推荐位名称
        :param recommend_edit_recommend_name_input: 编辑推荐位-推荐位名称
        :return: 设置'编辑推荐位-推荐位名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.recommend_edit_recommend_name_input, recommend_edit_recommend_name_input)
        return self.project.get_current_page_source()

    def click_recommend_edit_source_button_action(self):
        """
        动作：点击编辑推荐位-所属渠道
        :return: 点击'编辑推荐位-所属渠道'按钮后的页面
        """
        self.project.click(self.recommend_edit_source_button)
        return self.project.get_current_page_source()

    def click_recommend_edit_source_first_button_action(self):
        """
        动作：点击编辑推荐位-所属渠道-第一个
        :return: 点击'编辑推荐位-所属渠道-第一个'按钮后的页面
        """
        self.project.click(self.recommend_edit_source_first_button)
        return self.project.get_current_page_source()

    def get_recommend_edit_source_first_text_action(self):
        """
        动作：获取编辑推荐位-所属渠道-第一个文本的文本
        :return: '编辑推荐位-所属渠道-第一个文本'的文本
        """
        control_content = self.project.get_element_text(self.recommend_edit_source_first_text)
        return control_content

    def click_recommend_edit_source_second_button_action(self):
        """
        动作：点击编辑推荐位-所属渠道-第二个
        :return: 点击'编辑推荐位-所属渠道-第二个'按钮后的页面
        """
        self.project.click(self.recommend_edit_source_second_button)
        return self.project.get_current_page_source()

    def get_recommend_edit_source_second_text_action(self):
        """
        动作：获取编辑推荐位-所属渠道-第二个文本的文本
        :return: '编辑推荐位-所属渠道-第二个文本'的文本
        """
        control_content = self.project.get_element_text(self.recommend_edit_source_second_text)
        return control_content

    def get_recommend_edit_recommend_content_first_sort_text_action(self):
        """
        动作：获取编辑推荐位-推荐内容-第一个-排序的文本
        :return: '编辑推荐位-推荐内容-第一个-排序'的文本
        """
        control_content = self.project.get_element_text(self.recommend_edit_recommend_content_first_sort_text)
        return control_content

    def get_recommend_edit_recommend_content_first_content_id_text_action(self):
        """
        动作：获取编辑推荐位-推荐内容-第一个-内容ID的文本
        :return: '编辑推荐位-推荐内容-第一个-内容ID'的文本
        """
        control_content = self.project.get_element_text(self.recommend_edit_recommend_content_first_content_id_text)
        return control_content

    def get_recommend_edit_recommend_content_first_content_name_text_action(self):
        """
        动作：获取编辑推荐位-推荐内容-第一个-内容名称的文本
        :return: '编辑推荐位-推荐内容-第一个-内容名称'的文本
        """
        control_content = self.project.get_element_text(self.recommend_edit_recommend_content_first_content_name_text)
        return control_content

    def get_recommend_edit_recommend_content_first_user_name_text_action(self):
        """
        动作：获取编辑推荐位-推荐内容-第一个-用户名称的文本
        :return: '编辑推荐位-推荐内容-第一个-用户名称'的文本
        """
        control_content = self.project.get_element_text(self.recommend_edit_recommend_content_first_user_name_text)
        return control_content

    def get_recommend_edit_recommend_content_first_content_type_text_action(self):
        """
        动作：获取编辑推荐位-推荐内容-第一个-内容类型的文本
        :return: '编辑推荐位-推荐内容-第一个-内容类型'的文本
        """
        control_content = self.project.get_element_text(self.recommend_edit_recommend_content_first_content_type_text)
        return control_content

    def click_recommend_edit_recommend_content_first_replace_button_action(self):
        """
        动作：点击编辑推荐位-推荐内容-第一个-操作-替换
        :return: 点击'编辑推荐位-推荐内容-第一个-操作-替换'按钮后的页面
        """
        self.project.click(self.recommend_edit_recommend_content_first_replace_button)
        return self.project.get_current_page_source()

    def set_recommend_edit_content_select_search_content_name_input_action(self, recommend_edit_content_select_search_content_name_input):
        """
        动作：设置编辑推荐位-内容选择页-搜索-内容名称
        :param recommend_edit_content_select_search_content_name_input: 编辑推荐位-内容选择页-搜索-内容名称
        :return: 设置'编辑推荐位-内容选择页-搜索-内容名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.recommend_edit_content_select_search_content_name_input, recommend_edit_content_select_search_content_name_input)
        return self.project.get_current_page_source()

    def click_recommend_edit_content_select_search_query_button_action(self):
        """
        动作：点击编辑推荐位-内容选择页-搜索-查询按钮
        :return: 点击'编辑推荐位-内容选择页-搜索-查询按钮'按钮后的页面
        """
        self.project.click(self.recommend_edit_content_select_search_query_button)
        return self.project.get_current_page_source()

    def click_recommend_edit_content_select_list_first_select_button_action(self):
        """
        动作：点击编辑推荐位-内容选择页-列表-第一个-复选框
        :return: 点击'编辑推荐位-内容选择页-列表-第一个-复选框'按钮后的页面
        """
        self.project.click(self.recommend_edit_content_select_list_first_select_button)
        return self.project.get_current_page_source()

    def get_recommend_edit_content_select_list_first_content_id_text_action(self):
        """
        动作：获取编辑推荐位-内容选择页-列表-第一个-内容ID的文本
        :return: '编辑推荐位-内容选择页-列表-第一个-内容ID'的文本
        """
        control_content = self.project.get_element_text(self.recommend_edit_content_select_list_first_content_id_text)
        return control_content

    def get_recommend_edit_content_select_list_first_content_name_text_action(self):
        """
        动作：获取编辑推荐位-内容选择页-列表-第一个-内容名称的文本
        :return: '编辑推荐位-内容选择页-列表-第一个-内容名称'的文本
        """
        control_content = self.project.get_element_text(self.recommend_edit_content_select_list_first_content_name_text)
        return control_content

    def get_recommend_edit_content_select_list_first_user_name_text_action(self):
        """
        动作：获取编辑推荐位-内容选择页-列表-第一个-用户名称的文本
        :return: '编辑推荐位-内容选择页-列表-第一个-用户名称'的文本
        """
        control_content = self.project.get_element_text(self.recommend_edit_content_select_list_first_user_name_text)
        return control_content

    def get_recommend_edit_content_select_list_first_content_type_text_action(self):
        """
        动作：获取编辑推荐位-内容选择页-列表-第一个-内容类型的文本
        :return: '编辑推荐位-内容选择页-列表-第一个-内容类型'的文本
        """
        control_content = self.project.get_element_text(self.recommend_edit_content_select_list_first_content_type_text)
        return control_content

    def click_recommend_edit_content_select_list_second_select_button_action(self):
        """
        动作：点击编辑推荐位-内容选择页-列表-第二个-复选框
        :return: 点击'编辑推荐位-内容选择页-列表-第二个-复选框'按钮后的页面
        """
        self.project.click(self.recommend_edit_content_select_list_second_select_button)
        return self.project.get_current_page_source()

    def get_recommend_edit_content_select_list_second_content_id_text_action(self):
        """
        动作：获取编辑推荐位-内容选择页-列表-第二个-内容ID的文本
        :return: '编辑推荐位-内容选择页-列表-第二个-内容ID'的文本
        """
        control_content = self.project.get_element_text(self.recommend_edit_content_select_list_second_content_id_text)
        return control_content

    def get_recommend_edit_content_select_list_second_content_name_text_action(self):
        """
        动作：获取编辑推荐位-内容选择页-列表-第二个-内容名称的文本
        :return: '编辑推荐位-内容选择页-列表-第二个-内容名称'的文本
        """
        control_content = self.project.get_element_text(self.recommend_edit_content_select_list_second_content_name_text)
        return control_content

    def get_recommend_edit_content_select_list_second_user_name_text_action(self):
        """
        动作：获取编辑推荐位-内容选择页-列表-第二个-用户名称的文本
        :return: '编辑推荐位-内容选择页-列表-第二个-用户名称'的文本
        """
        control_content = self.project.get_element_text(self.recommend_edit_content_select_list_second_user_name_text)
        return control_content

    def get_recommend_edit_content_select_list_second_content_type_text_action(self):
        """
        动作：获取编辑推荐位-内容选择页-列表-第二个-内容类型的文本
        :return: '编辑推荐位-内容选择页-列表-第二个-内容类型'的文本
        """
        control_content = self.project.get_element_text(self.recommend_edit_content_select_list_second_content_type_text)
        return control_content

    def click_recommend_edit_content_select_confirm_button_action(self):
        """
        动作：点击编辑推荐位-内容选择页-确定按钮
        :return: 点击'编辑推荐位-内容选择页-确定按钮'按钮后的页面
        """
        self.project.click(self.recommend_edit_content_select_confirm_button)
        return self.project.get_current_page_source()

    def click_recommend_edit_content_select_cancel_button_action(self):
        """
        动作：点击编辑推荐位-内容选择页-关闭按钮
        :return: 点击'编辑推荐位-内容选择页-关闭按钮'按钮后的页面
        """
        self.project.click(self.recommend_edit_content_select_cancel_button)
        return self.project.get_current_page_source()

    def click_recommend_edit_save_button_action(self):
        """
        动作：点击编辑推荐位-保存按钮
        :return: 点击'编辑推荐位-保存按钮'按钮后的页面
        """
        self.project.click(self.recommend_edit_save_button)
        return self.project.get_current_page_source()

    def click_recommend_edit_cancel_button_action(self):
        """
        动作：点击编辑推荐位-返回按钮
        :return: 点击'编辑推荐位-返回按钮'按钮后的页面
        """
        self.project.click(self.recommend_edit_cancel_button)
        return self.project.get_current_page_source()

    # endregion Actions
