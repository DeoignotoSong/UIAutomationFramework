from Core.Decorator import test_case
from ..Base.Android_2021 import ProjectBase
from Projects.Android.Pages.Common.UserCenterPage import UserCenterPage
from Projects.Android.Pages.Common.MyInfoPage import MyInfoPage
from Projects.Android.Pages.Common.BindThirdAccountPage import BindThirdAccountPage
from Projects.Android.Pages.Common.BindThirdAccountByMailPage import BindThirdAccountByMailPage
from Projects.Android.Pages.Common.IdentityVerifyPage import IdentityVerifyPage
from ..TestCases.security_verify_operation import security_verify_operation


@test_case
def my_info_email_update(*args, **kwargs):
    """
    我的页面-我的资料-修改邮箱
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: ProjectBase
    user_center_page = UserCenterPage(project)
    # 点击编辑资料
    user_center_page.click_edit_info_button_action()
    my_info_page = MyInfoPage(project)
    # 向上滑动
    project.swipe_screen((0.5, 0.6), (0.5, 0.4))
    '''
    修改邮箱
    '''
    project.wait_until(my_info_page._my_bind_third_button_tag)
    # 点击绑定第三方账号
    my_info_page.click_my_bind_third_button_action()
    bind_third_account = BindThirdAccountPage(project)
    # 点击邮箱
    bind_third_account.click_mail_button_action()
    identity_verify = IdentityVerifyPage(project)
    # 点击获取验证码
    identity_verify.click_get_code_button_action()
    # 安全验证操作
    result = security_verify_operation(*args, **kwargs)
    # 输入验证码
    identity_verify.psw_change_code.send_keys(result['message'])
    # 点击验证
    identity_verify.click_submit_button_action()
    bind_third_account_mail = BindThirdAccountByMailPage(project)
    # 等待页面初始化完成
    project.wait_until(bind_third_account_mail._input_mail_tag)
    # 输入邮箱
    bind_third_account_mail.input_mail.send_keys('test@jjl.com')
    # 点击绑定
    bind_third_account_mail.click_submit_button_action()
    project.wait_until(bind_third_account._mail_button_tag)
    # 点击返回
    bind_third_account.click_back_button_action()
    # 点击返回
    bind_third_account.click_back_button_action()
