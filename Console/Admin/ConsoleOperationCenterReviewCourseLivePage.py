from Utils.Log import log

"""
后台首页-运营中心-审核管理-直播课程审核
console_url/review/course_live
"""


class ConsoleOperationCenterReviewCourseLivePage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/review/course_live'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 加载图层
        self._loading_mask_tag ='/html/body/div[@class="el-loading-mask is-fullscreen el-loading-fade-enter-active el-loading-fade-enter-to"]'
        # 下拉列表
        self._drop_down_list_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 课程ID输入框
        self._course_live_goods_id_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 课程标题输入框
        self._course_live_product_name_input_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 讲师姓名输入框
        self._course_live_teacher_name_input_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div/input'
        # 上课模式下拉框
        self._course_live_category_button_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div/div'
        # 频道下拉框
        self._course_live_channel_button_tag = '//*[@id="tableSearch"]/form/div/div[5]/div/div/div[1]'
        # 状态下拉框
        self._course_live_state_button_tag = '//*[@id="tableSearch"]/form/div/div[6]/div/div/div[1]'
        # 状态审核通过按钮
        self._course_live_state_pass_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[4]'
        # 角色类型-下拉框
        self._course_live_role_button_tag = '//*[@id="tableSearch"]/form/div/div[7]/div/div/div'
        # 班次状态下拉框
        self._course_live_class_state_button_tag = '//*[@id="tableSearch"]/form/div/div[8]/div/div/div'
        # 更新日期-开始日期输入框
        self._course_live_update_time_start_time_input_tag = '//*[@id="tableSearch"]/form/div/div[9]/div/div/input[1]'
        # 更新日期-结束日期输入框
        self._course_live_update_time_end_time_input_tag = '//*[@id="tableSearch"]/form/div/div[9]/div/div/input[2]'
        # 查询按钮
        self._course_live_search_button_tag = '//*[@id="tableSearch"]/form/div/div[last()-1]/div/button'
        # 清除按钮
        self._course_live_clear_button_tag = '//*[@id="tableSearch"]/form/div/div[last()]/div/button'
        # 列表-第一个课程状态
        self._course_live_list_first_course_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[12]/div'
        # 列表-第一个-操作按钮（审核/查看）
        self._course_live_list_first_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[last()]/div/a'
        # 审核详情-课程标题
        self._course_live_detail_product_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[1]/div/div/div'
        # 审核详情-上课模式
        self._course_live_detail_category_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[2]/div/div'
        # 审核详情-课程id
        self._course_live_detail_goods_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[3]/div/div'
        # 审核详情-课程副标题
        self._course_live_detail_sub_product_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[4]/div/div'
        # 审核详情-发布时间
        self._course_live_detail_create_at_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[6]/div/div'
        # 审核详情-课程状态
        self._course_live_detail_examine_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[7]/div/div/a/span'
        # 审核详情-一级类目标签
        self._course_live_detail_first_label_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[3]/div[1]/div/div'
        # 审核详情-二级类目标签
        self._course_live_detail_second_label_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[3]/div[2]/div/div'
        # 审核详情-内容主题
        self._course_live_detail_sub_content_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[3]/div[3]/div/div'
        # 审核详情-关键词
        self._course_live_detail_keywords_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[3]/div[4]/div/div'
        # 审核详情-课程特色
        self._course_live_detail_feature_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[5]/div[1]/div/div'
        # 审核详情-限售人数
        self._course_live_detail_restricted_sales_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[5]/div[2]/div/div'
        # 审核详情-第一课节-课节名称
        self._course_live_detail_first_item_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[7]/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 审核详情-第一课街-课件名称
        self._course_live_detail_first_item_pdf_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[7]/div/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/a/span'
        # 审核详情-第一课节-课件按钮
        self._course_live_detail_first_item_pdf_name_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[7]/div/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/a'
        # 审核详情-第二课节-课节名称
        self._course_live_detail_second_item_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[7]/div/div[1]/div[3]/table/tbody/tr[2]/td[2]/div'
        # 审核详情-第二节课-课件名称
        self._course_live_detail_second_item_pdf_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[7]/div/div[1]/div[3]/table/tbody/tr[2]/td[3]/div/a/span'
        # 审核详情-第二课节-课件按钮
        self._course_live_detail_second_item_pdf_name_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[7]/div/div[1]/div[3]/table/tbody/tr[2]/td[3]/div/a'
        # 审核详情-讲师姓名
        self._course_live_detail_teacher_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div[2]/form/div/div[1]/div/div'
        # 审核详情-讲师id
        self._course_live_detail_teacher_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div[2]/form/div/div[2]/div/div'
        # 审核详情-频道
        self._course_live_detail_channel_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div[2]/form/div/div[3]/div/div'
        # 审核详情-角色类型
        self._course_live_detail_role_type_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div[2]/form/div/div[4]/div/div'
        # 审核详情-问题一
        self._course_live_detail_first_question_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[2]/div'
        # 审核详情-答案一
        self._course_live_detail_first_answer_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[3]/div'
        # 审核详情-问题二
        self._course_live_detail_second_question_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div[2]/div/div/div[3]/table/tbody/tr[2]/td[2]/div'
        # 审核详情-答案二
        self._course_live_detail_second_answer_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div[2]/div/div/div[3]/table/tbody/tr[2]/td[3]/div'
        # 审核详情-班次一-班次名称
        self._course_live_detail_first_class_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[2]/div'
        # 审核详情-班次一-班次周期
        self._course_live_detail_first_class_date_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[3]/div'
        # 审核详情-班次一-销售价格
        self._course_live_detail_first_class_price_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[4]/div'
        # 审核详情-班次一-优惠价格
        self._course_live_detail_first_class_discount_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[5]/div'
        # 审核详情-班次一-优惠是否建群
        self._course_live_detail_first_class_is_group_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[6]/div'
        # 审核详情-班次一-创建时间
        self._course_live_detail_first_class_create_at_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[7]/div'
        # 审核详情-班次一-更新时间
        self._course_live_detail_first_class_update_at_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[8]/div'
        # 审核详情-班次一-班次状态
        self._course_live_detail_first_class_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[9]/div'
        # 审核详情-班次一-审核通过按钮
        self._course_live_detail_first_class_pass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/a[1]'
        # 审核详情-班次审核-通过-确定按钮
        self._course_live_detail_class_pass_confirm_button_tag = '/html/body/div[last()-1]/div/div[3]/button[2]'
        # 审核详情-班次审核-通过-取消按钮
        self._course_live_detail_class_pass_cancel_button_tag = '/html/body/div[last()-1]/div/div[3]/button[1]'
        # 审核详情-班次一-审核不通过按钮
        self._course_live_detail_first_class_unpass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div/div[4]/div[2]/table/tbody/tr/td[10]/div/a[2]'
        # 审核详情-班次审核-不通过-未通过理由下拉框
        self._course_live_detail_class_unpass_reason_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[2]/div/div/div[2]/form/div[1]/div/div'
        # 审核详情-班次审核-不通过-未通过理由自定义输入框
        self._course_live_detail_class_unpass_reason_custom_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[2]/div/div/div[2]/form/div[2]/div/div/textarea'
        # 审核详情-班次审核-不通过-提交按钮
        self._course_live_detail_class_unpass_confirm_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[2]/div/div/div[3]/span/button[1]'
        # 审核详情-班次审核-不通过-返回按钮
        self._course_live_detail_class_unpass_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[2]/div/div/div[3]/span/button[2]'
        # 审核详情-班次审核-不通过-关闭按钮
        self._course_live_detail_class_unpass_close_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[2]/div/div/div[1]/button'
        # 审核详情-课程审核通过按钮
        self._course_live_detail_course_pass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[last()-1]/div[1]/button[1]'
        # 课程详情-弹出确认框
        self._course_detail_course_pass_confirm_box_tag = '/html/body/div[last()-1]'
        # 审核详情-课程审核通过-确认按钮
        self._course_live_detail_course_pass_confirm_button_tag = '/html/body/div[last()-1]/div/div[3]/button[2]'
        # 审核详情-课程审核通过-取消按钮
        self._course_live_detail_course_pass_cancel_button_tag = '/html/body/div[last()-1]/div/div[3]/button[1]'
        # 审核详情-课程审核不通过按钮
        self._course_live_detail_course_unpass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[last()-1]/div[1]/button[2]'
        # 审核详情-课程审核-不通过-未通过理由下拉框
        self._course_live_detail_course_unpass_reason_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[last()-1]/div[2]/div/div/div[2]/form/div[1]/div/div'
        # 审核详情-课程审核-不通过-自定义输入框
        self._course_live_detail_course_unpass_custom_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[last()-1]/div[2]/div/div/div[2]/form/div[2]/div/div/textarea'
        # 审核详情-课程审核-不通过-提交按钮
        self._course_live_detail_course_unpass_commit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[last()-1]/div[2]/div/div/div[3]/span/button[1]'
        # 审核详情-课程审核-不通过-返回按钮
        self._course_live_detail_course_unpass_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[last()-1]/div[2]/div/div/div[3]/span/button[2]'
        # 审核详情-课程审核-不通过-关闭按钮
        self._course_live_detail_course_unpass_close_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[last()-1]/div[2]/div/div/div[1]/button'
        # 审核详情课程-返回按钮
        self._course_live_detail_course_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[last()-1]/div[1]/button[3]'
        # 审核详情-操作记录-最后一个审核结果
        self._course_live_detail_exe_log_last_examine_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[last()]/div/div[2]/div/div/div[3]/table/tbody/tr[last()]/td[3]/div'
        # 1对1课-审核详情-课程标题
        self._course_one_detail_product_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[1]/div/div/div'
        # 1对1课-审核详情-上课模式
        self._course_one_detail_category_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[2]/div/div'
        # 1对1课-审核详情-课程id
        self._course_one_detail_goods_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[3]/div/div'
        # 1对1课-审核详情-课程副标题
        self._course_one_detail_sub_product_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[4]/div/div'
        # 1对1课-审核详情-发布时间
        self._course_one_detail_create_at_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[8]/div/div'
        # 1对1课-审核详情-课程状态
        self._course_one_detail_examine_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[9]/div/div/a/span'
        # 1对1课-审核详情-一级类目标签
        self._course_one_detail_first_label_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[3]/div[1]/div/div'
        # 1对1课-审核详情-二级类目标签
        self._course_one_detail_second_label_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[3]/div[2]/div/div'
        # 1对1课-审核详情-内容主题
        self._course_one_detail_sub_content_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[3]/div[3]/div/div'
        # 1对1课-审核详情-关键词
        self._course_one_detail_keywords_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[3]/div[4]/div/div'
        # 1对1课-审核详情-第一课节-课节名称
        self._course_one_detail_first_item_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[7]/div/div[1]/div[3]/table/tbody/tr/td[2]/div'
        # 1对1课-审核详情-第一课街-课件名称
        self._course_one_detail_first_item_pdf_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[7]/div/div[1]/div[3]/table/tbody/tr/td[3]/div/a/span'
        # 1对1课-审核详情-讲师姓名
        self._course_one_detail_teacher_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div[2]/form/div/div[1]/div/div'
        # 1对1课-审核详情-讲师id
        self._course_one_detail_teacher_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div[2]/form/div/div[2]/div/div'
        # 1对1课-审核详情-频道
        self._course_one_detail_channel_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div[2]/form/div/div[3]/div/div'
        # 1对1课-审核详情-角色类型
        self._course_one_detail_role_type_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div[2]/form/div/div[4]/div/div'
        # 1对1课-审核详情-问题一
        self._course_one_detail_first_question_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div[2]/div/div/div[3]/table/tbody/tr/td[2]/div'
        # 1对1课-审核详情-答案一
        self._course_one_detail_first_answer_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div[2]/div/div/div[3]/table/tbody/tr/td[3]/div'
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
    def loading_mask(self):
        """
        属性: 加载图层
        :return: 加载图层
        """
        element = None
        try:
            element = self.project.get_element(self._loading_mask_tag)
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
    def course_live_goods_id_input(self):
        """
        属性: 课程ID输入框
        :return: 课程ID输入框
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_goods_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_product_name_input(self):
        """
        属性: 课程标题输入框
        :return: 课程标题输入框
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_product_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_teacher_name_input(self):
        """
        属性: 讲师姓名输入框
        :return: 讲师姓名输入框
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_teacher_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_category_button(self):
        """
        属性: 上课模式下拉框
        :return: 上课模式下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_category_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_channel_button(self):
        """
        属性: 频道下拉框
        :return: 频道下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_channel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_state_button(self):
        """
        属性: 状态下拉框
        :return: 状态下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_state_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_state_pass_button(self):
        """
        属性: 状态审核通过按钮
        :return: 状态审核通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_state_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_role_button(self):
        """
        属性: 角色类型-下拉框
        :return: 角色类型-下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_role_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_class_state_button(self):
        """
        属性: 班次状态下拉框
        :return: 班次状态下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_class_state_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_update_time_start_time_input(self):
        """
        属性: 更新日期-开始日期输入框
        :return: 更新日期-开始日期输入框
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_update_time_start_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_update_time_end_time_input(self):
        """
        属性: 更新日期-结束日期输入框
        :return: 更新日期-结束日期输入框
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_update_time_end_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_search_button(self):
        """
        属性: 查询按钮
        :return: 查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_search_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_clear_button(self):
        """
        属性: 清除按钮
        :return: 清除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_list_first_course_state_text(self):
        """
        属性: 列表-第一个课程状态
        :return: 列表-第一个课程状态
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_list_first_course_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_list_first_button(self):
        """
        属性: 列表-第一个-操作按钮（审核/查看）
        :return: 列表-第一个-操作按钮（审核/查看）
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_list_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_product_name_text(self):
        """
        属性: 审核详情-课程标题
        :return: 审核详情-课程标题
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_product_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_category_text(self):
        """
        属性: 审核详情-上课模式
        :return: 审核详情-上课模式
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_category_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_goods_id_text(self):
        """
        属性: 审核详情-课程id
        :return: 审核详情-课程id
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_goods_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_sub_product_name_text(self):
        """
        属性: 审核详情-课程副标题
        :return: 审核详情-课程副标题
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_sub_product_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_create_at_text(self):
        """
        属性: 审核详情-发布时间
        :return: 审核详情-发布时间
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_create_at_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_examine_state_text(self):
        """
        属性: 审核详情-课程状态
        :return: 审核详情-课程状态
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_examine_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_label_text(self):
        """
        属性: 审核详情-一级类目标签
        :return: 审核详情-一级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_label_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_second_label_text(self):
        """
        属性: 审核详情-二级类目标签
        :return: 审核详情-二级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_second_label_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_sub_content_text(self):
        """
        属性: 审核详情-内容主题
        :return: 审核详情-内容主题
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_sub_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_keywords_text(self):
        """
        属性: 审核详情-关键词
        :return: 审核详情-关键词
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_keywords_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_feature_text(self):
        """
        属性: 审核详情-课程特色
        :return: 审核详情-课程特色
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_feature_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_restricted_sales_text(self):
        """
        属性: 审核详情-限售人数
        :return: 审核详情-限售人数
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_restricted_sales_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_item_name_text(self):
        """
        属性: 审核详情-第一课节-课节名称
        :return: 审核详情-第一课节-课节名称
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_item_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_item_pdf_name_text(self):
        """
        属性: 审核详情-第一课街-课件名称
        :return: 审核详情-第一课街-课件名称
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_item_pdf_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_item_pdf_name_button(self):
        """
        属性: 审核详情-第一课节-课件按钮
        :return: 审核详情-第一课节-课件按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_item_pdf_name_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_second_item_name_text(self):
        """
        属性: 审核详情-第二课节-课节名称
        :return: 审核详情-第二课节-课节名称
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_second_item_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_second_item_pdf_name_text(self):
        """
        属性: 审核详情-第二节课-课件名称
        :return: 审核详情-第二节课-课件名称
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_second_item_pdf_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_second_item_pdf_name_button(self):
        """
        属性: 审核详情-第二课节-课件按钮
        :return: 审核详情-第二课节-课件按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_second_item_pdf_name_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_teacher_name_text(self):
        """
        属性: 审核详情-讲师姓名
        :return: 审核详情-讲师姓名
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_teacher_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_teacher_id_text(self):
        """
        属性: 审核详情-讲师id
        :return: 审核详情-讲师id
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_teacher_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_channel_text(self):
        """
        属性: 审核详情-频道
        :return: 审核详情-频道
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_channel_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_role_type_text(self):
        """
        属性: 审核详情-角色类型
        :return: 审核详情-角色类型
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_role_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_question_text(self):
        """
        属性: 审核详情-问题一
        :return: 审核详情-问题一
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_question_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_answer_text(self):
        """
        属性: 审核详情-答案一
        :return: 审核详情-答案一
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_answer_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_second_question_text(self):
        """
        属性: 审核详情-问题二
        :return: 审核详情-问题二
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_second_question_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_second_answer_text(self):
        """
        属性: 审核详情-答案二
        :return: 审核详情-答案二
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_second_answer_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_class_name_text(self):
        """
        属性: 审核详情-班次一-班次名称
        :return: 审核详情-班次一-班次名称
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_class_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_class_date_text(self):
        """
        属性: 审核详情-班次一-班次周期
        :return: 审核详情-班次一-班次周期
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_class_date_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_class_price_text(self):
        """
        属性: 审核详情-班次一-销售价格
        :return: 审核详情-班次一-销售价格
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_class_price_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_class_discount_text(self):
        """
        属性: 审核详情-班次一-优惠价格
        :return: 审核详情-班次一-优惠价格
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_class_discount_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_class_is_group_text(self):
        """
        属性: 审核详情-班次一-优惠是否建群
        :return: 审核详情-班次一-优惠是否建群
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_class_is_group_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_class_create_at_text(self):
        """
        属性: 审核详情-班次一-创建时间
        :return: 审核详情-班次一-创建时间
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_class_create_at_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_class_update_at_text(self):
        """
        属性: 审核详情-班次一-更新时间
        :return: 审核详情-班次一-更新时间
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_class_update_at_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_class_state_text(self):
        """
        属性: 审核详情-班次一-班次状态
        :return: 审核详情-班次一-班次状态
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_class_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_class_pass_button(self):
        """
        属性: 审核详情-班次一-审核通过按钮
        :return: 审核详情-班次一-审核通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_class_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_class_pass_confirm_button(self):
        """
        属性: 审核详情-班次审核-通过-确定按钮
        :return: 审核详情-班次审核-通过-确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_class_pass_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_class_pass_cancel_button(self):
        """
        属性: 审核详情-班次审核-通过-取消按钮
        :return: 审核详情-班次审核-通过-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_class_pass_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_first_class_unpass_button(self):
        """
        属性: 审核详情-班次一-审核不通过按钮
        :return: 审核详情-班次一-审核不通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_first_class_unpass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_class_unpass_reason_button(self):
        """
        属性: 审核详情-班次审核-不通过-未通过理由下拉框
        :return: 审核详情-班次审核-不通过-未通过理由下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_class_unpass_reason_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_class_unpass_reason_custom_input(self):
        """
        属性: 审核详情-班次审核-不通过-未通过理由自定义输入框
        :return: 审核详情-班次审核-不通过-未通过理由自定义输入框
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_class_unpass_reason_custom_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_class_unpass_confirm_button(self):
        """
        属性: 审核详情-班次审核-不通过-提交按钮
        :return: 审核详情-班次审核-不通过-提交按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_class_unpass_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_class_unpass_cancel_button(self):
        """
        属性: 审核详情-班次审核-不通过-返回按钮
        :return: 审核详情-班次审核-不通过-返回按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_class_unpass_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_class_unpass_close_button(self):
        """
        属性: 审核详情-班次审核-不通过-关闭按钮
        :return: 审核详情-班次审核-不通过-关闭按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_class_unpass_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_course_pass_button(self):
        """
        属性: 审核详情-课程审核通过按钮
        :return: 审核详情-课程审核通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_course_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_detail_course_pass_confirm_box(self):
        """
        属性: 课程详情-弹出确认框
        :return: 课程详情-弹出确认框
        """
        element = None
        try:
            element = self.project.get_element(self._course_detail_course_pass_confirm_box_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_course_pass_confirm_button(self):
        """
        属性: 审核详情-课程审核通过-确认按钮
        :return: 审核详情-课程审核通过-确认按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_course_pass_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_course_pass_cancel_button(self):
        """
        属性: 审核详情-课程审核通过-取消按钮
        :return: 审核详情-课程审核通过-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_course_pass_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_course_unpass_button(self):
        """
        属性: 审核详情-课程审核不通过按钮
        :return: 审核详情-课程审核不通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_course_unpass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_course_unpass_reason_button(self):
        """
        属性: 审核详情-课程审核-不通过-未通过理由下拉框
        :return: 审核详情-课程审核-不通过-未通过理由下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_course_unpass_reason_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_course_unpass_custom_input(self):
        """
        属性: 审核详情-课程审核-不通过-自定义输入框
        :return: 审核详情-课程审核-不通过-自定义输入框
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_course_unpass_custom_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_course_unpass_commit_button(self):
        """
        属性: 审核详情-课程审核-不通过-提交按钮
        :return: 审核详情-课程审核-不通过-提交按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_course_unpass_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_course_unpass_cancel_button(self):
        """
        属性: 审核详情-课程审核-不通过-返回按钮
        :return: 审核详情-课程审核-不通过-返回按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_course_unpass_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_course_unpass_close_button(self):
        """
        属性: 审核详情-课程审核-不通过-关闭按钮
        :return: 审核详情-课程审核-不通过-关闭按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_course_unpass_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_course_cancel_button(self):
        """
        属性: 审核详情课程-返回按钮
        :return: 审核详情课程-返回按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_course_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_live_detail_exe_log_last_examine_state_text(self):
        """
        属性: 审核详情-操作记录-最后一个审核结果
        :return: 审核详情-操作记录-最后一个审核结果
        """
        element = None
        try:
            element = self.project.get_element(self._course_live_detail_exe_log_last_examine_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_product_name_text(self):
        """
        属性: 1对1课-审核详情-课程标题
        :return: 1对1课-审核详情-课程标题
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_product_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_category_text(self):
        """
        属性: 1对1课-审核详情-上课模式
        :return: 1对1课-审核详情-上课模式
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_category_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_goods_id_text(self):
        """
        属性: 1对1课-审核详情-课程id
        :return: 1对1课-审核详情-课程id
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_goods_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_sub_product_name_text(self):
        """
        属性: 1对1课-审核详情-课程副标题
        :return: 1对1课-审核详情-课程副标题
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_sub_product_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_create_at_text(self):
        """
        属性: 1对1课-审核详情-发布时间
        :return: 1对1课-审核详情-发布时间
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_create_at_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_examine_state_text(self):
        """
        属性: 1对1课-审核详情-课程状态
        :return: 1对1课-审核详情-课程状态
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_examine_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_first_label_text(self):
        """
        属性: 1对1课-审核详情-一级类目标签
        :return: 1对1课-审核详情-一级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_first_label_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_second_label_text(self):
        """
        属性: 1对1课-审核详情-二级类目标签
        :return: 1对1课-审核详情-二级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_second_label_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_sub_content_text(self):
        """
        属性: 1对1课-审核详情-内容主题
        :return: 1对1课-审核详情-内容主题
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_sub_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_keywords_text(self):
        """
        属性: 1对1课-审核详情-关键词
        :return: 1对1课-审核详情-关键词
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_keywords_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_first_item_name_text(self):
        """
        属性: 1对1课-审核详情-第一课节-课节名称
        :return: 1对1课-审核详情-第一课节-课节名称
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_first_item_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_first_item_pdf_name_text(self):
        """
        属性: 1对1课-审核详情-第一课街-课件名称
        :return: 1对1课-审核详情-第一课街-课件名称
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_first_item_pdf_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_teacher_name_text(self):
        """
        属性: 1对1课-审核详情-讲师姓名
        :return: 1对1课-审核详情-讲师姓名
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_teacher_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_teacher_id_text(self):
        """
        属性: 1对1课-审核详情-讲师id
        :return: 1对1课-审核详情-讲师id
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_teacher_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_channel_text(self):
        """
        属性: 1对1课-审核详情-频道
        :return: 1对1课-审核详情-频道
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_channel_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_role_type_text(self):
        """
        属性: 1对1课-审核详情-角色类型
        :return: 1对1课-审核详情-角色类型
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_role_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_first_question_text(self):
        """
        属性: 1对1课-审核详情-问题一
        :return: 1对1课-审核详情-问题一
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_first_question_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_one_detail_first_answer_text(self):
        """
        属性: 1对1课-审核详情-答案一
        :return: 1对1课-审核详情-答案一
        """
        element = None
        try:
            element = self.project.get_element(self._course_one_detail_first_answer_text_tag)
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

    def set_course_live_goods_id_input_action(self, course_live_goods_id_input):
        """
        动作：设置课程ID输入框
        :param course_live_goods_id_input: 课程ID输入框
        :return: 设置'课程ID输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.course_live_goods_id_input, course_live_goods_id_input)
        return self.project.get_current_page_source()

    def set_course_live_product_name_input_action(self, course_live_product_name_input):
        """
        动作：设置课程标题输入框
        :param course_live_product_name_input: 课程标题输入框
        :return: 设置'课程标题输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.course_live_product_name_input, course_live_product_name_input)
        return self.project.get_current_page_source()

    def set_course_live_teacher_name_input_action(self, course_live_teacher_name_input):
        """
        动作：设置讲师姓名输入框
        :param course_live_teacher_name_input: 讲师姓名输入框
        :return: 设置'讲师姓名输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.course_live_teacher_name_input, course_live_teacher_name_input)
        return self.project.get_current_page_source()

    def click_course_live_category_button_action(self):
        """
        动作：点击上课模式下拉框
        :return: 点击'上课模式下拉框'按钮后的页面
        """
        self.project.click(self.course_live_category_button)
        return self.project.get_current_page_source()

    def click_course_live_channel_button_action(self):
        """
        动作：点击频道下拉框
        :return: 点击'频道下拉框'按钮后的页面
        """
        self.project.click(self.course_live_channel_button)
        return self.project.get_current_page_source()

    def click_course_live_state_button_action(self):
        """
        动作：点击状态下拉框
        :return: 点击'状态下拉框'按钮后的页面
        """
        self.project.click(self.course_live_state_button)
        return self.project.get_current_page_source()

    def click_course_live_state_pass_button_action(self):
        """
        动作：点击状态审核通过按钮
        :return: 点击'状态审核通过按钮'按钮后的页面
        """
        self.project.click(self.course_live_state_pass_button)
        return self.project.get_current_page_source()

    def click_course_live_role_button_action(self):
        """
        动作：点击角色类型-下拉框
        :return: 点击'角色类型-下拉框'按钮后的页面
        """
        self.project.click(self.course_live_role_button)
        return self.project.get_current_page_source()

    def click_course_live_class_state_button_action(self):
        """
        动作：点击班次状态下拉框
        :return: 点击'班次状态下拉框'按钮后的页面
        """
        self.project.click(self.course_live_class_state_button)
        return self.project.get_current_page_source()

    def set_course_live_update_time_start_time_input_action(self, course_live_update_time_start_time_input):
        """
        动作：设置更新日期-开始日期输入框
        :param course_live_update_time_start_time_input: 更新日期-开始日期输入框
        :return: 设置'更新日期-开始日期输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.course_live_update_time_start_time_input, course_live_update_time_start_time_input)
        return self.project.get_current_page_source()

    def set_course_live_update_time_end_time_input_action(self, course_live_update_time_end_time_input):
        """
        动作：设置更新日期-结束日期输入框
        :param course_live_update_time_end_time_input: 更新日期-结束日期输入框
        :return: 设置'更新日期-结束日期输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.course_live_update_time_end_time_input, course_live_update_time_end_time_input)
        return self.project.get_current_page_source()

    def click_course_live_search_button_action(self):
        """
        动作：点击查询按钮
        :return: 点击'查询按钮'按钮后的页面
        """
        self.project.click(self.course_live_search_button)
        return self.project.get_current_page_source()

    def click_course_live_clear_button_action(self):
        """
        动作：点击清除按钮
        :return: 点击'清除按钮'按钮后的页面
        """
        self.project.click(self.course_live_clear_button)
        return self.project.get_current_page_source()

    def get_course_live_list_first_course_state_text_action(self):
        """
        动作：获取列表-第一个课程状态的文本
        :return: '列表-第一个课程状态'的文本
        """
        control_content = self.project.get_element_text(self.course_live_list_first_course_state_text)
        return control_content

    def click_course_live_list_first_button_action(self):
        """
        动作：点击列表-第一个-操作按钮（审核/查看）
        :return: 点击'列表-第一个-操作按钮（审核/查看）'按钮后的页面
        """
        self.project.click(self.course_live_list_first_button)
        return self.project.get_current_page_source()

    def get_course_live_detail_product_name_text_action(self):
        """
        动作：获取审核详情-课程标题的文本
        :return: '审核详情-课程标题'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_product_name_text)
        return control_content

    def get_course_live_detail_category_text_action(self):
        """
        动作：获取审核详情-上课模式的文本
        :return: '审核详情-上课模式'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_category_text)
        return control_content

    def get_course_live_detail_goods_id_text_action(self):
        """
        动作：获取审核详情-课程id的文本
        :return: '审核详情-课程id'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_goods_id_text)
        return control_content

    def get_course_live_detail_sub_product_name_text_action(self):
        """
        动作：获取审核详情-课程副标题的文本
        :return: '审核详情-课程副标题'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_sub_product_name_text)
        return control_content

    def get_course_live_detail_create_at_text_action(self):
        """
        动作：获取审核详情-发布时间的文本
        :return: '审核详情-发布时间'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_create_at_text)
        return control_content

    def get_course_live_detail_examine_state_text_action(self):
        """
        动作：获取审核详情-课程状态的文本
        :return: '审核详情-课程状态'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_examine_state_text)
        return control_content

    def get_course_live_detail_first_label_text_action(self):
        """
        动作：获取审核详情-一级类目标签的文本
        :return: '审核详情-一级类目标签'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_first_label_text)
        return control_content

    def get_course_live_detail_second_label_text_action(self):
        """
        动作：获取审核详情-二级类目标签的文本
        :return: '审核详情-二级类目标签'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_second_label_text)
        return control_content

    def get_course_live_detail_sub_content_text_action(self):
        """
        动作：获取审核详情-内容主题的文本
        :return: '审核详情-内容主题'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_sub_content_text)
        return control_content

    def get_course_live_detail_keywords_text_action(self):
        """
        动作：获取审核详情-关键词的文本
        :return: '审核详情-关键词'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_keywords_text)
        return control_content

    def get_course_live_detail_feature_text_action(self):
        """
        动作：获取审核详情-课程特色的文本
        :return: '审核详情-课程特色'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_feature_text)
        return control_content

    def get_course_live_detail_restricted_sales_text_action(self):
        """
        动作：获取审核详情-限售人数的文本
        :return: '审核详情-限售人数'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_restricted_sales_text)
        return control_content

    def get_course_live_detail_first_item_name_text_action(self):
        """
        动作：获取审核详情-第一课节-课节名称的文本
        :return: '审核详情-第一课节-课节名称'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_first_item_name_text)
        return control_content

    def get_course_live_detail_first_item_pdf_name_text_action(self):
        """
        动作：获取审核详情-第一课街-课件名称的文本
        :return: '审核详情-第一课街-课件名称'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_first_item_pdf_name_text)
        return control_content

    def click_course_live_detail_first_item_pdf_name_button_action(self):
        """
        动作：点击审核详情-第一课节-课件按钮
        :return: 点击'审核详情-第一课节-课件按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_first_item_pdf_name_button)
        return self.project.get_current_page_source()

    def get_course_live_detail_second_item_name_text_action(self):
        """
        动作：获取审核详情-第二课节-课节名称的文本
        :return: '审核详情-第二课节-课节名称'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_second_item_name_text)
        return control_content

    def get_course_live_detail_second_item_pdf_name_text_action(self):
        """
        动作：获取审核详情-第二节课-课件名称的文本
        :return: '审核详情-第二节课-课件名称'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_second_item_pdf_name_text)
        return control_content

    def click_course_live_detail_second_item_pdf_name_button_action(self):
        """
        动作：点击审核详情-第二课节-课件按钮
        :return: 点击'审核详情-第二课节-课件按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_second_item_pdf_name_button)
        return self.project.get_current_page_source()

    def get_course_live_detail_teacher_name_text_action(self):
        """
        动作：获取审核详情-讲师姓名的文本
        :return: '审核详情-讲师姓名'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_teacher_name_text)
        return control_content

    def get_course_live_detail_teacher_id_text_action(self):
        """
        动作：获取审核详情-讲师id的文本
        :return: '审核详情-讲师id'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_teacher_id_text)
        return control_content

    def get_course_live_detail_channel_text_action(self):
        """
        动作：获取审核详情-频道的文本
        :return: '审核详情-频道'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_channel_text)
        return control_content

    def get_course_live_detail_role_type_text_action(self):
        """
        动作：获取审核详情-角色类型的文本
        :return: '审核详情-角色类型'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_role_type_text)
        return control_content

    def get_course_live_detail_first_question_text_action(self):
        """
        动作：获取审核详情-问题一的文本
        :return: '审核详情-问题一'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_first_question_text)
        return control_content

    def get_course_live_detail_first_answer_text_action(self):
        """
        动作：获取审核详情-答案一的文本
        :return: '审核详情-答案一'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_first_answer_text)
        return control_content

    def get_course_live_detail_second_question_text_action(self):
        """
        动作：获取审核详情-问题二的文本
        :return: '审核详情-问题二'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_second_question_text)
        return control_content

    def get_course_live_detail_second_answer_text_action(self):
        """
        动作：获取审核详情-答案二的文本
        :return: '审核详情-答案二'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_second_answer_text)
        return control_content

    def get_course_live_detail_first_class_name_text_action(self):
        """
        动作：获取审核详情-班次一-班次名称的文本
        :return: '审核详情-班次一-班次名称'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_first_class_name_text)
        return control_content

    def get_course_live_detail_first_class_date_text_action(self):
        """
        动作：获取审核详情-班次一-班次周期的文本
        :return: '审核详情-班次一-班次周期'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_first_class_date_text)
        return control_content

    def get_course_live_detail_first_class_price_text_action(self):
        """
        动作：获取审核详情-班次一-销售价格的文本
        :return: '审核详情-班次一-销售价格'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_first_class_price_text)
        return control_content

    def get_course_live_detail_first_class_discount_text_action(self):
        """
        动作：获取审核详情-班次一-优惠价格的文本
        :return: '审核详情-班次一-优惠价格'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_first_class_discount_text)
        return control_content

    def get_course_live_detail_first_class_is_group_text_action(self):
        """
        动作：获取审核详情-班次一-优惠是否建群的文本
        :return: '审核详情-班次一-优惠是否建群'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_first_class_is_group_text)
        return control_content

    def get_course_live_detail_first_class_create_at_text_action(self):
        """
        动作：获取审核详情-班次一-创建时间的文本
        :return: '审核详情-班次一-创建时间'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_first_class_create_at_text)
        return control_content

    def get_course_live_detail_first_class_update_at_text_action(self):
        """
        动作：获取审核详情-班次一-更新时间的文本
        :return: '审核详情-班次一-更新时间'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_first_class_update_at_text)
        return control_content

    def get_course_live_detail_first_class_state_text_action(self):
        """
        动作：获取审核详情-班次一-班次状态的文本
        :return: '审核详情-班次一-班次状态'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_first_class_state_text)
        return control_content

    def click_course_live_detail_first_class_pass_button_action(self):
        """
        动作：点击审核详情-班次一-审核通过按钮
        :return: 点击'审核详情-班次一-审核通过按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_first_class_pass_button)
        return self.project.get_current_page_source()

    def click_course_live_detail_class_pass_confirm_button_action(self):
        """
        动作：点击审核详情-班次审核-通过-确定按钮
        :return: 点击'审核详情-班次审核-通过-确定按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_class_pass_confirm_button)
        return self.project.get_current_page_source()

    def click_course_live_detail_class_pass_cancel_button_action(self):
        """
        动作：点击审核详情-班次审核-通过-取消按钮
        :return: 点击'审核详情-班次审核-通过-取消按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_class_pass_cancel_button)
        return self.project.get_current_page_source()

    def click_course_live_detail_first_class_unpass_button_action(self):
        """
        动作：点击审核详情-班次一-审核不通过按钮
        :return: 点击'审核详情-班次一-审核不通过按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_first_class_unpass_button)
        return self.project.get_current_page_source()

    def click_course_live_detail_class_unpass_reason_button_action(self):
        """
        动作：点击审核详情-班次审核-不通过-未通过理由下拉框
        :return: 点击'审核详情-班次审核-不通过-未通过理由下拉框'按钮后的页面
        """
        self.project.click(self.course_live_detail_class_unpass_reason_button)
        return self.project.get_current_page_source()

    def set_course_live_detail_class_unpass_reason_custom_input_action(self, course_live_detail_class_unpass_reason_custom_input):
        """
        动作：设置审核详情-班次审核-不通过-未通过理由自定义输入框
        :param course_live_detail_class_unpass_reason_custom_input: 审核详情-班次审核-不通过-未通过理由自定义输入框
        :return: 设置'审核详情-班次审核-不通过-未通过理由自定义输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.course_live_detail_class_unpass_reason_custom_input, course_live_detail_class_unpass_reason_custom_input)
        return self.project.get_current_page_source()

    def click_course_live_detail_class_unpass_confirm_button_action(self):
        """
        动作：点击审核详情-班次审核-不通过-提交按钮
        :return: 点击'审核详情-班次审核-不通过-提交按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_class_unpass_confirm_button)
        return self.project.get_current_page_source()

    def click_course_live_detail_class_unpass_cancel_button_action(self):
        """
        动作：点击审核详情-班次审核-不通过-返回按钮
        :return: 点击'审核详情-班次审核-不通过-返回按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_class_unpass_cancel_button)
        return self.project.get_current_page_source()

    def click_course_live_detail_class_unpass_close_button_action(self):
        """
        动作：点击审核详情-班次审核-不通过-关闭按钮
        :return: 点击'审核详情-班次审核-不通过-关闭按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_class_unpass_close_button)
        return self.project.get_current_page_source()

    def click_course_live_detail_course_pass_button_action(self):
        """
        动作：点击审核详情-课程审核通过按钮
        :return: 点击'审核详情-课程审核通过按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_course_pass_button)
        return self.project.get_current_page_source()

    def click_course_live_detail_course_pass_confirm_button_action(self):
        """
        动作：点击审核详情-课程审核通过-确认按钮
        :return: 点击'审核详情-课程审核通过-确认按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_course_pass_confirm_button)
        return self.project.get_current_page_source()

    def click_course_live_detail_course_pass_cancel_button_action(self):
        """
        动作：点击审核详情-课程审核通过-取消按钮
        :return: 点击'审核详情-课程审核通过-取消按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_course_pass_cancel_button)
        return self.project.get_current_page_source()

    def click_course_live_detail_course_unpass_button_action(self):
        """
        动作：点击审核详情-课程审核不通过按钮
        :return: 点击'审核详情-课程审核不通过按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_course_unpass_button)
        return self.project.get_current_page_source()

    def click_course_live_detail_course_unpass_reason_button_action(self):
        """
        动作：点击审核详情-课程审核-不通过-未通过理由下拉框
        :return: 点击'审核详情-课程审核-不通过-未通过理由下拉框'按钮后的页面
        """
        self.project.click(self.course_live_detail_course_unpass_reason_button)
        return self.project.get_current_page_source()

    def set_course_live_detail_course_unpass_custom_input_action(self, course_live_detail_course_unpass_custom_input):
        """
        动作：设置审核详情-课程审核-不通过-自定义输入框
        :param course_live_detail_course_unpass_custom_input: 审核详情-课程审核-不通过-自定义输入框
        :return: 设置'审核详情-课程审核-不通过-自定义输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.course_live_detail_course_unpass_custom_input, course_live_detail_course_unpass_custom_input)
        return self.project.get_current_page_source()

    def click_course_live_detail_course_unpass_commit_button_action(self):
        """
        动作：点击审核详情-课程审核-不通过-提交按钮
        :return: 点击'审核详情-课程审核-不通过-提交按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_course_unpass_commit_button)
        return self.project.get_current_page_source()

    def click_course_live_detail_course_unpass_cancel_button_action(self):
        """
        动作：点击审核详情-课程审核-不通过-返回按钮
        :return: 点击'审核详情-课程审核-不通过-返回按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_course_unpass_cancel_button)
        return self.project.get_current_page_source()

    def click_course_live_detail_course_unpass_close_button_action(self):
        """
        动作：点击审核详情-课程审核-不通过-关闭按钮
        :return: 点击'审核详情-课程审核-不通过-关闭按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_course_unpass_close_button)
        return self.project.get_current_page_source()

    def click_course_live_detail_course_cancel_button_action(self):
        """
        动作：点击审核详情课程-返回按钮
        :return: 点击'审核详情课程-返回按钮'按钮后的页面
        """
        self.project.click(self.course_live_detail_course_cancel_button)
        return self.project.get_current_page_source()

    def get_course_live_detail_exe_log_last_examine_state_text_action(self):
        """
        动作：获取审核详情-操作记录-最后一个审核结果的文本
        :return: '审核详情-操作记录-最后一个审核结果'的文本
        """
        control_content = self.project.get_element_text(self.course_live_detail_exe_log_last_examine_state_text)
        return control_content

    def get_course_one_detail_product_name_text_action(self):
        """
        动作：获取1对1课-审核详情-课程标题的文本
        :return: '1对1课-审核详情-课程标题'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_product_name_text)
        return control_content

    def get_course_one_detail_category_text_action(self):
        """
        动作：获取1对1课-审核详情-上课模式的文本
        :return: '1对1课-审核详情-上课模式'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_category_text)
        return control_content

    def get_course_one_detail_goods_id_text_action(self):
        """
        动作：获取1对1课-审核详情-课程id的文本
        :return: '1对1课-审核详情-课程id'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_goods_id_text)
        return control_content

    def get_course_one_detail_sub_product_name_text_action(self):
        """
        动作：获取1对1课-审核详情-课程副标题的文本
        :return: '1对1课-审核详情-课程副标题'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_sub_product_name_text)
        return control_content

    def get_course_one_detail_create_at_text_action(self):
        """
        动作：获取1对1课-审核详情-发布时间的文本
        :return: '1对1课-审核详情-发布时间'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_create_at_text)
        return control_content

    def get_course_one_detail_examine_state_text_action(self):
        """
        动作：获取1对1课-审核详情-课程状态的文本
        :return: '1对1课-审核详情-课程状态'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_examine_state_text)
        return control_content

    def get_course_one_detail_first_label_text_action(self):
        """
        动作：获取1对1课-审核详情-一级类目标签的文本
        :return: '1对1课-审核详情-一级类目标签'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_first_label_text)
        return control_content

    def get_course_one_detail_second_label_text_action(self):
        """
        动作：获取1对1课-审核详情-二级类目标签的文本
        :return: '1对1课-审核详情-二级类目标签'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_second_label_text)
        return control_content

    def get_course_one_detail_sub_content_text_action(self):
        """
        动作：获取1对1课-审核详情-内容主题的文本
        :return: '1对1课-审核详情-内容主题'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_sub_content_text)
        return control_content

    def get_course_one_detail_keywords_text_action(self):
        """
        动作：获取1对1课-审核详情-关键词的文本
        :return: '1对1课-审核详情-关键词'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_keywords_text)
        return control_content

    def get_course_one_detail_first_item_name_text_action(self):
        """
        动作：获取1对1课-审核详情-第一课节-课节名称的文本
        :return: '1对1课-审核详情-第一课节-课节名称'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_first_item_name_text)
        return control_content

    def get_course_one_detail_first_item_pdf_name_text_action(self):
        """
        动作：获取1对1课-审核详情-第一课街-课件名称的文本
        :return: '1对1课-审核详情-第一课街-课件名称'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_first_item_pdf_name_text)
        return control_content

    def get_course_one_detail_teacher_name_text_action(self):
        """
        动作：获取1对1课-审核详情-讲师姓名的文本
        :return: '1对1课-审核详情-讲师姓名'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_teacher_name_text)
        return control_content

    def get_course_one_detail_teacher_id_text_action(self):
        """
        动作：获取1对1课-审核详情-讲师id的文本
        :return: '1对1课-审核详情-讲师id'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_teacher_id_text)
        return control_content

    def get_course_one_detail_channel_text_action(self):
        """
        动作：获取1对1课-审核详情-频道的文本
        :return: '1对1课-审核详情-频道'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_channel_text)
        return control_content

    def get_course_one_detail_role_type_text_action(self):
        """
        动作：获取1对1课-审核详情-角色类型的文本
        :return: '1对1课-审核详情-角色类型'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_role_type_text)
        return control_content

    def get_course_one_detail_first_question_text_action(self):
        """
        动作：获取1对1课-审核详情-问题一的文本
        :return: '1对1课-审核详情-问题一'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_first_question_text)
        return control_content

    def get_course_one_detail_first_answer_text_action(self):
        """
        动作：获取1对1课-审核详情-答案一的文本
        :return: '1对1课-审核详情-答案一'的文本
        """
        control_content = self.project.get_element_text(self.course_one_detail_first_answer_text)
        return control_content

    # endregion Actions
