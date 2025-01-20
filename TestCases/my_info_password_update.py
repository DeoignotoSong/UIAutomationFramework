from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.UserCenterPage import UserCenterPage
from Projects.Android.Pages.Common.MyInfoPage import MyInfoPage
from Projects.Android.Pages.Common.UserLoginRegisterPage import UserLoginRegisterPage
from Projects.Android.Pages.Common.UpdatePasswordPage import UpdatePasswordPage
from ..TestCases.security_verify_operation import security_verify_operation


@test_case
def my_info_password_update(*args, **kwargs):
    """
    我的页面-我的资料-密码修改
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
    修改密码
    '''
    project.wait_until(my_info_page._my_psw_button_tag)
    # 点击设置密码
    my_info_page.click_my_psw_button_action()
    update_password_page = UpdatePasswordPage(project)
    # 点击获取验证码
    update_password_page.click_get_code_button_action()
    # 滑动安全验证图片
    result = security_verify_operation(*args, **kwargs)
    # 输入验证码
    update_password_page.psw_change_code.send_keys(result['message'])
    # 输入密码
    update_password_page.psw_change_new1.send_keys('t11111111')
    # 点检完成
    update_password_page.click_submit_button_action()
    # 登录页面展示
    user_login = UserLoginRegisterPage(project)
    # 等待页面展示
    project.wait_until(user_login._closed_button_tag)
    # 关闭登录页面
    user_login.click_closed_button_action()
