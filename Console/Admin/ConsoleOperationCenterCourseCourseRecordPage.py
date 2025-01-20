from Utils.Log import log

"""
后台首页-运营中心-课程管理-录播课程管理
console_url/course/course_record
"""


class ConsoleOperationCenterCourseCourseRecordPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/course/course_record'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 搜索-课程ID输入框
        self._search_product_id_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 搜索-课程标题输入框
        self._search_product_name_input_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 搜索-讲师名称输入框
        self._search_teacher_name_input_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div/input'
        # 搜索-状态下拉框
        self._search_state_button_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div/div[1]'
        # 搜索-状态-下拉列表
        self._search_state_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 搜索-角色类型下拉框
        self._search_role_button_tag = '//*[@id="tableSearch"]/form/div/div[5]/div/div/div'
        # 搜索-角色类型-下拉列表
        self._search_role_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 搜索-频道下拉框
        self._search_channel_button_tag = '//*[@id="tableSearch"]/form/div/div[6]/div/div/div[1]'
        # 搜搜-频道-下拉列表
        self._search_channel_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 搜索-一级类目标签下拉框
        self._search_first_label_button_tag = '//*[@id="tableSearch"]/form/div/div[7]/div/div/div[1]'
        # 搜索-一级类目标签-下拉列表
        self._search_first_label_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 搜索-二级类目标签-下拉框
        self._search_second_label_button_tag = '//*[@id="tableSearch"]/form/div/div[8]/div/div/div[1]'
        # 搜索-二级类目标签-下拉列表
        self._search_second_label_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 搜索-内容主题下拉框
        self._search_sub_content_button_tag = '//*[@id="tableSearch"]/form/div/div[9]/div/div/div[1]'
        # 搜索-内容主题下拉列表
        self._search_sub_content_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 搜索-更新日期-起始日期
        self._search_update_date_start_input_tag = '//*[@id="tableSearch"]/form/div/div[10]/div/div/input[1]'
        # 搜索-更新日期-结束日期
        self._search_update_date_end_input_tag = '//*[@id="tableSearch"]/form/div/div[10]/div/div/input[2]'
        # 查询按钮
        self._search_query_button_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div[1]/div[13]/div/button'
        # 清除按钮
        self._search_clear_button_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div[1]/div[14]/div/button'
        # 列表-第一个-课程ID按钮
        self._list_first_product_id_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/a'
        # 列表-第一个-课程ID
        self._list_first_product_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/a/span'
        # 列表-第一个-课程标题
        self._list_first_product_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 列表-第一个-讲师名称
        self._list_first_teacher_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 列表-第一个-角色类型
        self._list_first_role_type_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 列表-第一个-频道
        self._list_first_channel_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 列表-第一个-一级类目标签
        self._list_first_first_label_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 列表-第一个-二级类目标签
        self._list_first_second_label_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div'
        # 列表-第一个-内容主题
        self._list_first_sub_content_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div'
        # 列表-第一个-上课模式
        self._list_first_category_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div'
        # 列表-第一个-销售价格
        self._list_first_price_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[10]/div'
        # 列表-第一个-优惠价格
        self._list_first_discount_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[11]/div'
        # 列表-第一个-发布时间
        self._list_first_create_at_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[12]/div'
        # 列表-第一个-更新时间
        self._list_first_update_at_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[13]/div'
        # 列表-第一个-状态
        self._list_first_state_text_tag = '/html/body/div/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[15]/div'
        # 列表-第一个-操作按钮
        self._list_first_button_tag = '/html/body/div/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[16]/div/a'
        # 上架-理由输入框
        self._upper_shelf_reason_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[2]/form/div/div/div[1]/textarea'
        # 上架-确认按钮
        self._upper_shelf_confirm_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[3]/span/button[2]'
        # 上架-取消按钮
        self._upper_shelf_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div/div[3]/span/button[1]'
        # 下架-理由下拉框
        self._lower_shelf_reason_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div/div[2]/form/div[1]/div/div/div[1]'
        # 下架-理由-下拉列表
        self._lower_shelf_reason_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 下架-自定义理由输入框
        self._lower_shelf_reason_custom_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div/div[2]/form/div[2]/div/div/textarea'
        # 下架-确定按钮
        self._lower_shelf_confirm_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div/div[3]/span/button[2]'
        # 下架-取消按钮
        self._lower_shelf_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div/div[3]/span/button[1]'
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
    def search_product_id_input(self):
        """
        属性: 搜索-课程ID输入框
        :return: 搜索-课程ID输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_product_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_product_name_input(self):
        """
        属性: 搜索-课程标题输入框
        :return: 搜索-课程标题输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_product_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_teacher_name_input(self):
        """
        属性: 搜索-讲师名称输入框
        :return: 搜索-讲师名称输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_teacher_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_state_button(self):
        """
        属性: 搜索-状态下拉框
        :return: 搜索-状态下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._search_state_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_state_select(self):
        """
        属性: 搜索-状态-下拉列表
        :return: 搜索-状态-下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._search_state_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_role_button(self):
        """
        属性: 搜索-角色类型下拉框
        :return: 搜索-角色类型下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._search_role_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_role_select(self):
        """
        属性: 搜索-角色类型-下拉列表
        :return: 搜索-角色类型-下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._search_role_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_channel_button(self):
        """
        属性: 搜索-频道下拉框
        :return: 搜索-频道下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._search_channel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_channel_select(self):
        """
        属性: 搜搜-频道-下拉列表
        :return: 搜搜-频道-下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._search_channel_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_first_label_button(self):
        """
        属性: 搜索-一级类目标签下拉框
        :return: 搜索-一级类目标签下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._search_first_label_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_first_label_select(self):
        """
        属性: 搜索-一级类目标签-下拉列表
        :return: 搜索-一级类目标签-下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._search_first_label_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_second_label_button(self):
        """
        属性: 搜索-二级类目标签-下拉框
        :return: 搜索-二级类目标签-下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._search_second_label_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_second_label_select(self):
        """
        属性: 搜索-二级类目标签-下拉列表
        :return: 搜索-二级类目标签-下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._search_second_label_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_sub_content_button(self):
        """
        属性: 搜索-内容主题下拉框
        :return: 搜索-内容主题下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._search_sub_content_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_sub_content_select(self):
        """
        属性: 搜索-内容主题下拉列表
        :return: 搜索-内容主题下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._search_sub_content_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_update_date_start_input(self):
        """
        属性: 搜索-更新日期-起始日期
        :return: 搜索-更新日期-起始日期
        """
        element = None
        try:
            element = self.project.get_element(self._search_update_date_start_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_update_date_end_input(self):
        """
        属性: 搜索-更新日期-结束日期
        :return: 搜索-更新日期-结束日期
        """
        element = None
        try:
            element = self.project.get_element(self._search_update_date_end_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_query_button(self):
        """
        属性: 查询按钮
        :return: 查询按钮
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
        属性: 清除按钮
        :return: 清除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_product_id_button(self):
        """
        属性: 列表-第一个-课程ID按钮
        :return: 列表-第一个-课程ID按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_product_id_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_product_id_text(self):
        """
        属性: 列表-第一个-课程ID
        :return: 列表-第一个-课程ID
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_product_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_product_name_text(self):
        """
        属性: 列表-第一个-课程标题
        :return: 列表-第一个-课程标题
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_product_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_teacher_name_text(self):
        """
        属性: 列表-第一个-讲师名称
        :return: 列表-第一个-讲师名称
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_teacher_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_role_type_text(self):
        """
        属性: 列表-第一个-角色类型
        :return: 列表-第一个-角色类型
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_role_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_channel_text(self):
        """
        属性: 列表-第一个-频道
        :return: 列表-第一个-频道
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_channel_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_first_label_text(self):
        """
        属性: 列表-第一个-一级类目标签
        :return: 列表-第一个-一级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_first_label_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_second_label_text(self):
        """
        属性: 列表-第一个-二级类目标签
        :return: 列表-第一个-二级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_second_label_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_sub_content_text(self):
        """
        属性: 列表-第一个-内容主题
        :return: 列表-第一个-内容主题
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_sub_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_category_text(self):
        """
        属性: 列表-第一个-上课模式
        :return: 列表-第一个-上课模式
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_category_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_price_text(self):
        """
        属性: 列表-第一个-销售价格
        :return: 列表-第一个-销售价格
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_price_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_discount_text(self):
        """
        属性: 列表-第一个-优惠价格
        :return: 列表-第一个-优惠价格
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_discount_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_create_at_text(self):
        """
        属性: 列表-第一个-发布时间
        :return: 列表-第一个-发布时间
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_create_at_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_update_at_text(self):
        """
        属性: 列表-第一个-更新时间
        :return: 列表-第一个-更新时间
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_update_at_text_tag)
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
    def list_first_button(self):
        """
        属性: 列表-第一个-操作按钮
        :return: 列表-第一个-操作按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def upper_shelf_reason_input(self):
        """
        属性: 上架-理由输入框
        :return: 上架-理由输入框
        """
        element = None
        try:
            element = self.project.get_element(self._upper_shelf_reason_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def upper_shelf_confirm_button(self):
        """
        属性: 上架-确认按钮
        :return: 上架-确认按钮
        """
        element = None
        try:
            element = self.project.get_element(self._upper_shelf_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def upper_shelf_cancel_button(self):
        """
        属性: 上架-取消按钮
        :return: 上架-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._upper_shelf_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def lower_shelf_reason_button(self):
        """
        属性: 下架-理由下拉框
        :return: 下架-理由下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._lower_shelf_reason_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def lower_shelf_reason_select(self):
        """
        属性: 下架-理由-下拉列表
        :return: 下架-理由-下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._lower_shelf_reason_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def lower_shelf_reason_custom_input(self):
        """
        属性: 下架-自定义理由输入框
        :return: 下架-自定义理由输入框
        """
        element = None
        try:
            element = self.project.get_element(self._lower_shelf_reason_custom_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def lower_shelf_confirm_button(self):
        """
        属性: 下架-确定按钮
        :return: 下架-确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._lower_shelf_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def lower_shelf_cancel_button(self):
        """
        属性: 下架-取消按钮
        :return: 下架-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._lower_shelf_cancel_button_tag)
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

    def set_search_product_id_input_action(self, search_product_id_input):
        """
        动作：设置搜索-课程ID输入框
        :param search_product_id_input: 搜索-课程ID输入框
        :return: 设置'搜索-课程ID输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_product_id_input, search_product_id_input)
        return self.project.get_current_page_source()

    def set_search_product_name_input_action(self, search_product_name_input):
        """
        动作：设置搜索-课程标题输入框
        :param search_product_name_input: 搜索-课程标题输入框
        :return: 设置'搜索-课程标题输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_product_name_input, search_product_name_input)
        return self.project.get_current_page_source()

    def set_search_teacher_name_input_action(self, search_teacher_name_input):
        """
        动作：设置搜索-讲师名称输入框
        :param search_teacher_name_input: 搜索-讲师名称输入框
        :return: 设置'搜索-讲师名称输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_teacher_name_input, search_teacher_name_input)
        return self.project.get_current_page_source()

    def click_search_state_button_action(self):
        """
        动作：点击搜索-状态下拉框
        :return: 点击'搜索-状态下拉框'按钮后的页面
        """
        self.project.click(self.search_state_button)
        return self.project.get_current_page_source()

    def get_select_search_state_action(self, search_state_select):
        """
        动作：获取搜索-状态-下拉列表列表选中的文本
        :param search_state_select: 搜索-状态-下拉列表列表索引或文本
        :return: '搜索-状态-下拉列表'的文本
        """
        control_content = self.project.get_select_content(self.search_state_select, search_state_select)
        return control_content

    def select_search_state_action(self, search_state_select):
        """
        动作：选择搜索-状态-下拉列表
        :param search_state_select: 搜索-状态-下拉列表列表索引或文本
        :return: 选择'搜索-状态-下拉列表'选择器后的页面
        """
        self.project.select_control(self.search_state_select, search_state_select)
        return self.project.get_current_page_source()

    def click_search_role_button_action(self):
        """
        动作：点击搜索-角色类型下拉框
        :return: 点击'搜索-角色类型下拉框'按钮后的页面
        """
        self.project.click(self.search_role_button)
        return self.project.get_current_page_source()

    def get_select_search_role_action(self, search_role_select):
        """
        动作：获取搜索-角色类型-下拉列表列表选中的文本
        :param search_role_select: 搜索-角色类型-下拉列表列表索引或文本
        :return: '搜索-角色类型-下拉列表'的文本
        """
        control_content = self.project.get_select_content(self.search_role_select, search_role_select)
        return control_content

    def select_search_role_action(self, search_role_select):
        """
        动作：选择搜索-角色类型-下拉列表
        :param search_role_select: 搜索-角色类型-下拉列表列表索引或文本
        :return: 选择'搜索-角色类型-下拉列表'选择器后的页面
        """
        self.project.select_control(self.search_role_select, search_role_select)
        return self.project.get_current_page_source()

    def click_search_channel_button_action(self):
        """
        动作：点击搜索-频道下拉框
        :return: 点击'搜索-频道下拉框'按钮后的页面
        """
        self.project.click(self.search_channel_button)
        return self.project.get_current_page_source()

    def get_select_search_channel_action(self, search_channel_select):
        """
        动作：获取搜搜-频道-下拉列表列表选中的文本
        :param search_channel_select: 搜搜-频道-下拉列表列表索引或文本
        :return: '搜搜-频道-下拉列表'的文本
        """
        control_content = self.project.get_select_content(self.search_channel_select, search_channel_select)
        return control_content

    def select_search_channel_action(self, search_channel_select):
        """
        动作：选择搜搜-频道-下拉列表
        :param search_channel_select: 搜搜-频道-下拉列表列表索引或文本
        :return: 选择'搜搜-频道-下拉列表'选择器后的页面
        """
        self.project.select_control(self.search_channel_select, search_channel_select)
        return self.project.get_current_page_source()

    def click_search_first_label_button_action(self):
        """
        动作：点击搜索-一级类目标签下拉框
        :return: 点击'搜索-一级类目标签下拉框'按钮后的页面
        """
        self.project.click(self.search_first_label_button)
        return self.project.get_current_page_source()

    def get_select_search_first_label_action(self, search_first_label_select):
        """
        动作：获取搜索-一级类目标签-下拉列表列表选中的文本
        :param search_first_label_select: 搜索-一级类目标签-下拉列表列表索引或文本
        :return: '搜索-一级类目标签-下拉列表'的文本
        """
        control_content = self.project.get_select_content(self.search_first_label_select, search_first_label_select)
        return control_content

    def select_search_first_label_action(self, search_first_label_select):
        """
        动作：选择搜索-一级类目标签-下拉列表
        :param search_first_label_select: 搜索-一级类目标签-下拉列表列表索引或文本
        :return: 选择'搜索-一级类目标签-下拉列表'选择器后的页面
        """
        self.project.select_control(self.search_first_label_select, search_first_label_select)
        return self.project.get_current_page_source()

    def click_search_second_label_button_action(self):
        """
        动作：点击搜索-二级类目标签-下拉框
        :return: 点击'搜索-二级类目标签-下拉框'按钮后的页面
        """
        self.project.click(self.search_second_label_button)
        return self.project.get_current_page_source()

    def get_select_search_second_label_action(self, search_second_label_select):
        """
        动作：获取搜索-二级类目标签-下拉列表列表选中的文本
        :param search_second_label_select: 搜索-二级类目标签-下拉列表列表索引或文本
        :return: '搜索-二级类目标签-下拉列表'的文本
        """
        control_content = self.project.get_select_content(self.search_second_label_select, search_second_label_select)
        return control_content

    def select_search_second_label_action(self, search_second_label_select):
        """
        动作：选择搜索-二级类目标签-下拉列表
        :param search_second_label_select: 搜索-二级类目标签-下拉列表列表索引或文本
        :return: 选择'搜索-二级类目标签-下拉列表'选择器后的页面
        """
        self.project.select_control(self.search_second_label_select, search_second_label_select)
        return self.project.get_current_page_source()

    def click_search_sub_content_button_action(self):
        """
        动作：点击搜索-内容主题下拉框
        :return: 点击'搜索-内容主题下拉框'按钮后的页面
        """
        self.project.click(self.search_sub_content_button)
        return self.project.get_current_page_source()

    def get_select_search_sub_content_action(self, search_sub_content_select):
        """
        动作：获取搜索-内容主题下拉列表列表选中的文本
        :param search_sub_content_select: 搜索-内容主题下拉列表列表索引或文本
        :return: '搜索-内容主题下拉列表'的文本
        """
        control_content = self.project.get_select_content(self.search_sub_content_select, search_sub_content_select)
        return control_content

    def select_search_sub_content_action(self, search_sub_content_select):
        """
        动作：选择搜索-内容主题下拉列表
        :param search_sub_content_select: 搜索-内容主题下拉列表列表索引或文本
        :return: 选择'搜索-内容主题下拉列表'选择器后的页面
        """
        self.project.select_control(self.search_sub_content_select, search_sub_content_select)
        return self.project.get_current_page_source()

    def set_search_update_date_start_input_action(self, search_update_date_start_input):
        """
        动作：设置搜索-更新日期-起始日期
        :param search_update_date_start_input: 搜索-更新日期-起始日期
        :return: 设置'搜索-更新日期-起始日期'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_update_date_start_input, search_update_date_start_input)
        return self.project.get_current_page_source()

    def set_search_update_date_end_input_action(self, search_update_date_end_input):
        """
        动作：设置搜索-更新日期-结束日期
        :param search_update_date_end_input: 搜索-更新日期-结束日期
        :return: 设置'搜索-更新日期-结束日期'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_update_date_end_input, search_update_date_end_input)
        return self.project.get_current_page_source()

    def click_search_query_button_action(self):
        """
        动作：点击查询按钮
        :return: 点击'查询按钮'按钮后的页面
        """
        self.project.click(self.search_query_button)
        return self.project.get_current_page_source()

    def click_search_clear_button_action(self):
        """
        动作：点击清除按钮
        :return: 点击'清除按钮'按钮后的页面
        """
        self.project.click(self.search_clear_button)
        return self.project.get_current_page_source()

    def click_list_first_product_id_button_action(self):
        """
        动作：点击列表-第一个-课程ID按钮
        :return: 点击'列表-第一个-课程ID按钮'按钮后的页面
        """
        self.project.click(self.list_first_product_id_button)
        return self.project.get_current_page_source()

    def get_list_first_product_id_text_action(self):
        """
        动作：获取列表-第一个-课程ID的文本
        :return: '列表-第一个-课程ID'的文本
        """
        control_content = self.project.get_element_text(self.list_first_product_id_text)
        return control_content

    def get_list_first_product_name_text_action(self):
        """
        动作：获取列表-第一个-课程标题的文本
        :return: '列表-第一个-课程标题'的文本
        """
        control_content = self.project.get_element_text(self.list_first_product_name_text)
        return control_content

    def get_list_first_teacher_name_text_action(self):
        """
        动作：获取列表-第一个-讲师名称的文本
        :return: '列表-第一个-讲师名称'的文本
        """
        control_content = self.project.get_element_text(self.list_first_teacher_name_text)
        return control_content

    def get_list_first_role_type_text_action(self):
        """
        动作：获取列表-第一个-角色类型的文本
        :return: '列表-第一个-角色类型'的文本
        """
        control_content = self.project.get_element_text(self.list_first_role_type_text)
        return control_content

    def get_list_first_channel_text_action(self):
        """
        动作：获取列表-第一个-频道的文本
        :return: '列表-第一个-频道'的文本
        """
        control_content = self.project.get_element_text(self.list_first_channel_text)
        return control_content

    def get_list_first_first_label_text_action(self):
        """
        动作：获取列表-第一个-一级类目标签的文本
        :return: '列表-第一个-一级类目标签'的文本
        """
        control_content = self.project.get_element_text(self.list_first_first_label_text)
        return control_content

    def get_list_first_second_label_text_action(self):
        """
        动作：获取列表-第一个-二级类目标签的文本
        :return: '列表-第一个-二级类目标签'的文本
        """
        control_content = self.project.get_element_text(self.list_first_second_label_text)
        return control_content

    def get_list_first_sub_content_text_action(self):
        """
        动作：获取列表-第一个-内容主题的文本
        :return: '列表-第一个-内容主题'的文本
        """
        control_content = self.project.get_element_text(self.list_first_sub_content_text)
        return control_content

    def get_list_first_category_text_action(self):
        """
        动作：获取列表-第一个-上课模式的文本
        :return: '列表-第一个-上课模式'的文本
        """
        control_content = self.project.get_element_text(self.list_first_category_text)
        return control_content

    def get_list_first_price_text_action(self):
        """
        动作：获取列表-第一个-销售价格的文本
        :return: '列表-第一个-销售价格'的文本
        """
        control_content = self.project.get_element_text(self.list_first_price_text)
        return control_content

    def get_list_first_discount_text_action(self):
        """
        动作：获取列表-第一个-优惠价格的文本
        :return: '列表-第一个-优惠价格'的文本
        """
        control_content = self.project.get_element_text(self.list_first_discount_text)
        return control_content

    def get_list_first_create_at_text_action(self):
        """
        动作：获取列表-第一个-发布时间的文本
        :return: '列表-第一个-发布时间'的文本
        """
        control_content = self.project.get_element_text(self.list_first_create_at_text)
        return control_content

    def get_list_first_update_at_text_action(self):
        """
        动作：获取列表-第一个-更新时间的文本
        :return: '列表-第一个-更新时间'的文本
        """
        control_content = self.project.get_element_text(self.list_first_update_at_text)
        return control_content

    def get_list_first_state_text_action(self):
        """
        动作：获取列表-第一个-状态的文本
        :return: '列表-第一个-状态'的文本
        """
        control_content = self.project.get_element_text(self.list_first_state_text)
        return control_content

    def click_list_first_button_action(self):
        """
        动作：点击列表-第一个-操作按钮
        :return: 点击'列表-第一个-操作按钮'按钮后的页面
        """
        self.project.click(self.list_first_button)
        return self.project.get_current_page_source()

    def set_upper_shelf_reason_input_action(self, upper_shelf_reason_input):
        """
        动作：设置上架-理由输入框
        :param upper_shelf_reason_input: 上架-理由输入框
        :return: 设置'上架-理由输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.upper_shelf_reason_input, upper_shelf_reason_input)
        return self.project.get_current_page_source()

    def click_upper_shelf_confirm_button_action(self):
        """
        动作：点击上架-确认按钮
        :return: 点击'上架-确认按钮'按钮后的页面
        """
        self.project.click(self.upper_shelf_confirm_button)
        return self.project.get_current_page_source()

    def click_upper_shelf_cancel_button_action(self):
        """
        动作：点击上架-取消按钮
        :return: 点击'上架-取消按钮'按钮后的页面
        """
        self.project.click(self.upper_shelf_cancel_button)
        return self.project.get_current_page_source()

    def click_lower_shelf_reason_button_action(self):
        """
        动作：点击下架-理由下拉框
        :return: 点击'下架-理由下拉框'按钮后的页面
        """
        self.project.click(self.lower_shelf_reason_button)
        return self.project.get_current_page_source()

    def get_select_lower_shelf_reason_action(self, lower_shelf_reason_select):
        """
        动作：获取下架-理由-下拉列表列表选中的文本
        :param lower_shelf_reason_select: 下架-理由-下拉列表列表索引或文本
        :return: '下架-理由-下拉列表'的文本
        """
        control_content = self.project.get_select_content(self.lower_shelf_reason_select, lower_shelf_reason_select)
        return control_content

    def select_lower_shelf_reason_action(self, lower_shelf_reason_select):
        """
        动作：选择下架-理由-下拉列表
        :param lower_shelf_reason_select: 下架-理由-下拉列表列表索引或文本
        :return: 选择'下架-理由-下拉列表'选择器后的页面
        """
        self.project.select_control(self.lower_shelf_reason_select, lower_shelf_reason_select)
        return self.project.get_current_page_source()

    def set_lower_shelf_reason_custom_input_action(self, lower_shelf_reason_custom_input):
        """
        动作：设置下架-自定义理由输入框
        :param lower_shelf_reason_custom_input: 下架-自定义理由输入框
        :return: 设置'下架-自定义理由输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.lower_shelf_reason_custom_input, lower_shelf_reason_custom_input)
        return self.project.get_current_page_source()

    def click_lower_shelf_confirm_button_action(self):
        """
        动作：点击下架-确定按钮
        :return: 点击'下架-确定按钮'按钮后的页面
        """
        self.project.click(self.lower_shelf_confirm_button)
        return self.project.get_current_page_source()

    def click_lower_shelf_cancel_button_action(self):
        """
        动作：点击下架-取消按钮
        :return: 点击'下架-取消按钮'按钮后的页面
        """
        self.project.click(self.lower_shelf_cancel_button)
        return self.project.get_current_page_source()

    # endregion Actions
