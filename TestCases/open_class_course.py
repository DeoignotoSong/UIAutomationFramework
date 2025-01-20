from Core.Decorator import test_case
from Core.Base import Base
from ..TestCases.search_course_lectures import search_course_lectures
from Projects.Android.Pages.Common.CourseDetailPage import CourseDetailPage


@test_case
def open_class_course(*args, **kwargs):
    """
    公开课程购买
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    # 指定搜索内容
    search_content = '讲座'
    kwargs['search_content'] = search_content
    # 搜索课程
    result = search_course_lectures(*args, **kwargs)
    course_detail_page = CourseDetailPage(project)
    # 点击立即预约
    course_detail_page.click_course_detail_goods_buy_button_action()
    return result
