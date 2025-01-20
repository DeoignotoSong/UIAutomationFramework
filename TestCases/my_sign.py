from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.UserCenterPage import UserCenterPage
from Projects.Android.Pages.Common.AppCommonDialogPage import AppCommonDialogPage


@test_case
def my_sign(*args, **kwargs):
    """
    我的页面-签到
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    user_center_page = UserCenterPage(project)
    text = user_center_page.sign_text.get_attribute('text')
    # 点击签到
    user_center_page.click_sign_button_action()
    app_common_dialog_page = AppCommonDialogPage(project)
    if text == '每日签到':
        # 点击立即签到
        app_common_dialog_page.click_signed_button_action()
    # 关闭签到成功卡片
    app_common_dialog_page.click_share_close_button_action()

