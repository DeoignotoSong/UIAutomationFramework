from Utils.Log import log


"""
后台-商品服务管理-商品管理
console_url/review/course_record
"""


class ConsoleAbroadCenterGoodsManagementListPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/abroad_center/goods_managementList'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/p'
        # 删除消息提示
        self._message_del_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 输入搜索
        self._search_product_name_input_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div[1]/div[1]/div/div/input'
        # 服务编码
        self._search_sevice_id_input_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div[1]/div[2]/div/div/input'
        # 商品编码
        self._search_product_id_input_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div[1]/div[3]/div/div/input'
        # 搜索所属国家及地区
        self._search_country_place_list_select_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div[1]/div[4]/div/div/div[1]/input'
        # 搜索所属国家及地区全部
        self._search_country_place_all_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[1]'
        # 搜索所属国家及地区美国
        self._search_country_place_america_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[2]'
        # 搜索所属国家及地区澳大利亚
        self._search_country_place_australia_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[3]'
        # 搜索上架状态
        self._search_upper_list_select_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[1]/form/div[1]/div[5]/div/div/div/input'
        # 搜索上架状态全部
        self._search_upper_all_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[1]'
        # 搜索上架状态已下线
        self._search_upper_lower_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[2]'
        # 搜索上架状态已上线
        self._search_upper_upper_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[3]'
        # 搜索上架状态服务下架
        self._search_upper_lower_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[4]'
        # 搜索上架状态待上架
        self._search_upper_wait_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[5]'
        # 搜索前台是否露出
        self._search_reception_list_select_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div[1]/div[6]/div/div/div[1]/input'
        # 搜索前台是否露出全部按钮
        self._search_reception_all_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[1]'
        # 搜索前台是否露出隐藏按钮
        self._search_reception_hide_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[2]'
        # 搜索前台是否露出露出按钮
        self._search_reception_expose_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[3]'
        # 搜索审核状态
        self._search_audit_state_list_select_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[1]/form/div[1]/div[10]/div/div/div/input'
        # 搜索审核状态全部
        self._search_audit_state_all_button_tag = '/html/body/div[6]/div[1]/div[1]/ul/li[1]'
        # 搜索审核状态待审核
        self._search_audit_state_wait_button_tag = '/html/body/div[6]/div[1]/div[1]/ul/li[2]'
        # 搜索审核状态审核通过
        self._search_audit_state_pass_button_tag = '/html/body/div[6]/div[1]/div[1]/ul/li[3]'
        # 搜索审核状态审核未通过
        self._search_audit_state_unpass_button_tag = '/html/body/div[6]/div[1]/div[1]/ul/li[4]'
        # 搜索查询按钮
        self._search_button_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div[1]/div[13]/div/button'
        # 搜索清除按钮
        self._search_clear_button_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div[1]/div[14]/div/button'
        # 商品包装按钮
        self._product_pack_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[1]/form/div[2]/div/div/button'
        # 已包装商品
        self._search_product_packed_button_tag = '/html/body/div/div/section/main/div/div[2]/div[2]/label[1]'
        # 已包装商品列表第一条数据商品id
        self._first_list_packed_product_id_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div'
        # 已包装商品列表第一条数据商品编码
        self._first_list_packed_product_code_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 已包装商品列表第一条数据商品名称
        self._first_list_packed_product_name_text_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr/td[3]/div/a/span'
        # 已包装商品列表第一条数据商品名称点击
        self._first_list_packed_product_name_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/a/span'
        # 已包装商品列表第一条数据服务编码
        self._first_list_packed_product_service_id_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 已包装商品列表第一条数据服务名称
        self._first_list_packed_product_service_name_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 已包装商品列表第一条数据所属国家及地区
        self._first_list_packed_product_service_country_place_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 已包装商品列表第一条数据商品价格
        self._first_list_packed_product_price_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div'
        # 已包装商品列表第一条数据审核状态
        self._first_list_packed_product_audit_state_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div'
        # 已包装商品列表第一条数据上架状态
        self._first_list_packed_product_upper_state_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[10]/div'
        # 已包装商品列表第一条数据操作前台隐藏
        self._first_list_packed_product_hide_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr/td[11]/div/a[1]/span'
        # 已包装商品列表第一条数据操作前台隐藏文案
        self._first_list_packed_product_hide_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr/td[11]/div/a[1]/span'
        # 已包装商品列表第一条数据操作前台隐藏确认
        self._first_list_packed_product_hide_commit_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # 已包装商品列表第一条数据操作修改
        self._first_list_packed_product_edit_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr/td[11]/div/a[2]/span'
        # 已包装商品列表第一条数据操作关联商品
        self._first_list_packed_product_associate_button_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr/td[11]/div/a[3]'
        # 已包装商品列表第一条数据操作复制
        self._first_list_packed_product_copy_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[11]/div/a[4]/span'
        # 已包装商品列表无数据文本
        self._first_list_packed_product_no_data_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div/div[3]/div/span/label'
        # 草稿箱商品列表第一条数据操作删除
        self._first_list_draft_product_delete_button_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[7]/div/a[2]'
        # 草稿箱商品列表第一条数据删除确认
        self._first_list_draft_product_delete_commit_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # 草稿箱按钮
        self._search_product_draft_button_tag = '/html/body/div/div/section/main/div/div[2]/div[2]/label[2]'
        # 草稿箱商品列表第一条数据商品编码
        self._first_list_draft_product_id_text_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div'
        # 草稿箱商品列表第一条数据服务名称
        self._first_list_draft_product_name_text_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a/span'
        # 草稿箱商品列表第一条数据商品名称点击
        self._first_list_draft_product_name_button_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a'
        # 草稿箱商品列表第一条数据服务编码
        self._first_list_draft_product_service_id_text_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 草稿箱商品列表第一条数据服务名称
        self._first_list_draft_product_service_name_text_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 草稿箱商品列表第一条数据所属国家及地区
        self._first_list_draft_product_service_country_place_text_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 草稿箱商品列表第一条数据商品价格
        self._first_list_draft_product_price_text_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 草稿箱商品列表第一条数据操作包装
        self._first_list_draft_product_pack_button_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/a[1]'
        # 草稿箱商品列表第一条数据操作删除
        self._first_list_draft_product_pack_button_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr/td[8]/div/a[1]/span'
        # 草稿箱商品列表第一条数据操作删除
        self._first_list_draft_product_delete_button_tag = '/html/body/div/div/section/main/div/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr/td[8]/div/a[2]/span'
        # 草稿箱商品列表第一条数据删除确认
        self._first_list_draft_product_delete_commit_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # 草稿箱列表无数据文本
        self._first_list_draft_product_no_data_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[3]/div/div[3]/div/span/label'
        # 商品包装组合服务选择
        self._product_pack_service_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[2]/form/div/div/a'
        # 商品包装组合服务服务编码查询
        self._product_pack_service_id_input_tag = '/html/body/div[4]/div/div[2]/div[1]/form/div/div[1]/div/div/input'
        # 商品包装组合服务服务名称查询
        self._product_pack_service_name_input_tag = '/html/body/div[2]/div/div[2]/div[1]/form/div/div[2]/div/div/input'
        # 商品包装组合服务所属国家及地区
        self._product_pack_service_country_list_select_tag = '/html/body/div[4]/div/div[2]/div[1]/form/div/div[3]/div/div/div[1]/input'
        # 商品包装组合服务所属国家及地区全部
        self._product_pack_service_country_all_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[1]'
        # 商品包装组合服务所属国家及地区美国
        self._product_pack_service_country_america_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[2]'
        # 商品包装组合服务查询
        self._product_pack_service_search_button_tag = '/html/body/div[2]/div/div[2]/div[1]/form/div/div[4]/div/button'
        # 商品包装组合服务重置
        self._product_pack_service_clear_button_tag = '/html/body/div[4]/div/div[2]/div[1]/form/div/div[5]/div/button'
        # 商品包装组合服务第一条数据服务编码
        self._first_list_product_pack_service_id_text_tag = '/html/body/div[4]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div'
        # 商品包装组合服务第一条数据服务名称
        self._first_list_product_pack_service_name_text_tag = '/html/body/div[4]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 商品包装组合服务第一条数据所属国家和地区
        self._first_list_product_pack_service_country_text_tag = '/html/body/div[4]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 商品包装组合服务第一条数据包装
        self._first_list_product_pack_service_pack_button_tag = '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[4]/div/a/span'
        # 商品包装基本信息商品名称
        self._product_pack_product_name_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/input'
        # 商品服务内容合计价格
        self._product_service_content_all_price_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[4]/div/div/div[2]/span'
        # 商品包装基本信息商品价格
        self._product_pack_product_price_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[3]/div/div/div[2]/div[1]/input'
        # 商品服务内容合计价格作为划线价展示在前台
        self._product_pack_product_price_display_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[4]/div/div/div[2]/label[1]/span[2]'
        # 商品服务内容合计价格作为划线价不展示在前台
        self._product_pack_product_price_undisplay_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[4]/div/div/div[2]/label[2]/span[2]'
        # 商品包装基本信息商品标签优选
        self._product_pack_product_lable_preference_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[5]/div/div/div[2]/label[1]/span[2]'
        # 商品包装基本信息商品标签人气
        self._product_pack_product_lable_popularity_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[5]/div/div/div[2]/label[2]/span[2]'
        # 商品包装基本信息商品标签特色
        self._product_pack_product_lable_characteristic_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[5]/div/div/div[2]/label[3]/span[2]'
        # 商品包装基本信息商品卖点
        self._product_pack_product_usp_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[6]/div/div/div[2]/div[1]/textarea'
        # 商品包装基本信息退款说明
        self._product_pack_product_refund_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[7]/div/div/div[2]/div/textarea'
        # 商品包装基本信息专项条款
        self._product_pack_product_terms_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[8]/div/div/div[2]/div/textarea'
        # 商品包装基本信息搜索关键词1
        self._product_pack_product_first_key_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[2]/div[1]/div/input'
        # 商品包装基本信息搜索关键词2
        self._product_pack_product_second_key_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[2]/div[2]/div/input'
        # 商品包装基本信息搜索关键词3
        self._product_pack_product_third_key_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[2]/div[3]/div/input'
        # 商品包装基本信息主图1
        self._product_pack_product_first_image_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[10]/div/div/div[2]/div[1]/div[1]/div/div'
        # 商品包装基本信息主图1上传
        self._product_pack_product_first_image_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[10]/div/div/div[2]/div[1]/div[1]/div/div/input'
        # 商品包装基本信息主图2
        self._product_pack_product_second_image_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[10]/div/div/div[2]/div[1]/div[2]'
        # 商品包装基本信息主图2上传
        self._product_pack_product_second_image_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[10]/div/div/div[2]/div[1]/div[2]/div/div/input'
        # 商品包装基本信息主图3
        self._product_pack_product_third_image_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[10]/div/div/div[2]/div[1]/div[3]'
        # 商品包装基本信息主图3上传
        self._product_pack_product_third_image_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[10]/div/div/div[2]/div[1]/div[3]/div/div/input'
        # 商品包装基本信息主图4
        self._product_pack_product_third_image_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[10]/div/div/div[2]/div[1]/div[4]'
        # 商品包装基本信息主图4上传
        self._product_pack_product_third_image_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[10]/div/div/div[2]/div[1]/div[4]/div/div/input'
        # 商品包装基本信息主图5
        self._product_pack_product_third_image_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[10]/div/div/div[2]/div[1]/div[5]'
        # 商品包装基本信息主图5上传
        self._product_pack_product_third_image_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[10]/div/div/div[2]/div[1]/div[5]/div/div/input'
        # 商品包装基本信息视频
        self._product_pack_product_video_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[11]/div/div/div[2]/div[1]/label'
        # 商品包装基本信息视频上传
        self._product_pack_product_video_upload_input_tag = '//*[@id="file00"]'
        # 商品包装基本信息feed流图片
        self._product_pack_product_feed_image_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[12]/div/div/div[2]/div[1]/div/div'
        # 商品包装基本信息feed流图片上传
        self._product_pack_product_feed_image_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[12]/div/div/div[2]/div[1]/div/div/input'
        # 商品包装其他信息服务退款保障
        self._product_pack_other_ensue_refund_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[1]/div/div/div[2]/div/label[1]/span[2]'
        # 商品包装其他信息服务平台保障
        self._product_pack_other_ensue_platform_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[1]/div/div/div[2]/div/label[2]/span[2]'
        # 商品包装其他信息服务服务流程
        self._product_pack_other_ensue_service_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[1]/div/div/div[2]/div/label[3]/span[2]'
        # 商品包装其他信息服务常见问题1
        self._product_pack_other_first_question_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/input'
        # 商品包装其他信息服务常见问题1回答
        self._product_pack_other_first_question_answer_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/textarea'
        # 商品包装其他信息服务常见问题添加
        self._product_pack_other_first_question_add_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[2]/div[2]/a/span'
        # 商品包装其他信息服务常见问题2
        self._product_pack_other_second_question_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div/input'
        # 商品包装其他信息服务常见问题2回答
        self._product_pack_other_second_question_answer_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/textarea'
        # 商品包装商品详情详情图
        self._product_pack_product_detail_image_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[3]/div[2]/div/div/div/div[2]/div[1]/div/div'
        # 商品包装商品详情详情图上传
        self._product_pack_product_detail_image_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[3]/div[2]/div/div/div/div[2]/div[1]/div/div/input'
        # 商品包装附件合同
        self._product_pack_product_contract_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[4]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div'
        # 商品包装附件合同上传
        self._product_pack_product_contract_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[4]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/input'
        # 商品包装预览
        self._product_pack_product_prview_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/button[1]'
        # 商品包装保存
        self._product_pack_product_save_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/button[2]'
        # 商品包装提交审核
        self._product_pack_product_submit_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/button[3]'
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
    def message_del_content_text(self):
        """
        属性: 删除消息提示
        :return: 删除消息提示
        """
        element = None
        try:
            element = self.project.get_element(self._message_del_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_product_name_input(self):
        """
        属性: 输入搜索
        :return: 输入搜索
        """
        element = None
        try:
            element = self.project.get_element(self._search_product_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_sevice_id_input(self):
        """
        属性: 服务编码
        :return: 服务编码
        """
        element = None
        try:
            element = self.project.get_element(self._search_sevice_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_product_id_input(self):
        """
        属性: 商品编码
        :return: 商品编码
        """
        element = None
        try:
            element = self.project.get_element(self._search_product_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_country_place_list_select(self):
        """
        属性: 搜索所属国家及地区
        :return: 搜索所属国家及地区
        """
        element = None
        try:
            element = self.project.get_element(self._search_country_place_list_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_country_place_all_button(self):
        """
        属性: 搜索所属国家及地区全部
        :return: 搜索所属国家及地区全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_country_place_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_country_place_america_button(self):
        """
        属性: 搜索所属国家及地区美国
        :return: 搜索所属国家及地区美国
        """
        element = None
        try:
            element = self.project.get_element(self._search_country_place_america_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_country_place_australia_button(self):
        """
        属性: 搜索所属国家及地区澳大利亚
        :return: 搜索所属国家及地区澳大利亚
        """
        element = None
        try:
            element = self.project.get_element(self._search_country_place_australia_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_upper_list_select(self):
        """
        属性: 搜索上架状态
        :return: 搜索上架状态
        """
        element = None
        try:
            element = self.project.get_element(self._search_upper_list_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_upper_all_button(self):
        """
        属性: 搜索上架状态全部
        :return: 搜索上架状态全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_upper_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_upper_lower_button(self):
        """
        属性: 搜索上架状态已下线
        :return: 搜索上架状态已下线
        """
        element = None
        try:
            element = self.project.get_element(self._search_upper_lower_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_upper_upper_button(self):
        """
        属性: 搜索上架状态已上线
        :return: 搜索上架状态已上线
        """
        element = None
        try:
            element = self.project.get_element(self._search_upper_upper_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_upper_lower_button(self):
        """
        属性: 搜索上架状态服务下架
        :return: 搜索上架状态服务下架
        """
        element = None
        try:
            element = self.project.get_element(self._search_upper_lower_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_upper_wait_button(self):
        """
        属性: 搜索上架状态待上架
        :return: 搜索上架状态待上架
        """
        element = None
        try:
            element = self.project.get_element(self._search_upper_wait_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_reception_list_select(self):
        """
        属性: 搜索前台是否露出
        :return: 搜索前台是否露出
        """
        element = None
        try:
            element = self.project.get_element(self._search_reception_list_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_reception_all_button(self):
        """
        属性: 搜索前台是否露出全部按钮
        :return: 搜索前台是否露出全部按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_reception_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_reception_hide_button(self):
        """
        属性: 搜索前台是否露出隐藏按钮
        :return: 搜索前台是否露出隐藏按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_reception_hide_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_reception_expose_button(self):
        """
        属性: 搜索前台是否露出露出按钮
        :return: 搜索前台是否露出露出按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_reception_expose_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_audit_state_list_select(self):
        """
        属性: 搜索审核状态
        :return: 搜索审核状态
        """
        element = None
        try:
            element = self.project.get_element(self._search_audit_state_list_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_audit_state_all_button(self):
        """
        属性: 搜索审核状态全部
        :return: 搜索审核状态全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_audit_state_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_audit_state_wait_button(self):
        """
        属性: 搜索审核状态待审核
        :return: 搜索审核状态待审核
        """
        element = None
        try:
            element = self.project.get_element(self._search_audit_state_wait_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_audit_state_pass_button(self):
        """
        属性: 搜索审核状态审核通过
        :return: 搜索审核状态审核通过
        """
        element = None
        try:
            element = self.project.get_element(self._search_audit_state_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_audit_state_unpass_button(self):
        """
        属性: 搜索审核状态审核未通过
        :return: 搜索审核状态审核未通过
        """
        element = None
        try:
            element = self.project.get_element(self._search_audit_state_unpass_button_tag)
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
    def search_clear_button(self):
        """
        属性: 搜索清除按钮
        :return: 搜索清除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_button(self):
        """
        属性: 商品包装按钮
        :return: 商品包装按钮
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_product_packed_button(self):
        """
        属性: 已包装商品
        :return: 已包装商品
        """
        element = None
        try:
            element = self.project.get_element(self._search_product_packed_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_id_text(self):
        """
        属性: 已包装商品列表第一条数据商品id
        :return: 已包装商品列表第一条数据商品id
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_code_text(self):
        """
        属性: 已包装商品列表第一条数据商品编码
        :return: 已包装商品列表第一条数据商品编码
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_code_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_name_text(self):
        """
        属性: 已包装商品列表第一条数据商品名称
        :return: 已包装商品列表第一条数据商品名称
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_name_button(self):
        """
        属性: 已包装商品列表第一条数据商品名称点击
        :return: 已包装商品列表第一条数据商品名称点击
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_name_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_service_id_text(self):
        """
        属性: 已包装商品列表第一条数据服务编码
        :return: 已包装商品列表第一条数据服务编码
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_service_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_service_name_text(self):
        """
        属性: 已包装商品列表第一条数据服务名称
        :return: 已包装商品列表第一条数据服务名称
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_service_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_service_country_place_text(self):
        """
        属性: 已包装商品列表第一条数据所属国家及地区
        :return: 已包装商品列表第一条数据所属国家及地区
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_service_country_place_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_price_text(self):
        """
        属性: 已包装商品列表第一条数据商品价格
        :return: 已包装商品列表第一条数据商品价格
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_price_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_audit_state_text(self):
        """
        属性: 已包装商品列表第一条数据审核状态
        :return: 已包装商品列表第一条数据审核状态
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_audit_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_upper_state_text(self):
        """
        属性: 已包装商品列表第一条数据上架状态
        :return: 已包装商品列表第一条数据上架状态
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_upper_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_hide_button(self):
        """
        属性: 已包装商品列表第一条数据操作前台隐藏
        :return: 已包装商品列表第一条数据操作前台隐藏
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_hide_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_hide_text(self):
        """
        属性: 已包装商品列表第一条数据操作前台隐藏文案
        :return: 已包装商品列表第一条数据操作前台隐藏文案
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_hide_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_hide_commit_button(self):
        """
        属性: 已包装商品列表第一条数据操作前台隐藏确认
        :return: 已包装商品列表第一条数据操作前台隐藏确认
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_hide_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_edit_button(self):
        """
        属性: 已包装商品列表第一条数据操作修改
        :return: 已包装商品列表第一条数据操作修改
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_edit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_associate_button(self):
        """
        属性: 已包装商品列表第一条数据操作关联商品
        :return: 已包装商品列表第一条数据操作关联商品
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_associate_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_copy_button(self):
        """
        属性: 已包装商品列表第一条数据操作复制
        :return: 已包装商品列表第一条数据操作复制
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_copy_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_packed_product_no_data_text(self):
        """
        属性: 已包装商品列表无数据文本
        :return: 已包装商品列表无数据文本
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_packed_product_no_data_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_draft_product_delete_button(self):
        """
        属性: 草稿箱商品列表第一条数据操作删除
        :return: 草稿箱商品列表第一条数据操作删除
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_draft_product_delete_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_draft_product_delete_commit_button(self):
        """
        属性: 草稿箱商品列表第一条数据删除确认
        :return: 草稿箱商品列表第一条数据删除确认
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_draft_product_delete_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_product_draft_button(self):
        """
        属性: 草稿箱按钮
        :return: 草稿箱按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_product_draft_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_draft_product_id_text(self):
        """
        属性: 草稿箱商品列表第一条数据商品编码
        :return: 草稿箱商品列表第一条数据商品编码
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_draft_product_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_draft_product_name_text(self):
        """
        属性: 草稿箱商品列表第一条数据服务名称
        :return: 草稿箱商品列表第一条数据服务名称
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_draft_product_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_draft_product_name_button(self):
        """
        属性: 草稿箱商品列表第一条数据商品名称点击
        :return: 草稿箱商品列表第一条数据商品名称点击
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_draft_product_name_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_draft_product_service_id_text(self):
        """
        属性: 草稿箱商品列表第一条数据服务编码
        :return: 草稿箱商品列表第一条数据服务编码
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_draft_product_service_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_draft_product_service_name_text(self):
        """
        属性: 草稿箱商品列表第一条数据服务名称
        :return: 草稿箱商品列表第一条数据服务名称
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_draft_product_service_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_draft_product_service_country_place_text(self):
        """
        属性: 草稿箱商品列表第一条数据所属国家及地区
        :return: 草稿箱商品列表第一条数据所属国家及地区
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_draft_product_service_country_place_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_draft_product_price_text(self):
        """
        属性: 草稿箱商品列表第一条数据商品价格
        :return: 草稿箱商品列表第一条数据商品价格
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_draft_product_price_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_draft_product_pack_button(self):
        """
        属性: 草稿箱商品列表第一条数据操作包装
        :return: 草稿箱商品列表第一条数据操作包装
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_draft_product_pack_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_draft_product_pack_button(self):
        """
        属性: 草稿箱商品列表第一条数据操作删除
        :return: 草稿箱商品列表第一条数据操作删除
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_draft_product_pack_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_draft_product_delete_button(self):
        """
        属性: 草稿箱商品列表第一条数据操作删除
        :return: 草稿箱商品列表第一条数据操作删除
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_draft_product_delete_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_draft_product_delete_commit_button(self):
        """
        属性: 草稿箱商品列表第一条数据删除确认
        :return: 草稿箱商品列表第一条数据删除确认
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_draft_product_delete_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_draft_product_no_data_text(self):
        """
        属性: 草稿箱列表无数据文本
        :return: 草稿箱列表无数据文本
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_draft_product_no_data_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_service_button(self):
        """
        属性: 商品包装组合服务选择
        :return: 商品包装组合服务选择
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_service_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_service_id_input(self):
        """
        属性: 商品包装组合服务服务编码查询
        :return: 商品包装组合服务服务编码查询
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_service_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_service_name_input(self):
        """
        属性: 商品包装组合服务服务名称查询
        :return: 商品包装组合服务服务名称查询
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_service_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_service_country_list_select(self):
        """
        属性: 商品包装组合服务所属国家及地区
        :return: 商品包装组合服务所属国家及地区
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_service_country_list_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_service_country_all_button(self):
        """
        属性: 商品包装组合服务所属国家及地区全部
        :return: 商品包装组合服务所属国家及地区全部
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_service_country_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_service_country_america_button(self):
        """
        属性: 商品包装组合服务所属国家及地区美国
        :return: 商品包装组合服务所属国家及地区美国
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_service_country_america_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_service_search_button(self):
        """
        属性: 商品包装组合服务查询
        :return: 商品包装组合服务查询
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_service_search_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_service_clear_button(self):
        """
        属性: 商品包装组合服务重置
        :return: 商品包装组合服务重置
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_service_clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_product_pack_service_id_text(self):
        """
        属性: 商品包装组合服务第一条数据服务编码
        :return: 商品包装组合服务第一条数据服务编码
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_product_pack_service_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_product_pack_service_name_text(self):
        """
        属性: 商品包装组合服务第一条数据服务名称
        :return: 商品包装组合服务第一条数据服务名称
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_product_pack_service_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_product_pack_service_country_text(self):
        """
        属性: 商品包装组合服务第一条数据所属国家和地区
        :return: 商品包装组合服务第一条数据所属国家和地区
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_product_pack_service_country_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_product_pack_service_pack_button(self):
        """
        属性: 商品包装组合服务第一条数据包装
        :return: 商品包装组合服务第一条数据包装
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_product_pack_service_pack_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_name_input(self):
        """
        属性: 商品包装基本信息商品名称
        :return: 商品包装基本信息商品名称
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_service_content_all_price_text(self):
        """
        属性: 商品服务内容合计价格
        :return: 商品服务内容合计价格
        """
        element = None
        try:
            element = self.project.get_element(self._product_service_content_all_price_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_price_input(self):
        """
        属性: 商品包装基本信息商品价格
        :return: 商品包装基本信息商品价格
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_price_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_price_display_button(self):
        """
        属性: 商品服务内容合计价格作为划线价展示在前台
        :return: 商品服务内容合计价格作为划线价展示在前台
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_price_display_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_price_undisplay_button(self):
        """
        属性: 商品服务内容合计价格作为划线价不展示在前台
        :return: 商品服务内容合计价格作为划线价不展示在前台
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_price_undisplay_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_lable_preference_button(self):
        """
        属性: 商品包装基本信息商品标签优选
        :return: 商品包装基本信息商品标签优选
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_lable_preference_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_lable_popularity_button(self):
        """
        属性: 商品包装基本信息商品标签人气
        :return: 商品包装基本信息商品标签人气
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_lable_popularity_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_lable_characteristic_button(self):
        """
        属性: 商品包装基本信息商品标签特色
        :return: 商品包装基本信息商品标签特色
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_lable_characteristic_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_usp_input(self):
        """
        属性: 商品包装基本信息商品卖点
        :return: 商品包装基本信息商品卖点
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_usp_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_refund_input(self):
        """
        属性: 商品包装基本信息退款说明
        :return: 商品包装基本信息退款说明
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_refund_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_terms_input(self):
        """
        属性: 商品包装基本信息专项条款
        :return: 商品包装基本信息专项条款
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_terms_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_first_key_input(self):
        """
        属性: 商品包装基本信息搜索关键词1
        :return: 商品包装基本信息搜索关键词1
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_first_key_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_second_key_input(self):
        """
        属性: 商品包装基本信息搜索关键词2
        :return: 商品包装基本信息搜索关键词2
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_second_key_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_third_key_input(self):
        """
        属性: 商品包装基本信息搜索关键词3
        :return: 商品包装基本信息搜索关键词3
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_third_key_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_first_image_button(self):
        """
        属性: 商品包装基本信息主图1
        :return: 商品包装基本信息主图1
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_first_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_first_image_upload_input(self):
        """
        属性: 商品包装基本信息主图1上传
        :return: 商品包装基本信息主图1上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_first_image_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_second_image_button(self):
        """
        属性: 商品包装基本信息主图2
        :return: 商品包装基本信息主图2
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_second_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_second_image_upload_input(self):
        """
        属性: 商品包装基本信息主图2上传
        :return: 商品包装基本信息主图2上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_second_image_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_third_image_button(self):
        """
        属性: 商品包装基本信息主图3
        :return: 商品包装基本信息主图3
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_third_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_third_image_upload_input(self):
        """
        属性: 商品包装基本信息主图3上传
        :return: 商品包装基本信息主图3上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_third_image_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_third_image_button(self):
        """
        属性: 商品包装基本信息主图4
        :return: 商品包装基本信息主图4
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_third_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_third_image_upload_input(self):
        """
        属性: 商品包装基本信息主图4上传
        :return: 商品包装基本信息主图4上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_third_image_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_third_image_button(self):
        """
        属性: 商品包装基本信息主图5
        :return: 商品包装基本信息主图5
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_third_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_third_image_upload_input(self):
        """
        属性: 商品包装基本信息主图5上传
        :return: 商品包装基本信息主图5上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_third_image_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_video_button(self):
        """
        属性: 商品包装基本信息视频
        :return: 商品包装基本信息视频
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_video_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_video_upload_input(self):
        """
        属性: 商品包装基本信息视频上传
        :return: 商品包装基本信息视频上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_video_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_feed_image_button(self):
        """
        属性: 商品包装基本信息feed流图片
        :return: 商品包装基本信息feed流图片
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_feed_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_feed_image_upload_input(self):
        """
        属性: 商品包装基本信息feed流图片上传
        :return: 商品包装基本信息feed流图片上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_feed_image_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_other_ensue_refund_button(self):
        """
        属性: 商品包装其他信息服务退款保障
        :return: 商品包装其他信息服务退款保障
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_other_ensue_refund_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_other_ensue_platform_button(self):
        """
        属性: 商品包装其他信息服务平台保障
        :return: 商品包装其他信息服务平台保障
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_other_ensue_platform_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_other_ensue_service_button(self):
        """
        属性: 商品包装其他信息服务服务流程
        :return: 商品包装其他信息服务服务流程
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_other_ensue_service_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_other_first_question_input(self):
        """
        属性: 商品包装其他信息服务常见问题1
        :return: 商品包装其他信息服务常见问题1
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_other_first_question_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_other_first_question_answer_input(self):
        """
        属性: 商品包装其他信息服务常见问题1回答
        :return: 商品包装其他信息服务常见问题1回答
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_other_first_question_answer_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_other_first_question_add_button(self):
        """
        属性: 商品包装其他信息服务常见问题添加
        :return: 商品包装其他信息服务常见问题添加
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_other_first_question_add_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_other_second_question_input(self):
        """
        属性: 商品包装其他信息服务常见问题2
        :return: 商品包装其他信息服务常见问题2
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_other_second_question_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_other_second_question_answer_input(self):
        """
        属性: 商品包装其他信息服务常见问题2回答
        :return: 商品包装其他信息服务常见问题2回答
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_other_second_question_answer_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_detail_image_button(self):
        """
        属性: 商品包装商品详情详情图
        :return: 商品包装商品详情详情图
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_detail_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_detail_image_upload_input(self):
        """
        属性: 商品包装商品详情详情图上传
        :return: 商品包装商品详情详情图上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_detail_image_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_contract_button(self):
        """
        属性: 商品包装附件合同
        :return: 商品包装附件合同
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_contract_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_contract_upload_input(self):
        """
        属性: 商品包装附件合同上传
        :return: 商品包装附件合同上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_contract_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_prview_button(self):
        """
        属性: 商品包装预览
        :return: 商品包装预览
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_prview_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_save_button(self):
        """
        属性: 商品包装保存
        :return: 商品包装保存
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_save_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_submit_button(self):
        """
        属性: 商品包装提交审核
        :return: 商品包装提交审核
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_submit_button_tag)
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

    def get_message_del_content_text_action(self):
        """
        动作：获取删除消息提示的文本
        :return: '删除消息提示'的文本
        """
        control_content = self.project.get_element_text(self.message_del_content_text)
        return control_content

    def set_search_product_name_input_action(self, search_product_name_input):
        """
        动作：设置输入搜索
        :param search_product_name_input: 输入搜索
        :return: 设置'输入搜索'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_product_name_input, search_product_name_input)
        return self.project.get_current_page_source()

    def set_search_sevice_id_input_action(self, search_sevice_id_input):
        """
        动作：设置服务编码
        :param search_sevice_id_input: 服务编码
        :return: 设置'服务编码'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_sevice_id_input, search_sevice_id_input)
        return self.project.get_current_page_source()

    def set_search_product_id_input_action(self, search_product_id_input):
        """
        动作：设置商品编码
        :param search_product_id_input: 商品编码
        :return: 设置'商品编码'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_product_id_input, search_product_id_input)
        return self.project.get_current_page_source()

    def get_select_search_country_place_list_action(self, search_country_place_list_select):
        """
        动作：获取搜索所属国家及地区列表选中的文本
        :param search_country_place_list_select: 搜索所属国家及地区列表索引或文本
        :return: '搜索所属国家及地区'的文本
        """
        control_content = self.project.get_select_content(self.search_country_place_list_select, search_country_place_list_select)
        return control_content

    def select_search_country_place_list_action(self, search_country_place_list_select):
        """
        动作：选择搜索所属国家及地区
        :param search_country_place_list_select: 搜索所属国家及地区列表索引或文本
        :return: 选择'搜索所属国家及地区'选择器后的页面
        """
        self.project.select_control(self.search_country_place_list_select, search_country_place_list_select)
        return self.project.get_current_page_source()

    def click_search_country_place_all_button_action(self):
        """
        动作：点击搜索所属国家及地区全部
        :return: 点击'搜索所属国家及地区全部'按钮后的页面
        """
        self.project.click(self.search_country_place_all_button)
        return self.project.get_current_page_source()

    def click_search_country_place_america_button_action(self):
        """
        动作：点击搜索所属国家及地区美国
        :return: 点击'搜索所属国家及地区美国'按钮后的页面
        """
        self.project.click(self.search_country_place_america_button)
        return self.project.get_current_page_source()

    def click_search_country_place_australia_button_action(self):
        """
        动作：点击搜索所属国家及地区澳大利亚
        :return: 点击'搜索所属国家及地区澳大利亚'按钮后的页面
        """
        self.project.click(self.search_country_place_australia_button)
        return self.project.get_current_page_source()

    def get_select_search_upper_list_action(self, search_upper_list_select):
        """
        动作：获取搜索上架状态列表选中的文本
        :param search_upper_list_select: 搜索上架状态列表索引或文本
        :return: '搜索上架状态'的文本
        """
        control_content = self.project.get_select_content(self.search_upper_list_select, search_upper_list_select)
        return control_content

    def select_search_upper_list_action(self, search_upper_list_select):
        """
        动作：选择搜索上架状态
        :param search_upper_list_select: 搜索上架状态列表索引或文本
        :return: 选择'搜索上架状态'选择器后的页面
        """
        self.project.select_control(self.search_upper_list_select, search_upper_list_select)
        return self.project.get_current_page_source()

    def click_search_upper_all_button_action(self):
        """
        动作：点击搜索上架状态全部
        :return: 点击'搜索上架状态全部'按钮后的页面
        """
        self.project.click(self.search_upper_all_button)
        return self.project.get_current_page_source()

    def click_search_upper_lower_button_action(self):
        """
        动作：点击搜索上架状态已下线
        :return: 点击'搜索上架状态已下线'按钮后的页面
        """
        self.project.click(self.search_upper_lower_button)
        return self.project.get_current_page_source()

    def click_search_upper_upper_button_action(self):
        """
        动作：点击搜索上架状态已上线
        :return: 点击'搜索上架状态已上线'按钮后的页面
        """
        self.project.click(self.search_upper_upper_button)
        return self.project.get_current_page_source()

    def click_search_upper_lower_button_action(self):
        """
        动作：点击搜索上架状态服务下架
        :return: 点击'搜索上架状态服务下架'按钮后的页面
        """
        self.project.click(self.search_upper_lower_button)
        return self.project.get_current_page_source()

    def click_search_upper_wait_button_action(self):
        """
        动作：点击搜索上架状态待上架
        :return: 点击'搜索上架状态待上架'按钮后的页面
        """
        self.project.click(self.search_upper_wait_button)
        return self.project.get_current_page_source()

    def get_select_search_reception_list_action(self, search_reception_list_select):
        """
        动作：获取搜索前台是否露出列表选中的文本
        :param search_reception_list_select: 搜索前台是否露出列表索引或文本
        :return: '搜索前台是否露出'的文本
        """
        control_content = self.project.get_select_content(self.search_reception_list_select, search_reception_list_select)
        return control_content

    def select_search_reception_list_action(self, search_reception_list_select):
        """
        动作：选择搜索前台是否露出
        :param search_reception_list_select: 搜索前台是否露出列表索引或文本
        :return: 选择'搜索前台是否露出'选择器后的页面
        """
        self.project.select_control(self.search_reception_list_select, search_reception_list_select)
        return self.project.get_current_page_source()

    def click_search_reception_all_button_action(self):
        """
        动作：点击搜索前台是否露出全部按钮
        :return: 点击'搜索前台是否露出全部按钮'按钮后的页面
        """
        self.project.click(self.search_reception_all_button)
        return self.project.get_current_page_source()

    def click_search_reception_hide_button_action(self):
        """
        动作：点击搜索前台是否露出隐藏按钮
        :return: 点击'搜索前台是否露出隐藏按钮'按钮后的页面
        """
        self.project.click(self.search_reception_hide_button)
        return self.project.get_current_page_source()

    def click_search_reception_expose_button_action(self):
        """
        动作：点击搜索前台是否露出露出按钮
        :return: 点击'搜索前台是否露出露出按钮'按钮后的页面
        """
        self.project.click(self.search_reception_expose_button)
        return self.project.get_current_page_source()

    def get_select_search_audit_state_list_action(self, search_audit_state_list_select):
        """
        动作：获取搜索审核状态列表选中的文本
        :param search_audit_state_list_select: 搜索审核状态列表索引或文本
        :return: '搜索审核状态'的文本
        """
        control_content = self.project.get_select_content(self.search_audit_state_list_select, search_audit_state_list_select)
        return control_content

    def select_search_audit_state_list_action(self, search_audit_state_list_select):
        """
        动作：选择搜索审核状态
        :param search_audit_state_list_select: 搜索审核状态列表索引或文本
        :return: 选择'搜索审核状态'选择器后的页面
        """
        self.project.select_control(self.search_audit_state_list_select, search_audit_state_list_select)
        return self.project.get_current_page_source()

    def click_search_audit_state_all_button_action(self):
        """
        动作：点击搜索审核状态全部
        :return: 点击'搜索审核状态全部'按钮后的页面
        """
        self.project.click(self.search_audit_state_all_button)
        return self.project.get_current_page_source()

    def click_search_audit_state_wait_button_action(self):
        """
        动作：点击搜索审核状态待审核
        :return: 点击'搜索审核状态待审核'按钮后的页面
        """
        self.project.click(self.search_audit_state_wait_button)
        return self.project.get_current_page_source()

    def click_search_audit_state_pass_button_action(self):
        """
        动作：点击搜索审核状态审核通过
        :return: 点击'搜索审核状态审核通过'按钮后的页面
        """
        self.project.click(self.search_audit_state_pass_button)
        return self.project.get_current_page_source()

    def click_search_audit_state_unpass_button_action(self):
        """
        动作：点击搜索审核状态审核未通过
        :return: 点击'搜索审核状态审核未通过'按钮后的页面
        """
        self.project.click(self.search_audit_state_unpass_button)
        return self.project.get_current_page_source()

    def click_search_button_action(self):
        """
        动作：点击搜索查询按钮
        :return: 点击'搜索查询按钮'按钮后的页面
        """
        self.project.click(self.search_button)
        return self.project.get_current_page_source()

    def click_search_clear_button_action(self):
        """
        动作：点击搜索清除按钮
        :return: 点击'搜索清除按钮'按钮后的页面
        """
        self.project.click(self.search_clear_button)
        return self.project.get_current_page_source()

    def click_product_pack_button_action(self):
        """
        动作：点击商品包装按钮
        :return: 点击'商品包装按钮'按钮后的页面
        """
        self.project.click(self.product_pack_button)
        return self.project.get_current_page_source()

    def click_search_product_packed_button_action(self):
        """
        动作：点击已包装商品
        :return: 点击'已包装商品'按钮后的页面
        """
        self.project.click(self.search_product_packed_button)
        return self.project.get_current_page_source()

    def get_first_list_packed_product_id_text_action(self):
        """
        动作：获取已包装商品列表第一条数据商品id的文本
        :return: '已包装商品列表第一条数据商品id'的文本
        """
        control_content = self.project.get_element_text(self.first_list_packed_product_id_text)
        return control_content

    def get_first_list_packed_product_code_text_action(self):
        """
        动作：获取已包装商品列表第一条数据商品编码的文本
        :return: '已包装商品列表第一条数据商品编码'的文本
        """
        control_content = self.project.get_element_text(self.first_list_packed_product_code_text)
        return control_content

    def get_first_list_packed_product_name_text_action(self):
        """
        动作：获取已包装商品列表第一条数据商品名称的文本
        :return: '已包装商品列表第一条数据商品名称'的文本
        """
        control_content = self.project.get_element_text(self.first_list_packed_product_name_text)
        return control_content

    def click_first_list_packed_product_name_button_action(self):
        """
        动作：点击已包装商品列表第一条数据商品名称点击
        :return: 点击'已包装商品列表第一条数据商品名称点击'按钮后的页面
        """
        self.project.click(self.first_list_packed_product_name_button)
        return self.project.get_current_page_source()

    def get_first_list_packed_product_service_id_text_action(self):
        """
        动作：获取已包装商品列表第一条数据服务编码的文本
        :return: '已包装商品列表第一条数据服务编码'的文本
        """
        control_content = self.project.get_element_text(self.first_list_packed_product_service_id_text)
        return control_content

    def get_first_list_packed_product_service_name_text_action(self):
        """
        动作：获取已包装商品列表第一条数据服务名称的文本
        :return: '已包装商品列表第一条数据服务名称'的文本
        """
        control_content = self.project.get_element_text(self.first_list_packed_product_service_name_text)
        return control_content

    def get_first_list_packed_product_service_country_place_text_action(self):
        """
        动作：获取已包装商品列表第一条数据所属国家及地区的文本
        :return: '已包装商品列表第一条数据所属国家及地区'的文本
        """
        control_content = self.project.get_element_text(self.first_list_packed_product_service_country_place_text)
        return control_content

    def get_first_list_packed_product_price_text_action(self):
        """
        动作：获取已包装商品列表第一条数据商品价格的文本
        :return: '已包装商品列表第一条数据商品价格'的文本
        """
        control_content = self.project.get_element_text(self.first_list_packed_product_price_text)
        return control_content

    def get_first_list_packed_product_audit_state_text_action(self):
        """
        动作：获取已包装商品列表第一条数据审核状态的文本
        :return: '已包装商品列表第一条数据审核状态'的文本
        """
        control_content = self.project.get_element_text(self.first_list_packed_product_audit_state_text)
        return control_content

    def get_first_list_packed_product_upper_state_text_action(self):
        """
        动作：获取已包装商品列表第一条数据上架状态的文本
        :return: '已包装商品列表第一条数据上架状态'的文本
        """
        control_content = self.project.get_element_text(self.first_list_packed_product_upper_state_text)
        return control_content

    def click_first_list_packed_product_hide_button_action(self):
        """
        动作：点击已包装商品列表第一条数据操作前台隐藏
        :return: 点击'已包装商品列表第一条数据操作前台隐藏'按钮后的页面
        """
        self.project.click(self.first_list_packed_product_hide_button)
        return self.project.get_current_page_source()

    def get_first_list_packed_product_hide_text_action(self):
        """
        动作：获取已包装商品列表第一条数据操作前台隐藏文案的文本
        :return: '已包装商品列表第一条数据操作前台隐藏文案'的文本
        """
        control_content = self.project.get_element_text(self.first_list_packed_product_hide_text)
        return control_content

    def click_first_list_packed_product_hide_commit_button_action(self):
        """
        动作：点击已包装商品列表第一条数据操作前台隐藏确认
        :return: 点击'已包装商品列表第一条数据操作前台隐藏确认'按钮后的页面
        """
        self.project.click(self.first_list_packed_product_hide_commit_button)
        return self.project.get_current_page_source()

    def click_first_list_packed_product_edit_button_action(self):
        """
        动作：点击已包装商品列表第一条数据操作修改
        :return: 点击'已包装商品列表第一条数据操作修改'按钮后的页面
        """
        self.project.click(self.first_list_packed_product_edit_button)
        return self.project.get_current_page_source()

    def click_first_list_packed_product_associate_button_action(self):
        """
        动作：点击已包装商品列表第一条数据操作关联商品
        :return: 点击'已包装商品列表第一条数据操作关联商品'按钮后的页面
        """
        self.project.click(self.first_list_packed_product_associate_button)
        return self.project.get_current_page_source()

    def click_first_list_packed_product_copy_button_action(self):
        """
        动作：点击已包装商品列表第一条数据操作复制
        :return: 点击'已包装商品列表第一条数据操作复制'按钮后的页面
        """
        self.project.click(self.first_list_packed_product_copy_button)
        return self.project.get_current_page_source()

    def get_first_list_packed_product_no_data_text_action(self):
        """
        动作：获取已包装商品列表无数据文本的文本
        :return: '已包装商品列表无数据文本'的文本
        """
        control_content = self.project.get_element_text(self.first_list_packed_product_no_data_text)
        return control_content

    def click_first_list_draft_product_delete_button_action(self):
        """
        动作：点击草稿箱商品列表第一条数据操作删除
        :return: 点击'草稿箱商品列表第一条数据操作删除'按钮后的页面
        """
        self.project.click(self.first_list_draft_product_delete_button)
        return self.project.get_current_page_source()

    def click_first_list_draft_product_delete_commit_button_action(self):
        """
        动作：点击草稿箱商品列表第一条数据删除确认
        :return: 点击'草稿箱商品列表第一条数据删除确认'按钮后的页面
        """
        self.project.click(self.first_list_draft_product_delete_commit_button)
        return self.project.get_current_page_source()

    def click_search_product_draft_button_action(self):
        """
        动作：点击草稿箱按钮
        :return: 点击'草稿箱按钮'按钮后的页面
        """
        self.project.click(self.search_product_draft_button)
        return self.project.get_current_page_source()

    def get_first_list_draft_product_id_text_action(self):
        """
        动作：获取草稿箱商品列表第一条数据商品编码的文本
        :return: '草稿箱商品列表第一条数据商品编码'的文本
        """
        control_content = self.project.get_element_text(self.first_list_draft_product_id_text)
        return control_content

    def get_first_list_draft_product_name_text_action(self):
        """
        动作：获取草稿箱商品列表第一条数据服务名称的文本
        :return: '草稿箱商品列表第一条数据服务名称'的文本
        """
        control_content = self.project.get_element_text(self.first_list_draft_product_name_text)
        return control_content

    def click_first_list_draft_product_name_button_action(self):
        """
        动作：点击草稿箱商品列表第一条数据商品名称点击
        :return: 点击'草稿箱商品列表第一条数据商品名称点击'按钮后的页面
        """
        self.project.click(self.first_list_draft_product_name_button)
        return self.project.get_current_page_source()

    def get_first_list_draft_product_service_id_text_action(self):
        """
        动作：获取草稿箱商品列表第一条数据服务编码的文本
        :return: '草稿箱商品列表第一条数据服务编码'的文本
        """
        control_content = self.project.get_element_text(self.first_list_draft_product_service_id_text)
        return control_content

    def get_first_list_draft_product_service_name_text_action(self):
        """
        动作：获取草稿箱商品列表第一条数据服务名称的文本
        :return: '草稿箱商品列表第一条数据服务名称'的文本
        """
        control_content = self.project.get_element_text(self.first_list_draft_product_service_name_text)
        return control_content

    def get_first_list_draft_product_service_country_place_text_action(self):
        """
        动作：获取草稿箱商品列表第一条数据所属国家及地区的文本
        :return: '草稿箱商品列表第一条数据所属国家及地区'的文本
        """
        control_content = self.project.get_element_text(self.first_list_draft_product_service_country_place_text)
        return control_content

    def get_first_list_draft_product_price_text_action(self):
        """
        动作：获取草稿箱商品列表第一条数据商品价格的文本
        :return: '草稿箱商品列表第一条数据商品价格'的文本
        """
        control_content = self.project.get_element_text(self.first_list_draft_product_price_text)
        return control_content

    def click_first_list_draft_product_pack_button_action(self):
        """
        动作：点击草稿箱商品列表第一条数据操作包装
        :return: 点击'草稿箱商品列表第一条数据操作包装'按钮后的页面
        """
        self.project.click(self.first_list_draft_product_pack_button)
        return self.project.get_current_page_source()

    def click_first_list_draft_product_pack_button_action(self):
        """
        动作：点击草稿箱商品列表第一条数据操作删除
        :return: 点击'草稿箱商品列表第一条数据操作删除'按钮后的页面
        """
        self.project.click(self.first_list_draft_product_pack_button)
        return self.project.get_current_page_source()

    def click_first_list_draft_product_delete_button_action(self):
        """
        动作：点击草稿箱商品列表第一条数据操作删除
        :return: 点击'草稿箱商品列表第一条数据操作删除'按钮后的页面
        """
        self.project.click(self.first_list_draft_product_delete_button)
        return self.project.get_current_page_source()

    def click_first_list_draft_product_delete_commit_button_action(self):
        """
        动作：点击草稿箱商品列表第一条数据删除确认
        :return: 点击'草稿箱商品列表第一条数据删除确认'按钮后的页面
        """
        self.project.click(self.first_list_draft_product_delete_commit_button)
        return self.project.get_current_page_source()

    def get_first_list_draft_product_no_data_text_action(self):
        """
        动作：获取草稿箱列表无数据文本的文本
        :return: '草稿箱列表无数据文本'的文本
        """
        control_content = self.project.get_element_text(self.first_list_draft_product_no_data_text)
        return control_content

    def click_product_pack_service_button_action(self):
        """
        动作：点击商品包装组合服务选择
        :return: 点击'商品包装组合服务选择'按钮后的页面
        """
        self.project.click(self.product_pack_service_button)
        return self.project.get_current_page_source()

    def set_product_pack_service_id_input_action(self, product_pack_service_id_input):
        """
        动作：设置商品包装组合服务服务编码查询
        :param product_pack_service_id_input: 商品包装组合服务服务编码查询
        :return: 设置'商品包装组合服务服务编码查询'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_service_id_input, product_pack_service_id_input)
        return self.project.get_current_page_source()

    def set_product_pack_service_name_input_action(self, product_pack_service_name_input):
        """
        动作：设置商品包装组合服务服务名称查询
        :param product_pack_service_name_input: 商品包装组合服务服务名称查询
        :return: 设置'商品包装组合服务服务名称查询'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_service_name_input, product_pack_service_name_input)
        return self.project.get_current_page_source()

    def get_select_product_pack_service_country_list_action(self, product_pack_service_country_list_select):
        """
        动作：获取商品包装组合服务所属国家及地区列表选中的文本
        :param product_pack_service_country_list_select: 商品包装组合服务所属国家及地区列表索引或文本
        :return: '商品包装组合服务所属国家及地区'的文本
        """
        control_content = self.project.get_select_content(self.product_pack_service_country_list_select, product_pack_service_country_list_select)
        return control_content

    def select_product_pack_service_country_list_action(self, product_pack_service_country_list_select):
        """
        动作：选择商品包装组合服务所属国家及地区
        :param product_pack_service_country_list_select: 商品包装组合服务所属国家及地区列表索引或文本
        :return: 选择'商品包装组合服务所属国家及地区'选择器后的页面
        """
        self.project.select_control(self.product_pack_service_country_list_select, product_pack_service_country_list_select)
        return self.project.get_current_page_source()

    def click_product_pack_service_country_all_button_action(self):
        """
        动作：点击商品包装组合服务所属国家及地区全部
        :return: 点击'商品包装组合服务所属国家及地区全部'按钮后的页面
        """
        self.project.click(self.product_pack_service_country_all_button)
        return self.project.get_current_page_source()

    def click_product_pack_service_country_america_button_action(self):
        """
        动作：点击商品包装组合服务所属国家及地区美国
        :return: 点击'商品包装组合服务所属国家及地区美国'按钮后的页面
        """
        self.project.click(self.product_pack_service_country_america_button)
        return self.project.get_current_page_source()

    def click_product_pack_service_search_button_action(self):
        """
        动作：点击商品包装组合服务查询
        :return: 点击'商品包装组合服务查询'按钮后的页面
        """
        self.project.click(self.product_pack_service_search_button)
        return self.project.get_current_page_source()

    def click_product_pack_service_clear_button_action(self):
        """
        动作：点击商品包装组合服务重置
        :return: 点击'商品包装组合服务重置'按钮后的页面
        """
        self.project.click(self.product_pack_service_clear_button)
        return self.project.get_current_page_source()

    def get_first_list_product_pack_service_id_text_action(self):
        """
        动作：获取商品包装组合服务第一条数据服务编码的文本
        :return: '商品包装组合服务第一条数据服务编码'的文本
        """
        control_content = self.project.get_element_text(self.first_list_product_pack_service_id_text)
        return control_content

    def get_first_list_product_pack_service_name_text_action(self):
        """
        动作：获取商品包装组合服务第一条数据服务名称的文本
        :return: '商品包装组合服务第一条数据服务名称'的文本
        """
        control_content = self.project.get_element_text(self.first_list_product_pack_service_name_text)
        return control_content

    def get_first_list_product_pack_service_country_text_action(self):
        """
        动作：获取商品包装组合服务第一条数据所属国家和地区的文本
        :return: '商品包装组合服务第一条数据所属国家和地区'的文本
        """
        control_content = self.project.get_element_text(self.first_list_product_pack_service_country_text)
        return control_content

    def click_first_list_product_pack_service_pack_button_action(self):
        """
        动作：点击商品包装组合服务第一条数据包装
        :return: 点击'商品包装组合服务第一条数据包装'按钮后的页面
        """
        self.project.click(self.first_list_product_pack_service_pack_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_name_input_action(self, product_pack_product_name_input):
        """
        动作：设置商品包装基本信息商品名称
        :param product_pack_product_name_input: 商品包装基本信息商品名称
        :return: 设置'商品包装基本信息商品名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_name_input, product_pack_product_name_input)
        return self.project.get_current_page_source()

    def get_product_service_content_all_price_text_action(self):
        """
        动作：获取商品服务内容合计价格的文本
        :return: '商品服务内容合计价格'的文本
        """
        control_content = self.project.get_element_text(self.product_service_content_all_price_text)
        return control_content

    def set_product_pack_product_price_input_action(self, product_pack_product_price_input):
        """
        动作：设置商品包装基本信息商品价格
        :param product_pack_product_price_input: 商品包装基本信息商品价格
        :return: 设置'商品包装基本信息商品价格'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_price_input, product_pack_product_price_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_price_display_button_action(self):
        """
        动作：点击商品服务内容合计价格作为划线价展示在前台
        :return: 点击'商品服务内容合计价格作为划线价展示在前台'按钮后的页面
        """
        self.project.click(self.product_pack_product_price_display_button)
        return self.project.get_current_page_source()

    def click_product_pack_product_price_undisplay_button_action(self):
        """
        动作：点击商品服务内容合计价格作为划线价不展示在前台
        :return: 点击'商品服务内容合计价格作为划线价不展示在前台'按钮后的页面
        """
        self.project.click(self.product_pack_product_price_undisplay_button)
        return self.project.get_current_page_source()

    def click_product_pack_product_lable_preference_button_action(self):
        """
        动作：点击商品包装基本信息商品标签优选
        :return: 点击'商品包装基本信息商品标签优选'按钮后的页面
        """
        self.project.click(self.product_pack_product_lable_preference_button)
        return self.project.get_current_page_source()

    def click_product_pack_product_lable_popularity_button_action(self):
        """
        动作：点击商品包装基本信息商品标签人气
        :return: 点击'商品包装基本信息商品标签人气'按钮后的页面
        """
        self.project.click(self.product_pack_product_lable_popularity_button)
        return self.project.get_current_page_source()

    def click_product_pack_product_lable_characteristic_button_action(self):
        """
        动作：点击商品包装基本信息商品标签特色
        :return: 点击'商品包装基本信息商品标签特色'按钮后的页面
        """
        self.project.click(self.product_pack_product_lable_characteristic_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_usp_input_action(self, product_pack_product_usp_input):
        """
        动作：设置商品包装基本信息商品卖点
        :param product_pack_product_usp_input: 商品包装基本信息商品卖点
        :return: 设置'商品包装基本信息商品卖点'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_usp_input, product_pack_product_usp_input)
        return self.project.get_current_page_source()

    def set_product_pack_product_refund_input_action(self, product_pack_product_refund_input):
        """
        动作：设置商品包装基本信息退款说明
        :param product_pack_product_refund_input: 商品包装基本信息退款说明
        :return: 设置'商品包装基本信息退款说明'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_refund_input, product_pack_product_refund_input)
        return self.project.get_current_page_source()

    def set_product_pack_product_terms_input_action(self, product_pack_product_terms_input):
        """
        动作：设置商品包装基本信息专项条款
        :param product_pack_product_terms_input: 商品包装基本信息专项条款
        :return: 设置'商品包装基本信息专项条款'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_terms_input, product_pack_product_terms_input)
        return self.project.get_current_page_source()

    def set_product_pack_product_first_key_input_action(self, product_pack_product_first_key_input):
        """
        动作：设置商品包装基本信息搜索关键词1
        :param product_pack_product_first_key_input: 商品包装基本信息搜索关键词1
        :return: 设置'商品包装基本信息搜索关键词1'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_first_key_input, product_pack_product_first_key_input)
        return self.project.get_current_page_source()

    def set_product_pack_product_second_key_input_action(self, product_pack_product_second_key_input):
        """
        动作：设置商品包装基本信息搜索关键词2
        :param product_pack_product_second_key_input: 商品包装基本信息搜索关键词2
        :return: 设置'商品包装基本信息搜索关键词2'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_second_key_input, product_pack_product_second_key_input)
        return self.project.get_current_page_source()

    def set_product_pack_product_third_key_input_action(self, product_pack_product_third_key_input):
        """
        动作：设置商品包装基本信息搜索关键词3
        :param product_pack_product_third_key_input: 商品包装基本信息搜索关键词3
        :return: 设置'商品包装基本信息搜索关键词3'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_third_key_input, product_pack_product_third_key_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_first_image_button_action(self):
        """
        动作：点击商品包装基本信息主图1
        :return: 点击'商品包装基本信息主图1'按钮后的页面
        """
        self.project.click(self.product_pack_product_first_image_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_first_image_upload_input_action(self, product_pack_product_first_image_upload_input):
        """
        动作：设置商品包装基本信息主图1上传
        :param product_pack_product_first_image_upload_input: 商品包装基本信息主图1上传
        :return: 设置'商品包装基本信息主图1上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_first_image_upload_input, product_pack_product_first_image_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_second_image_button_action(self):
        """
        动作：点击商品包装基本信息主图2
        :return: 点击'商品包装基本信息主图2'按钮后的页面
        """
        self.project.click(self.product_pack_product_second_image_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_second_image_upload_input_action(self, product_pack_product_second_image_upload_input):
        """
        动作：设置商品包装基本信息主图2上传
        :param product_pack_product_second_image_upload_input: 商品包装基本信息主图2上传
        :return: 设置'商品包装基本信息主图2上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_second_image_upload_input, product_pack_product_second_image_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_third_image_button_action(self):
        """
        动作：点击商品包装基本信息主图3
        :return: 点击'商品包装基本信息主图3'按钮后的页面
        """
        self.project.click(self.product_pack_product_third_image_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_third_image_upload_input_action(self, product_pack_product_third_image_upload_input):
        """
        动作：设置商品包装基本信息主图3上传
        :param product_pack_product_third_image_upload_input: 商品包装基本信息主图3上传
        :return: 设置'商品包装基本信息主图3上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_third_image_upload_input, product_pack_product_third_image_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_third_image_button_action(self):
        """
        动作：点击商品包装基本信息主图4
        :return: 点击'商品包装基本信息主图4'按钮后的页面
        """
        self.project.click(self.product_pack_product_third_image_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_third_image_upload_input_action(self, product_pack_product_third_image_upload_input):
        """
        动作：设置商品包装基本信息主图4上传
        :param product_pack_product_third_image_upload_input: 商品包装基本信息主图4上传
        :return: 设置'商品包装基本信息主图4上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_third_image_upload_input, product_pack_product_third_image_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_third_image_button_action(self):
        """
        动作：点击商品包装基本信息主图5
        :return: 点击'商品包装基本信息主图5'按钮后的页面
        """
        self.project.click(self.product_pack_product_third_image_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_third_image_upload_input_action(self, product_pack_product_third_image_upload_input):
        """
        动作：设置商品包装基本信息主图5上传
        :param product_pack_product_third_image_upload_input: 商品包装基本信息主图5上传
        :return: 设置'商品包装基本信息主图5上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_third_image_upload_input, product_pack_product_third_image_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_video_button_action(self):
        """
        动作：点击商品包装基本信息视频
        :return: 点击'商品包装基本信息视频'按钮后的页面
        """
        self.project.click(self.product_pack_product_video_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_video_upload_input_action(self, product_pack_product_video_upload_input):
        """
        动作：设置商品包装基本信息视频上传
        :param product_pack_product_video_upload_input: 商品包装基本信息视频上传
        :return: 设置'商品包装基本信息视频上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_video_upload_input, product_pack_product_video_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_feed_image_button_action(self):
        """
        动作：点击商品包装基本信息feed流图片
        :return: 点击'商品包装基本信息feed流图片'按钮后的页面
        """
        self.project.click(self.product_pack_product_feed_image_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_feed_image_upload_input_action(self, product_pack_product_feed_image_upload_input):
        """
        动作：设置商品包装基本信息feed流图片上传
        :param product_pack_product_feed_image_upload_input: 商品包装基本信息feed流图片上传
        :return: 设置'商品包装基本信息feed流图片上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_feed_image_upload_input, product_pack_product_feed_image_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_other_ensue_refund_button_action(self):
        """
        动作：点击商品包装其他信息服务退款保障
        :return: 点击'商品包装其他信息服务退款保障'按钮后的页面
        """
        self.project.click(self.product_pack_other_ensue_refund_button)
        return self.project.get_current_page_source()

    def click_product_pack_other_ensue_platform_button_action(self):
        """
        动作：点击商品包装其他信息服务平台保障
        :return: 点击'商品包装其他信息服务平台保障'按钮后的页面
        """
        self.project.click(self.product_pack_other_ensue_platform_button)
        return self.project.get_current_page_source()

    def click_product_pack_other_ensue_service_button_action(self):
        """
        动作：点击商品包装其他信息服务服务流程
        :return: 点击'商品包装其他信息服务服务流程'按钮后的页面
        """
        self.project.click(self.product_pack_other_ensue_service_button)
        return self.project.get_current_page_source()

    def set_product_pack_other_first_question_input_action(self, product_pack_other_first_question_input):
        """
        动作：设置商品包装其他信息服务常见问题1
        :param product_pack_other_first_question_input: 商品包装其他信息服务常见问题1
        :return: 设置'商品包装其他信息服务常见问题1'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_other_first_question_input, product_pack_other_first_question_input)
        return self.project.get_current_page_source()

    def set_product_pack_other_first_question_answer_input_action(self, product_pack_other_first_question_answer_input):
        """
        动作：设置商品包装其他信息服务常见问题1回答
        :param product_pack_other_first_question_answer_input: 商品包装其他信息服务常见问题1回答
        :return: 设置'商品包装其他信息服务常见问题1回答'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_other_first_question_answer_input, product_pack_other_first_question_answer_input)
        return self.project.get_current_page_source()

    def click_product_pack_other_first_question_add_button_action(self):
        """
        动作：点击商品包装其他信息服务常见问题添加
        :return: 点击'商品包装其他信息服务常见问题添加'按钮后的页面
        """
        self.project.click(self.product_pack_other_first_question_add_button)
        return self.project.get_current_page_source()

    def set_product_pack_other_second_question_input_action(self, product_pack_other_second_question_input):
        """
        动作：设置商品包装其他信息服务常见问题2
        :param product_pack_other_second_question_input: 商品包装其他信息服务常见问题2
        :return: 设置'商品包装其他信息服务常见问题2'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_other_second_question_input, product_pack_other_second_question_input)
        return self.project.get_current_page_source()

    def set_product_pack_other_second_question_answer_input_action(self, product_pack_other_second_question_answer_input):
        """
        动作：设置商品包装其他信息服务常见问题2回答
        :param product_pack_other_second_question_answer_input: 商品包装其他信息服务常见问题2回答
        :return: 设置'商品包装其他信息服务常见问题2回答'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_other_second_question_answer_input, product_pack_other_second_question_answer_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_detail_image_button_action(self):
        """
        动作：点击商品包装商品详情详情图
        :return: 点击'商品包装商品详情详情图'按钮后的页面
        """
        self.project.click(self.product_pack_product_detail_image_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_detail_image_upload_input_action(self, product_pack_product_detail_image_upload_input):
        """
        动作：设置商品包装商品详情详情图上传
        :param product_pack_product_detail_image_upload_input: 商品包装商品详情详情图上传
        :return: 设置'商品包装商品详情详情图上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_detail_image_upload_input, product_pack_product_detail_image_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_contract_button_action(self):
        """
        动作：点击商品包装附件合同
        :return: 点击'商品包装附件合同'按钮后的页面
        """
        self.project.click(self.product_pack_product_contract_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_contract_upload_input_action(self, product_pack_product_contract_upload_input):
        """
        动作：设置商品包装附件合同上传
        :param product_pack_product_contract_upload_input: 商品包装附件合同上传
        :return: 设置'商品包装附件合同上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_contract_upload_input, product_pack_product_contract_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_prview_button_action(self):
        """
        动作：点击商品包装预览
        :return: 点击'商品包装预览'按钮后的页面
        """
        self.project.click(self.product_pack_product_prview_button)
        return self.project.get_current_page_source()

    def click_product_pack_product_save_button_action(self):
        """
        动作：点击商品包装保存
        :return: 点击'商品包装保存'按钮后的页面
        """
        self.project.click(self.product_pack_product_save_button)
        return self.project.get_current_page_source()

    def click_product_pack_product_submit_button_action(self):
        """
        动作：点击商品包装提交审核
        :return: 点击'商品包装提交审核'按钮后的页面
        """
        self.project.click(self.product_pack_product_submit_button)
        return self.project.get_current_page_source()

    # endregion Actions
