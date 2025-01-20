from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.SearchPage import SearchPage
from Projects.Android.Pages.Common.SearchResultPage import SearchResultPage
from Projects.Android.Pages.Common.HomePage import HomePage
from Projects.Android.Pages.Common.CourseDetailPage import CourseDetailPage
from appium.webdriver.common.touch_action import TouchAction


@test_case
def search_course(*args, **kwargs):
    """
    综合搜索-搜索课程-课程详情
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
    # 点击找课程
    search_result_page.click_search_result_class_button_action()
    # 等待搜索结果出现
    project.wait_until(search_result_page._search_result_class_button_tag)
    # 筛选课程类型
    search_result_page.click_search_result_search_sort_button_action()
    course_type = kwargs["course_type"]
    search_xpath = '//*[@text="{}"]'.format(course_type)
    if not project.element_is_exist(search_xpath, timeout=2):
        # 向上滑动操作
        TouchAction(project.driver).long_press(x=550, y=1200).move_to(x=550, y=600).release().perform()
    # 等待搜索结果出现
    project.wait_until(search_xpath)
    project.driver.find_element_by_xpath(xpath=search_xpath).click()
    # 点击确定按钮
    search_result_page.click_search_result_submit_button_action()
    # 点击价格，按照价格从低到高排序
    # search_result_page.click_price_button_action()
    # 等待搜索结果出现
    project.wait_until(search_result_page._search_result_course_title_text_tag)
    titles = project.driver.find_elements_by_xpath(search_result_page._search_result_course_title_text_tag)
    course_name = titles[0].get_attribute('text')
    # 点击第一条结果
    titles[0].click()
    # for title in titles:
    #     title.click()
    #     app_404_invalidate_resource = App404InvalidateResourcePage(project)
    #     if not project.element_is_exist(app_404_invalidate_resource._prompt_error_info_tag, timeout=2):
    #         break
    #     app_404_invalidate_resource.click_back_button_action()
    course_detail_page = CourseDetailPage(project)
    # 等待搜索结果出现
    project.wait_until(course_detail_page._course_detail_title_text_tag)
    return {
        "course_name": course_name
    }
