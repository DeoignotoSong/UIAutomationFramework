from Utils.Log import log

"""
后台-运营中心-问答管理-问答列表
console_url/questions_and_answers/questions_list
"""


class ConsoleOperationCenterQaQuestionListPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/questions_and_answers/questions_list'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 搜索-问答ID输入框
        self._search_qa_id_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 搜索-问答标题
        self._search_qa_title_input_atg = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 搜索-问答状态下拉框
        self._search_qa_state_button_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div/div[1]'
        # 搜索-问答状态-全部
        self._search_qa_state_all_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[1]'
        # 搜索-问答状态-非悬赏
        self._search_qa_state_not_bounty_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[2]'
        # 搜索-问答状态-悬赏中
        self._search_qa_state_being_bounty_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[3]'
        # 搜索-问答状态-悬赏成功
        self._search_qa_state_bounty_success_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[4]'
        # 搜搜-问答状态-悬赏结束
        self._search_qa_state_bounty_over_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[5]'
        # 搜索-问答内容输入框
        self._search_qa_content_input_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div/input'
        # 搜索-创建人昵称输入框
        self._search_create_user_nick_input_tag = '//*[@id="tableSearch"]/form/div/div[5]/div/div/input'
        # 搜索-创建人姓名输入框
        self._search_create_user_name_input_tag = '//*[@id="tableSearch"]/form/div/div[6]/div/div/input'
        # 搜索-频道下拉框
        self._search_channel_button_tag = '//*[@id="tableSearch"]/form/div/div[7]/div/div/div[1]'
        # 搜索-频道-全部
        self._search_channel_all_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[1]'
        # 搜索-频道-出国留学
        self._search_channel_abroad_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[2]'
        # 搜索-频道-语言培训
        self._search_channel_language_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[3]'
        # 搜索-频道-院校直通车
        self._search_channel_school_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[4]'
        # 搜索-频道-海外移民
        self._search_channel_immi_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[5]'
        # 搜索-频道-总首页
        self._search_channel_homepage_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[6]'
        # 搜索-频道-学科辅导
        self._search_channel_coach_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[7]'
        # 搜索-一级类目标签下拉框
        self._search_first_label_button_tag = '//*[@id="tableSearch"]/form/div/div[8]/div/div/div[1]'
        # 搜索-一级类目标签-全部
        self._search_first_label_all_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[1]'
        # 搜索-二级类目标签下拉框
        self._search_second_label_button_tag = '//*[@id="tableSearch"]/form/div/div[9]/div/div/div[1]'
        # 搜索-二级类目标签-全部
        self._search_second_label_button_all_tag = '/html/body/div[5]/div[1]/div[1]/ul/li'
        # 搜索-内容主题下拉框
        self._search_sub_content_button_tag = '//*[@id="tableSearch"]/form/div/div[10]/div/div/div[1]'
        # 搜索-内容主题-全部
        self._search_sub_content_all_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li'
        # 搜索-最佳答案下拉框
        self._search_best_answer_button_tag = '//*[@id="tableSearch"]/form/div/div[11]/div/div/div[1]'
        # 搜索-最佳答案-全部
        self._search_best_answer_all_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[1]'
        # 搜索-最佳答案-是
        self._search_beset_answer_yes_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[2]'
        # 搜索-最佳答案-否
        self._search_best_answer_no_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[3]'
        # 搜索-查询按钮
        self._search_query_button_tag = '//*[@id="tableSearch"]/form/div/div[12]/div/button'
        # 搜索-清除按钮
        self._search_clear_button_tag = '//*[@id="tableSearch"]/form/div/div[13]/div/button'
        # 问答列表-第一个问答-问答ID按钮
        self._qa_list_first_qa_id_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a'
        # 问答列表-第一个问答-问答ID
        self._qa_list_first_qa_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a/span'
        # 问答列表-第一个问答-问答标题
        self._qa_list_first_qa_title_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 问答列表-第一个问答-频道
        self._qa_list_first_channel_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 问答列表-第一个问答-一级类目标签
        self._qa_list_first_first_label_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 问答列表-第一个问答-二级类目标签
        self._qa_list_first_second_label_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 问答列表-第一个问答-内容主题
        self._qa_list_first_sub_content_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div'
        # 问答列表-第一个问答-问答内容
        self._qa_list_first_qa_content_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div'
        # 问答列表-第一个问答-最佳答案
        self._qa_list_first_best_answer_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div'
        # 问答列表-第一个问答-回复数
        self._qa_list_first_reply_number_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[10]/div'
        # 问答列表-第一个问答-参与人数
        self._qa_list_first_participants_number_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[11]/div'
        # 问答列表-第一个问答-创建人昵称
        self._qa_list_first_create_user_nick_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[12]/div'
        # 问答列表-第一个问答-创建人姓名
        self._qa_list_first_create_user_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[13]/div'
        # 问答列表-第一个问答-问题创建时间
        self._qa_list_first_qa_create_time_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[14]/div'
        # 问答列表-第一个问答-删除按钮
        self._qa_list_first_delete_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[15]/div/a'
        # 问答列表-第一个问答-删除-确认
        self._qa_list_first_delete_confirm_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # 问答列表-第一个问答-删除-取消
        self._qa_list_first_delete_cancel_button_tag = '/html/body/div[2]/div/div[3]/button[1]'
        # 问答列表-第一个问答-删除-关闭
        self._qa_list_first_delete_close_button_tag = '/html/body/div[2]/div/div[1]/button/i'
        # 问答详情-问答ID
        self._qa_detail_qa_id_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 问答详情-问答标题
        self._qa_detail_qa_title_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 问答详情-悬赏状态
        self._qa_detail_bounty_state_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div/input'
        # 问答详情-悬赏内容
        self._qa_detail_bounty_content_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div/input'
        # 问答详情-发布人id
        self._qa_detail_create_user_id_tag = '//*[@id="tableSearch"]/form/div/div[5]/div/div/input'
        # 问答详情-发布人昵称
        self._qa_detail_create_user_nick_tag = '//*[@id="tableSearch"]/form/div/div[6]/div/div/input'
        # 问答详情-状态
        self._qa_detail_state_tag = '//*[@id="tableSearch"]/form/div/div[7]/div/div/input'
        # 问答详情-频道
        self._qa_detail_channel_tag = '//*[@id="tableSearch"]/form/div/div[8]/div/div/input'
        # 问答详情-一级类目标签
        self._qa_detail_first_label_tag = '//*[@id="tableSearch"]/form/div/div[9]/div/div/input'
        # 问答详情-二级类目标签
        self._qa_detail_second_label_tag = '//*[@id="tableSearch"]/form/div/div[10]/div/div/input'
        # 问答详情-内容主题
        self._qa_detail_sub_content_tag = '//*[@id="tableSearch"]/form/div/div[11]/div/div/input'
        # 问答详情-浏览数
        self._qa_detail_browse_number_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[2]/div/div/div[3]/table/tbody/tr/td[1]/div'
        # 问答详情-分享数
        self._qa_detail_share_number_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[2]/div/div/div[3]/table/tbody/tr/td[2]/div'
        # 问答详情-收藏数
        self._qa_detail_collect_number_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[2]/div/div/div[3]/table/tbody/tr/td[3]/div'
        # 问答详情-评论数
        self._qa_detail_comment_number_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[2]/div/div/div[3]/table/tbody/tr/td[4]/div'
        # 问答详情-点赞数
        self._qa_detail_liked_number_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[2]/div/div/div[3]/table/tbody/tr/td[5]/div'
        # 问答详情-一级回复列表-搜索-回复内容输入框
        self._qa_detail_first_level_reply_list_search_reply_content_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 问答详情-一级回复列表-搜索-回复人输入框
        self._qa_detail_first_level_reply_list_search_reply_user_name_input_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 问答详情-一级回复列表-搜索-回复id输入框
        self._qa_detail_first_level_reply_list_search_reply_user_id_input_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div/input'
        # 问答详情-一级回复列表-搜索-回复时间-开始日期
        self._qa_detail_first_level_reply_list_search_reply_date_start_input_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div/input[1]'
        # 问答详情-一级回复列表-搜索-回复日期-结束日期
        self._qa_detail_first_level_reply_list_search_reply_date_end_input_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div/input[2]'
        # 问答详情-一级回复列表-搜索-查询按钮
        self._qa_detail_first_level_reply_list_search_query_button_tag = '//*[@id="tableSearch"]/form/div/div[5]/div/button'
        # 问答详情-一级回复列表-搜搜-清除按钮
        self._qa_detail_first_level_reply_list_search_clear_button_tag = '//*[@id="tableSearch"]/form/div/div[6]/div/button'
        # 问答详情-一级回复列表-第一个回复-回复id
        self._qa_detail_first_level_reply_list_first_reply_id_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a'
        # 问答详情-一级回复列表-第一个回复-回复内容
        self._qa_detail_first_level_reply_list_first_reply_content_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 问答详情-一级回复列表-第一个回复-回复人
        self._qa_detail_first_level_reply_list_first_reply_user_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 问答详情-一级回复列表-第一个回复-回复时间
        self._qa_detail_first_level_reply_list_first_reply_time_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 问答详情-一级回复列表-第一个回复-回复渠道
        self._qa_detail_first_level_reply_list_first_reply_source_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 问答详情-一级回复列表-第一个回复-最佳答案
        self._qa_detail_first_level_reply_list_first_best_answer_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div'
        # 问答详情-一级回复列表-第一个回复-二级回复
        self._qa_detail_first_level_reply_list_first_second_level_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div'
        # 问答详情-一级回复列表-第一个回复-删除按钮
        self._qa_detail_first_level_reply_list_first_delete_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/a/span'
        # 问答小青-一级回复列表-第一个回复-删除按钮-确认
        self._qa_detail_first_level_reply_list_delete_confirm_button_tag = '/html/body/div[2]/div/div[3]/button[2]/span'
        # 问答小青-一级回复列表-第一个回复-删除按钮-取消
        self._qa_detail_first_level_reply_list_delete_cancel_button_tag = '/html/body/div[2]/div/div[3]/button[1]/span'
        # 问答小青-一级回复列表-第一个回复-删除按钮-关闭
        self._qa_detail_first_level_reply_list_delete_close_button_tag = '/html/body/div[2]/div/div[1]/button/i'
        # 问答回复详情-问答ID
        self._qa_reply_detail_qa_id_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 问答回复详情-回答标题
        self._qa_reply_detail_qa_title_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 问答回复详情-悬赏状态
        self._qa_reply_detail_bounty_state_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div/input'
        # 问答回复详情-悬赏内容
        self._qa_reply_detail_bounty_content_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div/input'
        # 问答回复详情-发布人id
        self._qa_reply_detail_create_user_id_tag = '//*[@id="tableSearch"]/form/div/div[5]/div/div/input'
        # 问答回复详情-发布人昵称
        self._qa_reply_detail_create_user_nick_tag = '//*[@id="tableSearch"]/form/div/div[6]/div/div/input'
        # 问答回复详情-状态
        self._qa_reply_detail_state_tag = '//*[@id="tableSearch"]/form/div/div[7]/div/div/input'
        # 问答回复详情-频道
        self._qa_reply_detail_channel_tag = '//*[@id="tableSearch"]/form/div/div[8]/div/div/input'
        # 问答回复详情-一级类目标签
        self._qa_reply_detail_first_label_tag = '//*[@id="tableSearch"]/form/div/div[9]/div/div/input'
        # 问答回复详情-二级类目标签
        self._qa_reply_detail_second_label_tag = '//*[@id="tableSearch"]/form/div/div[10]/div/div/input'
        # 问答回复详情-内容主题
        self._qa_reply_detail_sub_content_tag = '//*[@id="tableSearch"]/form/div/div[11]/div/div/input'
        # 问答回复详情-一级回复信息-回复人
        self._qa_reply_detail_first_level_info_reply_user_name_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 问答回复详情-一级回复信息-回复id
        self._qa_reply_detail_first_level_info_reply_id_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 问答回复详情-一级回复信息-回复时间
        self._qa_reply_detail_first_level_info_reply_time_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div/input'
        # 问答回复详情-一级回复信息-最佳答案
        self._qa_reply_detail_first_level_info_best_answer_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div/input'
        # 问答回复详情-一级回复信息-回复内容
        self._qa_reply_detail_first_level_info_reply_content_tag = '//*[@id="tableSearch"]/form/div/div[5]/div/div/textarea'
        # 问答回复详情-回复列表-二级回复ID按钮
        self._qa_reply_detail_reply_list_second_level_reply_id_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div[2]/div/div[1]/div[3]/table/tbody/tr/td[2]/div/a'
        # 问答回复详情-回复列表-二级回复ID
        self._qa_reply_detail_reply_list_second_level_reply_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div[2]/div/div[1]/div[3]/table/tbody/tr/td[2]/div/a/span'
        # 问答回复详情-回复列表-二级回复内容
        self._qa_reply_detail_reply_list_second_level_reply_content_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div[2]/div/div[1]/div[3]/table/tbody/tr/td[3]/div'
        # 问答回复详情-回复列表-二级回复人
        self._qa_reply_detail_reply_list_second_level_reply_user_nick_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div[2]/div/div[1]/div[3]/table/tbody/tr/td[4]/div'
        # 问答回复详情-回复列表-回复时间
        self._qa_reply_detail_reply_list_reply_time_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div[2]/div/div[1]/div[3]/table/tbody/tr/td[5]/div'
        # 问答回复详情-回复列表-回复渠道
        self._qa_reply_detail_reply_list_reply_source_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div[2]/div/div[1]/div[3]/table/tbody/tr/td[6]/div'
        # 问答回复详情-回复列表-删除按钮
        self._qa_reply_detail_reply_list_delete_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[3]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr/td[7]/div/a'
        # 问答回复详情-回复列表-删除-确定
        self._qa_reply_detail_reply_list_delete_confirm_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # 问答回复详情-回复列表-删除-取消
        self._qa_reply_detail_reply_list_delete_cancel_button_tag = '/html/body/div[2]/div/div[3]/button[1]'
        # 问答回复详情-回复列表-删除-关闭
        self._qa_reply_detail_reply_list_delete_close_button_tag = '/html/body/div[2]/div/div[1]/button/i'
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
    def search_qa_id_input(self):
        """
        属性: 搜索-问答ID输入框
        :return: 搜索-问答ID输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_qa_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_qa_state_button(self):
        """
        属性: 搜索-问答状态下拉框
        :return: 搜索-问答状态下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._search_qa_state_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_qa_state_all_button(self):
        """
        属性: 搜索-问答状态-全部
        :return: 搜索-问答状态-全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_qa_state_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_qa_state_not_bounty_button(self):
        """
        属性: 搜索-问答状态-非悬赏
        :return: 搜索-问答状态-非悬赏
        """
        element = None
        try:
            element = self.project.get_element(self._search_qa_state_not_bounty_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_qa_state_being_bounty_button(self):
        """
        属性: 搜索-问答状态-悬赏中
        :return: 搜索-问答状态-悬赏中
        """
        element = None
        try:
            element = self.project.get_element(self._search_qa_state_being_bounty_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_qa_state_bounty_success_button(self):
        """
        属性: 搜索-问答状态-悬赏成功
        :return: 搜索-问答状态-悬赏成功
        """
        element = None
        try:
            element = self.project.get_element(self._search_qa_state_bounty_success_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_qa_state_bounty_over_button(self):
        """
        属性: 搜搜-问答状态-悬赏结束
        :return: 搜搜-问答状态-悬赏结束
        """
        element = None
        try:
            element = self.project.get_element(self._search_qa_state_bounty_over_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_qa_content_input(self):
        """
        属性: 搜索-问答内容输入框
        :return: 搜索-问答内容输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_qa_content_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_create_user_nick_input(self):
        """
        属性: 搜索-创建人昵称输入框
        :return: 搜索-创建人昵称输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_create_user_nick_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_create_user_name_input(self):
        """
        属性: 搜索-创建人姓名输入框
        :return: 搜索-创建人姓名输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_create_user_name_input_tag)
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
    def search_channel_abroad_button(self):
        """
        属性: 搜索-频道-出国留学
        :return: 搜索-频道-出国留学
        """
        element = None
        try:
            element = self.project.get_element(self._search_channel_abroad_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_channel_language_button(self):
        """
        属性: 搜索-频道-语言培训
        :return: 搜索-频道-语言培训
        """
        element = None
        try:
            element = self.project.get_element(self._search_channel_language_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_channel_school_button(self):
        """
        属性: 搜索-频道-院校直通车
        :return: 搜索-频道-院校直通车
        """
        element = None
        try:
            element = self.project.get_element(self._search_channel_school_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_channel_immi_button(self):
        """
        属性: 搜索-频道-海外移民
        :return: 搜索-频道-海外移民
        """
        element = None
        try:
            element = self.project.get_element(self._search_channel_immi_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_channel_homepage_button(self):
        """
        属性: 搜索-频道-总首页
        :return: 搜索-频道-总首页
        """
        element = None
        try:
            element = self.project.get_element(self._search_channel_homepage_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_channel_coach_button(self):
        """
        属性: 搜索-频道-学科辅导
        :return: 搜索-频道-学科辅导
        """
        element = None
        try:
            element = self.project.get_element(self._search_channel_coach_button_tag)
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
    def search_first_label_all_button(self):
        """
        属性: 搜索-一级类目标签-全部
        :return: 搜索-一级类目标签-全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_first_label_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_second_label_button(self):
        """
        属性: 搜索-二级类目标签下拉框
        :return: 搜索-二级类目标签下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._search_second_label_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_second_label_button_all(self):
        """
        属性: 搜索-二级类目标签-全部
        :return: 搜索-二级类目标签-全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_second_label_button_all_tag)
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
    def search_sub_content_all_button(self):
        """
        属性: 搜索-内容主题-全部
        :return: 搜索-内容主题-全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_sub_content_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_best_answer_button(self):
        """
        属性: 搜索-最佳答案下拉框
        :return: 搜索-最佳答案下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._search_best_answer_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_best_answer_all_button(self):
        """
        属性: 搜索-最佳答案-全部
        :return: 搜索-最佳答案-全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_best_answer_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_beset_answer_yes_button(self):
        """
        属性: 搜索-最佳答案-是
        :return: 搜索-最佳答案-是
        """
        element = None
        try:
            element = self.project.get_element(self._search_beset_answer_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_best_answer_no_button(self):
        """
        属性: 搜索-最佳答案-否
        :return: 搜索-最佳答案-否
        """
        element = None
        try:
            element = self.project.get_element(self._search_best_answer_no_button_tag)
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
    def qa_list_first_qa_id_button(self):
        """
        属性: 问答列表-第一个问答-问答ID按钮
        :return: 问答列表-第一个问答-问答ID按钮
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_qa_id_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_qa_id_text(self):
        """
        属性: 问答列表-第一个问答-问答ID
        :return: 问答列表-第一个问答-问答ID
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_qa_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_qa_title_text(self):
        """
        属性: 问答列表-第一个问答-问答标题
        :return: 问答列表-第一个问答-问答标题
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_qa_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_channel_text(self):
        """
        属性: 问答列表-第一个问答-频道
        :return: 问答列表-第一个问答-频道
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_channel_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_first_label_text(self):
        """
        属性: 问答列表-第一个问答-一级类目标签
        :return: 问答列表-第一个问答-一级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_first_label_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_second_label_text(self):
        """
        属性: 问答列表-第一个问答-二级类目标签
        :return: 问答列表-第一个问答-二级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_second_label_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_sub_content_text(self):
        """
        属性: 问答列表-第一个问答-内容主题
        :return: 问答列表-第一个问答-内容主题
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_sub_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_qa_content_text(self):
        """
        属性: 问答列表-第一个问答-问答内容
        :return: 问答列表-第一个问答-问答内容
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_qa_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_best_answer_text(self):
        """
        属性: 问答列表-第一个问答-最佳答案
        :return: 问答列表-第一个问答-最佳答案
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_best_answer_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_reply_number_text(self):
        """
        属性: 问答列表-第一个问答-回复数
        :return: 问答列表-第一个问答-回复数
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_reply_number_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_participants_number_text(self):
        """
        属性: 问答列表-第一个问答-参与人数
        :return: 问答列表-第一个问答-参与人数
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_participants_number_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_create_user_nick_text(self):
        """
        属性: 问答列表-第一个问答-创建人昵称
        :return: 问答列表-第一个问答-创建人昵称
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_create_user_nick_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_create_user_name_text(self):
        """
        属性: 问答列表-第一个问答-创建人姓名
        :return: 问答列表-第一个问答-创建人姓名
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_create_user_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_qa_create_time_text(self):
        """
        属性: 问答列表-第一个问答-问题创建时间
        :return: 问答列表-第一个问答-问题创建时间
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_qa_create_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_delete_button(self):
        """
        属性: 问答列表-第一个问答-删除按钮
        :return: 问答列表-第一个问答-删除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_delete_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_delete_confirm_button(self):
        """
        属性: 问答列表-第一个问答-删除-确认
        :return: 问答列表-第一个问答-删除-确认
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_delete_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_delete_cancel_button(self):
        """
        属性: 问答列表-第一个问答-删除-取消
        :return: 问答列表-第一个问答-删除-取消
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_delete_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_list_first_delete_close_button(self):
        """
        属性: 问答列表-第一个问答-删除-关闭
        :return: 问答列表-第一个问答-删除-关闭
        """
        element = None
        try:
            element = self.project.get_element(self._qa_list_first_delete_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_qa_id(self):
        """
        属性: 问答详情-问答ID
        :return: 问答详情-问答ID
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_qa_id_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_qa_title(self):
        """
        属性: 问答详情-问答标题
        :return: 问答详情-问答标题
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_qa_title_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_bounty_state(self):
        """
        属性: 问答详情-悬赏状态
        :return: 问答详情-悬赏状态
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_bounty_state_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_bounty_content(self):
        """
        属性: 问答详情-悬赏内容
        :return: 问答详情-悬赏内容
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_bounty_content_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_create_user_id(self):
        """
        属性: 问答详情-发布人id
        :return: 问答详情-发布人id
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_create_user_id_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_create_user_nick(self):
        """
        属性: 问答详情-发布人昵称
        :return: 问答详情-发布人昵称
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_create_user_nick_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_state(self):
        """
        属性: 问答详情-状态
        :return: 问答详情-状态
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_state_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_channel(self):
        """
        属性: 问答详情-频道
        :return: 问答详情-频道
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_channel_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_label(self):
        """
        属性: 问答详情-一级类目标签
        :return: 问答详情-一级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_label_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_second_label(self):
        """
        属性: 问答详情-二级类目标签
        :return: 问答详情-二级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_second_label_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_sub_content(self):
        """
        属性: 问答详情-内容主题
        :return: 问答详情-内容主题
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_sub_content_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_browse_number_text(self):
        """
        属性: 问答详情-浏览数
        :return: 问答详情-浏览数
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_browse_number_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_share_number_text(self):
        """
        属性: 问答详情-分享数
        :return: 问答详情-分享数
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_share_number_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_collect_number_text(self):
        """
        属性: 问答详情-收藏数
        :return: 问答详情-收藏数
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_collect_number_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_comment_number_text(self):
        """
        属性: 问答详情-评论数
        :return: 问答详情-评论数
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_comment_number_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_liked_number_text(self):
        """
        属性: 问答详情-点赞数
        :return: 问答详情-点赞数
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_liked_number_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_search_reply_content_input(self):
        """
        属性: 问答详情-一级回复列表-搜索-回复内容输入框
        :return: 问答详情-一级回复列表-搜索-回复内容输入框
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_search_reply_content_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_search_reply_user_name_input(self):
        """
        属性: 问答详情-一级回复列表-搜索-回复人输入框
        :return: 问答详情-一级回复列表-搜索-回复人输入框
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_search_reply_user_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_search_reply_user_id_input(self):
        """
        属性: 问答详情-一级回复列表-搜索-回复id输入框
        :return: 问答详情-一级回复列表-搜索-回复id输入框
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_search_reply_user_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_search_reply_date_start_input(self):
        """
        属性: 问答详情-一级回复列表-搜索-回复时间-开始日期
        :return: 问答详情-一级回复列表-搜索-回复时间-开始日期
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_search_reply_date_start_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_search_reply_date_end_input(self):
        """
        属性: 问答详情-一级回复列表-搜索-回复日期-结束日期
        :return: 问答详情-一级回复列表-搜索-回复日期-结束日期
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_search_reply_date_end_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_search_query_button(self):
        """
        属性: 问答详情-一级回复列表-搜索-查询按钮
        :return: 问答详情-一级回复列表-搜索-查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_search_query_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_search_clear_button(self):
        """
        属性: 问答详情-一级回复列表-搜搜-清除按钮
        :return: 问答详情-一级回复列表-搜搜-清除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_search_clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_first_reply_id_button(self):
        """
        属性: 问答详情-一级回复列表-第一个回复-回复id
        :return: 问答详情-一级回复列表-第一个回复-回复id
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_first_reply_id_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_first_reply_content_text(self):
        """
        属性: 问答详情-一级回复列表-第一个回复-回复内容
        :return: 问答详情-一级回复列表-第一个回复-回复内容
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_first_reply_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_first_reply_user_name_text(self):
        """
        属性: 问答详情-一级回复列表-第一个回复-回复人
        :return: 问答详情-一级回复列表-第一个回复-回复人
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_first_reply_user_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_first_reply_time_text(self):
        """
        属性: 问答详情-一级回复列表-第一个回复-回复时间
        :return: 问答详情-一级回复列表-第一个回复-回复时间
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_first_reply_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_first_reply_source_text(self):
        """
        属性: 问答详情-一级回复列表-第一个回复-回复渠道
        :return: 问答详情-一级回复列表-第一个回复-回复渠道
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_first_reply_source_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_first_best_answer_text(self):
        """
        属性: 问答详情-一级回复列表-第一个回复-最佳答案
        :return: 问答详情-一级回复列表-第一个回复-最佳答案
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_first_best_answer_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_first_second_level_text(self):
        """
        属性: 问答详情-一级回复列表-第一个回复-二级回复
        :return: 问答详情-一级回复列表-第一个回复-二级回复
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_first_second_level_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_first_delete_button(self):
        """
        属性: 问答详情-一级回复列表-第一个回复-删除按钮
        :return: 问答详情-一级回复列表-第一个回复-删除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_first_delete_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_delete_confirm_button(self):
        """
        属性: 问答小青-一级回复列表-第一个回复-删除按钮-确认
        :return: 问答小青-一级回复列表-第一个回复-删除按钮-确认
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_delete_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_delete_cancel_button(self):
        """
        属性: 问答小青-一级回复列表-第一个回复-删除按钮-取消
        :return: 问答小青-一级回复列表-第一个回复-删除按钮-取消
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_delete_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_detail_first_level_reply_list_delete_close_button(self):
        """
        属性: 问答小青-一级回复列表-第一个回复-删除按钮-关闭
        :return: 问答小青-一级回复列表-第一个回复-删除按钮-关闭
        """
        element = None
        try:
            element = self.project.get_element(self._qa_detail_first_level_reply_list_delete_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_qa_id(self):
        """
        属性: 问答回复详情-问答ID
        :return: 问答回复详情-问答ID
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_qa_id_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_qa_title(self):
        """
        属性: 问答回复详情-回答标题
        :return: 问答回复详情-回答标题
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_qa_title_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_bounty_state(self):
        """
        属性: 问答回复详情-悬赏状态
        :return: 问答回复详情-悬赏状态
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_bounty_state_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_bounty_content(self):
        """
        属性: 问答回复详情-悬赏内容
        :return: 问答回复详情-悬赏内容
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_bounty_content_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_create_user_id(self):
        """
        属性: 问答回复详情-发布人id
        :return: 问答回复详情-发布人id
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_create_user_id_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_create_user_nick(self):
        """
        属性: 问答回复详情-发布人昵称
        :return: 问答回复详情-发布人昵称
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_create_user_nick_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_state(self):
        """
        属性: 问答回复详情-状态
        :return: 问答回复详情-状态
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_state_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_channel(self):
        """
        属性: 问答回复详情-频道
        :return: 问答回复详情-频道
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_channel_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_first_label(self):
        """
        属性: 问答回复详情-一级类目标签
        :return: 问答回复详情-一级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_first_label_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_second_label(self):
        """
        属性: 问答回复详情-二级类目标签
        :return: 问答回复详情-二级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_second_label_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_sub_content(self):
        """
        属性: 问答回复详情-内容主题
        :return: 问答回复详情-内容主题
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_sub_content_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_first_level_info_reply_user_name(self):
        """
        属性: 问答回复详情-一级回复信息-回复人
        :return: 问答回复详情-一级回复信息-回复人
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_first_level_info_reply_user_name_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_first_level_info_reply_id(self):
        """
        属性: 问答回复详情-一级回复信息-回复id
        :return: 问答回复详情-一级回复信息-回复id
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_first_level_info_reply_id_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_first_level_info_reply_time(self):
        """
        属性: 问答回复详情-一级回复信息-回复时间
        :return: 问答回复详情-一级回复信息-回复时间
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_first_level_info_reply_time_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_first_level_info_best_answer(self):
        """
        属性: 问答回复详情-一级回复信息-最佳答案
        :return: 问答回复详情-一级回复信息-最佳答案
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_first_level_info_best_answer_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_first_level_info_reply_content(self):
        """
        属性: 问答回复详情-一级回复信息-回复内容
        :return: 问答回复详情-一级回复信息-回复内容
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_first_level_info_reply_content_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_reply_list_second_level_reply_id_button(self):
        """
        属性: 问答回复详情-回复列表-二级回复ID按钮
        :return: 问答回复详情-回复列表-二级回复ID按钮
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_reply_list_second_level_reply_id_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_reply_list_second_level_reply_id_text(self):
        """
        属性: 问答回复详情-回复列表-二级回复ID
        :return: 问答回复详情-回复列表-二级回复ID
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_reply_list_second_level_reply_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_reply_list_second_level_reply_content_text(self):
        """
        属性: 问答回复详情-回复列表-二级回复内容
        :return: 问答回复详情-回复列表-二级回复内容
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_reply_list_second_level_reply_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_reply_list_second_level_reply_user_nick_text(self):
        """
        属性: 问答回复详情-回复列表-二级回复人
        :return: 问答回复详情-回复列表-二级回复人
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_reply_list_second_level_reply_user_nick_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_reply_list_reply_time_text(self):
        """
        属性: 问答回复详情-回复列表-回复时间
        :return: 问答回复详情-回复列表-回复时间
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_reply_list_reply_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_reply_list_reply_source_text(self):
        """
        属性: 问答回复详情-回复列表-回复渠道
        :return: 问答回复详情-回复列表-回复渠道
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_reply_list_reply_source_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_reply_list_delete_button(self):
        """
        属性: 问答回复详情-回复列表-删除按钮
        :return: 问答回复详情-回复列表-删除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_reply_list_delete_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_reply_list_delete_confirm_button(self):
        """
        属性: 问答回复详情-回复列表-删除-确定
        :return: 问答回复详情-回复列表-删除-确定
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_reply_list_delete_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_reply_list_delete_cancel_button(self):
        """
        属性: 问答回复详情-回复列表-删除-取消
        :return: 问答回复详情-回复列表-删除-取消
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_reply_list_delete_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def qa_reply_detail_reply_list_delete_close_button(self):
        """
        属性: 问答回复详情-回复列表-删除-关闭
        :return: 问答回复详情-回复列表-删除-关闭
        """
        element = None
        try:
            element = self.project.get_element(self._qa_reply_detail_reply_list_delete_close_button_tag)
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

    def set_search_qa_id_input_action(self, search_qa_id_input):
        """
        动作：设置搜索-问答ID输入框
        :param search_qa_id_input: 搜索-问答ID输入框
        :return: 设置'搜索-问答ID输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_qa_id_input, search_qa_id_input)
        return self.project.get_current_page_source()

    def click_search_qa_state_button_action(self):
        """
        动作：点击搜索-问答状态下拉框
        :return: 点击'搜索-问答状态下拉框'按钮后的页面
        """
        self.project.click(self.search_qa_state_button)
        return self.project.get_current_page_source()

    def click_search_qa_state_all_button_action(self):
        """
        动作：点击搜索-问答状态-全部
        :return: 点击'搜索-问答状态-全部'按钮后的页面
        """
        self.project.click(self.search_qa_state_all_button)
        return self.project.get_current_page_source()

    def click_search_qa_state_not_bounty_button_action(self):
        """
        动作：点击搜索-问答状态-非悬赏
        :return: 点击'搜索-问答状态-非悬赏'按钮后的页面
        """
        self.project.click(self.search_qa_state_not_bounty_button)
        return self.project.get_current_page_source()

    def click_search_qa_state_being_bounty_button_action(self):
        """
        动作：点击搜索-问答状态-悬赏中
        :return: 点击'搜索-问答状态-悬赏中'按钮后的页面
        """
        self.project.click(self.search_qa_state_being_bounty_button)
        return self.project.get_current_page_source()

    def click_search_qa_state_bounty_success_button_action(self):
        """
        动作：点击搜索-问答状态-悬赏成功
        :return: 点击'搜索-问答状态-悬赏成功'按钮后的页面
        """
        self.project.click(self.search_qa_state_bounty_success_button)
        return self.project.get_current_page_source()

    def click_search_qa_state_bounty_over_button_action(self):
        """
        动作：点击搜搜-问答状态-悬赏结束
        :return: 点击'搜搜-问答状态-悬赏结束'按钮后的页面
        """
        self.project.click(self.search_qa_state_bounty_over_button)
        return self.project.get_current_page_source()

    def set_search_qa_content_input_action(self, search_qa_content_input):
        """
        动作：设置搜索-问答内容输入框
        :param search_qa_content_input: 搜索-问答内容输入框
        :return: 设置'搜索-问答内容输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_qa_content_input, search_qa_content_input)
        return self.project.get_current_page_source()

    def set_search_create_user_nick_input_action(self, search_create_user_nick_input):
        """
        动作：设置搜索-创建人昵称输入框
        :param search_create_user_nick_input: 搜索-创建人昵称输入框
        :return: 设置'搜索-创建人昵称输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_create_user_nick_input, search_create_user_nick_input)
        return self.project.get_current_page_source()

    def set_search_create_user_name_input_action(self, search_create_user_name_input):
        """
        动作：设置搜索-创建人姓名输入框
        :param search_create_user_name_input: 搜索-创建人姓名输入框
        :return: 设置'搜索-创建人姓名输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_create_user_name_input, search_create_user_name_input)
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

    def click_search_channel_abroad_button_action(self):
        """
        动作：点击搜索-频道-出国留学
        :return: 点击'搜索-频道-出国留学'按钮后的页面
        """
        self.project.click(self.search_channel_abroad_button)
        return self.project.get_current_page_source()

    def click_search_channel_language_button_action(self):
        """
        动作：点击搜索-频道-语言培训
        :return: 点击'搜索-频道-语言培训'按钮后的页面
        """
        self.project.click(self.search_channel_language_button)
        return self.project.get_current_page_source()

    def click_search_channel_school_button_action(self):
        """
        动作：点击搜索-频道-院校直通车
        :return: 点击'搜索-频道-院校直通车'按钮后的页面
        """
        self.project.click(self.search_channel_school_button)
        return self.project.get_current_page_source()

    def click_search_channel_immi_button_action(self):
        """
        动作：点击搜索-频道-海外移民
        :return: 点击'搜索-频道-海外移民'按钮后的页面
        """
        self.project.click(self.search_channel_immi_button)
        return self.project.get_current_page_source()

    def click_search_channel_homepage_button_action(self):
        """
        动作：点击搜索-频道-总首页
        :return: 点击'搜索-频道-总首页'按钮后的页面
        """
        self.project.click(self.search_channel_homepage_button)
        return self.project.get_current_page_source()

    def click_search_channel_coach_button_action(self):
        """
        动作：点击搜索-频道-学科辅导
        :return: 点击'搜索-频道-学科辅导'按钮后的页面
        """
        self.project.click(self.search_channel_coach_button)
        return self.project.get_current_page_source()

    def click_search_first_label_button_action(self):
        """
        动作：点击搜索-一级类目标签下拉框
        :return: 点击'搜索-一级类目标签下拉框'按钮后的页面
        """
        self.project.click(self.search_first_label_button)
        return self.project.get_current_page_source()

    def click_search_first_label_all_button_action(self):
        """
        动作：点击搜索-一级类目标签-全部
        :return: 点击'搜索-一级类目标签-全部'按钮后的页面
        """
        self.project.click(self.search_first_label_all_button)
        return self.project.get_current_page_source()

    def click_search_second_label_button_action(self):
        """
        动作：点击搜索-二级类目标签下拉框
        :return: 点击'搜索-二级类目标签下拉框'按钮后的页面
        """
        self.project.click(self.search_second_label_button)
        return self.project.get_current_page_source()

    def click_search_sub_content_button_action(self):
        """
        动作：点击搜索-内容主题下拉框
        :return: 点击'搜索-内容主题下拉框'按钮后的页面
        """
        self.project.click(self.search_sub_content_button)
        return self.project.get_current_page_source()

    def click_search_sub_content_all_button_action(self):
        """
        动作：点击搜索-内容主题-全部
        :return: 点击'搜索-内容主题-全部'按钮后的页面
        """
        self.project.click(self.search_sub_content_all_button)
        return self.project.get_current_page_source()

    def click_search_best_answer_button_action(self):
        """
        动作：点击搜索-最佳答案下拉框
        :return: 点击'搜索-最佳答案下拉框'按钮后的页面
        """
        self.project.click(self.search_best_answer_button)
        return self.project.get_current_page_source()

    def click_search_best_answer_all_button_action(self):
        """
        动作：点击搜索-最佳答案-全部
        :return: 点击'搜索-最佳答案-全部'按钮后的页面
        """
        self.project.click(self.search_best_answer_all_button)
        return self.project.get_current_page_source()

    def click_search_beset_answer_yes_button_action(self):
        """
        动作：点击搜索-最佳答案-是
        :return: 点击'搜索-最佳答案-是'按钮后的页面
        """
        self.project.click(self.search_beset_answer_yes_button)
        return self.project.get_current_page_source()

    def click_search_best_answer_no_button_action(self):
        """
        动作：点击搜索-最佳答案-否
        :return: 点击'搜索-最佳答案-否'按钮后的页面
        """
        self.project.click(self.search_best_answer_no_button)
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

    def click_qa_list_first_qa_id_button_action(self):
        """
        动作：点击问答列表-第一个问答-问答ID按钮
        :return: 点击'问答列表-第一个问答-问答ID按钮'按钮后的页面
        """
        self.project.click(self.qa_list_first_qa_id_button)
        return self.project.get_current_page_source()

    def get_qa_list_first_qa_id_text_action(self):
        """
        动作：获取问答列表-第一个问答-问答ID的文本
        :return: '问答列表-第一个问答-问答ID'的文本
        """
        control_content = self.project.get_element_text(self.qa_list_first_qa_id_text)
        return control_content

    def get_qa_list_first_qa_title_text_action(self):
        """
        动作：获取问答列表-第一个问答-问答标题的文本
        :return: '问答列表-第一个问答-问答标题'的文本
        """
        control_content = self.project.get_element_text(self.qa_list_first_qa_title_text)
        return control_content

    def get_qa_list_first_channel_text_action(self):
        """
        动作：获取问答列表-第一个问答-频道的文本
        :return: '问答列表-第一个问答-频道'的文本
        """
        control_content = self.project.get_element_text(self.qa_list_first_channel_text)
        return control_content

    def get_qa_list_first_first_label_text_action(self):
        """
        动作：获取问答列表-第一个问答-一级类目标签的文本
        :return: '问答列表-第一个问答-一级类目标签'的文本
        """
        control_content = self.project.get_element_text(self.qa_list_first_first_label_text)
        return control_content

    def get_qa_list_first_second_label_text_action(self):
        """
        动作：获取问答列表-第一个问答-二级类目标签的文本
        :return: '问答列表-第一个问答-二级类目标签'的文本
        """
        control_content = self.project.get_element_text(self.qa_list_first_second_label_text)
        return control_content

    def get_qa_list_first_sub_content_text_action(self):
        """
        动作：获取问答列表-第一个问答-内容主题的文本
        :return: '问答列表-第一个问答-内容主题'的文本
        """
        control_content = self.project.get_element_text(self.qa_list_first_sub_content_text)
        return control_content

    def get_qa_list_first_qa_content_text_action(self):
        """
        动作：获取问答列表-第一个问答-问答内容的文本
        :return: '问答列表-第一个问答-问答内容'的文本
        """
        control_content = self.project.get_element_text(self.qa_list_first_qa_content_text)
        return control_content

    def get_qa_list_first_best_answer_text_action(self):
        """
        动作：获取问答列表-第一个问答-最佳答案的文本
        :return: '问答列表-第一个问答-最佳答案'的文本
        """
        control_content = self.project.get_element_text(self.qa_list_first_best_answer_text)
        return control_content

    def get_qa_list_first_reply_number_text_action(self):
        """
        动作：获取问答列表-第一个问答-回复数的文本
        :return: '问答列表-第一个问答-回复数'的文本
        """
        control_content = self.project.get_element_text(self.qa_list_first_reply_number_text)
        return control_content

    def get_qa_list_first_participants_number_text_action(self):
        """
        动作：获取问答列表-第一个问答-参与人数的文本
        :return: '问答列表-第一个问答-参与人数'的文本
        """
        control_content = self.project.get_element_text(self.qa_list_first_participants_number_text)
        return control_content

    def get_qa_list_first_create_user_nick_text_action(self):
        """
        动作：获取问答列表-第一个问答-创建人昵称的文本
        :return: '问答列表-第一个问答-创建人昵称'的文本
        """
        control_content = self.project.get_element_text(self.qa_list_first_create_user_nick_text)
        return control_content

    def get_qa_list_first_create_user_name_text_action(self):
        """
        动作：获取问答列表-第一个问答-创建人姓名的文本
        :return: '问答列表-第一个问答-创建人姓名'的文本
        """
        control_content = self.project.get_element_text(self.qa_list_first_create_user_name_text)
        return control_content

    def get_qa_list_first_qa_create_time_text_action(self):
        """
        动作：获取问答列表-第一个问答-问题创建时间的文本
        :return: '问答列表-第一个问答-问题创建时间'的文本
        """
        control_content = self.project.get_element_text(self.qa_list_first_qa_create_time_text)
        return control_content

    def click_qa_list_first_delete_button_action(self):
        """
        动作：点击问答列表-第一个问答-删除按钮
        :return: 点击'问答列表-第一个问答-删除按钮'按钮后的页面
        """
        self.project.click(self.qa_list_first_delete_button)
        return self.project.get_current_page_source()

    def click_qa_list_first_delete_confirm_button_action(self):
        """
        动作：点击问答列表-第一个问答-删除-确认
        :return: 点击'问答列表-第一个问答-删除-确认'按钮后的页面
        """
        self.project.click(self.qa_list_first_delete_confirm_button)
        return self.project.get_current_page_source()

    def click_qa_list_first_delete_cancel_button_action(self):
        """
        动作：点击问答列表-第一个问答-删除-取消
        :return: 点击'问答列表-第一个问答-删除-取消'按钮后的页面
        """
        self.project.click(self.qa_list_first_delete_cancel_button)
        return self.project.get_current_page_source()

    def click_qa_list_first_delete_close_button_action(self):
        """
        动作：点击问答列表-第一个问答-删除-关闭
        :return: 点击'问答列表-第一个问答-删除-关闭'按钮后的页面
        """
        self.project.click(self.qa_list_first_delete_close_button)
        return self.project.get_current_page_source()

    def get_qa_detail_browse_number_text_action(self):
        """
        动作：获取问答详情-浏览数的文本
        :return: '问答详情-浏览数'的文本
        """
        control_content = self.project.get_element_text(self.qa_detail_browse_number_text)
        return control_content

    def get_qa_detail_share_number_text_action(self):
        """
        动作：获取问答详情-分享数的文本
        :return: '问答详情-分享数'的文本
        """
        control_content = self.project.get_element_text(self.qa_detail_share_number_text)
        return control_content

    def get_qa_detail_collect_number_text_action(self):
        """
        动作：获取问答详情-收藏数的文本
        :return: '问答详情-收藏数'的文本
        """
        control_content = self.project.get_element_text(self.qa_detail_collect_number_text)
        return control_content

    def get_qa_detail_comment_number_text_action(self):
        """
        动作：获取问答详情-评论数的文本
        :return: '问答详情-评论数'的文本
        """
        control_content = self.project.get_element_text(self.qa_detail_comment_number_text)
        return control_content

    def get_qa_detail_liked_number_text_action(self):
        """
        动作：获取问答详情-点赞数的文本
        :return: '问答详情-点赞数'的文本
        """
        control_content = self.project.get_element_text(self.qa_detail_liked_number_text)
        return control_content

    def set_qa_detail_first_level_reply_list_search_reply_content_input_action(self, qa_detail_first_level_reply_list_search_reply_content_input):
        """
        动作：设置问答详情-一级回复列表-搜索-回复内容输入框
        :param qa_detail_first_level_reply_list_search_reply_content_input: 问答详情-一级回复列表-搜索-回复内容输入框
        :return: 设置'问答详情-一级回复列表-搜索-回复内容输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.qa_detail_first_level_reply_list_search_reply_content_input, qa_detail_first_level_reply_list_search_reply_content_input)
        return self.project.get_current_page_source()

    def set_qa_detail_first_level_reply_list_search_reply_user_name_input_action(self, qa_detail_first_level_reply_list_search_reply_user_name_input):
        """
        动作：设置问答详情-一级回复列表-搜索-回复人输入框
        :param qa_detail_first_level_reply_list_search_reply_user_name_input: 问答详情-一级回复列表-搜索-回复人输入框
        :return: 设置'问答详情-一级回复列表-搜索-回复人输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.qa_detail_first_level_reply_list_search_reply_user_name_input, qa_detail_first_level_reply_list_search_reply_user_name_input)
        return self.project.get_current_page_source()

    def set_qa_detail_first_level_reply_list_search_reply_user_id_input_action(self, qa_detail_first_level_reply_list_search_reply_user_id_input):
        """
        动作：设置问答详情-一级回复列表-搜索-回复id输入框
        :param qa_detail_first_level_reply_list_search_reply_user_id_input: 问答详情-一级回复列表-搜索-回复id输入框
        :return: 设置'问答详情-一级回复列表-搜索-回复id输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.qa_detail_first_level_reply_list_search_reply_user_id_input, qa_detail_first_level_reply_list_search_reply_user_id_input)
        return self.project.get_current_page_source()

    def set_qa_detail_first_level_reply_list_search_reply_date_start_input_action(self, qa_detail_first_level_reply_list_search_reply_date_start_input):
        """
        动作：设置问答详情-一级回复列表-搜索-回复时间-开始日期
        :param qa_detail_first_level_reply_list_search_reply_date_start_input: 问答详情-一级回复列表-搜索-回复时间-开始日期
        :return: 设置'问答详情-一级回复列表-搜索-回复时间-开始日期'文本后的页面
        """
        self.project.clear_and_send_keys(self.qa_detail_first_level_reply_list_search_reply_date_start_input, qa_detail_first_level_reply_list_search_reply_date_start_input)
        return self.project.get_current_page_source()

    def set_qa_detail_first_level_reply_list_search_reply_date_end_input_action(self, qa_detail_first_level_reply_list_search_reply_date_end_input):
        """
        动作：设置问答详情-一级回复列表-搜索-回复日期-结束日期
        :param qa_detail_first_level_reply_list_search_reply_date_end_input: 问答详情-一级回复列表-搜索-回复日期-结束日期
        :return: 设置'问答详情-一级回复列表-搜索-回复日期-结束日期'文本后的页面
        """
        self.project.clear_and_send_keys(self.qa_detail_first_level_reply_list_search_reply_date_end_input, qa_detail_first_level_reply_list_search_reply_date_end_input)
        return self.project.get_current_page_source()

    def click_qa_detail_first_level_reply_list_search_query_button_action(self):
        """
        动作：点击问答详情-一级回复列表-搜索-查询按钮
        :return: 点击'问答详情-一级回复列表-搜索-查询按钮'按钮后的页面
        """
        self.project.click(self.qa_detail_first_level_reply_list_search_query_button)
        return self.project.get_current_page_source()

    def click_qa_detail_first_level_reply_list_search_clear_button_action(self):
        """
        动作：点击问答详情-一级回复列表-搜搜-清除按钮
        :return: 点击'问答详情-一级回复列表-搜搜-清除按钮'按钮后的页面
        """
        self.project.click(self.qa_detail_first_level_reply_list_search_clear_button)
        return self.project.get_current_page_source()

    def click_qa_detail_first_level_reply_list_first_reply_id_button_action(self):
        """
        动作：点击问答详情-一级回复列表-第一个回复-回复id
        :return: 点击'问答详情-一级回复列表-第一个回复-回复id'按钮后的页面
        """
        self.project.click(self.qa_detail_first_level_reply_list_first_reply_id_button)
        return self.project.get_current_page_source()

    def get_qa_detail_first_level_reply_list_first_reply_content_text_action(self):
        """
        动作：获取问答详情-一级回复列表-第一个回复-回复内容的文本
        :return: '问答详情-一级回复列表-第一个回复-回复内容'的文本
        """
        control_content = self.project.get_element_text(self.qa_detail_first_level_reply_list_first_reply_content_text)
        return control_content

    def get_qa_detail_first_level_reply_list_first_reply_user_name_text_action(self):
        """
        动作：获取问答详情-一级回复列表-第一个回复-回复人的文本
        :return: '问答详情-一级回复列表-第一个回复-回复人'的文本
        """
        control_content = self.project.get_element_text(self.qa_detail_first_level_reply_list_first_reply_user_name_text)
        return control_content

    def get_qa_detail_first_level_reply_list_first_reply_time_text_action(self):
        """
        动作：获取问答详情-一级回复列表-第一个回复-回复时间的文本
        :return: '问答详情-一级回复列表-第一个回复-回复时间'的文本
        """
        control_content = self.project.get_element_text(self.qa_detail_first_level_reply_list_first_reply_time_text)
        return control_content

    def get_qa_detail_first_level_reply_list_first_reply_source_text_action(self):
        """
        动作：获取问答详情-一级回复列表-第一个回复-回复渠道的文本
        :return: '问答详情-一级回复列表-第一个回复-回复渠道'的文本
        """
        control_content = self.project.get_element_text(self.qa_detail_first_level_reply_list_first_reply_source_text)
        return control_content

    def get_qa_detail_first_level_reply_list_first_best_answer_text_action(self):
        """
        动作：获取问答详情-一级回复列表-第一个回复-最佳答案的文本
        :return: '问答详情-一级回复列表-第一个回复-最佳答案'的文本
        """
        control_content = self.project.get_element_text(self.qa_detail_first_level_reply_list_first_best_answer_text)
        return control_content

    def get_qa_detail_first_level_reply_list_first_second_level_text_action(self):
        """
        动作：获取问答详情-一级回复列表-第一个回复-二级回复的文本
        :return: '问答详情-一级回复列表-第一个回复-二级回复'的文本
        """
        control_content = self.project.get_element_text(self.qa_detail_first_level_reply_list_first_second_level_text)
        return control_content

    def click_qa_detail_first_level_reply_list_first_delete_button_action(self):
        """
        动作：点击问答详情-一级回复列表-第一个回复-删除按钮
        :return: 点击'问答详情-一级回复列表-第一个回复-删除按钮'按钮后的页面
        """
        self.project.click(self.qa_detail_first_level_reply_list_first_delete_button)
        return self.project.get_current_page_source()

    def click_qa_detail_first_level_reply_list_delete_confirm_button_action(self):
        """
        动作：点击问答小青-一级回复列表-第一个回复-删除按钮-确认
        :return: 点击'问答小青-一级回复列表-第一个回复-删除按钮-确认'按钮后的页面
        """
        self.project.click(self.qa_detail_first_level_reply_list_delete_confirm_button)
        return self.project.get_current_page_source()

    def click_qa_detail_first_level_reply_list_delete_cancel_button_action(self):
        """
        动作：点击问答小青-一级回复列表-第一个回复-删除按钮-取消
        :return: 点击'问答小青-一级回复列表-第一个回复-删除按钮-取消'按钮后的页面
        """
        self.project.click(self.qa_detail_first_level_reply_list_delete_cancel_button)
        return self.project.get_current_page_source()

    def click_qa_detail_first_level_reply_list_delete_close_button_action(self):
        """
        动作：点击问答小青-一级回复列表-第一个回复-删除按钮-关闭
        :return: 点击'问答小青-一级回复列表-第一个回复-删除按钮-关闭'按钮后的页面
        """
        self.project.click(self.qa_detail_first_level_reply_list_delete_close_button)
        return self.project.get_current_page_source()

    def click_qa_reply_detail_reply_list_second_level_reply_id_button_action(self):
        """
        动作：点击问答回复详情-回复列表-二级回复ID按钮
        :return: 点击'问答回复详情-回复列表-二级回复ID按钮'按钮后的页面
        """
        self.project.click(self.qa_reply_detail_reply_list_second_level_reply_id_button)
        return self.project.get_current_page_source()

    def get_qa_reply_detail_reply_list_second_level_reply_id_text_action(self):
        """
        动作：获取问答回复详情-回复列表-二级回复ID的文本
        :return: '问答回复详情-回复列表-二级回复ID'的文本
        """
        control_content = self.project.get_element_text(self.qa_reply_detail_reply_list_second_level_reply_id_text)
        return control_content

    def get_qa_reply_detail_reply_list_second_level_reply_content_text_action(self):
        """
        动作：获取问答回复详情-回复列表-二级回复内容的文本
        :return: '问答回复详情-回复列表-二级回复内容'的文本
        """
        control_content = self.project.get_element_text(self.qa_reply_detail_reply_list_second_level_reply_content_text)
        return control_content

    def get_qa_reply_detail_reply_list_second_level_reply_user_nick_text_action(self):
        """
        动作：获取问答回复详情-回复列表-二级回复人的文本
        :return: '问答回复详情-回复列表-二级回复人'的文本
        """
        control_content = self.project.get_element_text(self.qa_reply_detail_reply_list_second_level_reply_user_nick_text)
        return control_content

    def get_qa_reply_detail_reply_list_reply_time_text_action(self):
        """
        动作：获取问答回复详情-回复列表-回复时间的文本
        :return: '问答回复详情-回复列表-回复时间'的文本
        """
        control_content = self.project.get_element_text(self.qa_reply_detail_reply_list_reply_time_text)
        return control_content

    def get_qa_reply_detail_reply_list_reply_source_text_action(self):
        """
        动作：获取问答回复详情-回复列表-回复渠道的文本
        :return: '问答回复详情-回复列表-回复渠道'的文本
        """
        control_content = self.project.get_element_text(self.qa_reply_detail_reply_list_reply_source_text)
        return control_content

    def click_qa_reply_detail_reply_list_delete_button_action(self):
        """
        动作：点击问答回复详情-回复列表-删除按钮
        :return: 点击'问答回复详情-回复列表-删除按钮'按钮后的页面
        """
        self.project.click(self.qa_reply_detail_reply_list_delete_button)
        return self.project.get_current_page_source()

    def click_qa_reply_detail_reply_list_delete_confirm_button_action(self):
        """
        动作：点击问答回复详情-回复列表-删除-确定
        :return: 点击'问答回复详情-回复列表-删除-确定'按钮后的页面
        """
        self.project.click(self.qa_reply_detail_reply_list_delete_confirm_button)
        return self.project.get_current_page_source()

    def click_qa_reply_detail_reply_list_delete_cancel_button_action(self):
        """
        动作：点击问答回复详情-回复列表-删除-取消
        :return: 点击'问答回复详情-回复列表-删除-取消'按钮后的页面
        """
        self.project.click(self.qa_reply_detail_reply_list_delete_cancel_button)
        return self.project.get_current_page_source()

    def click_qa_reply_detail_reply_list_delete_close_button_action(self):
        """
        动作：点击问答回复详情-回复列表-删除-关闭
        :return: 点击'问答回复详情-回复列表-删除-关闭'按钮后的页面
        """
        self.project.click(self.qa_reply_detail_reply_list_delete_close_button)
        return self.project.get_current_page_source()

    # endregion Actions
