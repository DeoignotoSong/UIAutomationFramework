from Core.Decorator import test_case
from Projects.Android.Pages.Common.SearchPage import SearchPage
from Projects.Android.Pages.Common.SearchResultPage import SearchResultPage
from Projects.Android.Pages.Common.HomePage import HomePage
from Projects.Android.Pages.Common.ArticleDetailPage import ArticleDetailPage
from Projects.Android.Pages.Common.CourseDetailPage import CourseDetailPage
from Projects.Android.Pages.Common.CollegeDetailPage import CollegeDetailPage
from Core.Assert import Assert


@test_case()
def search(*args, **kwargs):
    """
    综合搜索
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    home_page = HomePage(project)
    home_page.click_search_bar_button_action()
    search_page = SearchPage(project)
    keywords = '留学'
    project.get_element(value=search_page._search_bar_button_tag).send_keys(keywords)
    # 点击搜索
    search_page.click_search_button_action()
    search_result_page = SearchResultPage(project)
    '''
    点击找文章
    '''
    search_result_page.click_search_result_article_button_action()
    # 等待搜索结果出现
    project.wait_until(search_result_page._search_result_title_text_tag)
    articles = project.driver.find_elements_by_xpath(search_result_page._search_result_title_text_tag)
    for article in articles:
        Assert.is_containing(expected_value=keywords, actual_value=article.get_attribute('text'), position='校验标题包含搜索关键字')
    article_title = articles[0].get_attribute('text')
    articles[0].click()
    article_detail_page = ArticleDetailPage(project)
    # 等待文章详情展示
    project.wait_until(article_detail_page._article_detail_title_text_tag)
    Assert.is_equal(expected_value=article_title,
                    actual_value=article_detail_page.get_article_detail_title_text_action(),
                    position='校验列表title与详情title一致')
    # 点击返回按钮
    article_detail_page.click_article_detail_back_button_action()

    '''
    点击找课程标签
    '''
    search_result_page.click_search_result_class_button_action()
    # 等待搜课程索结果出现
    project.wait_until(search_result_page._search_result_course_title_text_tag)
    courses = project.driver.find_elements_by_xpath(search_result_page._search_result_course_title_text_tag)
    for course in courses:
        Assert.is_containing(expected_value=keywords, actual_value=course.get_attribute('text'), position='校验课程标题包含搜索关键字')
    course_title = courses[0].get_attribute('text')
    courses[0].click()
    course_page = CourseDetailPage(project)
    # 等待课程详情展示
    project.wait_until(course_page._course_detail_title_text_tag)
    Assert.is_equal(expected_value=course_title,
                    actual_value=course_page.get_course_detail_title_text_action(),
                    position='校验列表title与详情title一致')
    # 点击返回按钮
    course_page.click_course_detail_back_button_action()

    '''
    点击找讲座标签
    '''
    search_result_page.click_search_result_lecture_button_action()
    # 等待搜课程索结果出现
    project.wait_until(search_result_page._search_result_lecture_title_text_tag)
    lectures = project.driver.find_elements_by_xpath(search_result_page._search_result_lecture_title_text_tag)
    for lecture in lectures:
        Assert.is_containing(expected_value=keywords, actual_value=lecture.get_attribute('text'),
                             position='校验讲座标题包含搜索关键字')
    lecture_title = lectures[0].get_attribute('text')
    lectures[0].click()
    lecture_page = CourseDetailPage(project)
    # 等待文章详情展示
    project.wait_until(lecture_page._course_detail_title_text_tag)
    Assert.is_equal(expected_value=lecture_title,
                    actual_value=lecture_page.get_course_detail_title_text_action(),
                    position='校验列表title与详情title一致')
    # 点击返回按钮
    course_page.click_course_detail_back_button_action()

    '''
    点击学校标签
    '''
    search_result_page.click_search_result_college_button_action()
    # 等待学校搜索结果出现
    project.wait_until(search_result_page._search_result_college_title_text_tag)
    colleges = project.driver.find_elements_by_xpath(search_result_page._search_result_college_title_text_tag)
    Assert.is_containing(expected_value=keywords, actual_value=colleges[0].get_attribute('text'),
                         position='校验第一个学校标题包含搜索关键字')
    college_title = colleges[0].get_attribute('text')
    colleges[0].click()
    college_page = CollegeDetailPage(project)
    # 等待学校详情展示
    project.wait_until(college_page._college_detail_title_text_tag)
    Assert.is_equal(expected_value=college_title,
                    actual_value=college_page.get_college_detail_title_text_action(),
                    position='校验列表title与详情title一致')
    # 点击返回按钮
    college_page.click_college_detail_back_button_action()
