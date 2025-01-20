from Utils.Log import log


"""
后台首页-运营中心-审核管理-录播课程审核
console_url/review/course_record
"""


class ConsoleOperationCenterReviewCourseRecordPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/review/course_record'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 课程ID输入框
        self._course_record_goods_id_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 课程标题输入框
        self._course_record_product_name_input_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 讲师姓名输入框
        self._course_record_teacher_name_input_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div/input'
        # 上课模式下拉框
        self._course_record_category_button_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div'
        # 上课模式-下拉列表
        self._course_record_category_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 频道下拉框
        self._course_record_channel_button_tag = '//*[@id="tableSearch"]/form/div/div[5]/div/div'
        # 频道-下拉列表
        self._course_record_channel_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 课程状态下拉框
        self._course_record_state_button_tag = '//*[@id="tableSearch"]/form/div/div[6]/div/div'
        # 课程状态-下拉列表
        self._course_record_state_all_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 角色类型下拉框
        self._course_record_role_button_tag = '//*[@id="tableSearch"]/form/div/div[7]/div/div'
        # 角色类型-下拉列表
        self._course_record_role_all_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 课节状态下拉框
        self._course_record_item_state_button_tag = '//*[@id="tableSearch"]/form/div/div[8]/div/div'
        # 课节状态-下拉列表
        self._course_record_item_state_all_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 更新日期-开始日期输入框
        self._course_record_update_time_start_time_input_tag = '//*[@id="tableSearch"]/form/div/div[9]/div/div/input[1]'
        # 更新日期-结束日期输入框
        self._course_record_update_time_end_time_input_tag = '//*[@id="tableSearch"]/form/div/div[9]/div/div/input[2]'
        # 查询按钮
        self._course_record_search_button_tag = '//*[@id="tableSearch"]/form/div/div[10]/div/button'
        # 清楚按钮
        self._course_record_clear_button_tag = '//*[@id="tableSearch"]/form/div/div[11]/div/button'
        # 第一行操作按钮（审核/查看）
        self._course_record_first_line_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[13]/div/a'
        # 第一行课程状态
        self._course_record_first_line_course_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[11]/div'
        # 审核详情-课程标题
        self._course_record_detail_product_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[1]/div/div/div'
        # 审核详情-上课模式
        self._course_record_detail_category_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[2]/div/div'
        # 审核详情-课程id
        self._course_record_detail_goods_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[3]/div/div'
        # 审核详情-课程副标题
        self._course_record_detail_sub_product_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[4]/div/div'
        # 审核详情-销售价格
        self._course_record_detail_price_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[5]/div/div'
        # 审核详情-优惠价格
        self._course_record_detail_discount_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[6]/div/div'
        # 审核详情-发布时间
        self._course_record_detail_created_at_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[8]/div/div'
        # 审核详情-课程状态
        self._course_record_detail_goods_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[9]/div/div/a/span'
        # 审核详情-课程分类
        self._course_record_detail_first_label_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[3]/div[1]/div/div'
        # 审核详情课程标签
        self._course_record_detail_second_label_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[3]/div[2]/div/div'
        # 审核详情-内容主题
        self._course_record_detail_sub_content_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[3]/div[3]/div/div'
        # 审核详情-关键词
        self._course_record_detail_keywords_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[3]/div[4]/div/div'
        # 审核详情-课程有效期
        self._course_record_detail_review_date_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[5]/div[1]/div/div'
        # 审核详情-是否建群
        self._course_record_detail_is_group_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[5]/div[2]/div/div'
        # 审核详情-课程特色
        self._course_record_detail_feature_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/form/div[5]/div[3]/div/div'
        # 审核详情-讲师姓名
        self._course_record_detail_teacher_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div[2]/form/div/div[1]/div/div'
        # 审核详情-讲师id
        self._course_record_detail_teacher_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div[2]/form/div/div[2]/div/div'
        # 审核详情-频道
        self._course_record_detail_channel_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div[2]/form/div/div[3]/div/div'
        # 审核详情-角色类型
        self._course_record_detail_role_type_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div/div[2]/form/div/div[4]/div/div'
        # 审核详情-问题一
        self._course_record_detail_first_question_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[2]/div'
        # 审核详情-答案一
        self._course_record_detail_first_answer_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[3]/div'
        # 审核详情-问题二
        self._course_record_detail_second_question_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div[2]/div/div/div[3]/table/tbody/tr[2]/td[2]/div'
        # 审核详情-答案二
        self._course_record_detail_second_answer_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[4]/div/div[2]/div/div/div[3]/table/tbody/tr[2]/td[3]/div'
        # 审核详情-第一个课节-名称
        self._course_record_detail_first_item_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 审核详情-第一个课节-视频名称
        self._course_record_detail_first_item_video_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div[1]/div[3]/table/tbody/tr[1]/td[4]/div/a/span'
        # 审核详情-第一个课节-审核通过按钮
        self._course_record_detail_first_item_pass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr/td[10]/div/a[1]/span'
        # 审核详情-第一个课节-审核不通过按钮
        self._course_record_detail_first_item_unpass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/a[2]/span'
        # 审核详情-第二个课节-名称
        self._course_record_detail_second_item_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div[1]/div[3]/table/tbody/tr[2]/td[2]/div'
        # 审核详情-第二个课节-视频名称
        self._course_record_detail_second_item_video_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div[1]/div[3]/table/tbody/tr[2]/td[4]/div/a/span'
        # 审核详情-第二个课节-审核通过按钮
        self._course_record_detail_second_item_pass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr[2]/td[10]/div/a[1]/span'
        # 审核详情-第二个课节-审核不通过按钮
        self._course_record_detail_second_item_unpass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[1]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr[2]/td[10]/div/a[2]/span'
        # 审核详情-课节审核通过确定按钮
        self._course_record_detail_item_pass_confirm_button_tag = '/html/body/div[last()-1]/div/div[3]/button[2]'
        # 审核详情-课节审核通过取消按钮
        self._course_record_detail_item_pass_cancel_button_tag = '/html/body/div[last()-1]/div/div[3]/button[1]'
        # 审核详情-课节审核不通过-未通过理由下拉框
        self._course_record_detail_item_unpass_reason_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[2]/div/div/div[2]/form/div[1]/div/div'
        # 审核详情-课节审核不通过-未通过理由-下拉列表
        self._course_record_detail_item_unpass_reason_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 审核详情-课节审核不通过-自定义输入框
        self._course_record_detail_item_unpass_custom_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[2]/div/div/div[2]/form/div[2]/div/div/textarea'
        # 审核详情-课节审核不通过-提交按钮
        self._course_record_detail_item_unpass_commit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[2]/div/div/div[3]/span/button[1]'
        # 审核详情-课节审核不通过-返回按钮
        self._course_record_detail_item_unpass_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[2]/div/div/div[3]/span/button[2]'
        # 审核详情-课节审核不通过-关闭按钮
        self._course_record_detail_item_unpass_close_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[5]/div[2]/div/div/div[1]/button'
        # 审核详情-课程审核通过按钮
        self._course_record_detail_course_pass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[6]/div[1]/button[1]'
        # 审核详情-课程课程审核不通过按钮
        self._course_record_detail_course_unpass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[6]/div[1]/button[2]'
        # 审核详情-课程返回按钮
        self._course_record_detail_course_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[6]/div[1]/button[3]'
        # 审核详情-课程审核通过-确认按钮
        self._course_record_detail_course_pass_confirm_button_tag = '/html/body/div[last()-1]/div/div[3]/button[2]'
        # 审核详情-课程审核通过-取消按钮
        self._course_record_detail_course_pass_cancel_button_tag = '/html/body/div[last()-1]/div/div[3]/button[1]'
        # 审核详情-课程审核不通过-未通过理由下拉框
        self._course_record_detail_course_unpass_reason_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[6]/div[2]/div/div/div[2]/form/div[1]/div/div'
        # 审核详情-课程审核不通过理由自定义按钮
        self._course_record_detail_course_unpass_reason_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 审核详情-课程审核不通过理由自定义输入框
        self._course_record_detail_course_unpass_reason_custom_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[6]/div[2]/div/div/div[2]/form/div[2]/div/div/textarea'
        # 审核详情-课程审核不通过-提交按钮
        self._course_record_detail_course_unpass_commit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[6]/div[2]/div/div/div[3]/span/button[1]'
        # 审核详情-课程审核不通过-取消按钮
        self._course_record_detail_course_unpass_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[6]/div[2]/div/div/div[3]/span/button[2]'
        # 审核详情-操作记录最后一个审核结果
        self._course_record_detail_exe_log_last_examine_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[7]/div/div[2]/div/div/div[3]/table/tbody/tr[last()]/td[3]/div'
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
    def course_record_goods_id_input(self):
        """
        属性: 课程ID输入框
        :return: 课程ID输入框
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_goods_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_product_name_input(self):
        """
        属性: 课程标题输入框
        :return: 课程标题输入框
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_product_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_teacher_name_input(self):
        """
        属性: 讲师姓名输入框
        :return: 讲师姓名输入框
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_teacher_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_category_button(self):
        """
        属性: 上课模式下拉框
        :return: 上课模式下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_category_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_category_select(self):
        """
        属性: 上课模式-下拉列表
        :return: 上课模式-下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_category_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_channel_button(self):
        """
        属性: 频道下拉框
        :return: 频道下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_channel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_channel_select(self):
        """
        属性: 频道-下拉列表
        :return: 频道-下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_channel_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_state_button(self):
        """
        属性: 课程状态下拉框
        :return: 课程状态下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_state_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_state_all_button(self):
        """
        属性: 课程状态-下拉列表
        :return: 课程状态-下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_state_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_role_button(self):
        """
        属性: 角色类型下拉框
        :return: 角色类型下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_role_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_role_all_button(self):
        """
        属性: 角色类型-下拉列表
        :return: 角色类型-下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_role_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_item_state_button(self):
        """
        属性: 课节状态下拉框
        :return: 课节状态下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_item_state_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_item_state_all_button(self):
        """
        属性: 课节状态-下拉列表
        :return: 课节状态-下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_item_state_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_update_time_start_time_input(self):
        """
        属性: 更新日期-开始日期输入框
        :return: 更新日期-开始日期输入框
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_update_time_start_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_update_time_end_time_input(self):
        """
        属性: 更新日期-结束日期输入框
        :return: 更新日期-结束日期输入框
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_update_time_end_time_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_search_button(self):
        """
        属性: 查询按钮
        :return: 查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_search_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_clear_button(self):
        """
        属性: 清楚按钮
        :return: 清楚按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_first_line_button(self):
        """
        属性: 第一行操作按钮（审核/查看）
        :return: 第一行操作按钮（审核/查看）
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_first_line_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_first_line_course_state_text(self):
        """
        属性: 第一行课程状态
        :return: 第一行课程状态
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_first_line_course_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_product_name_text(self):
        """
        属性: 审核详情-课程标题
        :return: 审核详情-课程标题
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_product_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_category_text(self):
        """
        属性: 审核详情-上课模式
        :return: 审核详情-上课模式
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_category_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_goods_id_text(self):
        """
        属性: 审核详情-课程id
        :return: 审核详情-课程id
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_goods_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_sub_product_name_text(self):
        """
        属性: 审核详情-课程副标题
        :return: 审核详情-课程副标题
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_sub_product_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_price_text(self):
        """
        属性: 审核详情-销售价格
        :return: 审核详情-销售价格
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_price_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_discount_text(self):
        """
        属性: 审核详情-优惠价格
        :return: 审核详情-优惠价格
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_discount_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_created_at_text(self):
        """
        属性: 审核详情-发布时间
        :return: 审核详情-发布时间
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_created_at_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_goods_state_text(self):
        """
        属性: 审核详情-课程状态
        :return: 审核详情-课程状态
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_goods_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_first_label_text(self):
        """
        属性: 审核详情-课程分类
        :return: 审核详情-课程分类
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_first_label_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_second_label_text(self):
        """
        属性: 审核详情课程标签
        :return: 审核详情课程标签
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_second_label_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_sub_content_text(self):
        """
        属性: 审核详情-内容主题
        :return: 审核详情-内容主题
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_sub_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_keywords_text(self):
        """
        属性: 审核详情-关键词
        :return: 审核详情-关键词
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_keywords_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_review_date_text(self):
        """
        属性: 审核详情-课程有效期
        :return: 审核详情-课程有效期
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_review_date_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_is_group_text(self):
        """
        属性: 审核详情-是否建群
        :return: 审核详情-是否建群
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_is_group_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_feature_text(self):
        """
        属性: 审核详情-课程特色
        :return: 审核详情-课程特色
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_feature_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_teacher_name_text(self):
        """
        属性: 审核详情-讲师姓名
        :return: 审核详情-讲师姓名
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_teacher_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_teacher_id_text(self):
        """
        属性: 审核详情-讲师id
        :return: 审核详情-讲师id
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_teacher_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_channel_text(self):
        """
        属性: 审核详情-频道
        :return: 审核详情-频道
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_channel_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_role_type_text(self):
        """
        属性: 审核详情-角色类型
        :return: 审核详情-角色类型
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_role_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_first_question_text(self):
        """
        属性: 审核详情-问题一
        :return: 审核详情-问题一
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_first_question_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_first_answer_text(self):
        """
        属性: 审核详情-答案一
        :return: 审核详情-答案一
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_first_answer_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_second_question_text(self):
        """
        属性: 审核详情-问题二
        :return: 审核详情-问题二
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_second_question_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_second_answer_text(self):
        """
        属性: 审核详情-答案二
        :return: 审核详情-答案二
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_second_answer_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_first_item_name_text(self):
        """
        属性: 审核详情-第一个课节-名称
        :return: 审核详情-第一个课节-名称
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_first_item_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_first_item_video_text(self):
        """
        属性: 审核详情-第一个课节-视频名称
        :return: 审核详情-第一个课节-视频名称
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_first_item_video_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_first_item_pass_button(self):
        """
        属性: 审核详情-第一个课节-审核通过按钮
        :return: 审核详情-第一个课节-审核通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_first_item_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_first_item_unpass_button(self):
        """
        属性: 审核详情-第一个课节-审核不通过按钮
        :return: 审核详情-第一个课节-审核不通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_first_item_unpass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_second_item_name_text(self):
        """
        属性: 审核详情-第二个课节-名称
        :return: 审核详情-第二个课节-名称
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_second_item_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_second_item_video_text(self):
        """
        属性: 审核详情-第二个课节-视频名称
        :return: 审核详情-第二个课节-视频名称
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_second_item_video_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_second_item_pass_button(self):
        """
        属性: 审核详情-第二个课节-审核通过按钮
        :return: 审核详情-第二个课节-审核通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_second_item_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_second_item_unpass_button(self):
        """
        属性: 审核详情-第二个课节-审核不通过按钮
        :return: 审核详情-第二个课节-审核不通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_second_item_unpass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_item_pass_confirm_button(self):
        """
        属性: 审核详情-课节审核通过确定按钮
        :return: 审核详情-课节审核通过确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_item_pass_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_item_pass_cancel_button(self):
        """
        属性: 审核详情-课节审核通过取消按钮
        :return: 审核详情-课节审核通过取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_item_pass_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_item_unpass_reason_button(self):
        """
        属性: 审核详情-课节审核不通过-未通过理由下拉框
        :return: 审核详情-课节审核不通过-未通过理由下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_item_unpass_reason_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_item_unpass_reason_select(self):
        """
        属性: 审核详情-课节审核不通过-未通过理由-下拉列表
        :return: 审核详情-课节审核不通过-未通过理由-下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_item_unpass_reason_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_item_unpass_custom_input(self):
        """
        属性: 审核详情-课节审核不通过-自定义输入框
        :return: 审核详情-课节审核不通过-自定义输入框
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_item_unpass_custom_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_item_unpass_commit_button(self):
        """
        属性: 审核详情-课节审核不通过-提交按钮
        :return: 审核详情-课节审核不通过-提交按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_item_unpass_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_item_unpass_cancel_button(self):
        """
        属性: 审核详情-课节审核不通过-返回按钮
        :return: 审核详情-课节审核不通过-返回按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_item_unpass_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_item_unpass_close_button(self):
        """
        属性: 审核详情-课节审核不通过-关闭按钮
        :return: 审核详情-课节审核不通过-关闭按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_item_unpass_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_course_pass_button(self):
        """
        属性: 审核详情-课程审核通过按钮
        :return: 审核详情-课程审核通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_course_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_course_unpass_button(self):
        """
        属性: 审核详情-课程课程审核不通过按钮
        :return: 审核详情-课程课程审核不通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_course_unpass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_course_cancel_button(self):
        """
        属性: 审核详情-课程返回按钮
        :return: 审核详情-课程返回按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_course_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_course_pass_confirm_button(self):
        """
        属性: 审核详情-课程审核通过-确认按钮
        :return: 审核详情-课程审核通过-确认按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_course_pass_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_course_pass_cancel_button(self):
        """
        属性: 审核详情-课程审核通过-取消按钮
        :return: 审核详情-课程审核通过-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_course_pass_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_course_unpass_reason_button(self):
        """
        属性: 审核详情-课程审核不通过-未通过理由下拉框
        :return: 审核详情-课程审核不通过-未通过理由下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_course_unpass_reason_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_course_unpass_reason_select(self):
        """
        属性: 审核详情-课程审核不通过理由自定义按钮
        :return: 审核详情-课程审核不通过理由自定义按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_course_unpass_reason_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_course_unpass_reason_custom_input(self):
        """
        属性: 审核详情-课程审核不通过理由自定义输入框
        :return: 审核详情-课程审核不通过理由自定义输入框
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_course_unpass_reason_custom_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_course_unpass_commit_button(self):
        """
        属性: 审核详情-课程审核不通过-提交按钮
        :return: 审核详情-课程审核不通过-提交按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_course_unpass_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_course_unpass_cancel_button(self):
        """
        属性: 审核详情-课程审核不通过-取消按钮
        :return: 审核详情-课程审核不通过-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_course_unpass_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_record_detail_exe_log_last_examine_state_text(self):
        """
        属性: 审核详情-操作记录最后一个审核结果
        :return: 审核详情-操作记录最后一个审核结果
        """
        element = None
        try:
            element = self.project.get_element(self._course_record_detail_exe_log_last_examine_state_text_tag)
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

    def set_course_record_goods_id_input_action(self, course_record_goods_id_input):
        """
        动作：设置课程ID输入框
        :param course_record_goods_id_input: 课程ID输入框
        :return: 设置'课程ID输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.course_record_goods_id_input, course_record_goods_id_input)
        return self.project.get_current_page_source()

    def set_course_record_product_name_input_action(self, course_record_product_name_input):
        """
        动作：设置课程标题输入框
        :param course_record_product_name_input: 课程标题输入框
        :return: 设置'课程标题输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.course_record_product_name_input, course_record_product_name_input)
        return self.project.get_current_page_source()

    def set_course_record_teacher_name_input_action(self, course_record_teacher_name_input):
        """
        动作：设置讲师姓名输入框
        :param course_record_teacher_name_input: 讲师姓名输入框
        :return: 设置'讲师姓名输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.course_record_teacher_name_input, course_record_teacher_name_input)
        return self.project.get_current_page_source()

    def click_course_record_category_button_action(self):
        """
        动作：点击上课模式下拉框
        :return: 点击'上课模式下拉框'按钮后的页面
        """
        self.project.click(self.course_record_category_button)
        return self.project.get_current_page_source()

    def get_select_course_record_category_action(self, course_record_category_select):
        """
        动作：获取上课模式-下拉列表列表选中的文本
        :param course_record_category_select: 上课模式-下拉列表列表索引或文本
        :return: '上课模式-下拉列表'的文本
        """
        control_content = self.project.get_select_content(self.course_record_category_select, course_record_category_select)
        return control_content

    def select_course_record_category_action(self, course_record_category_select):
        """
        动作：选择上课模式-下拉列表
        :param course_record_category_select: 上课模式-下拉列表列表索引或文本
        :return: 选择'上课模式-下拉列表'选择器后的页面
        """
        self.project.select_control(self.course_record_category_select, course_record_category_select)
        return self.project.get_current_page_source()

    def click_course_record_channel_button_action(self):
        """
        动作：点击频道下拉框
        :return: 点击'频道下拉框'按钮后的页面
        """
        self.project.click(self.course_record_channel_button)
        return self.project.get_current_page_source()

    def get_select_course_record_channel_action(self, course_record_channel_select):
        """
        动作：获取频道-下拉列表列表选中的文本
        :param course_record_channel_select: 频道-下拉列表列表索引或文本
        :return: '频道-下拉列表'的文本
        """
        control_content = self.project.get_select_content(self.course_record_channel_select, course_record_channel_select)
        return control_content

    def select_course_record_channel_action(self, course_record_channel_select):
        """
        动作：选择频道-下拉列表
        :param course_record_channel_select: 频道-下拉列表列表索引或文本
        :return: 选择'频道-下拉列表'选择器后的页面
        """
        self.project.select_control(self.course_record_channel_select, course_record_channel_select)
        return self.project.get_current_page_source()

    def click_course_record_state_button_action(self):
        """
        动作：点击课程状态下拉框
        :return: 点击'课程状态下拉框'按钮后的页面
        """
        self.project.click(self.course_record_state_button)
        return self.project.get_current_page_source()

    def click_course_record_state_all_button_action(self):
        """
        动作：点击课程状态-下拉列表
        :return: 点击'课程状态-下拉列表'按钮后的页面
        """
        self.project.click(self.course_record_state_all_button)
        return self.project.get_current_page_source()

    def click_course_record_role_button_action(self):
        """
        动作：点击角色类型下拉框
        :return: 点击'角色类型下拉框'按钮后的页面
        """
        self.project.click(self.course_record_role_button)
        return self.project.get_current_page_source()

    def click_course_record_role_all_button_action(self):
        """
        动作：点击角色类型-下拉列表
        :return: 点击'角色类型-下拉列表'按钮后的页面
        """
        self.project.click(self.course_record_role_all_button)
        return self.project.get_current_page_source()

    def click_course_record_item_state_button_action(self):
        """
        动作：点击课节状态下拉框
        :return: 点击'课节状态下拉框'按钮后的页面
        """
        self.project.click(self.course_record_item_state_button)
        return self.project.get_current_page_source()

    def click_course_record_item_state_all_button_action(self):
        """
        动作：点击课节状态-下拉列表
        :return: 点击'课节状态-下拉列表'按钮后的页面
        """
        self.project.click(self.course_record_item_state_all_button)
        return self.project.get_current_page_source()

    def set_course_record_update_time_start_time_input_action(self, course_record_update_time_start_time_input):
        """
        动作：设置更新日期-开始日期输入框
        :param course_record_update_time_start_time_input: 更新日期-开始日期输入框
        :return: 设置'更新日期-开始日期输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.course_record_update_time_start_time_input, course_record_update_time_start_time_input)
        return self.project.get_current_page_source()

    def set_course_record_update_time_end_time_input_action(self, course_record_update_time_end_time_input):
        """
        动作：设置更新日期-结束日期输入框
        :param course_record_update_time_end_time_input: 更新日期-结束日期输入框
        :return: 设置'更新日期-结束日期输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.course_record_update_time_end_time_input, course_record_update_time_end_time_input)
        return self.project.get_current_page_source()

    def click_course_record_search_button_action(self):
        """
        动作：点击查询按钮
        :return: 点击'查询按钮'按钮后的页面
        """
        self.project.click(self.course_record_search_button)
        return self.project.get_current_page_source()

    def click_course_record_clear_button_action(self):
        """
        动作：点击清楚按钮
        :return: 点击'清楚按钮'按钮后的页面
        """
        self.project.click(self.course_record_clear_button)
        return self.project.get_current_page_source()

    def click_course_record_first_line_button_action(self):
        """
        动作：点击第一行操作按钮（审核/查看）
        :return: 点击'第一行操作按钮（审核/查看）'按钮后的页面
        """
        self.project.click(self.course_record_first_line_button)
        return self.project.get_current_page_source()

    def get_course_record_first_line_course_state_text_action(self):
        """
        动作：获取第一行课程状态的文本
        :return: '第一行课程状态'的文本
        """
        control_content = self.project.get_element_text(self.course_record_first_line_course_state_text)
        return control_content

    def get_course_record_detail_product_name_text_action(self):
        """
        动作：获取审核详情-课程标题的文本
        :return: '审核详情-课程标题'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_product_name_text)
        return control_content

    def get_course_record_detail_category_text_action(self):
        """
        动作：获取审核详情-上课模式的文本
        :return: '审核详情-上课模式'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_category_text)
        return control_content

    def get_course_record_detail_goods_id_text_action(self):
        """
        动作：获取审核详情-课程id的文本
        :return: '审核详情-课程id'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_goods_id_text)
        return control_content

    def get_course_record_detail_sub_product_name_text_action(self):
        """
        动作：获取审核详情-课程副标题的文本
        :return: '审核详情-课程副标题'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_sub_product_name_text)
        return control_content

    def get_course_record_detail_price_text_action(self):
        """
        动作：获取审核详情-销售价格的文本
        :return: '审核详情-销售价格'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_price_text)
        return control_content

    def get_course_record_detail_discount_text_action(self):
        """
        动作：获取审核详情-优惠价格的文本
        :return: '审核详情-优惠价格'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_discount_text)
        return control_content

    def get_course_record_detail_created_at_text_action(self):
        """
        动作：获取审核详情-发布时间的文本
        :return: '审核详情-发布时间'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_created_at_text)
        return control_content

    def get_course_record_detail_goods_state_text_action(self):
        """
        动作：获取审核详情-课程状态的文本
        :return: '审核详情-课程状态'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_goods_state_text)
        return control_content

    def get_course_record_detail_first_label_text_action(self):
        """
        动作：获取审核详情-课程分类的文本
        :return: '审核详情-课程分类'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_first_label_text)
        return control_content

    def get_course_record_detail_second_label_text_action(self):
        """
        动作：获取审核详情课程标签的文本
        :return: '审核详情课程标签'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_second_label_text)
        return control_content

    def get_course_record_detail_sub_content_text_action(self):
        """
        动作：获取审核详情-内容主题的文本
        :return: '审核详情-内容主题'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_sub_content_text)
        return control_content

    def get_course_record_detail_keywords_text_action(self):
        """
        动作：获取审核详情-关键词的文本
        :return: '审核详情-关键词'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_keywords_text)
        return control_content

    def get_course_record_detail_review_date_text_action(self):
        """
        动作：获取审核详情-课程有效期的文本
        :return: '审核详情-课程有效期'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_review_date_text)
        return control_content

    def get_course_record_detail_is_group_text_action(self):
        """
        动作：获取审核详情-是否建群的文本
        :return: '审核详情-是否建群'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_is_group_text)
        return control_content

    def get_course_record_detail_feature_text_action(self):
        """
        动作：获取审核详情-课程特色的文本
        :return: '审核详情-课程特色'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_feature_text)
        return control_content

    def get_course_record_detail_teacher_name_text_action(self):
        """
        动作：获取审核详情-讲师姓名的文本
        :return: '审核详情-讲师姓名'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_teacher_name_text)
        return control_content

    def get_course_record_detail_teacher_id_text_action(self):
        """
        动作：获取审核详情-讲师id的文本
        :return: '审核详情-讲师id'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_teacher_id_text)
        return control_content

    def get_course_record_detail_channel_text_action(self):
        """
        动作：获取审核详情-频道的文本
        :return: '审核详情-频道'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_channel_text)
        return control_content

    def get_course_record_detail_role_type_text_action(self):
        """
        动作：获取审核详情-角色类型的文本
        :return: '审核详情-角色类型'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_role_type_text)
        return control_content

    def get_course_record_detail_first_question_text_action(self):
        """
        动作：获取审核详情-问题一的文本
        :return: '审核详情-问题一'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_first_question_text)
        return control_content

    def get_course_record_detail_first_answer_text_action(self):
        """
        动作：获取审核详情-答案一的文本
        :return: '审核详情-答案一'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_first_answer_text)
        return control_content

    def get_course_record_detail_second_question_text_action(self):
        """
        动作：获取审核详情-问题二的文本
        :return: '审核详情-问题二'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_second_question_text)
        return control_content

    def get_course_record_detail_second_answer_text_action(self):
        """
        动作：获取审核详情-答案二的文本
        :return: '审核详情-答案二'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_second_answer_text)
        return control_content

    def get_course_record_detail_first_item_name_text_action(self):
        """
        动作：获取审核详情-第一个课节-名称的文本
        :return: '审核详情-第一个课节-名称'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_first_item_name_text)
        return control_content

    def get_course_record_detail_first_item_video_text_action(self):
        """
        动作：获取审核详情-第一个课节-视频名称的文本
        :return: '审核详情-第一个课节-视频名称'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_first_item_video_text)
        return control_content

    def click_course_record_detail_first_item_pass_button_action(self):
        """
        动作：点击审核详情-第一个课节-审核通过按钮
        :return: 点击'审核详情-第一个课节-审核通过按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_first_item_pass_button)
        return self.project.get_current_page_source()

    def click_course_record_detail_first_item_unpass_button_action(self):
        """
        动作：点击审核详情-第一个课节-审核不通过按钮
        :return: 点击'审核详情-第一个课节-审核不通过按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_first_item_unpass_button)
        return self.project.get_current_page_source()

    def get_course_record_detail_second_item_name_text_action(self):
        """
        动作：获取审核详情-第二个课节-名称的文本
        :return: '审核详情-第二个课节-名称'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_second_item_name_text)
        return control_content

    def get_course_record_detail_second_item_video_text_action(self):
        """
        动作：获取审核详情-第二个课节-视频名称的文本
        :return: '审核详情-第二个课节-视频名称'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_second_item_video_text)
        return control_content

    def click_course_record_detail_second_item_pass_button_action(self):
        """
        动作：点击审核详情-第二个课节-审核通过按钮
        :return: 点击'审核详情-第二个课节-审核通过按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_second_item_pass_button)
        return self.project.get_current_page_source()

    def click_course_record_detail_second_item_unpass_button_action(self):
        """
        动作：点击审核详情-第二个课节-审核不通过按钮
        :return: 点击'审核详情-第二个课节-审核不通过按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_second_item_unpass_button)
        return self.project.get_current_page_source()

    def click_course_record_detail_item_pass_confirm_button_action(self):
        """
        动作：点击审核详情-课节审核通过确定按钮
        :return: 点击'审核详情-课节审核通过确定按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_item_pass_confirm_button)
        return self.project.get_current_page_source()

    def click_course_record_detail_item_pass_cancel_button_action(self):
        """
        动作：点击审核详情-课节审核通过取消按钮
        :return: 点击'审核详情-课节审核通过取消按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_item_pass_cancel_button)
        return self.project.get_current_page_source()

    def click_course_record_detail_item_unpass_reason_button_action(self):
        """
        动作：点击审核详情-课节审核不通过-未通过理由下拉框
        :return: 点击'审核详情-课节审核不通过-未通过理由下拉框'按钮后的页面
        """
        self.project.click(self.course_record_detail_item_unpass_reason_button)
        return self.project.get_current_page_source()

    def get_select_course_record_detail_item_unpass_reason_action(self, course_record_detail_item_unpass_reason_select):
        """
        动作：获取审核详情-课节审核不通过-未通过理由-下拉列表列表选中的文本
        :param course_record_detail_item_unpass_reason_select: 审核详情-课节审核不通过-未通过理由-下拉列表列表索引或文本
        :return: '审核详情-课节审核不通过-未通过理由-下拉列表'的文本
        """
        control_content = self.project.get_select_content(self.course_record_detail_item_unpass_reason_select, course_record_detail_item_unpass_reason_select)
        return control_content

    def select_course_record_detail_item_unpass_reason_action(self, course_record_detail_item_unpass_reason_select):
        """
        动作：选择审核详情-课节审核不通过-未通过理由-下拉列表
        :param course_record_detail_item_unpass_reason_select: 审核详情-课节审核不通过-未通过理由-下拉列表列表索引或文本
        :return: 选择'审核详情-课节审核不通过-未通过理由-下拉列表'选择器后的页面
        """
        self.project.select_control(self.course_record_detail_item_unpass_reason_select, course_record_detail_item_unpass_reason_select)
        return self.project.get_current_page_source()

    def set_course_record_detail_item_unpass_custom_input_action(self, course_record_detail_item_unpass_custom_input):
        """
        动作：设置审核详情-课节审核不通过-自定义输入框
        :param course_record_detail_item_unpass_custom_input: 审核详情-课节审核不通过-自定义输入框
        :return: 设置'审核详情-课节审核不通过-自定义输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.course_record_detail_item_unpass_custom_input, course_record_detail_item_unpass_custom_input)
        return self.project.get_current_page_source()

    def click_course_record_detail_item_unpass_commit_button_action(self):
        """
        动作：点击审核详情-课节审核不通过-提交按钮
        :return: 点击'审核详情-课节审核不通过-提交按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_item_unpass_commit_button)
        return self.project.get_current_page_source()

    def click_course_record_detail_item_unpass_cancel_button_action(self):
        """
        动作：点击审核详情-课节审核不通过-返回按钮
        :return: 点击'审核详情-课节审核不通过-返回按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_item_unpass_cancel_button)
        return self.project.get_current_page_source()

    def click_course_record_detail_item_unpass_close_button_action(self):
        """
        动作：点击审核详情-课节审核不通过-关闭按钮
        :return: 点击'审核详情-课节审核不通过-关闭按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_item_unpass_close_button)
        return self.project.get_current_page_source()

    def click_course_record_detail_course_pass_button_action(self):
        """
        动作：点击审核详情-课程审核通过按钮
        :return: 点击'审核详情-课程审核通过按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_course_pass_button)
        return self.project.get_current_page_source()

    def click_course_record_detail_course_unpass_button_action(self):
        """
        动作：点击审核详情-课程课程审核不通过按钮
        :return: 点击'审核详情-课程课程审核不通过按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_course_unpass_button)
        return self.project.get_current_page_source()

    def click_course_record_detail_course_cancel_button_action(self):
        """
        动作：点击审核详情-课程返回按钮
        :return: 点击'审核详情-课程返回按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_course_cancel_button)
        return self.project.get_current_page_source()

    def click_course_record_detail_course_pass_confirm_button_action(self):
        """
        动作：点击审核详情-课程审核通过-确认按钮
        :return: 点击'审核详情-课程审核通过-确认按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_course_pass_confirm_button)
        return self.project.get_current_page_source()

    def click_course_record_detail_course_pass_cancel_button_action(self):
        """
        动作：点击审核详情-课程审核通过-取消按钮
        :return: 点击'审核详情-课程审核通过-取消按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_course_pass_cancel_button)
        return self.project.get_current_page_source()

    def click_course_record_detail_course_unpass_reason_button_action(self):
        """
        动作：点击审核详情-课程审核不通过-未通过理由下拉框
        :return: 点击'审核详情-课程审核不通过-未通过理由下拉框'按钮后的页面
        """
        self.project.click(self.course_record_detail_course_unpass_reason_button)
        return self.project.get_current_page_source()

    def get_select_course_record_detail_course_unpass_reason_action(self, course_record_detail_course_unpass_reason_select):
        """
        动作：获取审核详情-课程审核不通过理由自定义按钮列表选中的文本
        :param course_record_detail_course_unpass_reason_select: 审核详情-课程审核不通过理由自定义按钮列表索引或文本
        :return: '审核详情-课程审核不通过理由自定义按钮'的文本
        """
        control_content = self.project.get_select_content(self.course_record_detail_course_unpass_reason_select, course_record_detail_course_unpass_reason_select)
        return control_content

    def select_course_record_detail_course_unpass_reason_action(self, course_record_detail_course_unpass_reason_select):
        """
        动作：选择审核详情-课程审核不通过理由自定义按钮
        :param course_record_detail_course_unpass_reason_select: 审核详情-课程审核不通过理由自定义按钮列表索引或文本
        :return: 选择'审核详情-课程审核不通过理由自定义按钮'选择器后的页面
        """
        self.project.select_control(self.course_record_detail_course_unpass_reason_select, course_record_detail_course_unpass_reason_select)
        return self.project.get_current_page_source()

    def set_course_record_detail_course_unpass_reason_custom_input_action(self, course_record_detail_course_unpass_reason_custom_input):
        """
        动作：设置审核详情-课程审核不通过理由自定义输入框
        :param course_record_detail_course_unpass_reason_custom_input: 审核详情-课程审核不通过理由自定义输入框
        :return: 设置'审核详情-课程审核不通过理由自定义输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.course_record_detail_course_unpass_reason_custom_input, course_record_detail_course_unpass_reason_custom_input)
        return self.project.get_current_page_source()

    def click_course_record_detail_course_unpass_commit_button_action(self):
        """
        动作：点击审核详情-课程审核不通过-提交按钮
        :return: 点击'审核详情-课程审核不通过-提交按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_course_unpass_commit_button)
        return self.project.get_current_page_source()

    def click_course_record_detail_course_unpass_cancel_button_action(self):
        """
        动作：点击审核详情-课程审核不通过-取消按钮
        :return: 点击'审核详情-课程审核不通过-取消按钮'按钮后的页面
        """
        self.project.click(self.course_record_detail_course_unpass_cancel_button)
        return self.project.get_current_page_source()

    def get_course_record_detail_exe_log_last_examine_state_text_action(self):
        """
        动作：获取审核详情-操作记录最后一个审核结果的文本
        :return: '审核详情-操作记录最后一个审核结果'的文本
        """
        control_content = self.project.get_element_text(self.course_record_detail_exe_log_last_examine_state_text)
        return control_content

    # endregion Actions
