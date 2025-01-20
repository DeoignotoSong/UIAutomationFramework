from Utils.Log import log

"""
后台首页-运营中心-问答管理-话题列表
console_url/questions_and_answers/topic_list
"""


class ConsoleOperationCenterQaTopicListPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/questions_and_answers/topic_list'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 加载图层
        self._loading_mask_tag = '/html/body/div[last()]/div/svg'
        # 下拉列表
        self._drop_down_list_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 搜索-话题ID
        self._search_topic_id_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[1]/div/div/input'
        # 搜索-话题标题
        self._search_topic_title_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[2]/div/div/input'
        # 搜索-发布时间-开始日期输入框
        self._search_publish_time_start_date_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[3]/div/div/input[1]'
        # 搜素-发布时间-结束日期输入框
        self._search_publish_time_end_date_input_tag = '//*[@id="tableSearch"]/form/div[1]/div[3]/div/div/input[2]'
        # 搜索-话题频道下拉框
        self._search_topic_channel_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[4]/div/div'
        # 搜索-一级类目标签下拉框
        self._search_topic_first_label_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[5]/div/div/div'
        # 搜索-二级类目标签下拉框
        self._search_topic_second_label_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[6]/div/div/div[1]'
        # 搜索-查询按钮
        self._search_query_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[7]/div/button'
        # 搜索-清除按钮
        self._search_clear_button_tag = '//*[@id="tableSearch"]/form/div[1]/div[8]/div/button'
        # 列表-第一个话题-话题ID按钮
        self._list_first_topic_id_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a'
        # 列表-第一个话题-话题ID文本
        self._list_first_topic_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a/span'
        # 列表-第一个话题-标题
        self._list_first_topic_title_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 列表-第一个话题-内容
        self._list_first_topic_content_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 列表-第一个话题-频道
        self._list_first_topic_channel_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 列表-第一个话题-一级类目标签
        self._list_first_topic_first_label_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 列表-第一个话题-二级类目标签
        self._list_first_topic_second_label_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div'
        # 列表-第一个话题-创建人
        self._list_first_topic_create_user_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div'
        # 列表-第一个话题-创建时间
        self._list_first_topic_create_time_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div'
        # 列表-第一个话题-编辑按钮
        self._list_first_topic_update_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/a[1]'
        # 列表-第一个话题-删除按钮
        self._list_first_topic_delete_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/a[2]'
        # 列表-第一个话题-删除-确认按钮
        self._list_first_topic_delete_confirm_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # 列表-第一个话题-删除-取消按钮
        self._list_first_topic_delete_cancel_button_tag = '/html/body/div[2]/div/div[3]/button[1]'
        # 列表-第一个话题-删除-关闭按钮
        self._list_first_topic_delete_close_button_tag = '/html/body/div[2]/div/div[1]/button'
        # 添加按钮
        self._add_topic_button_tag = '//*[@id="tableSearch"]/form/div[2]/div/div/button'
        # 添加话题-话题标题输入框
        self._add_topic_title_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[1]/div[1]/div/div/div/input'
        # 添加话题-话题标题错误提示
        self._add_topic_title_error_tip_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[1]/div[1]/div/div/div[2]'
        # 添加话题-话题频道下拉框
        self._add_topic_channel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[1]/div[2]/div/div/div'
        # 添加话题-话题频道-第一个频道
        self._add_topic_channel_first_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 添加话题-话题频道-第一个频道文本
        self._add_topic_channel_first_text_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]/span'
        # 添加话题-话题频道-第二个频道
        self._add_topic_channel_second_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]'
        # 添加话题-话题频道-第二个频道文本
        self._add_topic_channel_second_text_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]/span'
        # 添加话题-话题内容输入框
        self._add_topic_content_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[2]/div/div[1]/textarea'
        # 添加话题-话题内容错误提示
        self._add_topic_content_error_tip_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[2]/div/div[2]'
        # 添加话题-话题标签-第一个标签
        self._add_topic_first_label_first_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[3]/div/div/label[1]'
        # 添加话题-话题标签-第一个标签文本
        self._add_topic_first_label_first_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[3]/div/div/label[1]/span[2]'
        # 添加话题-话题标签-第二个标签
        self._add_topic_first_label_second_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[3]/div/div/label[2]'
        # 添加话题-话题标签-第二个标签文本
        self._add_topic_first_label_second_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[3]/div/div/label[2]/span[2]'
        # 添加话题-推荐标签-第一个标签
        self._add_topic_second_label_first_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[4]/div/div/label[1]'
        # 添加话题-推荐标签-第一个标签文本
        self._add_topic_second_label_first_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[4]/div/div/label[1]/span[2]'
        # 添加话题-推荐标签-第二个标签
        self._add_topic_second_label_second_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[4]/div/div/label[2]'
        # 添加话题-推荐标签-第二个标签文本
        self._add_topic_second_label_second_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[4]/div/div/label[1]/span[2]'
        # 添加话题-封面图片上传输入框
        self._add_topic_cover_image_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[5]/div/div/div/div/input'
        # 添加话题-封面图片-上传后图片
        self._add_topic_cover_image_success_image_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[5]/div/div/div/div/div[1]/img'
        # 添加话题-添加问答按钮
        self._add_topic_qa_add_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[6]/div/button'
        # 添加话题-添加问答-问答ID
        self._add_topic_qa_add_id_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 添加话题-添加问答-问答标题
        self._add_topic_qa_add_title_input_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 添加话题-添加问答-问答状态下拉框
        self._add_topic_qa_add_state_button_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div/div'
        # 添加话题-添加问答-问答状态-全部
        self._add_topic_qa_add_state_all_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 添加话题-添加问答-问答状态-非悬赏
        self._add_topic_qa_add_state_not_bounty_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]'
        # 添加话题-添加问答-问答状态-悬赏中
        self._add_topic_qa_add_state_paying_bounty_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[3]'
        # 添加话题-添加问答-问答状态-悬赏成功
        self._add_topic_qa_add_state_bounty_done_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[4]'
        # 添加话题-添加问答-问答状态-悬赏结束
        self._add_topic_qa_add_state_bounty_end_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[5]'
        # 添加话题-添加问答-问题内容输入框
        self._add_topic_qa_add_content_input_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div/input'
        # 添加话题-添加问答-创建人昵称输入框
        self._add_topic_qa_add_created_user_nick_input_tag = '//*[@id="tableSearch"]/form/div/div[5]/div/div/input'
        # 添加话题-添加问答-创建人姓名输入框
        self._add_topic_qa_add_created_user_name_input_tag = '//*[@id="tableSearch"]/form/div/div[6]/div/div/input'
        # 添加话题-添加问答-一级类目标签下拉框
        self._add_topic_qa_add_first_label_button_tag = '//*[@id="tableSearch"]/form/div/div[8]/div/div/div[1]'
        # 添加话题-添加问答-一级类目标签-全部
        self._add_topic_qa_add_first_label_all_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 添加话题-添加问答-一级类目标签-第二个标签
        self._add_topic_qa_add_first_label_second_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]'
        # 添加话题-添加回答-二级类目标签下拉框
        self._add_topic_qa_add_second_label_button_tag = '//*[@id="tableSearch"]/form/div/div[9]/div/div/div[1]'
        # 添加话题-添加问答-二级类目标签-全部
        self._add_topic_qa_add_second_label_all_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 添加话题-添加问答-二级类目标签-第二个标签
        self._add_topic_qa_add_second_label_second_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 添加话题-添加问答-内容主题下拉框
        self._add_topic_qa_add_sub_content_button_tag = '//*[@id="tableSearch"]/form/div/div[10]/div/div/div'
        # 添加话题-添加问答-内容主题-全部
        self._add_topic_qa_add_sub_content_all_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 添加话题-添加问答-内容主题-第二个标签
        self._add_topic_qa_add_sub_content_second_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]'
        # 添加话题-添加问答-最佳答案下拉框
        self._add_topic_qa_add_best_answer_button_tag = '//*[@id="tableSearch"]/form/div/div[11]/div/div/div[1]'
        # 添加话题-添加问答-最佳答案-全部
        self._add_topic_qa_add_best_answer_all_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 添加话题-添加问答-最佳答案-是
        self._add_topic_qa_add__best_answer_yes_button_tag = '/html/body/div[lsat()]/div[1]/div[1]/ul/li[2]'
        # 添加话题-添加问答-最佳答案-否
        self._add_topic_qa_add_best_answer_no_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[3]'
        # 添加话题-添加问答-查询按钮
        self._add_topic_qa_add_query_button_tag = '//*[@id="tableSearch"]/form/div/div[12]/div/button'
        # 添加话题-添加问答-清除按钮
        self._add_topic_qa_add_clear_button_tag = '//*[@id="tableSearch"]/form/div/div[13]/div/button'
        # 添加话题-添加问答-问答列表-第一个问答勾选框
        self._add_topic_qa_add_qa_list_first_selection_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label'
        # 添加话题-添加问答-问答列表-第一个问答ID按钮
        self._add_topic_qa_add_qa_list_first_qa_id_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a'
        # 添加话题-添加问答-问答列表-第一个问答ID文本
        self._add_topic_qa_add_qa_list_first_qa_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a/span'
        # 添加话题-添加问答-确定按钮
        self._add_topic_qa_add_confirm_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div/div/div/div[3]/span/button[2]'
        # 添加话题-添加问答-取消按钮
        self._add_topic_qa_add_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div/div/div/div[3]/span/button[1]'
        # 添加话题-添加问答-关闭按钮
        self._add_topic_qa_add_close_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div/div/div/div[1]/button/i'
        # 添加话题-问答列表第一个问答ID
        self._add_topic_qa_list_first_qa_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[6]/div/div/div/div[3]/table/tbody/tr[1]/td[1]/div'
        # 添加话题-第一个问答删除按钮
        self._add_topic_qa_list_first_qa_delete_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[6]/div/div/div/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/a'
        # 添加话题-提交按钮
        self._add_topic_commit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[2]/button'
        # 话题编辑-话题ID
        self._update_topic_id_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[1]/div[1]/div/div/div/input'
        # 话题编辑-创建时间
        self._update_create_time_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[1]/div[2]/div/div/div/input'
        # 话题编辑-创建人
        self._update_create_user_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[1]/div[3]/div/div/div/input'
        # 话题编辑-话题标题输入框
        self._update_topic_title_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[2]/div[1]/div/div/div/input'
        # 话题编辑-话题频道下拉框
        self._update_topic_channel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[2]/div[2]/div/div/div/div[1]'
        # 话题编辑-话题频道-第一个频道
        self._update_topic_channel_first_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 话题编辑-话题频道-第一个频道文本
        self._update_topic_channel_first_text_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]/span'
        # 话题编辑-话题频道-第二个频道
        self._update_topic_channel_second_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]'
        # 话题编辑-话题频道-第二个频道文本
        self._update_topic_channel_second_text_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]/span'
        # 话题编辑-话题内容输入框
        self._update_topic_content_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[3]/div/div/textarea'
        # 话题编辑-话题标签-第一个标签
        self._update_topic_first_label_first_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[4]/div/div/label[1]'
        # 话题编辑-话题标签-第一个标签文本
        self._update_topic_first_label_first_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[4]/div/div/label[1]/span[2]'
        # 话题编辑-话题标签-第二个标签
        self._update_topic_first_label_second_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[4]/div/div/label[2]'
        # 话题编辑-话题标签-第二个标签文本
        self._update_topic_first_label_second_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[4]/div/div/label[2]/span[2]'
        # 话题编辑-推荐标签-第一个标签
        self._update_topic_second_label_first_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[5]/div/div/label[1]'
        # 话题编辑-推荐标签-第一个标签文本
        self._update_topic_second_label_first_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[5]/div/div/label[1]/span[2]'
        # 话题编辑-推荐标签-第二个标签
        self._update_topic_second_label_second_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[5]/div/div/label[2]'
        # 话题编辑-推荐标签-第二个标签文本
        self._update_topic_second_label_second_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[5]/div/div/label[2]/span[2]'
        # 话题编辑-封面图片上传输入框
        self._update_topic_cover_image_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[6]/div/div/div/div/input'
        # 话题编辑-封面图片-图片
        self._update_topic_cover_image_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[6]/div/div/div/div/div[1]/img'
        # 话题编辑-列表-添加问答按钮
        self._update_topic_qa_add_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[7]/div/button'
        # 话题编辑-添加问答-问答ID
        self._update_topic_qa_add_qa_id_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 话题编辑-添加问答-问答标题
        self._update_topic_qa_add_qa_title_input_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 话题编辑-添加问答-问答状态下拉框
        self._update_topic_qa_add_qa_state_button_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div/div[1]'
        # 话题编辑-添加问答-问答状态-全部
        self._update_topic_qa_add_qa_state_all_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 话题编辑-添加问答-问答状态-非悬赏
        self._update_topic_qa_add_qa_state_not_bounty_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]'
        # 话题编辑-添加问答-问答状态-悬赏中
        self._update_topic_qa_add_qa_state_in_bounty_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[3]'
        # 话题编辑-添加问答-问答状态-悬赏成功
        self._update_topic_qa_add_qa_state_bounty_success_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[4]'
        # 话题编辑-添加问答-问答状态-悬赏结束
        self._update_topic_qa_add_qa_state_bounty_end_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[5]'
        # 话题编辑-添加问答-问题内容输入框
        self._update_topic_qa_add_qa_content_input_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div/input'
        # 话题编辑-添加问答-创建人昵称输入框
        self._update_topic_qa_add_create_user_nick_input_tag = '//*[@id="tableSearch"]/form/div/div[5]/div/div/input'
        # 话题编辑-添加问答-创建人姓名输入框
        self._update_topic_qa_add_create_user_name_input_tag = '//*[@id="tableSearch"]/form/div/div[6]/div/div/input'
        # 话题编辑-添加问答-一级类目标签下拉框
        self._update_topic_qa_add_first_label_button_tag = '//*[@id="tableSearch"]/form/div/div[8]/div/div/div'
        # 话题编辑-添加问答-一级类目标签-全部
        self._update_topic_qa_add_first_label_all_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 话题编辑-添加问答-一级类目标签-第二个标签
        self._update_topic_qa_add_first_label_second_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]'
        # 话题编辑-添加问答-二级类目标签下拉框
        self._update_topic_qa_add_second_label_button_tag = '//*[@id="tableSearch"]/form/div/div[9]/div/div/div'
        # 话题编辑-添加问答-二级类目标签-全部
        self._update_topic_qa_add_second_label_all_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 话题编辑-添加问答-二级类目标签-第二个标签
        self._update_topic_qa_add_second_label_second_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]'
        # 话题编辑-添加问答-内容主题下拉框
        self._update_topic_qa_add_sub_content_button_tag = '//*[@id="tableSearch"]/form/div/div[10]/div/div/div'
        # 话题编辑-添加问答-内容主题-全部
        self._update_topic_qa_add_sub_content_all_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 话题编辑-添加问答-内容主题-第二个
        self._update_topic_qa_add_sub_content_second_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]'
        # 话题编辑-添加问答-最佳答案下拉框
        self._update_topic_qa_add_best_answer_button_tag = '//*[@id="tableSearch"]/form/div/div[11]/div/div/div[1]'
        # 话题编辑-添加问答-最佳答案-全部
        self._update_topic_qa_add_best_answer_all_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[1]'
        # 话题编辑-添加问答-最佳答案-是
        self._update_topic_qa_add_best_answer_yes_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[2]'
        # 话题编辑-添加问答-最佳答案-否
        self._update_topic_qa_add_best_answer_no_button_tag = '/html/body/div[last()]/div[1]/div[1]/ul/li[3]'
        # 话题编辑-添加答案-查询按钮
        self._update_topic_qa_add_query_button_tag = '//*[@id="tableSearch"]/form/div/div[12]/div/button'
        # 话题编辑-添加答案-清除按钮
        self._update_topic_qa_add_clear_button_tag = '//*[@id="tableSearch"]/form/div/div[13]/div/button'
        # 话题编辑-添加答案-第一个问答勾选框
        self._update_topic_qa_add_qa_list_first_select_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span'
        # 话题编辑-添加答案-问答列表-第一个问答ID按钮
        self._update_topic_qa_add_qa_list_first_qa_id_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a'
        # 话题编辑-添加问答-问答列表-第一个问答ID文本
        self._update_topic_qa_add_qa_list_first_qa_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a/span'
        # 话题编辑-添加答案-确定按钮
        self._update_topic_qa_add_confirm_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div/div/div/div[3]/span/button[2]'
        # 话题编辑-添加答案-取消按钮
        self._update_topic_qa_add_confirm_cancel_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div/div/div/div[3]/span/button[1]'
        # 话题编辑-添加答案-关闭按钮
        self._update_topic_qa_add_close_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div/div/div/div[1]/button'
        # 话题编辑-问答列表-第一个问答-问答ID
        self._update_topic_qa_list_first_qa_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[7]/div/div/div/div[3]/table/tbody/tr[1]/td[1]/div'
        # 话题编辑-问答列表-第一个问答-删除按钮
        self._update_topic_qa_list_first_delete_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[1]/div/div[7]/div/div/div/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/a'
        # 话题编辑-提交按钮
        self._update_topic_commit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/form/div[2]/button'
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
    def search_topic_id_input(self):
        """
        属性: 搜索-话题ID
        :return: 搜索-话题ID
        """
        element = None
        try:
            element = self.project.get_element(self._search_topic_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_topic_title_input(self):
        """
        属性: 搜索-话题标题
        :return: 搜索-话题标题
        """
        element = None
        try:
            element = self.project.get_element(self._search_topic_title_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_publish_time_start_date_input(self):
        """
        属性: 搜索-发布时间-开始日期输入框
        :return: 搜索-发布时间-开始日期输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_publish_time_start_date_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_publish_time_end_date_input(self):
        """
        属性: 搜素-发布时间-结束日期输入框
        :return: 搜素-发布时间-结束日期输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_publish_time_end_date_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_topic_channel_button(self):
        """
        属性: 搜索-话题频道下拉框
        :return: 搜索-话题频道下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._search_topic_channel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_topic_first_label_button(self):
        """
        属性: 搜索-一级类目标签下拉框
        :return: 搜索-一级类目标签下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._search_topic_first_label_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_topic_second_label_button(self):
        """
        属性: 搜索-二级类目标签下拉框
        :return: 搜索-二级类目标签下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._search_topic_second_label_button_tag)
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
    def list_first_topic_id_button(self):
        """
        属性: 列表-第一个话题-话题ID按钮
        :return: 列表-第一个话题-话题ID按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_topic_id_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_topic_id_text(self):
        """
        属性: 列表-第一个话题-话题ID文本
        :return: 列表-第一个话题-话题ID文本
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_topic_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_topic_title_text(self):
        """
        属性: 列表-第一个话题-标题
        :return: 列表-第一个话题-标题
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_topic_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_topic_content_text(self):
        """
        属性: 列表-第一个话题-内容
        :return: 列表-第一个话题-内容
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_topic_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_topic_channel_text(self):
        """
        属性: 列表-第一个话题-频道
        :return: 列表-第一个话题-频道
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_topic_channel_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_topic_first_label_text(self):
        """
        属性: 列表-第一个话题-一级类目标签
        :return: 列表-第一个话题-一级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_topic_first_label_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_topic_second_label_text(self):
        """
        属性: 列表-第一个话题-二级类目标签
        :return: 列表-第一个话题-二级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_topic_second_label_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_topic_create_user_text(self):
        """
        属性: 列表-第一个话题-创建人
        :return: 列表-第一个话题-创建人
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_topic_create_user_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_topic_create_time_text(self):
        """
        属性: 列表-第一个话题-创建时间
        :return: 列表-第一个话题-创建时间
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_topic_create_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_topic_update_button(self):
        """
        属性: 列表-第一个话题-编辑按钮
        :return: 列表-第一个话题-编辑按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_topic_update_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_topic_delete_button(self):
        """
        属性: 列表-第一个话题-删除按钮
        :return: 列表-第一个话题-删除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_topic_delete_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_topic_delete_confirm_button(self):
        """
        属性: 列表-第一个话题-删除-确认按钮
        :return: 列表-第一个话题-删除-确认按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_topic_delete_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_topic_delete_cancel_button(self):
        """
        属性: 列表-第一个话题-删除-取消按钮
        :return: 列表-第一个话题-删除-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_topic_delete_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_topic_delete_close_button(self):
        """
        属性: 列表-第一个话题-删除-关闭按钮
        :return: 列表-第一个话题-删除-关闭按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_topic_delete_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_button(self):
        """
        属性: 添加按钮
        :return: 添加按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_title_input(self):
        """
        属性: 添加话题-话题标题输入框
        :return: 添加话题-话题标题输入框
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_title_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_title_error_tip(self):
        """
        属性: 添加话题-话题标题错误提示
        :return: 添加话题-话题标题错误提示
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_title_error_tip_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_channel_button(self):
        """
        属性: 添加话题-话题频道下拉框
        :return: 添加话题-话题频道下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_channel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_channel_first_button(self):
        """
        属性: 添加话题-话题频道-第一个频道
        :return: 添加话题-话题频道-第一个频道
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_channel_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_channel_first_text(self):
        """
        属性: 添加话题-话题频道-第一个频道文本
        :return: 添加话题-话题频道-第一个频道文本
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_channel_first_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_channel_second_button(self):
        """
        属性: 添加话题-话题频道-第二个频道
        :return: 添加话题-话题频道-第二个频道
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_channel_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_channel_second_text(self):
        """
        属性: 添加话题-话题频道-第二个频道文本
        :return: 添加话题-话题频道-第二个频道文本
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_channel_second_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_content_input(self):
        """
        属性: 添加话题-话题内容输入框
        :return: 添加话题-话题内容输入框
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_content_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_content_error_tip(self):
        """
        属性: 添加话题-话题内容错误提示
        :return: 添加话题-话题内容错误提示
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_content_error_tip_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_first_label_first_button(self):
        """
        属性: 添加话题-话题标签-第一个标签
        :return: 添加话题-话题标签-第一个标签
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_first_label_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_first_label_first_text(self):
        """
        属性: 添加话题-话题标签-第一个标签文本
        :return: 添加话题-话题标签-第一个标签文本
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_first_label_first_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_first_label_second_button(self):
        """
        属性: 添加话题-话题标签-第二个标签
        :return: 添加话题-话题标签-第二个标签
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_first_label_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_first_label_second_text(self):
        """
        属性: 添加话题-话题标签-第二个标签文本
        :return: 添加话题-话题标签-第二个标签文本
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_first_label_second_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_second_label_first_button(self):
        """
        属性: 添加话题-推荐标签-第一个标签
        :return: 添加话题-推荐标签-第一个标签
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_second_label_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_second_label_first_text(self):
        """
        属性: 添加话题-推荐标签-第一个标签文本
        :return: 添加话题-推荐标签-第一个标签文本
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_second_label_first_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_second_label_second_button(self):
        """
        属性: 添加话题-推荐标签-第二个标签
        :return: 添加话题-推荐标签-第二个标签
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_second_label_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_second_label_second_text(self):
        """
        属性: 添加话题-推荐标签-第二个标签文本
        :return: 添加话题-推荐标签-第二个标签文本
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_second_label_second_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_cover_image_input(self):
        """
        属性: 添加话题-封面图片上传输入框
        :return: 添加话题-封面图片上传输入框
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_cover_image_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_cover_image_success_image(self):
        """
        属性: 添加话题-封面图片-上传后图片
        :return: 添加话题-封面图片-上传后图片
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_cover_image_success_image_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_button(self):
        """
        属性: 添加话题-添加问答按钮
        :return: 添加话题-添加问答按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_id_input(self):
        """
        属性: 添加话题-添加问答-问答ID
        :return: 添加话题-添加问答-问答ID
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_title_input(self):
        """
        属性: 添加话题-添加问答-问答标题
        :return: 添加话题-添加问答-问答标题
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_title_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_state_button(self):
        """
        属性: 添加话题-添加问答-问答状态下拉框
        :return: 添加话题-添加问答-问答状态下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_state_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_state_all_button(self):
        """
        属性: 添加话题-添加问答-问答状态-全部
        :return: 添加话题-添加问答-问答状态-全部
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_state_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_state_not_bounty_button(self):
        """
        属性: 添加话题-添加问答-问答状态-非悬赏
        :return: 添加话题-添加问答-问答状态-非悬赏
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_state_not_bounty_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_state_paying_bounty_button(self):
        """
        属性: 添加话题-添加问答-问答状态-悬赏中
        :return: 添加话题-添加问答-问答状态-悬赏中
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_state_paying_bounty_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_state_bounty_done_button(self):
        """
        属性: 添加话题-添加问答-问答状态-悬赏成功
        :return: 添加话题-添加问答-问答状态-悬赏成功
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_state_bounty_done_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_state_bounty_end_button(self):
        """
        属性: 添加话题-添加问答-问答状态-悬赏结束
        :return: 添加话题-添加问答-问答状态-悬赏结束
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_state_bounty_end_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_content_input(self):
        """
        属性: 添加话题-添加问答-问题内容输入框
        :return: 添加话题-添加问答-问题内容输入框
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_content_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_created_user_nick_input(self):
        """
        属性: 添加话题-添加问答-创建人昵称输入框
        :return: 添加话题-添加问答-创建人昵称输入框
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_created_user_nick_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_created_user_name_input(self):
        """
        属性: 添加话题-添加问答-创建人姓名输入框
        :return: 添加话题-添加问答-创建人姓名输入框
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_created_user_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_first_label_button(self):
        """
        属性: 添加话题-添加问答-一级类目标签下拉框
        :return: 添加话题-添加问答-一级类目标签下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_first_label_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_first_label_all_button(self):
        """
        属性: 添加话题-添加问答-一级类目标签-全部
        :return: 添加话题-添加问答-一级类目标签-全部
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_first_label_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_first_label_second_button(self):
        """
        属性: 添加话题-添加问答-一级类目标签-第二个标签
        :return: 添加话题-添加问答-一级类目标签-第二个标签
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_first_label_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_second_label_button(self):
        """
        属性: 添加话题-添加回答-二级类目标签下拉框
        :return: 添加话题-添加回答-二级类目标签下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_second_label_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_second_label_all_button(self):
        """
        属性: 添加话题-添加问答-二级类目标签-全部
        :return: 添加话题-添加问答-二级类目标签-全部
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_second_label_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_second_label_second_button(self):
        """
        属性: 添加话题-添加问答-二级类目标签-第二个标签
        :return: 添加话题-添加问答-二级类目标签-第二个标签
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_second_label_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_sub_content_button(self):
        """
        属性: 添加话题-添加问答-内容主题下拉框
        :return: 添加话题-添加问答-内容主题下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_sub_content_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_sub_content_all_button(self):
        """
        属性: 添加话题-添加问答-内容主题-全部
        :return: 添加话题-添加问答-内容主题-全部
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_sub_content_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_sub_content_second_button(self):
        """
        属性: 添加话题-添加问答-内容主题-第二个标签
        :return: 添加话题-添加问答-内容主题-第二个标签
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_sub_content_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_best_answer_button(self):
        """
        属性: 添加话题-添加问答-最佳答案下拉框
        :return: 添加话题-添加问答-最佳答案下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_best_answer_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_best_answer_all_button(self):
        """
        属性: 添加话题-添加问答-最佳答案-全部
        :return: 添加话题-添加问答-最佳答案-全部
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_best_answer_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add__best_answer_yes_button(self):
        """
        属性: 添加话题-添加问答-最佳答案-是
        :return: 添加话题-添加问答-最佳答案-是
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add__best_answer_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_best_answer_no_button(self):
        """
        属性: 添加话题-添加问答-最佳答案-否
        :return: 添加话题-添加问答-最佳答案-否
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_best_answer_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_query_button(self):
        """
        属性: 添加话题-添加问答-查询按钮
        :return: 添加话题-添加问答-查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_query_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_clear_button(self):
        """
        属性: 添加话题-添加问答-清除按钮
        :return: 添加话题-添加问答-清除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_qa_list_first_selection_button(self):
        """
        属性: 添加话题-添加问答-问答列表-第一个问答勾选框
        :return: 添加话题-添加问答-问答列表-第一个问答勾选框
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_qa_list_first_selection_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_qa_list_first_qa_id_button(self):
        """
        属性: 添加话题-添加问答-问答列表-第一个问答ID按钮
        :return: 添加话题-添加问答-问答列表-第一个问答ID按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_qa_list_first_qa_id_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_qa_list_first_qa_id_text(self):
        """
        属性: 添加话题-添加问答-问答列表-第一个问答ID文本
        :return: 添加话题-添加问答-问答列表-第一个问答ID文本
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_qa_list_first_qa_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_confirm_button(self):
        """
        属性: 添加话题-添加问答-确定按钮
        :return: 添加话题-添加问答-确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_cancel_button(self):
        """
        属性: 添加话题-添加问答-取消按钮
        :return: 添加话题-添加问答-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_add_close_button(self):
        """
        属性: 添加话题-添加问答-关闭按钮
        :return: 添加话题-添加问答-关闭按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_add_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_list_first_qa_id_text(self):
        """
        属性: 添加话题-问答列表第一个问答ID
        :return: 添加话题-问答列表第一个问答ID
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_list_first_qa_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_qa_list_first_qa_delete_button(self):
        """
        属性: 添加话题-第一个问答删除按钮
        :return: 添加话题-第一个问答删除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_qa_list_first_qa_delete_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_topic_commit_button(self):
        """
        属性: 添加话题-提交按钮
        :return: 添加话题-提交按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_topic_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_id(self):
        """
        属性: 话题编辑-话题ID
        :return: 话题编辑-话题ID
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_id_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_create_time(self):
        """
        属性: 话题编辑-创建时间
        :return: 话题编辑-创建时间
        """
        element = None
        try:
            element = self.project.get_element(self._update_create_time_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_create_user(self):
        """
        属性: 话题编辑-创建人
        :return: 话题编辑-创建人
        """
        element = None
        try:
            element = self.project.get_element(self._update_create_user_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_title_input(self):
        """
        属性: 话题编辑-话题标题输入框
        :return: 话题编辑-话题标题输入框
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_title_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_channel_button(self):
        """
        属性: 话题编辑-话题频道下拉框
        :return: 话题编辑-话题频道下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_channel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_channel_first_button(self):
        """
        属性: 话题编辑-话题频道-第一个频道
        :return: 话题编辑-话题频道-第一个频道
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_channel_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_channel_first_text(self):
        """
        属性: 话题编辑-话题频道-第一个频道文本
        :return: 话题编辑-话题频道-第一个频道文本
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_channel_first_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_channel_second_button(self):
        """
        属性: 话题编辑-话题频道-第二个频道
        :return: 话题编辑-话题频道-第二个频道
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_channel_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_channel_second_text(self):
        """
        属性: 话题编辑-话题频道-第二个频道文本
        :return: 话题编辑-话题频道-第二个频道文本
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_channel_second_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_content_input(self):
        """
        属性: 话题编辑-话题内容输入框
        :return: 话题编辑-话题内容输入框
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_content_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_first_label_first_button(self):
        """
        属性: 话题编辑-话题标签-第一个标签
        :return: 话题编辑-话题标签-第一个标签
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_first_label_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_first_label_first_text(self):
        """
        属性: 话题编辑-话题标签-第一个标签文本
        :return: 话题编辑-话题标签-第一个标签文本
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_first_label_first_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_first_label_second_button(self):
        """
        属性: 话题编辑-话题标签-第二个标签
        :return: 话题编辑-话题标签-第二个标签
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_first_label_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_first_label_second_text(self):
        """
        属性: 话题编辑-话题标签-第二个标签文本
        :return: 话题编辑-话题标签-第二个标签文本
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_first_label_second_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_second_label_first_button(self):
        """
        属性: 话题编辑-推荐标签-第一个标签
        :return: 话题编辑-推荐标签-第一个标签
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_second_label_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_second_label_first_text(self):
        """
        属性: 话题编辑-推荐标签-第一个标签文本
        :return: 话题编辑-推荐标签-第一个标签文本
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_second_label_first_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_second_label_second_button(self):
        """
        属性: 话题编辑-推荐标签-第二个标签
        :return: 话题编辑-推荐标签-第二个标签
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_second_label_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_second_label_second_text(self):
        """
        属性: 话题编辑-推荐标签-第二个标签文本
        :return: 话题编辑-推荐标签-第二个标签文本
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_second_label_second_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_cover_image_input(self):
        """
        属性: 话题编辑-封面图片上传输入框
        :return: 话题编辑-封面图片上传输入框
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_cover_image_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_cover_image_button(self):
        """
        属性: 话题编辑-封面图片-图片
        :return: 话题编辑-封面图片-图片
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_cover_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_button(self):
        """
        属性: 话题编辑-列表-添加问答按钮
        :return: 话题编辑-列表-添加问答按钮
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_qa_id_input(self):
        """
        属性: 话题编辑-添加问答-问答ID
        :return: 话题编辑-添加问答-问答ID
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_qa_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_qa_title_input(self):
        """
        属性: 话题编辑-添加问答-问答标题
        :return: 话题编辑-添加问答-问答标题
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_qa_title_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_qa_state_button(self):
        """
        属性: 话题编辑-添加问答-问答状态下拉框
        :return: 话题编辑-添加问答-问答状态下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_qa_state_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_qa_state_all_button(self):
        """
        属性: 话题编辑-添加问答-问答状态-全部
        :return: 话题编辑-添加问答-问答状态-全部
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_qa_state_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_qa_state_not_bounty_button(self):
        """
        属性: 话题编辑-添加问答-问答状态-非悬赏
        :return: 话题编辑-添加问答-问答状态-非悬赏
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_qa_state_not_bounty_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_qa_state_in_bounty_button(self):
        """
        属性: 话题编辑-添加问答-问答状态-悬赏中
        :return: 话题编辑-添加问答-问答状态-悬赏中
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_qa_state_in_bounty_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_qa_state_bounty_success_button(self):
        """
        属性: 话题编辑-添加问答-问答状态-悬赏成功
        :return: 话题编辑-添加问答-问答状态-悬赏成功
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_qa_state_bounty_success_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_qa_state_bounty_end_button(self):
        """
        属性: 话题编辑-添加问答-问答状态-悬赏结束
        :return: 话题编辑-添加问答-问答状态-悬赏结束
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_qa_state_bounty_end_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_qa_content_input(self):
        """
        属性: 话题编辑-添加问答-问题内容输入框
        :return: 话题编辑-添加问答-问题内容输入框
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_qa_content_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_create_user_nick_input(self):
        """
        属性: 话题编辑-添加问答-创建人昵称输入框
        :return: 话题编辑-添加问答-创建人昵称输入框
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_create_user_nick_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_create_user_name_input(self):
        """
        属性: 话题编辑-添加问答-创建人姓名输入框
        :return: 话题编辑-添加问答-创建人姓名输入框
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_create_user_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_first_label_button(self):
        """
        属性: 话题编辑-添加问答-一级类目标签下拉框
        :return: 话题编辑-添加问答-一级类目标签下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_first_label_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_first_label_all_button(self):
        """
        属性: 话题编辑-添加问答-一级类目标签-全部
        :return: 话题编辑-添加问答-一级类目标签-全部
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_first_label_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_first_label_second_button(self):
        """
        属性: 话题编辑-添加问答-一级类目标签-第二个标签
        :return: 话题编辑-添加问答-一级类目标签-第二个标签
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_first_label_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_second_label_button(self):
        """
        属性: 话题编辑-添加问答-二级类目标签下拉框
        :return: 话题编辑-添加问答-二级类目标签下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_second_label_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_second_label_all_button(self):
        """
        属性: 话题编辑-添加问答-二级类目标签-全部
        :return: 话题编辑-添加问答-二级类目标签-全部
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_second_label_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_second_label_second_button(self):
        """
        属性: 话题编辑-添加问答-二级类目标签-第二个标签
        :return: 话题编辑-添加问答-二级类目标签-第二个标签
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_second_label_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_sub_content_button(self):
        """
        属性: 话题编辑-添加问答-内容主题下拉框
        :return: 话题编辑-添加问答-内容主题下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_sub_content_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_sub_content_all_button(self):
        """
        属性: 话题编辑-添加问答-内容主题-全部
        :return: 话题编辑-添加问答-内容主题-全部
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_sub_content_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_sub_content_second_button(self):
        """
        属性: 话题编辑-添加问答-内容主题-第二个
        :return: 话题编辑-添加问答-内容主题-第二个
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_sub_content_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_best_answer_button(self):
        """
        属性: 话题编辑-添加问答-最佳答案下拉框
        :return: 话题编辑-添加问答-最佳答案下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_best_answer_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_best_answer_all_button(self):
        """
        属性: 话题编辑-添加问答-最佳答案-全部
        :return: 话题编辑-添加问答-最佳答案-全部
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_best_answer_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_best_answer_yes_button(self):
        """
        属性: 话题编辑-添加问答-最佳答案-是
        :return: 话题编辑-添加问答-最佳答案-是
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_best_answer_yes_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_best_answer_no_button(self):
        """
        属性: 话题编辑-添加问答-最佳答案-否
        :return: 话题编辑-添加问答-最佳答案-否
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_best_answer_no_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_query_button(self):
        """
        属性: 话题编辑-添加答案-查询按钮
        :return: 话题编辑-添加答案-查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_query_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_clear_button(self):
        """
        属性: 话题编辑-添加答案-清除按钮
        :return: 话题编辑-添加答案-清除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_qa_list_first_select_button(self):
        """
        属性: 话题编辑-添加答案-第一个问答勾选框
        :return: 话题编辑-添加答案-第一个问答勾选框
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_qa_list_first_select_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_qa_list_first_qa_id_button(self):
        """
        属性: 话题编辑-添加答案-问答列表-第一个问答ID按钮
        :return: 话题编辑-添加答案-问答列表-第一个问答ID按钮
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_qa_list_first_qa_id_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_qa_list_first_qa_id_text(self):
        """
        属性: 话题编辑-添加问答-问答列表-第一个问答ID文本
        :return: 话题编辑-添加问答-问答列表-第一个问答ID文本
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_qa_list_first_qa_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_confirm_button(self):
        """
        属性: 话题编辑-添加答案-确定按钮
        :return: 话题编辑-添加答案-确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_confirm_cancel(self):
        """
        属性: 话题编辑-添加答案-取消按钮
        :return: 话题编辑-添加答案-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_confirm_cancel_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_add_close_button(self):
        """
        属性: 话题编辑-添加答案-关闭按钮
        :return: 话题编辑-添加答案-关闭按钮
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_add_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_list_first_qa_id_text(self):
        """
        属性: 话题编辑-问答列表-第一个问答-问答ID
        :return: 话题编辑-问答列表-第一个问答-问答ID
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_list_first_qa_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_qa_list_first_delete_button(self):
        """
        属性: 话题编辑-问答列表-第一个问答-删除按钮
        :return: 话题编辑-问答列表-第一个问答-删除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_qa_list_first_delete_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def update_topic_commit_button(self):
        """
        属性: 话题编辑-提交按钮
        :return: 话题编辑-提交按钮
        """
        element = None
        try:
            element = self.project.get_element(self._update_topic_commit_button_tag)
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

    def set_search_topic_id_input_action(self, search_topic_id_input):
        """
        动作：设置搜索-话题ID
        :param search_topic_id_input: 搜索-话题ID
        :return: 设置'搜索-话题ID'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_topic_id_input, search_topic_id_input)
        return self.project.get_current_page_source()

    def set_search_topic_title_input_action(self, search_topic_title_input):
        """
        动作：设置搜索-话题标题
        :param search_topic_title_input: 搜索-话题标题
        :return: 设置'搜索-话题标题'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_topic_title_input, search_topic_title_input)
        return self.project.get_current_page_source()

    def set_search_publish_time_start_date_input_action(self, search_publish_time_start_date_input):
        """
        动作：设置搜索-发布时间-开始日期输入框
        :param search_publish_time_start_date_input: 搜索-发布时间-开始日期输入框
        :return: 设置'搜索-发布时间-开始日期输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_publish_time_start_date_input, search_publish_time_start_date_input)
        return self.project.get_current_page_source()

    def set_search_publish_time_end_date_input_action(self, search_publish_time_end_date_input):
        """
        动作：设置搜素-发布时间-结束日期输入框
        :param search_publish_time_end_date_input: 搜素-发布时间-结束日期输入框
        :return: 设置'搜素-发布时间-结束日期输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_publish_time_end_date_input, search_publish_time_end_date_input)
        return self.project.get_current_page_source()

    def click_search_topic_channel_button_action(self):
        """
        动作：点击搜索-话题频道下拉框
        :return: 点击'搜索-话题频道下拉框'按钮后的页面
        """
        self.project.click(self.search_topic_channel_button)
        return self.project.get_current_page_source()

    def click_search_topic_first_label_button_action(self):
        """
        动作：点击搜索-一级类目标签下拉框
        :return: 点击'搜索-一级类目标签下拉框'按钮后的页面
        """
        self.project.click(self.search_topic_first_label_button)
        return self.project.get_current_page_source()

    def click_search_topic_second_label_button_action(self):
        """
        动作：点击搜索-二级类目标签下拉框
        :return: 点击'搜索-二级类目标签下拉框'按钮后的页面
        """
        self.project.click(self.search_topic_second_label_button)
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

    def click_list_first_topic_id_button_action(self):
        """
        动作：点击列表-第一个话题-话题ID按钮
        :return: 点击'列表-第一个话题-话题ID按钮'按钮后的页面
        """
        self.project.click(self.list_first_topic_id_button)
        return self.project.get_current_page_source()

    def get_list_first_topic_id_text_action(self):
        """
        动作：获取列表-第一个话题-话题ID文本的文本
        :return: '列表-第一个话题-话题ID文本'的文本
        """
        control_content = self.project.get_element_text(self.list_first_topic_id_text)
        return control_content

    def get_list_first_topic_title_text_action(self):
        """
        动作：获取列表-第一个话题-标题的文本
        :return: '列表-第一个话题-标题'的文本
        """
        control_content = self.project.get_element_text(self.list_first_topic_title_text)
        return control_content

    def get_list_first_topic_content_text_action(self):
        """
        动作：获取列表-第一个话题-内容的文本
        :return: '列表-第一个话题-内容'的文本
        """
        control_content = self.project.get_element_text(self.list_first_topic_content_text)
        return control_content

    def get_list_first_topic_channel_text_action(self):
        """
        动作：获取列表-第一个话题-频道的文本
        :return: '列表-第一个话题-频道'的文本
        """
        control_content = self.project.get_element_text(self.list_first_topic_channel_text)
        return control_content

    def get_list_first_topic_first_label_text_action(self):
        """
        动作：获取列表-第一个话题-一级类目标签的文本
        :return: '列表-第一个话题-一级类目标签'的文本
        """
        control_content = self.project.get_element_text(self.list_first_topic_first_label_text)
        return control_content

    def get_list_first_topic_second_label_text_action(self):
        """
        动作：获取列表-第一个话题-二级类目标签的文本
        :return: '列表-第一个话题-二级类目标签'的文本
        """
        control_content = self.project.get_element_text(self.list_first_topic_second_label_text)
        return control_content

    def get_list_first_topic_create_user_text_action(self):
        """
        动作：获取列表-第一个话题-创建人的文本
        :return: '列表-第一个话题-创建人'的文本
        """
        control_content = self.project.get_element_text(self.list_first_topic_create_user_text)
        return control_content

    def get_list_first_topic_create_time_text_action(self):
        """
        动作：获取列表-第一个话题-创建时间的文本
        :return: '列表-第一个话题-创建时间'的文本
        """
        control_content = self.project.get_element_text(self.list_first_topic_create_time_text)
        return control_content

    def click_list_first_topic_update_button_action(self):
        """
        动作：点击列表-第一个话题-编辑按钮
        :return: 点击'列表-第一个话题-编辑按钮'按钮后的页面
        """
        self.project.click(self.list_first_topic_update_button)
        return self.project.get_current_page_source()

    def click_list_first_topic_delete_button_action(self):
        """
        动作：点击列表-第一个话题-删除按钮
        :return: 点击'列表-第一个话题-删除按钮'按钮后的页面
        """
        self.project.click(self.list_first_topic_delete_button)
        return self.project.get_current_page_source()

    def click_list_first_topic_delete_confirm_button_action(self):
        """
        动作：点击列表-第一个话题-删除-确认按钮
        :return: 点击'列表-第一个话题-删除-确认按钮'按钮后的页面
        """
        self.project.click(self.list_first_topic_delete_confirm_button)
        return self.project.get_current_page_source()

    def click_list_first_topic_delete_cancel_button_action(self):
        """
        动作：点击列表-第一个话题-删除-取消按钮
        :return: 点击'列表-第一个话题-删除-取消按钮'按钮后的页面
        """
        self.project.click(self.list_first_topic_delete_cancel_button)
        return self.project.get_current_page_source()

    def click_list_first_topic_delete_close_button_action(self):
        """
        动作：点击列表-第一个话题-删除-关闭按钮
        :return: 点击'列表-第一个话题-删除-关闭按钮'按钮后的页面
        """
        self.project.click(self.list_first_topic_delete_close_button)
        return self.project.get_current_page_source()

    def click_add_topic_button_action(self):
        """
        动作：点击添加按钮
        :return: 点击'添加按钮'按钮后的页面
        """
        self.project.click(self.add_topic_button)
        return self.project.get_current_page_source()

    def set_add_topic_title_input_action(self, add_topic_title_input):
        """
        动作：设置添加话题-话题标题输入框
        :param add_topic_title_input: 添加话题-话题标题输入框
        :return: 设置'添加话题-话题标题输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_topic_title_input, add_topic_title_input)
        return self.project.get_current_page_source()

    def click_add_topic_channel_button_action(self):
        """
        动作：点击添加话题-话题频道下拉框
        :return: 点击'添加话题-话题频道下拉框'按钮后的页面
        """
        self.project.click(self.add_topic_channel_button)
        return self.project.get_current_page_source()

    def click_add_topic_channel_first_button_action(self):
        """
        动作：点击添加话题-话题频道-第一个频道
        :return: 点击'添加话题-话题频道-第一个频道'按钮后的页面
        """
        self.project.click(self.add_topic_channel_first_button)
        return self.project.get_current_page_source()

    def get_add_topic_channel_first_text_action(self):
        """
        动作：获取添加话题-话题频道-第一个频道文本的文本
        :return: '添加话题-话题频道-第一个频道文本'的文本
        """
        control_content = self.project.get_element_text(self.add_topic_channel_first_text)
        return control_content

    def click_add_topic_channel_second_button_action(self):
        """
        动作：点击添加话题-话题频道-第二个频道
        :return: 点击'添加话题-话题频道-第二个频道'按钮后的页面
        """
        self.project.click(self.add_topic_channel_second_button)
        return self.project.get_current_page_source()

    def get_add_topic_channel_second_text_action(self):
        """
        动作：获取添加话题-话题频道-第二个频道文本的文本
        :return: '添加话题-话题频道-第二个频道文本'的文本
        """
        control_content = self.project.get_element_text(self.add_topic_channel_second_text)
        return control_content

    def set_add_topic_content_input_action(self, add_topic_content_input):
        """
        动作：设置添加话题-话题内容输入框
        :param add_topic_content_input: 添加话题-话题内容输入框
        :return: 设置'添加话题-话题内容输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_topic_content_input, add_topic_content_input)
        return self.project.get_current_page_source()

    def click_add_topic_first_label_first_button_action(self):
        """
        动作：点击添加话题-话题标签-第一个标签
        :return: 点击'添加话题-话题标签-第一个标签'按钮后的页面
        """
        self.project.click(self.add_topic_first_label_first_button)
        return self.project.get_current_page_source()

    def get_add_topic_first_label_first_text_action(self):
        """
        动作：获取添加话题-话题标签-第一个标签文本的文本
        :return: '添加话题-话题标签-第一个标签文本'的文本
        """
        control_content = self.project.get_element_text(self.add_topic_first_label_first_text)
        return control_content

    def click_add_topic_first_label_second_button_action(self):
        """
        动作：点击添加话题-话题标签-第二个标签
        :return: 点击'添加话题-话题标签-第二个标签'按钮后的页面
        """
        self.project.click(self.add_topic_first_label_second_button)
        return self.project.get_current_page_source()

    def get_add_topic_first_label_second_text_action(self):
        """
        动作：获取添加话题-话题标签-第二个标签文本的文本
        :return: '添加话题-话题标签-第二个标签文本'的文本
        """
        control_content = self.project.get_element_text(self.add_topic_first_label_second_text)
        return control_content

    def click_add_topic_second_label_first_button_action(self):
        """
        动作：点击添加话题-推荐标签-第一个标签
        :return: 点击'添加话题-推荐标签-第一个标签'按钮后的页面
        """
        self.project.click(self.add_topic_second_label_first_button)
        return self.project.get_current_page_source()

    def get_add_topic_second_label_first_text_action(self):
        """
        动作：获取添加话题-推荐标签-第一个标签文本的文本
        :return: '添加话题-推荐标签-第一个标签文本'的文本
        """
        control_content = self.project.get_element_text(self.add_topic_second_label_first_text)
        return control_content

    def click_add_topic_second_label_second_button_action(self):
        """
        动作：点击添加话题-推荐标签-第二个标签
        :return: 点击'添加话题-推荐标签-第二个标签'按钮后的页面
        """
        self.project.click(self.add_topic_second_label_second_button)
        return self.project.get_current_page_source()

    def get_add_topic_second_label_second_text_action(self):
        """
        动作：获取添加话题-推荐标签-第二个标签文本的文本
        :return: '添加话题-推荐标签-第二个标签文本'的文本
        """
        control_content = self.project.get_element_text(self.add_topic_second_label_second_text)
        return control_content

    def set_add_topic_cover_image_input_action(self, add_topic_cover_image_input):
        """
        动作：设置添加话题-封面图片上传输入框
        :param add_topic_cover_image_input: 添加话题-封面图片上传输入框
        :return: 设置'添加话题-封面图片上传输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_topic_cover_image_input, add_topic_cover_image_input)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_button_action(self):
        """
        动作：点击添加话题-添加问答按钮
        :return: 点击'添加话题-添加问答按钮'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_button)
        return self.project.get_current_page_source()

    def set_add_topic_qa_add_id_input_action(self, add_topic_qa_add_id_input):
        """
        动作：设置添加话题-添加问答-问答ID
        :param add_topic_qa_add_id_input: 添加话题-添加问答-问答ID
        :return: 设置'添加话题-添加问答-问答ID'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_topic_qa_add_id_input, add_topic_qa_add_id_input)
        return self.project.get_current_page_source()

    def set_add_topic_qa_add_title_input_action(self, add_topic_qa_add_title_input):
        """
        动作：设置添加话题-添加问答-问答标题
        :param add_topic_qa_add_title_input: 添加话题-添加问答-问答标题
        :return: 设置'添加话题-添加问答-问答标题'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_topic_qa_add_title_input, add_topic_qa_add_title_input)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_state_button_action(self):
        """
        动作：点击添加话题-添加问答-问答状态下拉框
        :return: 点击'添加话题-添加问答-问答状态下拉框'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_state_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_state_all_button_action(self):
        """
        动作：点击添加话题-添加问答-问答状态-全部
        :return: 点击'添加话题-添加问答-问答状态-全部'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_state_all_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_state_not_bounty_button_action(self):
        """
        动作：点击添加话题-添加问答-问答状态-非悬赏
        :return: 点击'添加话题-添加问答-问答状态-非悬赏'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_state_not_bounty_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_state_paying_bounty_button_action(self):
        """
        动作：点击添加话题-添加问答-问答状态-悬赏中
        :return: 点击'添加话题-添加问答-问答状态-悬赏中'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_state_paying_bounty_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_state_bounty_done_button_action(self):
        """
        动作：点击添加话题-添加问答-问答状态-悬赏成功
        :return: 点击'添加话题-添加问答-问答状态-悬赏成功'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_state_bounty_done_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_state_bounty_end_button_action(self):
        """
        动作：点击添加话题-添加问答-问答状态-悬赏结束
        :return: 点击'添加话题-添加问答-问答状态-悬赏结束'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_state_bounty_end_button)
        return self.project.get_current_page_source()

    def set_add_topic_qa_add_content_input_action(self, add_topic_qa_add_content_input):
        """
        动作：设置添加话题-添加问答-问题内容输入框
        :param add_topic_qa_add_content_input: 添加话题-添加问答-问题内容输入框
        :return: 设置'添加话题-添加问答-问题内容输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_topic_qa_add_content_input, add_topic_qa_add_content_input)
        return self.project.get_current_page_source()

    def set_add_topic_qa_add_created_user_nick_input_action(self, add_topic_qa_add_created_user_nick_input):
        """
        动作：设置添加话题-添加问答-创建人昵称输入框
        :param add_topic_qa_add_created_user_nick_input: 添加话题-添加问答-创建人昵称输入框
        :return: 设置'添加话题-添加问答-创建人昵称输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_topic_qa_add_created_user_nick_input, add_topic_qa_add_created_user_nick_input)
        return self.project.get_current_page_source()

    def set_add_topic_qa_add_created_user_name_input_action(self, add_topic_qa_add_created_user_name_input):
        """
        动作：设置添加话题-添加问答-创建人姓名输入框
        :param add_topic_qa_add_created_user_name_input: 添加话题-添加问答-创建人姓名输入框
        :return: 设置'添加话题-添加问答-创建人姓名输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_topic_qa_add_created_user_name_input, add_topic_qa_add_created_user_name_input)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_first_label_button_action(self):
        """
        动作：点击添加话题-添加问答-一级类目标签下拉框
        :return: 点击'添加话题-添加问答-一级类目标签下拉框'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_first_label_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_first_label_all_button_action(self):
        """
        动作：点击添加话题-添加问答-一级类目标签-全部
        :return: 点击'添加话题-添加问答-一级类目标签-全部'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_first_label_all_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_first_label_second_button_action(self):
        """
        动作：点击添加话题-添加问答-一级类目标签-第二个标签
        :return: 点击'添加话题-添加问答-一级类目标签-第二个标签'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_first_label_second_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_second_label_button_action(self):
        """
        动作：点击添加话题-添加回答-二级类目标签下拉框
        :return: 点击'添加话题-添加回答-二级类目标签下拉框'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_second_label_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_second_label_all_button_action(self):
        """
        动作：点击添加话题-添加问答-二级类目标签-全部
        :return: 点击'添加话题-添加问答-二级类目标签-全部'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_second_label_all_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_second_label_second_button_action(self):
        """
        动作：点击添加话题-添加问答-二级类目标签-第二个标签
        :return: 点击'添加话题-添加问答-二级类目标签-第二个标签'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_second_label_second_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_sub_content_button_action(self):
        """
        动作：点击添加话题-添加问答-内容主题下拉框
        :return: 点击'添加话题-添加问答-内容主题下拉框'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_sub_content_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_sub_content_all_button_action(self):
        """
        动作：点击添加话题-添加问答-内容主题-全部
        :return: 点击'添加话题-添加问答-内容主题-全部'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_sub_content_all_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_sub_content_second_button_action(self):
        """
        动作：点击添加话题-添加问答-内容主题-第二个标签
        :return: 点击'添加话题-添加问答-内容主题-第二个标签'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_sub_content_second_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_best_answer_button_action(self):
        """
        动作：点击添加话题-添加问答-最佳答案下拉框
        :return: 点击'添加话题-添加问答-最佳答案下拉框'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_best_answer_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_best_answer_all_button_action(self):
        """
        动作：点击添加话题-添加问答-最佳答案-全部
        :return: 点击'添加话题-添加问答-最佳答案-全部'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_best_answer_all_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add__best_answer_yes_button_action(self):
        """
        动作：点击添加话题-添加问答-最佳答案-是
        :return: 点击'添加话题-添加问答-最佳答案-是'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add__best_answer_yes_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_best_answer_no_button_action(self):
        """
        动作：点击添加话题-添加问答-最佳答案-否
        :return: 点击'添加话题-添加问答-最佳答案-否'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_best_answer_no_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_query_button_action(self):
        """
        动作：点击添加话题-添加问答-查询按钮
        :return: 点击'添加话题-添加问答-查询按钮'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_query_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_clear_button_action(self):
        """
        动作：点击添加话题-添加问答-清除按钮
        :return: 点击'添加话题-添加问答-清除按钮'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_clear_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_qa_list_first_selection_button_action(self):
        """
        动作：点击添加话题-添加问答-问答列表-第一个问答勾选框
        :return: 点击'添加话题-添加问答-问答列表-第一个问答勾选框'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_qa_list_first_selection_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_qa_list_first_qa_id_button_action(self):
        """
        动作：点击添加话题-添加问答-问答列表-第一个问答ID按钮
        :return: 点击'添加话题-添加问答-问答列表-第一个问答ID按钮'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_qa_list_first_qa_id_button)
        return self.project.get_current_page_source()

    def get_add_topic_qa_add_qa_list_first_qa_id_text_action(self):
        """
        动作：获取添加话题-添加问答-问答列表-第一个问答ID文本的文本
        :return: '添加话题-添加问答-问答列表-第一个问答ID文本'的文本
        """
        control_content = self.project.get_element_text(self.add_topic_qa_add_qa_list_first_qa_id_text)
        return control_content

    def click_add_topic_qa_add_confirm_button_action(self):
        """
        动作：点击添加话题-添加问答-确定按钮
        :return: 点击'添加话题-添加问答-确定按钮'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_confirm_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_cancel_button_action(self):
        """
        动作：点击添加话题-添加问答-取消按钮
        :return: 点击'添加话题-添加问答-取消按钮'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_cancel_button)
        return self.project.get_current_page_source()

    def click_add_topic_qa_add_close_button_action(self):
        """
        动作：点击添加话题-添加问答-关闭按钮
        :return: 点击'添加话题-添加问答-关闭按钮'按钮后的页面
        """
        self.project.click(self.add_topic_qa_add_close_button)
        return self.project.get_current_page_source()

    def get_add_topic_qa_list_first_qa_id_text_action(self):
        """
        动作：获取添加话题-问答列表第一个问答ID的文本
        :return: '添加话题-问答列表第一个问答ID'的文本
        """
        control_content = self.project.get_element_text(self.add_topic_qa_list_first_qa_id_text)
        return control_content

    def click_add_topic_qa_list_first_qa_delete_button_action(self):
        """
        动作：点击添加话题-第一个问答删除按钮
        :return: 点击'添加话题-第一个问答删除按钮'按钮后的页面
        """
        self.project.click(self.add_topic_qa_list_first_qa_delete_button)
        return self.project.get_current_page_source()

    def click_add_topic_commit_button_action(self):
        """
        动作：点击添加话题-提交按钮
        :return: 点击'添加话题-提交按钮'按钮后的页面
        """
        self.project.click(self.add_topic_commit_button)
        return self.project.get_current_page_source()

    def set_update_topic_title_input_action(self, update_topic_title_input):
        """
        动作：设置话题编辑-话题标题输入框
        :param update_topic_title_input: 话题编辑-话题标题输入框
        :return: 设置'话题编辑-话题标题输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.update_topic_title_input, update_topic_title_input)
        return self.project.get_current_page_source()

    def click_update_topic_channel_button_action(self):
        """
        动作：点击话题编辑-话题频道下拉框
        :return: 点击'话题编辑-话题频道下拉框'按钮后的页面
        """
        self.project.click(self.update_topic_channel_button)
        return self.project.get_current_page_source()

    def click_update_topic_channel_first_button_action(self):
        """
        动作：点击话题编辑-话题频道-第一个频道
        :return: 点击'话题编辑-话题频道-第一个频道'按钮后的页面
        """
        self.project.click(self.update_topic_channel_first_button)
        return self.project.get_current_page_source()

    def get_update_topic_channel_first_text_action(self):
        """
        动作：获取话题编辑-话题频道-第一个频道文本的文本
        :return: '话题编辑-话题频道-第一个频道文本'的文本
        """
        control_content = self.project.get_element_text(self.update_topic_channel_first_text)
        return control_content

    def click_update_topic_channel_second_button_action(self):
        """
        动作：点击话题编辑-话题频道-第二个频道
        :return: 点击'话题编辑-话题频道-第二个频道'按钮后的页面
        """
        self.project.click(self.update_topic_channel_second_button)
        return self.project.get_current_page_source()

    def get_update_topic_channel_second_text_action(self):
        """
        动作：获取话题编辑-话题频道-第二个频道文本的文本
        :return: '话题编辑-话题频道-第二个频道文本'的文本
        """
        control_content = self.project.get_element_text(self.update_topic_channel_second_text)
        return control_content

    def set_update_topic_content_input_action(self, update_topic_content_input):
        """
        动作：设置话题编辑-话题内容输入框
        :param update_topic_content_input: 话题编辑-话题内容输入框
        :return: 设置'话题编辑-话题内容输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.update_topic_content_input, update_topic_content_input)
        return self.project.get_current_page_source()

    def click_update_topic_first_label_first_button_action(self):
        """
        动作：点击话题编辑-话题标签-第一个标签
        :return: 点击'话题编辑-话题标签-第一个标签'按钮后的页面
        """
        self.project.click(self.update_topic_first_label_first_button)
        return self.project.get_current_page_source()

    def get_update_topic_first_label_first_text_action(self):
        """
        动作：获取话题编辑-话题标签-第一个标签文本的文本
        :return: '话题编辑-话题标签-第一个标签文本'的文本
        """
        control_content = self.project.get_element_text(self.update_topic_first_label_first_text)
        return control_content

    def click_update_topic_first_label_second_button_action(self):
        """
        动作：点击话题编辑-话题标签-第二个标签
        :return: 点击'话题编辑-话题标签-第二个标签'按钮后的页面
        """
        self.project.click(self.update_topic_first_label_second_button)
        return self.project.get_current_page_source()

    def get_update_topic_first_label_second_text_action(self):
        """
        动作：获取话题编辑-话题标签-第二个标签文本的文本
        :return: '话题编辑-话题标签-第二个标签文本'的文本
        """
        control_content = self.project.get_element_text(self.update_topic_first_label_second_text)
        return control_content

    def click_update_topic_second_label_first_button_action(self):
        """
        动作：点击话题编辑-推荐标签-第一个标签
        :return: 点击'话题编辑-推荐标签-第一个标签'按钮后的页面
        """
        self.project.click(self.update_topic_second_label_first_button)
        return self.project.get_current_page_source()

    def get_update_topic_second_label_first_text_action(self):
        """
        动作：获取话题编辑-推荐标签-第一个标签文本的文本
        :return: '话题编辑-推荐标签-第一个标签文本'的文本
        """
        control_content = self.project.get_element_text(self.update_topic_second_label_first_text)
        return control_content

    def click_update_topic_second_label_second_button_action(self):
        """
        动作：点击话题编辑-推荐标签-第二个标签
        :return: 点击'话题编辑-推荐标签-第二个标签'按钮后的页面
        """
        self.project.click(self.update_topic_second_label_second_button)
        return self.project.get_current_page_source()

    def get_update_topic_second_label_second_text_action(self):
        """
        动作：获取话题编辑-推荐标签-第二个标签文本的文本
        :return: '话题编辑-推荐标签-第二个标签文本'的文本
        """
        control_content = self.project.get_element_text(self.update_topic_second_label_second_text)
        return control_content

    def set_update_topic_cover_image_input_action(self, update_topic_cover_image_input):
        """
        动作：设置话题编辑-封面图片上传输入框
        :param update_topic_cover_image_input: 话题编辑-封面图片上传输入框
        :return: 设置'话题编辑-封面图片上传输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.update_topic_cover_image_input, update_topic_cover_image_input)
        return self.project.get_current_page_source()

    def click_update_topic_cover_image_button_action(self):
        """
        动作：点击话题编辑-封面图片-图片
        :return: 点击'话题编辑-封面图片-图片'按钮后的页面
        """
        self.project.click(self.update_topic_cover_image_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_button_action(self):
        """
        动作：点击话题编辑-列表-添加问答按钮
        :return: 点击'话题编辑-列表-添加问答按钮'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_button)
        return self.project.get_current_page_source()

    def set_update_topic_qa_add_qa_id_input_action(self, update_topic_qa_add_qa_id_input):
        """
        动作：设置话题编辑-添加问答-问答ID
        :param update_topic_qa_add_qa_id_input: 话题编辑-添加问答-问答ID
        :return: 设置'话题编辑-添加问答-问答ID'文本后的页面
        """
        self.project.clear_and_send_keys(self.update_topic_qa_add_qa_id_input, update_topic_qa_add_qa_id_input)
        return self.project.get_current_page_source()

    def set_update_topic_qa_add_qa_title_input_action(self, update_topic_qa_add_qa_title_input):
        """
        动作：设置话题编辑-添加问答-问答标题
        :param update_topic_qa_add_qa_title_input: 话题编辑-添加问答-问答标题
        :return: 设置'话题编辑-添加问答-问答标题'文本后的页面
        """
        self.project.clear_and_send_keys(self.update_topic_qa_add_qa_title_input, update_topic_qa_add_qa_title_input)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_qa_state_button_action(self):
        """
        动作：点击话题编辑-添加问答-问答状态下拉框
        :return: 点击'话题编辑-添加问答-问答状态下拉框'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_qa_state_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_qa_state_all_button_action(self):
        """
        动作：点击话题编辑-添加问答-问答状态-全部
        :return: 点击'话题编辑-添加问答-问答状态-全部'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_qa_state_all_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_qa_state_not_bounty_button_action(self):
        """
        动作：点击话题编辑-添加问答-问答状态-非悬赏
        :return: 点击'话题编辑-添加问答-问答状态-非悬赏'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_qa_state_not_bounty_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_qa_state_in_bounty_button_action(self):
        """
        动作：点击话题编辑-添加问答-问答状态-悬赏中
        :return: 点击'话题编辑-添加问答-问答状态-悬赏中'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_qa_state_in_bounty_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_qa_state_bounty_success_button_action(self):
        """
        动作：点击话题编辑-添加问答-问答状态-悬赏成功
        :return: 点击'话题编辑-添加问答-问答状态-悬赏成功'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_qa_state_bounty_success_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_qa_state_bounty_end_button_action(self):
        """
        动作：点击话题编辑-添加问答-问答状态-悬赏结束
        :return: 点击'话题编辑-添加问答-问答状态-悬赏结束'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_qa_state_bounty_end_button)
        return self.project.get_current_page_source()

    def set_update_topic_qa_add_qa_content_input_action(self, update_topic_qa_add_qa_content_input):
        """
        动作：设置话题编辑-添加问答-问题内容输入框
        :param update_topic_qa_add_qa_content_input: 话题编辑-添加问答-问题内容输入框
        :return: 设置'话题编辑-添加问答-问题内容输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.update_topic_qa_add_qa_content_input, update_topic_qa_add_qa_content_input)
        return self.project.get_current_page_source()

    def set_update_topic_qa_add_create_user_nick_input_action(self, update_topic_qa_add_create_user_nick_input):
        """
        动作：设置话题编辑-添加问答-创建人昵称输入框
        :param update_topic_qa_add_create_user_nick_input: 话题编辑-添加问答-创建人昵称输入框
        :return: 设置'话题编辑-添加问答-创建人昵称输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.update_topic_qa_add_create_user_nick_input, update_topic_qa_add_create_user_nick_input)
        return self.project.get_current_page_source()

    def set_update_topic_qa_add_create_user_name_input_action(self, update_topic_qa_add_create_user_name_input):
        """
        动作：设置话题编辑-添加问答-创建人姓名输入框
        :param update_topic_qa_add_create_user_name_input: 话题编辑-添加问答-创建人姓名输入框
        :return: 设置'话题编辑-添加问答-创建人姓名输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.update_topic_qa_add_create_user_name_input, update_topic_qa_add_create_user_name_input)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_first_label_button_action(self):
        """
        动作：点击话题编辑-添加问答-一级类目标签下拉框
        :return: 点击'话题编辑-添加问答-一级类目标签下拉框'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_first_label_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_first_label_all_button_action(self):
        """
        动作：点击话题编辑-添加问答-一级类目标签-全部
        :return: 点击'话题编辑-添加问答-一级类目标签-全部'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_first_label_all_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_first_label_second_button_action(self):
        """
        动作：点击话题编辑-添加问答-一级类目标签-第二个标签
        :return: 点击'话题编辑-添加问答-一级类目标签-第二个标签'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_first_label_second_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_second_label_button_action(self):
        """
        动作：点击话题编辑-添加问答-二级类目标签下拉框
        :return: 点击'话题编辑-添加问答-二级类目标签下拉框'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_second_label_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_second_label_all_button_action(self):
        """
        动作：点击话题编辑-添加问答-二级类目标签-全部
        :return: 点击'话题编辑-添加问答-二级类目标签-全部'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_second_label_all_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_second_label_second_button_action(self):
        """
        动作：点击话题编辑-添加问答-二级类目标签-第二个标签
        :return: 点击'话题编辑-添加问答-二级类目标签-第二个标签'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_second_label_second_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_sub_content_button_action(self):
        """
        动作：点击话题编辑-添加问答-内容主题下拉框
        :return: 点击'话题编辑-添加问答-内容主题下拉框'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_sub_content_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_sub_content_all_button_action(self):
        """
        动作：点击话题编辑-添加问答-内容主题-全部
        :return: 点击'话题编辑-添加问答-内容主题-全部'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_sub_content_all_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_sub_content_second_button_action(self):
        """
        动作：点击话题编辑-添加问答-内容主题-第二个
        :return: 点击'话题编辑-添加问答-内容主题-第二个'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_sub_content_second_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_best_answer_button_action(self):
        """
        动作：点击话题编辑-添加问答-最佳答案下拉框
        :return: 点击'话题编辑-添加问答-最佳答案下拉框'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_best_answer_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_best_answer_all_button_action(self):
        """
        动作：点击话题编辑-添加问答-最佳答案-全部
        :return: 点击'话题编辑-添加问答-最佳答案-全部'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_best_answer_all_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_best_answer_yes_button_action(self):
        """
        动作：点击话题编辑-添加问答-最佳答案-是
        :return: 点击'话题编辑-添加问答-最佳答案-是'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_best_answer_yes_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_best_answer_no_button_action(self):
        """
        动作：点击话题编辑-添加问答-最佳答案-否
        :return: 点击'话题编辑-添加问答-最佳答案-否'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_best_answer_no_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_query_button_action(self):
        """
        动作：点击话题编辑-添加答案-查询按钮
        :return: 点击'话题编辑-添加答案-查询按钮'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_query_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_clear_button_action(self):
        """
        动作：点击话题编辑-添加答案-清除按钮
        :return: 点击'话题编辑-添加答案-清除按钮'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_clear_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_qa_list_first_select_button_action(self):
        """
        动作：点击话题编辑-添加答案-第一个问答勾选框
        :return: 点击'话题编辑-添加答案-第一个问答勾选框'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_qa_list_first_select_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_qa_list_first_qa_id_button_action(self):
        """
        动作：点击话题编辑-添加答案-问答列表-第一个问答ID按钮
        :return: 点击'话题编辑-添加答案-问答列表-第一个问答ID按钮'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_qa_list_first_qa_id_button)
        return self.project.get_current_page_source()

    def get_update_topic_qa_add_qa_list_first_qa_id_text_action(self):
        """
        动作：获取话题编辑-添加问答-问答列表-第一个问答ID文本的文本
        :return: '话题编辑-添加问答-问答列表-第一个问答ID文本'的文本
        """
        control_content = self.project.get_element_text(self.update_topic_qa_add_qa_list_first_qa_id_text)
        return control_content

    def click_update_topic_qa_add_confirm_button_action(self):
        """
        动作：点击话题编辑-添加答案-确定按钮
        :return: 点击'话题编辑-添加答案-确定按钮'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_confirm_button)
        return self.project.get_current_page_source()

    def click_update_topic_qa_add_close_button_action(self):
        """
        动作：点击话题编辑-添加答案-关闭按钮
        :return: 点击'话题编辑-添加答案-关闭按钮'按钮后的页面
        """
        self.project.click(self.update_topic_qa_add_close_button)
        return self.project.get_current_page_source()

    def get_update_topic_qa_list_first_qa_id_text_action(self):
        """
        动作：获取话题编辑-问答列表-第一个问答-问答ID的文本
        :return: '话题编辑-问答列表-第一个问答-问答ID'的文本
        """
        control_content = self.project.get_element_text(self.update_topic_qa_list_first_qa_id_text)
        return control_content

    def click_update_topic_qa_list_first_delete_button_action(self):
        """
        动作：点击话题编辑-问答列表-第一个问答-删除按钮
        :return: 点击'话题编辑-问答列表-第一个问答-删除按钮'按钮后的页面
        """
        self.project.click(self.update_topic_qa_list_first_delete_button)
        return self.project.get_current_page_source()

    def click_update_topic_commit_button_action(self):
        """
        动作：点击话题编辑-提交按钮
        :return: 点击'话题编辑-提交按钮'按钮后的页面
        """
        self.project.click(self.update_topic_commit_button)
        return self.project.get_current_page_source()

    # endregion Actions
