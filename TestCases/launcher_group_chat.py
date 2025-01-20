from Core.Decorator import test_case
from Projects.Android.Pages.Common.WechatHomePage import WechatHomePage
from Projects.Android.Pages.Common.ChoiceGroupMemberPage import ChoiceGroupMemberPage
from Projects.Android.Pages.Common.HomePage import HomePage
from Projects.Android.Pages.Common.WechatInnerPage import WechatInnerPage
from Core.Assert import Assert


@test_case()
def launcher_group_chat(*args, **kwargs):
    """
    发起群聊
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    home_page = HomePage(project)
    # 点击微聊
    home_page.click_footer_nav_chat_button_action()
    wechat_home = WechatHomePage(project)
    # 点击右上角option
    wechat_home.click_header_right_order_button_action()
    # 点击发起群聊
    wechat_home.click_grouper_button_action()
    # 选择发起群的成员
    choice_group_member = ChoiceGroupMemberPage(project)
    '''
    选择成员
    18118130511 -> 同学1f024c7a
    18129130408 -> 同学6c5625c0
    '''
    choice_group_member_xpath = "//*[@text='{}']"
    members = ["同学1f024c7a", "同学6c5625c0"]
    for member in members:
        project.driver.find_element_by_xpath(choice_group_member_xpath.format(member)).click()
    # 点击完成
    choice_group_member.click_header_right_button_action()
    wechat_inner_page = WechatInnerPage(project)
    project.wait_until(wechat_inner_page._group_num_tag)
    title = wechat_inner_page.header_center_title.get_attribute('text')
    group_num = wechat_inner_page.group_num.get_attribute('text')
    type = wechat_inner_page.session_type.get_attribute('text')
    Assert.is_equal(expected_value='Helloworld的群组', actual_value=title, position='')
    Assert.is_equal(expected_value='(3)', actual_value=group_num, position='')
    Assert.is_equal(expected_value='学友群', actual_value=type, position='')
