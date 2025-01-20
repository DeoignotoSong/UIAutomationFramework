from Utils.Log import log

"""
后台首页-客服中心-留言管理-用户举报
console_url/review/report_list
"""


class ConsoleServerCenterMessageReportListPage:

    def __init__(self, project):
        self.project = project
        self.url = 'console_url/review/report_list'
        # region Fields
        # 搜索-举报内容输入框
        self._search_report_content_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 搜搜-举报人ID输入框
        self._search_report_user_input_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 搜索-被举报人ID输入框
        self._search_reported_user_input_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div/input'
        # 搜索-举报时间-开始日期输入框
        self._search_report_date_start_input_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div/input[1]'
        # 搜索-举报时间-结束日期输入框
        self._search_report_date_end_input_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div/input[2]'
        # 搜索-回复状态下拉框
        self._search_reply_state_button_tag = '//*[@id="tableSearch"]/form/div/div[5]/div/div'
        # 搜索-回复状态-全部
        self._search_reply_state_all_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[1]'
        # 搜索-回复状态-已回复
        self._search_reply_state_replied_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[2]'
        # 搜索-回复状态-未回复
        self._search_reply_state_not_replied_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[2]'
        # 搜索-回复人输入框
        self._search_reply_user_input_tag = '//*[@id="tableSearch"]/form/div/div[6]/div/div/input'
        # 搜索-回复时间-开始日期
        self._search_reply_date_start_input_tag = '//*[@id="tableSearch"]/form/div/div[7]/div/div/input[1]'
        # 搜索-回复时间-结束日期
        self._search_reply_date_end_input_tag = '//*[@id="tableSearch"]/form/div/div[7]/div/div/input[2]'
        # 搜索-业务类别下拉框
        self._search_business_category_button_tag = '//*[@id="tableSearch"]/form/div/div[8]/div/div'
        # 搜索-业务类别-全部
        self._search_business_category_all_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[1]'
        # 搜索-业务类别-文章
        self._search_business_category_article_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[2]'
        # 搜索-业务类别-课程
        self._search_business_category_course_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[3]'
        # 搜索-业务类别-用户
        self._search_business_category_user_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[4]'
        # 搜索-业务类别-订单
        self._search_business_category_order_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[5]'
        # 搜索-业务类别-问题
        self._search_business_category_question_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[6]'
        # 搜索-举报原因下拉框
        self._search_report_reason_button_tag = '//*[@id="tableSearch"]/form/div/div[9]/div/div'
        # 搜索-举报原因-全部
        self._search_report_reason_all_button_tag = '/html/body/div[6]/div[1]/div[1]/ul/li[1]'
        # 搜索-举报原因-未知
        self._search_report_reason_unknow_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[2]'
        # 搜索-举报原因-不良粉丝
        self._search_report_reason_bad_fans_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[3]'
        # 搜索-举报原因-垃圾营销
        self._search_report_reason_garbage_marketing_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[4]'
        # 搜索-举报原因-不实信息
        self._search_report_reason_false_information_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[5]'
        # 搜索-举报原因-有害信息
        self._search_report_reason_harmful_information_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[6]'
        # 搜索-举报原因-违法信息
        self._search_report_reason_illegal_information_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[7]'
        # 搜索-举报原因-淫秽色情
        self._search_report_reason_obscenity_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[8]'
        # 搜索-举报原因-人身攻击
        self._search_report_reason_personal_attack_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[9]'
        # 搜索-举报原因-内容抄袭
        self._search_report_reason_content_copy_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[10]'
        # 搜索-举报原因-投诉
        self._search_report_reason_complain_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[11]'
        # 搜索-举报原因-申请售后
        self._search_report_reason_after_service_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[12]'
        # 搜索-频道下拉框
        self._search_channel_button_tag = '//*[@id="tableSearch"]/form/div/div[10]/div/div'
        # 搜索-频道-全部
        self._search_channel_all_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[1]'
        # 搜索-频道-总首页
        self._search_channel_main_home_page_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[2]'
        # 搜索-频道-出国留学
        self._search_channel_abroad_learning_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[3]'
        # 搜索-频道-语言培训
        self._search_channel_language_training_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[4]'
        # 搜索-频道-院校直通车
        self._search_channel_college_direction_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[5]'
        # 搜索-频道-海外移民
        self._search_channel_overseas_immigrants_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[6]'
        # 查询按钮
        self._search_button_tag = '//*[@id="tableSearch"]/form/div/div[last()-1]/div/button'
        # 清除按钮
        self._clear_button_tag = '//*[@id="tableSearch"]/form/div/div[last()]/div/button'
        # 列表第一个举报的频道
        self._list_first_channel_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 列表第一个举报的业务类型
        self._list_first_business_text_category_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 列表第一个举报的举报原因
        self._list_first_report_reason_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 列表第一个举报的订单编号
        self._list_first_order_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 列表第一个举报的举报内容
        self._list_first_report_content_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 列表第一个举报的被举报人ID
        self._list_first_reported_user_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div'
        # 列表第一个举报的举报人昵称
        self._list_first_reported_nick_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div'
        # 列表第一个举报的被举报人姓名
        self._list_first_reported_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div'
        # 列表第一个举报的举报人ID
        self._list_first_report_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[10]/div'
        # 列表第一个举报的举报人昵称
        self._list_first_report_nick_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[11]/div'
        # 列表第一个举报的举报人姓名
        self._list_first_report_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[12]/div'
        # 列表第一个举报的举报人电话
        self._list_first_report_mobile_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[13]/div'
        # 列表第一个举报的举报时间
        self._list_first_report_time_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[14]/div'
        # 列表第一个举报的回复状态
        self._list_first_reply_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[15]/div'
        # 列表第一个举报的回复人
        self._list_first_reply_user_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[16]/div'
        # 列表第一个举报的回复时间
        self._list_first_reply_time_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[17]/div'
        # 列表第一个举报的回复按钮
        self._list_first_reply_button_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[18]/div/a[1]'
        # 举报回复详情回复内容输入框
        self._report_reply_detail_reply_content_input_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[2]/form/div[4]/div/div/div/div/textarea'
        # 举报回复详情确认按钮
        self._report_reply_detail_confirm_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[3]/span/button[2]'
        # 举报回复详情取消按钮
        self._report_reply_detail_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[3]/div/div/div[3]/span/button[1]'
        # 列表第一个举报的删除按钮
        self._list_first_delete_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[18]/div/a[2]'
        # 举报删除确认按钮
        self._report_delete_confirm_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # 举报删除取消按钮
        self._report_delete_cancel_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # endregion Fields

    # region Properties
    @property
    def search_report_content_input(self):
        """
        属性: 搜索-举报内容输入框
        :return: 搜索-举报内容输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_content_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_user_input(self):
        """
        属性: 搜搜-举报人ID输入框
        :return: 搜搜-举报人ID输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_user_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_reported_user_input(self):
        """
        属性: 搜索-被举报人ID输入框
        :return: 搜索-被举报人ID输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_reported_user_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_date_start_input(self):
        """
        属性: 搜索-举报时间-开始日期输入框
        :return: 搜索-举报时间-开始日期输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_date_start_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_date_end_input(self):
        """
        属性: 搜索-举报时间-结束日期输入框
        :return: 搜索-举报时间-结束日期输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_date_end_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_reply_state_button(self):
        """
        属性: 搜索-回复状态下拉框
        :return: 搜索-回复状态下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._search_reply_state_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_reply_state_all_button(self):
        """
        属性: 搜索-回复状态-全部
        :return: 搜索-回复状态-全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_reply_state_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_reply_state_replied_button(self):
        """
        属性: 搜索-回复状态-已回复
        :return: 搜索-回复状态-已回复
        """
        element = None
        try:
            element = self.project.get_element(self._search_reply_state_replied_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_reply_state_not_replied_button(self):
        """
        属性: 搜索-回复状态-未回复
        :return: 搜索-回复状态-未回复
        """
        element = None
        try:
            element = self.project.get_element(self._search_reply_state_not_replied_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_reply_user_input(self):
        """
        属性: 搜索-回复人输入框
        :return: 搜索-回复人输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_reply_user_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_reply_date_start_input(self):
        """
        属性: 搜索-回复时间-开始日期
        :return: 搜索-回复时间-开始日期
        """
        element = None
        try:
            element = self.project.get_element(self._search_reply_date_start_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_reply_date_end_input(self):
        """
        属性: 搜索-回复时间-结束日期
        :return: 搜索-回复时间-结束日期
        """
        element = None
        try:
            element = self.project.get_element(self._search_reply_date_end_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_business_category_button(self):
        """
        属性: 搜索-业务类别下拉框
        :return: 搜索-业务类别下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._search_business_category_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_business_category_all_button(self):
        """
        属性: 搜索-业务类别-全部
        :return: 搜索-业务类别-全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_business_category_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_business_category_article_button(self):
        """
        属性: 搜索-业务类别-文章
        :return: 搜索-业务类别-文章
        """
        element = None
        try:
            element = self.project.get_element(self._search_business_category_article_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_business_category_course_button(self):
        """
        属性: 搜索-业务类别-课程
        :return: 搜索-业务类别-课程
        """
        element = None
        try:
            element = self.project.get_element(self._search_business_category_course_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_business_category_user_button(self):
        """
        属性: 搜索-业务类别-用户
        :return: 搜索-业务类别-用户
        """
        element = None
        try:
            element = self.project.get_element(self._search_business_category_user_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_business_category_order_button(self):
        """
        属性: 搜索-业务类别-订单
        :return: 搜索-业务类别-订单
        """
        element = None
        try:
            element = self.project.get_element(self._search_business_category_order_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_business_category_question_button(self):
        """
        属性: 搜索-业务类别-问题
        :return: 搜索-业务类别-问题
        """
        element = None
        try:
            element = self.project.get_element(self._search_business_category_question_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_reason_button(self):
        """
        属性: 搜索-举报原因下拉框
        :return: 搜索-举报原因下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_reason_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_reason_all_button(self):
        """
        属性: 搜索-举报原因-全部
        :return: 搜索-举报原因-全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_reason_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_reason_unknow_button(self):
        """
        属性: 搜索-举报原因-未知
        :return: 搜索-举报原因-未知
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_reason_unknow_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_reason_bad_fans_button(self):
        """
        属性: 搜索-举报原因-不良粉丝
        :return: 搜索-举报原因-不良粉丝
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_reason_bad_fans_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_reason_garbage_marketing_button(self):
        """
        属性: 搜索-举报原因-垃圾营销
        :return: 搜索-举报原因-垃圾营销
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_reason_garbage_marketing_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_reason_false_information_button(self):
        """
        属性: 搜索-举报原因-不实信息
        :return: 搜索-举报原因-不实信息
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_reason_false_information_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_reason_harmful_information_button(self):
        """
        属性: 搜索-举报原因-有害信息
        :return: 搜索-举报原因-有害信息
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_reason_harmful_information_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_reason_illegal_information_button(self):
        """
        属性: 搜索-举报原因-违法信息
        :return: 搜索-举报原因-违法信息
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_reason_illegal_information_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_reason_obscenity_button(self):
        """
        属性: 搜索-举报原因-淫秽色情
        :return: 搜索-举报原因-淫秽色情
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_reason_obscenity_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_reason_personal_attack_button(self):
        """
        属性: 搜索-举报原因-人身攻击
        :return: 搜索-举报原因-人身攻击
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_reason_personal_attack_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_reason_content_copy_button(self):
        """
        属性: 搜索-举报原因-内容抄袭
        :return: 搜索-举报原因-内容抄袭
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_reason_content_copy_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_reason_complain_button(self):
        """
        属性: 搜索-举报原因-投诉
        :return: 搜索-举报原因-投诉
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_reason_complain_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_report_reason_after_service_button(self):
        """
        属性: 搜索-举报原因-申请售后
        :return: 搜索-举报原因-申请售后
        """
        element = None
        try:
            element = self.project.get_element(self._search_report_reason_after_service_button_tag)
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
    def search_channel_all_button(self):
        """
        属性: 搜索-频道-全部
        :return: 搜索-频道-全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_channel_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_channel_main_home_page_button(self):
        """
        属性: 搜索-频道-总首页
        :return: 搜索-频道-总首页
        """
        element = None
        try:
            element = self.project.get_element(self._search_channel_main_home_page_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_channel_abroad_learning_button(self):
        """
        属性: 搜索-频道-出国留学
        :return: 搜索-频道-出国留学
        """
        element = None
        try:
            element = self.project.get_element(self._search_channel_abroad_learning_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_channel_language_training_button(self):
        """
        属性: 搜索-频道-语言培训
        :return: 搜索-频道-语言培训
        """
        element = None
        try:
            element = self.project.get_element(self._search_channel_language_training_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_channel_college_direction_button(self):
        """
        属性: 搜索-频道-院校直通车
        :return: 搜索-频道-院校直通车
        """
        element = None
        try:
            element = self.project.get_element(self._search_channel_college_direction_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_channel_overseas_immigrants_button(self):
        """
        属性: 搜索-频道-海外移民
        :return: 搜索-频道-海外移民
        """
        element = None
        try:
            element = self.project.get_element(self._search_channel_overseas_immigrants_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_button(self):
        """
        属性: 查询按钮
        :return: 查询按钮
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
        属性: 清除按钮
        :return: 清除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_channel_text(self):
        """
        属性: 列表第一个举报的频道
        :return: 列表第一个举报的频道
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_channel_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_business_text_category(self):
        """
        属性: 列表第一个举报的业务类型
        :return: 列表第一个举报的业务类型
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_business_text_category_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_report_reason_text(self):
        """
        属性: 列表第一个举报的举报原因
        :return: 列表第一个举报的举报原因
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_report_reason_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_order_id_text(self):
        """
        属性: 列表第一个举报的订单编号
        :return: 列表第一个举报的订单编号
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_order_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_report_content_text(self):
        """
        属性: 列表第一个举报的举报内容
        :return: 列表第一个举报的举报内容
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_report_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_reported_user_id_text(self):
        """
        属性: 列表第一个举报的被举报人ID
        :return: 列表第一个举报的被举报人ID
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_reported_user_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_reported_nick_text(self):
        """
        属性: 列表第一个举报的举报人昵称
        :return: 列表第一个举报的举报人昵称
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_reported_nick_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_reported_name_text(self):
        """
        属性: 列表第一个举报的被举报人姓名
        :return: 列表第一个举报的被举报人姓名
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_reported_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_report_id_text(self):
        """
        属性: 列表第一个举报的举报人ID
        :return: 列表第一个举报的举报人ID
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_report_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_report_nick_text(self):
        """
        属性: 列表第一个举报的举报人昵称
        :return: 列表第一个举报的举报人昵称
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_report_nick_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_report_name_text(self):
        """
        属性: 列表第一个举报的举报人姓名
        :return: 列表第一个举报的举报人姓名
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_report_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_report_mobile_text(self):
        """
        属性: 列表第一个举报的举报人电话
        :return: 列表第一个举报的举报人电话
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_report_mobile_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_report_time_text(self):
        """
        属性: 列表第一个举报的举报时间
        :return: 列表第一个举报的举报时间
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_report_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_reply_state_text(self):
        """
        属性: 列表第一个举报的回复状态
        :return: 列表第一个举报的回复状态
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_reply_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_reply_user_text(self):
        """
        属性: 列表第一个举报的回复人
        :return: 列表第一个举报的回复人
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_reply_user_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_reply_time_text(self):
        """
        属性: 列表第一个举报的回复时间
        :return: 列表第一个举报的回复时间
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_reply_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_reply_button_text(self):
        """
        属性: 列表第一个举报的回复按钮
        :return: 列表第一个举报的回复按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_reply_button_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def report_reply_detail_reply_content_input(self):
        """
        属性: 举报回复详情回复内容输入框
        :return: 举报回复详情回复内容输入框
        """
        element = None
        try:
            element = self.project.get_element(self._report_reply_detail_reply_content_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def report_reply_detail_confirm_button(self):
        """
        属性: 举报回复详情确认按钮
        :return: 举报回复详情确认按钮
        """
        element = None
        try:
            element = self.project.get_element(self._report_reply_detail_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def report_reply_detail_cancel_button(self):
        """
        属性: 举报回复详情取消按钮
        :return: 举报回复详情取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._report_reply_detail_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_delete_button(self):
        """
        属性: 列表第一个举报的删除按钮
        :return: 列表第一个举报的删除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_delete_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def report_delete_confirm_button(self):
        """
        属性: 举报删除确认按钮
        :return: 举报删除确认按钮
        """
        element = None
        try:
            element = self.project.get_element(self._report_delete_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def report_delete_cancel_button(self):
        """
        属性: 举报删除取消按钮
        :return: 举报删除取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._report_delete_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def set_search_report_content_input_action(self, search_report_content_input):
        """
        动作：设置搜索-举报内容输入框
        :param search_report_content_input: 搜索-举报内容输入框
        :return: 设置'搜索-举报内容输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_report_content_input, search_report_content_input)
        return self.project.get_current_page_source()

    def set_search_report_user_input_action(self, search_report_user_input):
        """
        动作：设置搜搜-举报人ID输入框
        :param search_report_user_input: 搜搜-举报人ID输入框
        :return: 设置'搜搜-举报人ID输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_report_user_input, search_report_user_input)
        return self.project.get_current_page_source()

    def set_search_reported_user_input_action(self, search_reported_user_input):
        """
        动作：设置搜索-被举报人ID输入框
        :param search_reported_user_input: 搜索-被举报人ID输入框
        :return: 设置'搜索-被举报人ID输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_reported_user_input, search_reported_user_input)
        return self.project.get_current_page_source()

    def set_search_report_date_start_input_action(self, search_report_date_start_input):
        """
        动作：设置搜索-举报时间-开始日期输入框
        :param search_report_date_start_input: 搜索-举报时间-开始日期输入框
        :return: 设置'搜索-举报时间-开始日期输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_report_date_start_input, search_report_date_start_input)
        return self.project.get_current_page_source()

    def set_search_report_date_end_input_action(self, search_report_date_end_input):
        """
        动作：设置搜索-举报时间-结束日期输入框
        :param search_report_date_end_input: 搜索-举报时间-结束日期输入框
        :return: 设置'搜索-举报时间-结束日期输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_report_date_end_input, search_report_date_end_input)
        return self.project.get_current_page_source()

    def click_search_reply_state_button_action(self):
        """
        动作：点击搜索-回复状态下拉框
        :return: 点击'搜索-回复状态下拉框'按钮后的页面
        """
        self.project.click(self.search_reply_state_button)
        return self.project.get_current_page_source()

    def click_search_reply_state_all_button_action(self):
        """
        动作：点击搜索-回复状态-全部
        :return: 点击'搜索-回复状态-全部'按钮后的页面
        """
        self.project.click(self.search_reply_state_all_button)
        return self.project.get_current_page_source()

    def click_search_reply_state_replied_button_action(self):
        """
        动作：点击搜索-回复状态-已回复
        :return: 点击'搜索-回复状态-已回复'按钮后的页面
        """
        self.project.click(self.search_reply_state_replied_button)
        return self.project.get_current_page_source()

    def click_search_reply_state_not_replied_button_action(self):
        """
        动作：点击搜索-回复状态-未回复
        :return: 点击'搜索-回复状态-未回复'按钮后的页面
        """
        self.project.click(self.search_reply_state_not_replied_button)
        return self.project.get_current_page_source()

    def set_search_reply_user_input_action(self, search_reply_user_input):
        """
        动作：设置搜索-回复人输入框
        :param search_reply_user_input: 搜索-回复人输入框
        :return: 设置'搜索-回复人输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_reply_user_input, search_reply_user_input)
        return self.project.get_current_page_source()

    def set_search_reply_date_start_input_action(self, search_reply_date_start_input):
        """
        动作：设置搜索-回复时间-开始日期
        :param search_reply_date_start_input: 搜索-回复时间-开始日期
        :return: 设置'搜索-回复时间-开始日期'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_reply_date_start_input, search_reply_date_start_input)
        return self.project.get_current_page_source()

    def set_search_reply_date_end_input_action(self, search_reply_date_end_input):
        """
        动作：设置搜索-回复时间-结束日期
        :param search_reply_date_end_input: 搜索-回复时间-结束日期
        :return: 设置'搜索-回复时间-结束日期'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_reply_date_end_input, search_reply_date_end_input)
        return self.project.get_current_page_source()

    def click_search_business_category_button_action(self):
        """
        动作：点击搜索-业务类别下拉框
        :return: 点击'搜索-业务类别下拉框'按钮后的页面
        """
        self.project.click(self.search_business_category_button)
        return self.project.get_current_page_source()

    def click_search_business_category_all_button_action(self):
        """
        动作：点击搜索-业务类别-全部
        :return: 点击'搜索-业务类别-全部'按钮后的页面
        """
        self.project.click(self.search_business_category_all_button)
        return self.project.get_current_page_source()

    def click_search_business_category_article_button_action(self):
        """
        动作：点击搜索-业务类别-文章
        :return: 点击'搜索-业务类别-文章'按钮后的页面
        """
        self.project.click(self.search_business_category_article_button)
        return self.project.get_current_page_source()

    def click_search_business_category_course_button_action(self):
        """
        动作：点击搜索-业务类别-课程
        :return: 点击'搜索-业务类别-课程'按钮后的页面
        """
        self.project.click(self.search_business_category_course_button)
        return self.project.get_current_page_source()

    def click_search_business_category_user_button_action(self):
        """
        动作：点击搜索-业务类别-用户
        :return: 点击'搜索-业务类别-用户'按钮后的页面
        """
        self.project.click(self.search_business_category_user_button)
        return self.project.get_current_page_source()

    def click_search_business_category_order_button_action(self):
        """
        动作：点击搜索-业务类别-订单
        :return: 点击'搜索-业务类别-订单'按钮后的页面
        """
        self.project.click(self.search_business_category_order_button)
        return self.project.get_current_page_source()

    def click_search_business_category_question_button_action(self):
        """
        动作：点击搜索-业务类别-问题
        :return: 点击'搜索-业务类别-问题'按钮后的页面
        """
        self.project.click(self.search_business_category_question_button)
        return self.project.get_current_page_source()

    def click_search_report_reason_button_action(self):
        """
        动作：点击搜索-举报原因下拉框
        :return: 点击'搜索-举报原因下拉框'按钮后的页面
        """
        self.project.click(self.search_report_reason_button)
        return self.project.get_current_page_source()

    def click_search_report_reason_all_button_action(self):
        """
        动作：点击搜索-举报原因-全部
        :return: 点击'搜索-举报原因-全部'按钮后的页面
        """
        self.project.click(self.search_report_reason_all_button)
        return self.project.get_current_page_source()

    def click_search_report_reason_unknow_button_action(self):
        """
        动作：点击搜索-举报原因-未知
        :return: 点击'搜索-举报原因-未知'按钮后的页面
        """
        self.project.click(self.search_report_reason_unknow_button)
        return self.project.get_current_page_source()

    def click_search_report_reason_bad_fans_button_action(self):
        """
        动作：点击搜索-举报原因-不良粉丝
        :return: 点击'搜索-举报原因-不良粉丝'按钮后的页面
        """
        self.project.click(self.search_report_reason_bad_fans_button)
        return self.project.get_current_page_source()

    def click_search_report_reason_garbage_marketing_button_action(self):
        """
        动作：点击搜索-举报原因-垃圾营销
        :return: 点击'搜索-举报原因-垃圾营销'按钮后的页面
        """
        self.project.click(self.search_report_reason_garbage_marketing_button)
        return self.project.get_current_page_source()

    def click_search_report_reason_false_information_button_action(self):
        """
        动作：点击搜索-举报原因-不实信息
        :return: 点击'搜索-举报原因-不实信息'按钮后的页面
        """
        self.project.click(self.search_report_reason_false_information_button)
        return self.project.get_current_page_source()

    def click_search_report_reason_harmful_information_button_action(self):
        """
        动作：点击搜索-举报原因-有害信息
        :return: 点击'搜索-举报原因-有害信息'按钮后的页面
        """
        self.project.click(self.search_report_reason_harmful_information_button)
        return self.project.get_current_page_source()

    def click_search_report_reason_illegal_information_button_action(self):
        """
        动作：点击搜索-举报原因-违法信息
        :return: 点击'搜索-举报原因-违法信息'按钮后的页面
        """
        self.project.click(self.search_report_reason_illegal_information_button)
        return self.project.get_current_page_source()

    def click_search_report_reason_obscenity_button_action(self):
        """
        动作：点击搜索-举报原因-淫秽色情
        :return: 点击'搜索-举报原因-淫秽色情'按钮后的页面
        """
        self.project.click(self.search_report_reason_obscenity_button)
        return self.project.get_current_page_source()

    def click_search_report_reason_personal_attack_button_action(self):
        """
        动作：点击搜索-举报原因-人身攻击
        :return: 点击'搜索-举报原因-人身攻击'按钮后的页面
        """
        self.project.click(self.search_report_reason_personal_attack_button)
        return self.project.get_current_page_source()

    def click_search_report_reason_content_copy_button_action(self):
        """
        动作：点击搜索-举报原因-内容抄袭
        :return: 点击'搜索-举报原因-内容抄袭'按钮后的页面
        """
        self.project.click(self.search_report_reason_content_copy_button)
        return self.project.get_current_page_source()

    def click_search_report_reason_complain_button_action(self):
        """
        动作：点击搜索-举报原因-投诉
        :return: 点击'搜索-举报原因-投诉'按钮后的页面
        """
        self.project.click(self.search_report_reason_complain_button)
        return self.project.get_current_page_source()

    def click_search_report_reason_after_service_button_action(self):
        """
        动作：点击搜索-举报原因-申请售后
        :return: 点击'搜索-举报原因-申请售后'按钮后的页面
        """
        self.project.click(self.search_report_reason_after_service_button)
        return self.project.get_current_page_source()

    def click_search_channel_button_action(self):
        """
        动作：点击搜索-频道下拉框
        :return: 点击'搜索-频道下拉框'按钮后的页面
        """
        self.project.click(self.search_channel_button)
        return self.project.get_current_page_source()

    def click_search_channel_all_button_action(self):
        """
        动作：点击搜索-频道-全部
        :return: 点击'搜索-频道-全部'按钮后的页面
        """
        self.project.click(self.search_channel_all_button)
        return self.project.get_current_page_source()

    def click_search_channel_main_home_page_button_action(self):
        """
        动作：点击搜索-频道-总首页
        :return: 点击'搜索-频道-总首页'按钮后的页面
        """
        self.project.click(self.search_channel_main_home_page_button)
        return self.project.get_current_page_source()

    def click_search_channel_abroad_learning_button_action(self):
        """
        动作：点击搜索-频道-出国留学
        :return: 点击'搜索-频道-出国留学'按钮后的页面
        """
        self.project.click(self.search_channel_abroad_learning_button)
        return self.project.get_current_page_source()

    def click_search_channel_language_training_button_action(self):
        """
        动作：点击搜索-频道-语言培训
        :return: 点击'搜索-频道-语言培训'按钮后的页面
        """
        self.project.click(self.search_channel_language_training_button)
        return self.project.get_current_page_source()

    def click_search_channel_college_direction_button_action(self):
        """
        动作：点击搜索-频道-院校直通车
        :return: 点击'搜索-频道-院校直通车'按钮后的页面
        """
        self.project.click(self.search_channel_college_direction_button)
        return self.project.get_current_page_source()

    def click_search_channel_overseas_immigrants_button_action(self):
        """
        动作：点击搜索-频道-海外移民
        :return: 点击'搜索-频道-海外移民'按钮后的页面
        """
        self.project.click(self.search_channel_overseas_immigrants_button)
        return self.project.get_current_page_source()

    def click_search_button_action(self):
        """
        动作：点击查询按钮
        :return: 点击'查询按钮'按钮后的页面
        """
        self.project.click(self.search_button)
        return self.project.get_current_page_source()

    def click_clear_button_action(self):
        """
        动作：点击清除按钮
        :return: 点击'清除按钮'按钮后的页面
        """
        self.project.click(self.clear_button)
        return self.project.get_current_page_source()

    def get_list_first_channel_text_action(self):
        """
        动作：获取列表第一个举报的频道的文本
        :return: '列表第一个举报的频道'的文本
        """
        control_content = self.project.get_element_text(self.list_first_channel_text)
        return control_content

    def get_list_first_report_reason_text_action(self):
        """
        动作：获取列表第一个举报的举报原因的文本
        :return: '列表第一个举报的举报原因'的文本
        """
        control_content = self.project.get_element_text(self.list_first_report_reason_text)
        return control_content

    def get_list_first_order_id_text_action(self):
        """
        动作：获取列表第一个举报的订单编号的文本
        :return: '列表第一个举报的订单编号'的文本
        """
        control_content = self.project.get_element_text(self.list_first_order_id_text)
        return control_content

    def get_list_first_report_content_text_action(self):
        """
        动作：获取列表第一个举报的举报内容的文本
        :return: '列表第一个举报的举报内容'的文本
        """
        control_content = self.project.get_element_text(self.list_first_report_content_text)
        return control_content

    def get_list_first_reported_user_id_text_action(self):
        """
        动作：获取列表第一个举报的被举报人ID的文本
        :return: '列表第一个举报的被举报人ID'的文本
        """
        control_content = self.project.get_element_text(self.list_first_reported_user_id_text)
        return control_content

    def get_list_first_reported_nick_text_action(self):
        """
        动作：获取列表第一个举报的举报人昵称的文本
        :return: '列表第一个举报的举报人昵称'的文本
        """
        control_content = self.project.get_element_text(self.list_first_reported_nick_text)
        return control_content

    def get_list_first_reported_name_text_action(self):
        """
        动作：获取列表第一个举报的被举报人姓名的文本
        :return: '列表第一个举报的被举报人姓名'的文本
        """
        control_content = self.project.get_element_text(self.list_first_reported_name_text)
        return control_content

    def get_list_first_report_id_text_action(self):
        """
        动作：获取列表第一个举报的举报人ID的文本
        :return: '列表第一个举报的举报人ID'的文本
        """
        control_content = self.project.get_element_text(self.list_first_report_id_text)
        return control_content

    def get_list_first_report_nick_text_action(self):
        """
        动作：获取列表第一个举报的举报人昵称的文本
        :return: '列表第一个举报的举报人昵称'的文本
        """
        control_content = self.project.get_element_text(self.list_first_report_nick_text)
        return control_content

    def get_list_first_report_name_text_action(self):
        """
        动作：获取列表第一个举报的举报人姓名的文本
        :return: '列表第一个举报的举报人姓名'的文本
        """
        control_content = self.project.get_element_text(self.list_first_report_name_text)
        return control_content

    def get_list_first_report_mobile_text_action(self):
        """
        动作：获取列表第一个举报的举报人电话的文本
        :return: '列表第一个举报的举报人电话'的文本
        """
        control_content = self.project.get_element_text(self.list_first_report_mobile_text)
        return control_content

    def get_list_first_report_time_text_action(self):
        """
        动作：获取列表第一个举报的举报时间的文本
        :return: '列表第一个举报的举报时间'的文本
        """
        control_content = self.project.get_element_text(self.list_first_report_time_text)
        return control_content

    def get_list_first_reply_state_text_action(self):
        """
        动作：获取列表第一个举报的回复状态的文本
        :return: '列表第一个举报的回复状态'的文本
        """
        control_content = self.project.get_element_text(self.list_first_reply_state_text)
        return control_content

    def get_list_first_reply_user_text_action(self):
        """
        动作：获取列表第一个举报的回复人的文本
        :return: '列表第一个举报的回复人'的文本
        """
        control_content = self.project.get_element_text(self.list_first_reply_user_text)
        return control_content

    def get_list_first_reply_time_text_action(self):
        """
        动作：获取列表第一个举报的回复时间的文本
        :return: '列表第一个举报的回复时间'的文本
        """
        control_content = self.project.get_element_text(self.list_first_reply_time_text)
        return control_content

    def get_list_first_reply_button_text_action(self):
        """
        动作：获取列表第一个举报的回复按钮的文本
        :return: '列表第一个举报的回复按钮'的文本
        """
        control_content = self.project.get_element_text(self.list_first_reply_button_text)
        return control_content

    def set_report_reply_detail_reply_content_input_action(self, report_reply_detail_reply_content_input):
        """
        动作：设置举报回复详情回复内容输入框
        :param report_reply_detail_reply_content_input: 举报回复详情回复内容输入框
        :return: 设置'举报回复详情回复内容输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.report_reply_detail_reply_content_input, report_reply_detail_reply_content_input)
        return self.project.get_current_page_source()

    def click_report_reply_detail_confirm_button_action(self):
        """
        动作：点击举报回复详情确认按钮
        :return: 点击'举报回复详情确认按钮'按钮后的页面
        """
        self.project.click(self.report_reply_detail_confirm_button)
        return self.project.get_current_page_source()

    def click_report_reply_detail_cancel_button_action(self):
        """
        动作：点击举报回复详情取消按钮
        :return: 点击'举报回复详情取消按钮'按钮后的页面
        """
        self.project.click(self.report_reply_detail_cancel_button)
        return self.project.get_current_page_source()

    def click_list_first_delete_button_action(self):
        """
        动作：点击列表第一个举报的删除按钮
        :return: 点击'列表第一个举报的删除按钮'按钮后的页面
        """
        self.project.click(self.list_first_delete_button)
        return self.project.get_current_page_source()

    def click_report_delete_confirm_button_action(self):
        """
        动作：点击举报删除确认按钮
        :return: 点击'举报删除确认按钮'按钮后的页面
        """
        self.project.click(self.report_delete_confirm_button)
        return self.project.get_current_page_source()

    def click_report_delete_cancel_button_action(self):
        """
        动作：点击举报删除取消按钮
        :return: 点击'举报删除取消按钮'按钮后的页面
        """
        self.project.click(self.report_delete_cancel_button)
        return self.project.get_current_page_source()

    # endregion Actions
