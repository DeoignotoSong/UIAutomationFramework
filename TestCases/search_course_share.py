from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.SearchPage import SearchPage
from Projects.Android.Pages.Common.SearchResultPage import SearchResultPage
from Projects.Android.Pages.Common.HomePage import HomePage
from Projects.Android.Pages.Common.CourseDetailPage import CourseDetailPage
from Projects.Android.Pages.Common.AppCommonDialogPage import AppCommonDialogPage


@test_case
def search_course_share(*args, **kwargs):
    """
    综合搜索-搜索课程-分享
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    home_page = HomePage(project)
    home_page.click_search_bar_button_action()
    search_page = SearchPage(project)
    keywords = kwargs["search_content"]
    project.get_element(value=search_page._search_bar_button_tag).send_keys(keywords)
    # 点击搜索
    search_page.click_search_button_action()
    search_result_page = SearchResultPage(project)
    # 点击课程
    search_result_page.click_search_result_class_button_action()
    # 等待搜课程索结果出现
    project.wait_until(search_result_page._search_result_course_title_text_tag)
    courses = project.driver.find_elements_by_xpath(search_result_page._search_result_course_title_text_tag)
    # 点击第一条结果
    courses[0].click()
    course_page = CourseDetailPage(project)
    # 等待搜索结果出现
    project.wait_until(course_page._course_shared_button_tag)
    # 点击右上角option
    course_page.click_course_shared_button_action()
    # 点击分享默认最近的第一个好友
    project.wait_until(course_page._recent_charts_button_tag)
    course_page.click_recent_charts_button_action()
    app_common_dialog = AppCommonDialogPage(project)
    project.wait_until(app_common_dialog._shared_send_button_tag)
    # 点击发送按钮
    app_common_dialog.click_shared_send_button_action()
