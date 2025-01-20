from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.UserCenterPage import UserCenterPage
from Projects.Android.Pages.Common.MyInfoPage import MyInfoPage
from Projects.Android.Pages.Common.SystemPage import SystemPage
from Projects.Android.Pages.Common.AppCommonDialogPage import AppCommonDialogPage
from Projects.Android.Pages.Common.SystemDialogPage import SystemDialogPage
from Projects.Android.Pages.Common.MyNickSetingPage import MyNickSetingPage
from Projects.Android.Pages.Common.LocationInfoPage import LocationInfoPage


@test_case
def my_info_edit(*args, **kwargs):
    """
    我的页面-我的资料编辑
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    user_center_page = UserCenterPage(project)
    # 点击编辑资料
    user_center_page.click_edit_info_button_action()
    my_info_page = MyInfoPage(project)
    '''
    修改头像
    '''
    my_info_page.click_my_head_button_action()
    system_dialog = SystemDialogPage(project)
    if project.element_is_exist(system_dialog._all_allow_button_tag):
        system_dialog.click_all_allow_button_action()
    system_page = SystemPage(project)
    # 选中图片
    system_page.click_picture_second_button_action()
    # 点击已完成
    system_page.click_picture_tv_ok_button_action()
    # 点击裁剪
    system_page.click_menu_crop_button_action()
    # 等待loading对话框消失
    app_common_dialog = AppCommonDialogPage(project)
    '''
    修改我的昵称
    '''
    project.wait_until(my_info_page._my_exhibition_nick_button_tag)
    # 点击我的昵称
    my_info_page.click_my_exhibition_nick_button_action()
    my_nick_setting = MyNickSetingPage(project)
    project.wait_until(my_nick_setting._my_nick_input_tag)
    # 输入用户名
    my_nick_setting.my_nick_input.send_keys('Helloworld')
    # 点击确定
    my_nick_setting.click_my_next_button_action()
    '''
    修改位置信息
    '''
    project.wait_until(my_info_page._my_location_map_value_tag)
    # 获取当前位置
    location_value = my_info_page.my_location_map_value.get_attribute("text")
    # 点击位置信息
    my_info_page.click_my_location_map_button_action()
    location_info = LocationInfoPage(project)
    # 点击位置修改
    location_info.click_location_country_modify_button_action()
    if location_value == '阿富汗':
        # 点击阿尔巴尼亚
        location_info.click_arbny_button_action()
        location_value = '阿尔巴尼亚'
    else:
        # 点击阿富汗
        location_info.click_afh_button_action()
        location_value = '阿富汗'
    # 修改详细地址
    location_info.location_name.send_keys('自动化测试')
    # 点击提交
    location_info.click_submit_button_action()
    # Assert.is_equal(expected_value=location_value,
    #                 actual_value=my_info_page.my_location_map_value.get_attribute("text").replace("自动化测试", ""),
    #                 position='校验位置是否设置成功')
    project.wait_until(my_info_page._article_detail_back_button_tag)
    # 点击返回->我的页面
    my_info_page.click_article_detail_back_button_action()
