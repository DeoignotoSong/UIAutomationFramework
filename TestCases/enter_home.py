from Core.Decorator import test_case
from Projects.Android.Pages.Common.SystemDialogPage import SystemDialogPage
from Projects.Android.Pages.Common.FirstStartPromptPage import FirstStartPromptPage
from Projects.Android.Pages.Common.ImmediatelyExperiencePage import ImmediatelyExperiencePage
from Projects.Android.Pages.Common.GuideModalsPage import GuideModalsPage
from Projects.Android.Pages.Common.AppCommonDialogPage import AppCommonDialogPage
from Projects.Android.Pages.Common.UserLoginRegisterPage import UserLoginRegisterPage


@test_case()
def enter_home(*args, **kwargs):
    """
    进入首页
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    app_common_dialog = AppCommonDialogPage(project)
    if project.element_is_exist(app_common_dialog._version_close_button_tag):
        project.click(app_common_dialog.version_close_button)
    system_dialog = SystemDialogPage(project)
    # 判断是否noReset应用启动
    if project.element_is_exist(system_dialog._duration_allow_button_tag):
        system_dialog.click_duration_allow_button_action()
        system_dialog.click_all_allow_button_action()
        start_prompt = FirstStartPromptPage(project)
        start_prompt.click_agree_button_action()
        # 3次翻页
        for i in range(0, int(kwargs['count'])):
            project.swipe_screen((kwargs['x1'], kwargs['y1']), (kwargs['x2'], kwargs['y2']))
        immediately_experience = ImmediatelyExperiencePage(project)
        # 立即体验按钮
        immediately_experience.click_immediately_experience_button_action()

        '''
        2021.03.11 需求变更影响,回避首页默认弹出登录对话框Bug
        '''
        system_dialog = SystemDialogPage(project)
        if project.element_is_exist(system_dialog._all_allow_button_tag):
            # 点击始终允许
            system_dialog.click_all_allow_button_action()
        user_login_register_page = UserLoginRegisterPage(project)
        if project.element_is_exist(user_login_register_page._closed_button_tag):
            # 点击始终允许
            user_login_register_page.click_closed_button_action()
        if project.element_is_exist(user_login_register_page._closed_button_tag):
            # 点击始终允许
            user_login_register_page.click_closed_button_action()
        '''
        2021.03.11 需求变更影响,回避首页默认弹出登录对话框Bug
        '''
        if project.element_is_exist(app_common_dialog._version_close_button_tag):
            project.click(app_common_dialog.version_close_button)
        if project.element_is_exist(app_common_dialog._ad_close_button_tag):
            project.click(app_common_dialog.ad_close_button)
        guide_modals = GuideModalsPage(project)
        # 点击下一步
        guide_modals.click_next_button_action()
        # 点击我知道了
        guide_modals.click_i_know_button_action()
    else:
        app_common_dialog = AppCommonDialogPage(project)
        if project.element_is_exist(app_common_dialog._ad_close_button_tag):
            project.click(app_common_dialog.ad_close_button)
        app_common_dialog = AppCommonDialogPage(project)
        # 发现学习守护模式弹窗，点击我知道了
        if project.element_is_exist(app_common_dialog._i_know_text_tag):
            project.click(app_common_dialog.i_know_text)
