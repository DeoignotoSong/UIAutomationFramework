from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.HomePage import HomePage
from Projects.Android.Pages.Common.QAHomePage import QAHomePage
from Projects.Android.Pages.Common.UserLoginRegisterPage import UserLoginRegisterPage
from Projects.Android.Pages.Common.PutForwardQuestionPage import PutForwardQuestionPage
from Projects.Android.Pages.Common.QuestionChoiceTabPage import QuestionChoiceTabPage
from Projects.Android.Pages.Common.SettingRewardQuestionPage import SettingRewardQuestionPage
from ..TestCases.user_login import user_login


@test_case
def put_forward_question(*args, **kwargs):
    """
    我的页面-签到
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    home_page = HomePage(project)
    # 点击问答
    home_page.click_footer_nav_qa_button_action()
    QA_home_page = QAHomePage(project)
    # 点击提出问题button
    QA_home_page.click_question_ask_button_action()
    # 判断是否已经登录
    user_login_page = UserLoginRegisterPage(project)
    if project.element_is_exist(user_login_page._password_login_button_tag):
        user_login_page.click_closed_button_action()
        user_login(*args, **kwargs)
        # 点击问答
        home_page.click_footer_nav_qa_button_action()
        # 点击提出问题button
        QA_home_page.click_question_ask_button_action()
    # 发起提问
    put_forward_question_page = PutForwardQuestionPage(project)
    import time
    question_title = str(time.time()).replace('.', '')
    put_forward_question_page.question_title_text.send_keys(question_title)
    put_forward_question_page.question_content_text.send_keys('自动化测试-内容-{}'.format(question_title))
    # 点击下一步
    put_forward_question_page.click_next_button_action()
    # 选择标签
    question_choice_tab = QuestionChoiceTabPage(project)
    # 选择标题
    question_choice_tab.click_tv_tab_title_button_action()
    # 点击一级标签
    question_choice_tab.click_one_level_first_button_action()
    # 点击二级标签
    question_choice_tab.click_two_level_second_button_action()
    # 点击下一步
    question_choice_tab.click_next_button_action()
    # 选择主题内容
    question_choice_tab.click_theme_level_second_button_action()
    # 点击下一步
    question_choice_tab.click_next_button_action()
    setting_reward_question = SettingRewardQuestionPage(project)
    # 点击不悬赏直接提问
    setting_reward_question.click_show_question_button_action()
    project.wait_until(home_page._footer_nav_qa_button_tag)
    result = {
        'question_title': question_title
    }
    return result



