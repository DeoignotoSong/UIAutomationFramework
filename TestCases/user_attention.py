from Core.Decorator import test_case
from Projects.Android.Pages.Common.UserHomePage import UserHomePage
from Projects.Android.Pages.Common.WechatPersonalDetailPage import WechatPersonalDetailPage


@test_case()
def user_attention(*args, **kwargs):
    """
    个人主页-关注用户
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    we_chat_personal_detail = WechatPersonalDetailPage(project)
    # 等待元素出现
    project.wait_until(we_chat_personal_detail._homepage_button_tag)
    # 点击个人主页
    we_chat_personal_detail.click_homepage_button_action()
    user_home_page = UserHomePage(project)
    """
    个人主页关注按钮为Icon,无法获取图片文字,无法判断点击后结果是否关注。
    解决方案：
    1）通过图片识别判断是否已经关注
    2）通过查库，判断点击后状态是否关注
    3）根据当前页粉丝数量变化，判断是否为关注
    
    本场景，通过粉丝数量变化判断是否未关注
    """
    # 等待元素出现
    project.wait_until(user_home_page._user_fans_count_tag)
    # 记录当前粉丝数量
    click_before_count = user_home_page.user_fans_count.get_attribute('text')
    # 点击关注
    user_home_page.click_user_focus_button_action()
    import time
    time.sleep(2)
    click_after_count = user_home_page.user_fans_count.get_attribute('text')
    # 点击后数量小于点击前数量，则为取消关注
    if click_after_count < click_before_count:
        # 点击关注
        user_home_page.click_user_focus_button_action()
