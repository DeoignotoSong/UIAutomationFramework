from Utils.Log import log


"""
后台-商品服务管理-上下架管理
console_url/abroad_center/goods_service/shelf_management
"""


class ConsoleAbroadCenterGoodsServiceShelfManagementPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/abroad_center/goods_service/shelf_management'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 搜索商品编码
        self._search_shelf_product_code_input_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div/div[1]/div/div/input'
        # 搜索商品名称
        self._search_shelf_goods_name_input_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div/div[2]/div/div/input'
        # 搜索所属国家及地区
        self._search_shelf_country_place_list_select_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div/div[3]/div/div/div[1]/input'
        # 搜索所属国家及地区全部
        self._search_shelf_country_place_all_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[1]'
        # 搜索所属国家及地区美国
        self._search_shelf_country_place_america_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[2]'
        # 搜索所属国家及地区澳大利亚
        self._search_shelf_country_place_australia_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[3]'
        # 搜索审核状态
        self._search_shelf_audit_state_input_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div/div[4]/div/div/div[1]/input'
        # 搜索上架开始时间
        self._search_shelf_upper_start_time_input_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div/div[5]/div/div/input[1]'
        # 搜索上架结束时间
        self._search_shelf_upper_end_time_input_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div/div[5]/div/div/input[2]'
        # 搜索下架开始时间
        self._search_shelf_lower_start_time_input_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div/div[6]/div/div/input[1]'
        # 搜索下架结束时间
        self._search_shelf_lower_end_time_input_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div/div[6]/div/div/input[2]'
        # 搜索上架状态
        self._search_shelf_upper_state_input_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div/div[7]/div/div/div[1]/input'
        # 搜索上架方式
        self._search_shelf_upper_method_input_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div/div[8]/div/div/div[1]/input'
        # 搜索下架方式
        self._search_shelf_lower_method_input_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div/div[9]/div/div/div[1]/input'
        # 搜索查询按钮
        self._search_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[1]/form/div/div[12]/div/button'
        # 搜索清除按钮
        self._clear_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[1]/form/div/div[11]/div/button'
        # 待设置按钮
        self._wait_set_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/label[1]/span'
        # 已设置按钮
        self._set_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/label[2]/span'
        # 待设置列表第一条数据商品编码
        self._first_wait_goods_code_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 待设置列表第一条数据商品名称
        self._first_wait_goods_name_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/a/span'
        # 待设置列表第一条数据商品名称按钮
        self._first_wait_goods_name_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/a/span'
        # 待设置列表第一条数据所属国家
        self._first_wait_country_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 待设置列表第一条数据操作
        self._first_wait_set_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/a/span'
        # 待设置列表第一条数据操作文本
        self._first_wait_set_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/a/span'
        # 待设置列表第一条数据立即上架下架日期
        self._first_wait_set_imit_lower_date_input_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[2]/form/div[2]/div/div/input'
        # 待设置列表第一条数据立即上架下架时间
        self._first_wait_set_imit_lower_time_input_tag = '/html/body/div[3]/div[1]/div/div[1]/span[2]/div[1]/input'
        # 设置定时列表第一条数据立即上架日期
        self._first_wait_set_timing_upper_date_input_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[2]/form/div[2]/div/div/input'
        # 设置定时列表第一条数据立即上架时间
        self._first_wait_set_timing_upper_time_input_tag = '/html/body/div[4]/div[1]/div/div[1]/span[2]/div[1]/input'
        # 设置定时列表第一条数据立即下架日期
        self._first_wait_set_timing_lower_date_input_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[2]/form/div[3]/div/div/input'
        # 设置定时列表第一条数据立即下架时间
        self._first_wait_set_timing_lower_time_input_tag = '/html/body/div[4]/div[1]/div/div[1]/span[2]/div[1]/input'
        # 设置定时列表第一条数据上架状态
        self._first_wait_set_upper_state_text_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr/td[10]/div'
        # 待设置时间确认按钮
        self._first_wait_set_timimg_commit_button_tag = '/html/body/div[3]/div[2]/button[2]'
        # 待设置定时时间确认按钮
        self._first_wait_set_time_commit_button_tag = '/html/body/div[4]/div[2]/button[2]'
        # 待设置列表第一条数据设置提交按钮
        self._first_wait_set_commit_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[3]/span/button'
        # 待设置无数据文案
        self._first_wait_set_no_data_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div/div[3]/div/span/label'
        # 待设置列表第一条数据选择框
        self._first_wait_product_button_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span'
        # 待设置列表第二条数据选择框
        self._second_wait_product_button_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[2]/td[1]/div/label/span/span'
        # 已设置列表第一条数据商品编码
        self._first_set_goods_code_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 已设置列表第一条数据商品名称
        self._first_set_goods_name_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/a/span'
        # 已设置列表第一条数据商品名称按钮
        self._first_set_goods_name_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/a/span'
        # 已设置列表第一条数据所属国家
        self._first_set_country_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 已设置列表第一条数据上架方式
        self._first_set_upper_method_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 已设置列表第一条数据上架时间
        self._first_set_upper_time_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 已设置列表第一条数据审核状态
        self._first_set_audit_state_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div'
        # 已设置列表第一条数据下架方式
        self._first_set_lower_method_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div'
        # 已设置列表第一条数据操作下架
        self._first_set_lower_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[12]/div/a[1]/span'
        # 已设置列表第一条数据操作下架文本
        self._first_set_lower_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[12]/div/a[1]/span'
        # 已设置列表第一条数据操作下架确定按钮
        self._first_set_lower_commit_button_tag = '/html/body/div[1]/div/section/main/div/div[4]/div/div/div[3]/span/button/span'
        # 已设置列表第一条数据操作审核记录
        self._first_set_audit_his_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[12]/div/a[2]/span'
        # 已设置列表第一条数据操作审核记录结果
        self._first_set_audit_his_result_text_tag = '/html/body/div[1]/div/section/main/div/div[5]/div/div/div[2]/div/div/div[3]/table/tbody/tr/td[3]/div'
        # 已设置列表第一条数据操作审核记录审核意见
        self._first_set_audit_his_suggestion_text_tag = '/html/body/div[1]/div/section/main/div/div[5]/div/div/div[2]/div/div/div[3]/table/tbody/tr/td[4]/div'
        # 批量设置上架按钮
        self._batch_upper_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[2]/div[1]/button'
        # 已设置列表第二条数据审核状态
        self._second_set_audit_state_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[2]/td[7]/div'
        # 已设置列表第二条数据商品名称
        self._second_set_goods_name_text_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[2]/td[3]/div/a/span'
        # 已设置列表第一条数据上架状态
        self._first_set_upper_state_text_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr/td[10]/div'
        # 已设置列表第一条数据操作审核记录文案
        self._first_set_audit_his_text_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr/td[12]/div/a[2]/span'
        # 已设置批量设置上架按钮
        self._set_batch_upper_button_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[2]/div[1]/button[1]'
        # 已设置批量设置下架按钮
        self._set_batch_lower_button_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[2]/div[1]/button[2]'
        # 设置定时上下架按钮
        self._wait_set_timing_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[2]/form/div[1]/div/label[2]/span[2]'
        # 设置下架立即下架按钮
        self._set_lower_button_tag = '/html/body/div[1]/div/section/main/div/div[4]/div/div/div[2]/form/div/div/label[1]/span[2]'
        # 设置定时下架按钮
        self._set_timing_lower_button_tag = '/html/body/div[1]/div/section/main/div/div[4]/div/div/div[2]/form/div/div/label[2]/span[2]'
        # 设置定时下架时间输入框
        self._set_timing_lower_time_input_tag = '/html/body/div[1]/div/section/main/div/div[4]/div/div/div[2]/form/div[2]/div/div/input'
        # 设置定时下架时间确定按钮
        self._set_timing_lower_commit_button_tag = '/html/body/div[3]/div[2]/button[2]/span'
        # 设置下架时间提交按钮
        self._set_lower_commit_button_tag = '/html/body/div[1]/div/section/main/div/div[4]/div/div/div[3]/span/button/span'
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
    def search_shelf_product_code_input(self):
        """
        属性: 搜索商品编码
        :return: 搜索商品编码
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_product_code_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_shelf_goods_name_input(self):
        """
        属性: 搜索商品名称
        :return: 搜索商品名称
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_goods_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_shelf_country_place_list_select(self):
        """
        属性: 搜索所属国家及地区
        :return: 搜索所属国家及地区
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_country_place_list_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_shelf_country_place_all_button(self):
        """
        属性: 搜索所属国家及地区全部
        :return: 搜索所属国家及地区全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_country_place_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_shelf_country_place_america_button(self):
        """
        属性: 搜索所属国家及地区美国
        :return: 搜索所属国家及地区美国
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_country_place_america_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_shelf_country_place_australia_button(self):
        """
        属性: 搜索所属国家及地区澳大利亚
        :return: 搜索所属国家及地区澳大利亚
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_country_place_australia_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_shelf_audit_state_input(self):
        """
        属性: 搜索审核状态
        :return: 搜索审核状态
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_audit_state_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_shelf_upper_start_time_input(self):
        """
        属性: 搜索上架开始时间
        :return: 搜索上架开始时间
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_upper_start_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_shelf_upper_end_time_input(self):
        """
        属性: 搜索上架结束时间
        :return: 搜索上架结束时间
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_upper_end_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_shelf_lower_start_time_input(self):
        """
        属性: 搜索下架开始时间
        :return: 搜索下架开始时间
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_lower_start_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_shelf_lower_end_time_input(self):
        """
        属性: 搜索下架结束时间
        :return: 搜索下架结束时间
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_lower_end_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_shelf_upper_state_input(self):
        """
        属性: 搜索上架状态
        :return: 搜索上架状态
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_upper_state_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_shelf_upper_method_input(self):
        """
        属性: 搜索上架方式
        :return: 搜索上架方式
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_upper_method_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_shelf_lower_method_input(self):
        """
        属性: 搜索下架方式
        :return: 搜索下架方式
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_lower_method_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_button(self):
        """
        属性: 搜索查询按钮
        :return: 搜索查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def clear_button(self):
        """
        属性: 搜索清除按钮
        :return: 搜索清除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def wait_set_button(self):
        """
        属性: 待设置按钮
        :return: 待设置按钮
        """
        element = None
        try:
            element = self.project.get_element(self._wait_set_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def set_button(self):
        """
        属性: 已设置按钮
        :return: 已设置按钮
        """
        element = None
        try:
            element = self.project.get_element(self._set_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_goods_code_text(self):
        """
        属性: 待设置列表第一条数据商品编码
        :return: 待设置列表第一条数据商品编码
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_goods_code_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_goods_name_text(self):
        """
        属性: 待设置列表第一条数据商品名称
        :return: 待设置列表第一条数据商品名称
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_goods_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_goods_name_button(self):
        """
        属性: 待设置列表第一条数据商品名称按钮
        :return: 待设置列表第一条数据商品名称按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_goods_name_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_country_text(self):
        """
        属性: 待设置列表第一条数据所属国家
        :return: 待设置列表第一条数据所属国家
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_country_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_set_button(self):
        """
        属性: 待设置列表第一条数据操作
        :return: 待设置列表第一条数据操作
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_set_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_set_text(self):
        """
        属性: 待设置列表第一条数据操作文本
        :return: 待设置列表第一条数据操作文本
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_set_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_set_imit_lower_date_input(self):
        """
        属性: 待设置列表第一条数据立即上架下架日期
        :return: 待设置列表第一条数据立即上架下架日期
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_set_imit_lower_date_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_set_imit_lower_time_input(self):
        """
        属性: 待设置列表第一条数据立即上架下架时间
        :return: 待设置列表第一条数据立即上架下架时间
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_set_imit_lower_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_set_timing_upper_date_input(self):
        """
        属性: 设置定时列表第一条数据立即上架日期
        :return: 设置定时列表第一条数据立即上架日期
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_set_timing_upper_date_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_set_timing_upper_time_input(self):
        """
        属性: 设置定时列表第一条数据立即上架时间
        :return: 设置定时列表第一条数据立即上架时间
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_set_timing_upper_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_set_timing_lower_date_input(self):
        """
        属性: 设置定时列表第一条数据立即下架日期
        :return: 设置定时列表第一条数据立即下架日期
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_set_timing_lower_date_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_set_timing_lower_time_input(self):
        """
        属性: 设置定时列表第一条数据立即下架时间
        :return: 设置定时列表第一条数据立即下架时间
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_set_timing_lower_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_set_upper_state_text(self):
        """
        属性: 设置定时列表第一条数据上架状态
        :return: 设置定时列表第一条数据上架状态
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_set_upper_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_set_timimg_commit_button(self):
        """
        属性: 待设置时间确认按钮
        :return: 待设置时间确认按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_set_timimg_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_set_time_commit_button(self):
        """
        属性: 待设置定时时间确认按钮
        :return: 待设置定时时间确认按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_set_time_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_set_commit_button(self):
        """
        属性: 待设置列表第一条数据设置提交按钮
        :return: 待设置列表第一条数据设置提交按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_set_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_set_no_data_text(self):
        """
        属性: 待设置无数据文案
        :return: 待设置无数据文案
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_set_no_data_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_wait_product_button(self):
        """
        属性: 待设置列表第一条数据选择框
        :return: 待设置列表第一条数据选择框
        """
        element = None
        try:
            element = self.project.get_element(self._first_wait_product_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def second_wait_product_button(self):
        """
        属性: 待设置列表第二条数据选择框
        :return: 待设置列表第二条数据选择框
        """
        element = None
        try:
            element = self.project.get_element(self._second_wait_product_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_goods_code_text(self):
        """
        属性: 已设置列表第一条数据商品编码
        :return: 已设置列表第一条数据商品编码
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_goods_code_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_goods_name_text(self):
        """
        属性: 已设置列表第一条数据商品名称
        :return: 已设置列表第一条数据商品名称
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_goods_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_goods_name_button(self):
        """
        属性: 已设置列表第一条数据商品名称按钮
        :return: 已设置列表第一条数据商品名称按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_goods_name_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_country_text(self):
        """
        属性: 已设置列表第一条数据所属国家
        :return: 已设置列表第一条数据所属国家
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_country_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_upper_method_text(self):
        """
        属性: 已设置列表第一条数据上架方式
        :return: 已设置列表第一条数据上架方式
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_upper_method_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_upper_time_text(self):
        """
        属性: 已设置列表第一条数据上架时间
        :return: 已设置列表第一条数据上架时间
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_upper_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_audit_state_text(self):
        """
        属性: 已设置列表第一条数据审核状态
        :return: 已设置列表第一条数据审核状态
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_audit_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_lower_method_text(self):
        """
        属性: 已设置列表第一条数据下架方式
        :return: 已设置列表第一条数据下架方式
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_lower_method_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_lower_button(self):
        """
        属性: 已设置列表第一条数据操作下架
        :return: 已设置列表第一条数据操作下架
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_lower_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_lower_text(self):
        """
        属性: 已设置列表第一条数据操作下架文本
        :return: 已设置列表第一条数据操作下架文本
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_lower_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_lower_commit_button(self):
        """
        属性: 已设置列表第一条数据操作下架确定按钮
        :return: 已设置列表第一条数据操作下架确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_lower_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_audit_his_button(self):
        """
        属性: 已设置列表第一条数据操作审核记录
        :return: 已设置列表第一条数据操作审核记录
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_audit_his_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_audit_his_result_text(self):
        """
        属性: 已设置列表第一条数据操作审核记录结果
        :return: 已设置列表第一条数据操作审核记录结果
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_audit_his_result_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_audit_his_suggestion_text(self):
        """
        属性: 已设置列表第一条数据操作审核记录审核意见
        :return: 已设置列表第一条数据操作审核记录审核意见
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_audit_his_suggestion_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def batch_upper_button(self):
        """
        属性: 批量设置上架按钮
        :return: 批量设置上架按钮
        """
        element = None
        try:
            element = self.project.get_element(self._batch_upper_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def second_set_audit_state_text(self):
        """
        属性: 已设置列表第二条数据审核状态
        :return: 已设置列表第二条数据审核状态
        """
        element = None
        try:
            element = self.project.get_element(self._second_set_audit_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def second_set_goods_name_text(self):
        """
        属性: 已设置列表第二条数据商品名称
        :return: 已设置列表第二条数据商品名称
        """
        element = None
        try:
            element = self.project.get_element(self._second_set_goods_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_upper_state_text(self):
        """
        属性: 已设置列表第一条数据上架状态
        :return: 已设置列表第一条数据上架状态
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_upper_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_set_audit_his_text(self):
        """
        属性: 已设置列表第一条数据操作审核记录文案
        :return: 已设置列表第一条数据操作审核记录文案
        """
        element = None
        try:
            element = self.project.get_element(self._first_set_audit_his_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def set_batch_upper_button(self):
        """
        属性: 已设置批量设置上架按钮
        :return: 已设置批量设置上架按钮
        """
        element = None
        try:
            element = self.project.get_element(self._set_batch_upper_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def set_batch_lower_button(self):
        """
        属性: 已设置批量设置下架按钮
        :return: 已设置批量设置下架按钮
        """
        element = None
        try:
            element = self.project.get_element(self._set_batch_lower_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def wait_set_timing_button(self):
        """
        属性: 设置定时上下架按钮
        :return: 设置定时上下架按钮
        """
        element = None
        try:
            element = self.project.get_element(self._wait_set_timing_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def set_lower_button(self):
        """
        属性: 设置下架立即下架按钮
        :return: 设置下架立即下架按钮
        """
        element = None
        try:
            element = self.project.get_element(self._set_lower_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def set_timing_lower_button(self):
        """
        属性: 设置定时下架按钮
        :return: 设置定时下架按钮
        """
        element = None
        try:
            element = self.project.get_element(self._set_timing_lower_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def set_timing_lower_time_input(self):
        """
        属性: 设置定时下架时间输入框
        :return: 设置定时下架时间输入框
        """
        element = None
        try:
            element = self.project.get_element(self._set_timing_lower_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def set_timing_lower_commit_button(self):
        """
        属性: 设置定时下架时间确定按钮
        :return: 设置定时下架时间确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._set_timing_lower_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def set_lower_commit_button(self):
        """
        属性: 设置下架时间提交按钮
        :return: 设置下架时间提交按钮
        """
        element = None
        try:
            element = self.project.get_element(self._set_lower_commit_button_tag)
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

    def set_search_shelf_product_code_input_action(self, search_shelf_product_code_input):
        """
        动作：设置搜索商品编码
        :param search_shelf_product_code_input: 搜索商品编码
        :return: 设置'搜索商品编码'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_shelf_product_code_input, search_shelf_product_code_input)
        return self.project.get_current_page_source()

    def set_search_shelf_goods_name_input_action(self, search_shelf_goods_name_input):
        """
        动作：设置搜索商品名称
        :param search_shelf_goods_name_input: 搜索商品名称
        :return: 设置'搜索商品名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_shelf_goods_name_input, search_shelf_goods_name_input)
        return self.project.get_current_page_source()

    def get_select_search_shelf_country_place_list_action(self, search_shelf_country_place_list_select):
        """
        动作：获取搜索所属国家及地区列表选中的文本
        :param search_shelf_country_place_list_select: 搜索所属国家及地区列表索引或文本
        :return: '搜索所属国家及地区'的文本
        """
        control_content = self.project.get_select_content(self.search_shelf_country_place_list_select, search_shelf_country_place_list_select)
        return control_content

    def select_search_shelf_country_place_list_action(self, search_shelf_country_place_list_select):
        """
        动作：选择搜索所属国家及地区
        :param search_shelf_country_place_list_select: 搜索所属国家及地区列表索引或文本
        :return: 选择'搜索所属国家及地区'选择器后的页面
        """
        self.project.select_control(self.search_shelf_country_place_list_select, search_shelf_country_place_list_select)
        return self.project.get_current_page_source()

    def click_search_shelf_country_place_all_button_action(self):
        """
        动作：点击搜索所属国家及地区全部
        :return: 点击'搜索所属国家及地区全部'按钮后的页面
        """
        self.project.click(self.search_shelf_country_place_all_button)
        return self.project.get_current_page_source()

    def click_search_shelf_country_place_america_button_action(self):
        """
        动作：点击搜索所属国家及地区美国
        :return: 点击'搜索所属国家及地区美国'按钮后的页面
        """
        self.project.click(self.search_shelf_country_place_america_button)
        return self.project.get_current_page_source()

    def click_search_shelf_country_place_australia_button_action(self):
        """
        动作：点击搜索所属国家及地区澳大利亚
        :return: 点击'搜索所属国家及地区澳大利亚'按钮后的页面
        """
        self.project.click(self.search_shelf_country_place_australia_button)
        return self.project.get_current_page_source()

    def set_search_shelf_audit_state_input_action(self, search_shelf_audit_state_input):
        """
        动作：设置搜索审核状态
        :param search_shelf_audit_state_input: 搜索审核状态
        :return: 设置'搜索审核状态'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_shelf_audit_state_input, search_shelf_audit_state_input)
        return self.project.get_current_page_source()

    def set_search_shelf_upper_start_time_input_action(self, search_shelf_upper_start_time_input):
        """
        动作：设置搜索上架开始时间
        :param search_shelf_upper_start_time_input: 搜索上架开始时间
        :return: 设置'搜索上架开始时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_shelf_upper_start_time_input, search_shelf_upper_start_time_input)
        return self.project.get_current_page_source()

    def set_search_shelf_upper_end_time_input_action(self, search_shelf_upper_end_time_input):
        """
        动作：设置搜索上架结束时间
        :param search_shelf_upper_end_time_input: 搜索上架结束时间
        :return: 设置'搜索上架结束时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_shelf_upper_end_time_input, search_shelf_upper_end_time_input)
        return self.project.get_current_page_source()

    def set_search_shelf_lower_start_time_input_action(self, search_shelf_lower_start_time_input):
        """
        动作：设置搜索下架开始时间
        :param search_shelf_lower_start_time_input: 搜索下架开始时间
        :return: 设置'搜索下架开始时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_shelf_lower_start_time_input, search_shelf_lower_start_time_input)
        return self.project.get_current_page_source()

    def set_search_shelf_lower_end_time_input_action(self, search_shelf_lower_end_time_input):
        """
        动作：设置搜索下架结束时间
        :param search_shelf_lower_end_time_input: 搜索下架结束时间
        :return: 设置'搜索下架结束时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_shelf_lower_end_time_input, search_shelf_lower_end_time_input)
        return self.project.get_current_page_source()

    def set_search_shelf_upper_state_input_action(self, search_shelf_upper_state_input):
        """
        动作：设置搜索上架状态
        :param search_shelf_upper_state_input: 搜索上架状态
        :return: 设置'搜索上架状态'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_shelf_upper_state_input, search_shelf_upper_state_input)
        return self.project.get_current_page_source()

    def set_search_shelf_upper_method_input_action(self, search_shelf_upper_method_input):
        """
        动作：设置搜索上架方式
        :param search_shelf_upper_method_input: 搜索上架方式
        :return: 设置'搜索上架方式'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_shelf_upper_method_input, search_shelf_upper_method_input)
        return self.project.get_current_page_source()

    def set_search_shelf_lower_method_input_action(self, search_shelf_lower_method_input):
        """
        动作：设置搜索下架方式
        :param search_shelf_lower_method_input: 搜索下架方式
        :return: 设置'搜索下架方式'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_shelf_lower_method_input, search_shelf_lower_method_input)
        return self.project.get_current_page_source()

    def click_search_button_action(self):
        """
        动作：点击搜索查询按钮
        :return: 点击'搜索查询按钮'按钮后的页面
        """
        self.project.click(self.search_button)
        return self.project.get_current_page_source()

    def click_clear_button_action(self):
        """
        动作：点击搜索清除按钮
        :return: 点击'搜索清除按钮'按钮后的页面
        """
        self.project.click(self.clear_button)
        return self.project.get_current_page_source()

    def click_wait_set_button_action(self):
        """
        动作：点击待设置按钮
        :return: 点击'待设置按钮'按钮后的页面
        """
        self.project.click(self.wait_set_button)
        return self.project.get_current_page_source()

    def click_set_button_action(self):
        """
        动作：点击已设置按钮
        :return: 点击'已设置按钮'按钮后的页面
        """
        self.project.click(self.set_button)
        return self.project.get_current_page_source()

    def get_first_wait_goods_code_text_action(self):
        """
        动作：获取待设置列表第一条数据商品编码的文本
        :return: '待设置列表第一条数据商品编码'的文本
        """
        control_content = self.project.get_element_text(self.first_wait_goods_code_text)
        return control_content

    def get_first_wait_goods_name_text_action(self):
        """
        动作：获取待设置列表第一条数据商品名称的文本
        :return: '待设置列表第一条数据商品名称'的文本
        """
        control_content = self.project.get_element_text(self.first_wait_goods_name_text)
        return control_content

    def click_first_wait_goods_name_button_action(self):
        """
        动作：点击待设置列表第一条数据商品名称按钮
        :return: 点击'待设置列表第一条数据商品名称按钮'按钮后的页面
        """
        self.project.click(self.first_wait_goods_name_button)
        return self.project.get_current_page_source()

    def get_first_wait_country_text_action(self):
        """
        动作：获取待设置列表第一条数据所属国家的文本
        :return: '待设置列表第一条数据所属国家'的文本
        """
        control_content = self.project.get_element_text(self.first_wait_country_text)
        return control_content

    def click_first_wait_set_button_action(self):
        """
        动作：点击待设置列表第一条数据操作
        :return: 点击'待设置列表第一条数据操作'按钮后的页面
        """
        self.project.click(self.first_wait_set_button)
        return self.project.get_current_page_source()

    def get_first_wait_set_text_action(self):
        """
        动作：获取待设置列表第一条数据操作文本的文本
        :return: '待设置列表第一条数据操作文本'的文本
        """
        control_content = self.project.get_element_text(self.first_wait_set_text)
        return control_content

    def set_first_wait_set_imit_lower_date_input_action(self, first_wait_set_imit_lower_date_input):
        """
        动作：设置待设置列表第一条数据立即上架下架日期
        :param first_wait_set_imit_lower_date_input: 待设置列表第一条数据立即上架下架日期
        :return: 设置'待设置列表第一条数据立即上架下架日期'文本后的页面
        """
        self.project.clear_and_send_keys(self.first_wait_set_imit_lower_date_input, first_wait_set_imit_lower_date_input)
        return self.project.get_current_page_source()

    def set_first_wait_set_imit_lower_time_input_action(self, first_wait_set_imit_lower_time_input):
        """
        动作：设置待设置列表第一条数据立即上架下架时间
        :param first_wait_set_imit_lower_time_input: 待设置列表第一条数据立即上架下架时间
        :return: 设置'待设置列表第一条数据立即上架下架时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.first_wait_set_imit_lower_time_input, first_wait_set_imit_lower_time_input)
        return self.project.get_current_page_source()

    def set_first_wait_set_timing_upper_date_input_action(self, first_wait_set_timing_upper_date_input):
        """
        动作：设置设置定时列表第一条数据立即上架日期
        :param first_wait_set_timing_upper_date_input: 设置定时列表第一条数据立即上架日期
        :return: 设置'设置定时列表第一条数据立即上架日期'文本后的页面
        """
        self.project.clear_and_send_keys(self.first_wait_set_timing_upper_date_input, first_wait_set_timing_upper_date_input)
        return self.project.get_current_page_source()

    def set_first_wait_set_timing_upper_time_input_action(self, first_wait_set_timing_upper_time_input):
        """
        动作：设置设置定时列表第一条数据立即上架时间
        :param first_wait_set_timing_upper_time_input: 设置定时列表第一条数据立即上架时间
        :return: 设置'设置定时列表第一条数据立即上架时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.first_wait_set_timing_upper_time_input, first_wait_set_timing_upper_time_input)
        return self.project.get_current_page_source()

    def set_first_wait_set_timing_lower_date_input_action(self, first_wait_set_timing_lower_date_input):
        """
        动作：设置设置定时列表第一条数据立即下架日期
        :param first_wait_set_timing_lower_date_input: 设置定时列表第一条数据立即下架日期
        :return: 设置'设置定时列表第一条数据立即下架日期'文本后的页面
        """
        self.project.clear_and_send_keys(self.first_wait_set_timing_lower_date_input, first_wait_set_timing_lower_date_input)
        return self.project.get_current_page_source()

    def set_first_wait_set_timing_lower_time_input_action(self, first_wait_set_timing_lower_time_input):
        """
        动作：设置设置定时列表第一条数据立即下架时间
        :param first_wait_set_timing_lower_time_input: 设置定时列表第一条数据立即下架时间
        :return: 设置'设置定时列表第一条数据立即下架时间'文本后的页面
        """
        self.project.clear_and_send_keys(self.first_wait_set_timing_lower_time_input, first_wait_set_timing_lower_time_input)
        return self.project.get_current_page_source()

    def get_first_wait_set_upper_state_text_action(self):
        """
        动作：获取设置定时列表第一条数据上架状态的文本
        :return: '设置定时列表第一条数据上架状态'的文本
        """
        control_content = self.project.get_element_text(self.first_wait_set_upper_state_text)
        return control_content

    def click_first_wait_set_timimg_commit_button_action(self):
        """
        动作：点击待设置时间确认按钮
        :return: 点击'待设置时间确认按钮'按钮后的页面
        """
        self.project.click(self.first_wait_set_timimg_commit_button)
        return self.project.get_current_page_source()

    def click_first_wait_set_time_commit_button_action(self):
        """
        动作：点击待设置定时时间确认按钮
        :return: 点击'待设置定时时间确认按钮'按钮后的页面
        """
        self.project.click(self.first_wait_set_time_commit_button)
        return self.project.get_current_page_source()

    def click_first_wait_set_commit_button_action(self):
        """
        动作：点击待设置列表第一条数据设置提交按钮
        :return: 点击'待设置列表第一条数据设置提交按钮'按钮后的页面
        """
        self.project.click(self.first_wait_set_commit_button)
        return self.project.get_current_page_source()

    def get_first_wait_set_no_data_text_action(self):
        """
        动作：获取待设置无数据文案的文本
        :return: '待设置无数据文案'的文本
        """
        control_content = self.project.get_element_text(self.first_wait_set_no_data_text)
        return control_content

    def click_first_wait_product_button_action(self):
        """
        动作：点击待设置列表第一条数据选择框
        :return: 点击'待设置列表第一条数据选择框'按钮后的页面
        """
        self.project.click(self.first_wait_product_button)
        return self.project.get_current_page_source()

    def click_second_wait_product_button_action(self):
        """
        动作：点击待设置列表第二条数据选择框
        :return: 点击'待设置列表第二条数据选择框'按钮后的页面
        """
        self.project.click(self.second_wait_product_button)
        return self.project.get_current_page_source()

    def get_first_set_goods_code_text_action(self):
        """
        动作：获取已设置列表第一条数据商品编码的文本
        :return: '已设置列表第一条数据商品编码'的文本
        """
        control_content = self.project.get_element_text(self.first_set_goods_code_text)
        return control_content

    def get_first_set_goods_name_text_action(self):
        """
        动作：获取已设置列表第一条数据商品名称的文本
        :return: '已设置列表第一条数据商品名称'的文本
        """
        control_content = self.project.get_element_text(self.first_set_goods_name_text)
        return control_content

    def click_first_set_goods_name_button_action(self):
        """
        动作：点击已设置列表第一条数据商品名称按钮
        :return: 点击'已设置列表第一条数据商品名称按钮'按钮后的页面
        """
        self.project.click(self.first_set_goods_name_button)
        return self.project.get_current_page_source()

    def get_first_set_country_text_action(self):
        """
        动作：获取已设置列表第一条数据所属国家的文本
        :return: '已设置列表第一条数据所属国家'的文本
        """
        control_content = self.project.get_element_text(self.first_set_country_text)
        return control_content

    def get_first_set_upper_method_text_action(self):
        """
        动作：获取已设置列表第一条数据上架方式的文本
        :return: '已设置列表第一条数据上架方式'的文本
        """
        control_content = self.project.get_element_text(self.first_set_upper_method_text)
        return control_content

    def get_first_set_upper_time_text_action(self):
        """
        动作：获取已设置列表第一条数据上架时间的文本
        :return: '已设置列表第一条数据上架时间'的文本
        """
        control_content = self.project.get_element_text(self.first_set_upper_time_text)
        return control_content

    def get_first_set_audit_state_text_action(self):
        """
        动作：获取已设置列表第一条数据审核状态的文本
        :return: '已设置列表第一条数据审核状态'的文本
        """
        control_content = self.project.get_element_text(self.first_set_audit_state_text)
        return control_content

    def get_first_set_lower_method_text_action(self):
        """
        动作：获取已设置列表第一条数据下架方式的文本
        :return: '已设置列表第一条数据下架方式'的文本
        """
        control_content = self.project.get_element_text(self.first_set_lower_method_text)
        return control_content

    def click_first_set_lower_button_action(self):
        """
        动作：点击已设置列表第一条数据操作下架
        :return: 点击'已设置列表第一条数据操作下架'按钮后的页面
        """
        self.project.click(self.first_set_lower_button)
        return self.project.get_current_page_source()

    def get_first_set_lower_text_action(self):
        """
        动作：获取已设置列表第一条数据操作下架文本的文本
        :return: '已设置列表第一条数据操作下架文本'的文本
        """
        control_content = self.project.get_element_text(self.first_set_lower_text)
        return control_content

    def click_first_set_lower_commit_button_action(self):
        """
        动作：点击已设置列表第一条数据操作下架确定按钮
        :return: 点击'已设置列表第一条数据操作下架确定按钮'按钮后的页面
        """
        self.project.click(self.first_set_lower_commit_button)
        return self.project.get_current_page_source()

    def click_first_set_audit_his_button_action(self):
        """
        动作：点击已设置列表第一条数据操作审核记录
        :return: 点击'已设置列表第一条数据操作审核记录'按钮后的页面
        """
        self.project.click(self.first_set_audit_his_button)
        return self.project.get_current_page_source()

    def get_first_set_audit_his_result_text_action(self):
        """
        动作：获取已设置列表第一条数据操作审核记录结果的文本
        :return: '已设置列表第一条数据操作审核记录结果'的文本
        """
        control_content = self.project.get_element_text(self.first_set_audit_his_result_text)
        return control_content

    def get_first_set_audit_his_suggestion_text_action(self):
        """
        动作：获取已设置列表第一条数据操作审核记录审核意见的文本
        :return: '已设置列表第一条数据操作审核记录审核意见'的文本
        """
        control_content = self.project.get_element_text(self.first_set_audit_his_suggestion_text)
        return control_content

    def click_batch_upper_button_action(self):
        """
        动作：点击批量设置上架按钮
        :return: 点击'批量设置上架按钮'按钮后的页面
        """
        self.project.click(self.batch_upper_button)
        return self.project.get_current_page_source()

    def get_second_set_audit_state_text_action(self):
        """
        动作：获取已设置列表第二条数据审核状态的文本
        :return: '已设置列表第二条数据审核状态'的文本
        """
        control_content = self.project.get_element_text(self.second_set_audit_state_text)
        return control_content

    def get_second_set_goods_name_text_action(self):
        """
        动作：获取已设置列表第二条数据商品名称的文本
        :return: '已设置列表第二条数据商品名称'的文本
        """
        control_content = self.project.get_element_text(self.second_set_goods_name_text)
        return control_content

    def get_first_set_upper_state_text_action(self):
        """
        动作：获取已设置列表第一条数据上架状态的文本
        :return: '已设置列表第一条数据上架状态'的文本
        """
        control_content = self.project.get_element_text(self.first_set_upper_state_text)
        return control_content

    def get_first_set_audit_his_text_action(self):
        """
        动作：获取已设置列表第一条数据操作审核记录文案的文本
        :return: '已设置列表第一条数据操作审核记录文案'的文本
        """
        control_content = self.project.get_element_text(self.first_set_audit_his_text)
        return control_content

    def click_set_batch_upper_button_action(self):
        """
        动作：点击已设置批量设置上架按钮
        :return: 点击'已设置批量设置上架按钮'按钮后的页面
        """
        self.project.click(self.set_batch_upper_button)
        return self.project.get_current_page_source()

    def click_set_batch_lower_button_action(self):
        """
        动作：点击已设置批量设置下架按钮
        :return: 点击'已设置批量设置下架按钮'按钮后的页面
        """
        self.project.click(self.set_batch_lower_button)
        return self.project.get_current_page_source()

    def click_wait_set_timing_button_action(self):
        """
        动作：点击设置定时上下架按钮
        :return: 点击'设置定时上下架按钮'按钮后的页面
        """
        self.project.click(self.wait_set_timing_button)
        return self.project.get_current_page_source()

    def click_set_lower_button_action(self):
        """
        动作：点击设置下架立即下架按钮
        :return: 点击'设置下架立即下架按钮'按钮后的页面
        """
        self.project.click(self.set_lower_button)
        return self.project.get_current_page_source()

    def click_set_timing_lower_button_action(self):
        """
        动作：点击设置定时下架按钮
        :return: 点击'设置定时下架按钮'按钮后的页面
        """
        self.project.click(self.set_timing_lower_button)
        return self.project.get_current_page_source()

    def set_set_timing_lower_time_input_action(self, set_timing_lower_time_input):
        """
        动作：设置设置定时下架时间输入框
        :param set_timing_lower_time_input: 设置定时下架时间输入框
        :return: 设置'设置定时下架时间输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.set_timing_lower_time_input, set_timing_lower_time_input)
        return self.project.get_current_page_source()

    def click_set_timing_lower_commit_button_action(self):
        """
        动作：点击设置定时下架时间确定按钮
        :return: 点击'设置定时下架时间确定按钮'按钮后的页面
        """
        self.project.click(self.set_timing_lower_commit_button)
        return self.project.get_current_page_source()

    def click_set_lower_commit_button_action(self):
        """
        动作：点击设置下架时间提交按钮
        :return: 点击'设置下架时间提交按钮'按钮后的页面
        """
        self.project.click(self.set_lower_commit_button)
        return self.project.get_current_page_source()

    # endregion Actions
