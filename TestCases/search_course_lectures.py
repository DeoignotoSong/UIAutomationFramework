from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.SearchPage import SearchPage
from Projects.Android.Pages.Common.SearchResultPage import SearchResultPage
from Projects.Android.Pages.Common.HomePage import HomePage
from Projects.Android.Pages.Common.CourseDetailPage import CourseDetailPage
from Projects.Android.Pages.Common.App404InvalidateResourcePage import App404InvalidateResourcePage


@test_case
def search_course_lectures(*args, **kwargs):
    """
    综合搜索-搜索讲座-讲座详情
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    home_page = HomePage(project)
    home_page.click_search_bar_button_action()
    search_page = SearchPage(project)
    keywords = kwargs["search_content"]
    project.driver.find_element_by_xpath(xpath=search_page._search_bar_button_tag).send_keys(keywords)
    # 点击搜索
    search_page.click_search_button_action()
    search_result_page = SearchResultPage(project)
    # 点击找讲座
    search_result_page.click_search_result_lecture_button_action()
    # 等待搜索结果出现
    project.wait_until(search_result_page._search_result_class_button_tag)
    # 点击开播时间，按照开播时间从近期到过去
    search_result_page.click_begin_time_button_action()
    # 等待搜索结果出现
    project.wait_until(search_result_page._search_result_lecture_title_text_tag)
    titles = project.driver.find_elements_by_xpath(search_result_page._search_result_lecture_title_text_tag)
    course_name = titles[0].get_attribute('text')
    for title in titles:
        title.click()
        app_404_invalidate_resource = App404InvalidateResourcePage(project)
        if not project.element_is_exist(app_404_invalidate_resource._prompt_error_info_tag, timeout=2):
            break
        app_404_invalidate_resource.click_back_button_action()
    course_detail_page = CourseDetailPage(project)
    # 等待搜索结果出现
    project.wait_until(course_detail_page._course_detail_title_text_tag)
    return {
        "course_name": course_name
    }
