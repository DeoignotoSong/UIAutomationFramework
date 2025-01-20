from Core.Decorator import test_case
from Projects.Android.Pages.Common.UserLoginRegisterPage import UserLoginRegisterPage
from Projects.Android.Pages.Common.HomePage import HomePage
from Projects.Android.Pages.Common.UserCenterPage import UserCenterPage
from Projects.Android.Pages.Common.GuideModalsPage import GuideModalsPage
from Projects.Android.Pages.Common.SystemDialogPage import SystemDialogPage
from Projects.Android.Pages.Common.AppCommonDialogPage import AppCommonDialogPage
from ..TestCases.security_verify_operation import security_verify_operation


@test_case()
def user_login(*args, **kwargs):
    """
    用户登录
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    home_page = HomePage(project)
    home_page.click_footer_nav_my_button_action()
    # 用户中心页面
    user_center_page = UserCenterPage(project)
    # 未登录状态-点击姓名处-弹出登录对话框
    project.click(user_center_page.login_username_text)
    '''
    2021.03.11 需求变更影响
    '''
    system_dialog = SystemDialogPage(project)
    if project.element_is_exist(system_dialog._all_allow_button_tag):
        # 点击始终允许
        system_dialog.click_all_allow_button_action()
    # 初始化
    user_login_register_page = UserLoginRegisterPage(project)
    project.wait_until(user_login_register_page._password_login_button_tag)
    user_login_register_page.click_password_login_button_action()
    # 输入账号用户名
    user_login_register_page.set_mobile_input_action(kwargs["mobile"])
    # 输入账号密码
    user_login_register_page.set_password_input_action(kwargs["password"])
    # 点击同意协议button
    user_login_register_page.click_agree_checkbox_button_action()
    # 点击登录按钮
    user_login_register_page.click_login_button_action()
    # 图片验证
    security_verify_operation(*args, **kwargs)
    # 判断是否存在用户指导蒙层
    guide_modals = GuideModalsPage(project)
    if project.element_is_exist(guide_modals._i_know_button_tag):
        project.click(guide_modals.i_know_button)
    app_common_dialog = AppCommonDialogPage(project)
    if project.element_is_exist(app_common_dialog._version_close_button_tag):
        project.click(app_common_dialog.version_close_button)
    # 登录用户名
    username = project.wait_until(user_center_page._login_username_text_tag)
    # 用户名文本
    username_text = username.get_attribute("text")
