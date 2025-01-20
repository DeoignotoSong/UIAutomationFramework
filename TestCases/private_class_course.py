from Core.Decorator import test_case
from Core.Base import Base
from ..TestCases.search_course import search_course
from Projects.Android.Pages.Common.CourseDetailPage import CourseDetailPage
from Projects.Android.Pages.Common.OrderEnsurePage import OrderEnsurePage
from Projects.Android.Pages.Common.OrderPaySuccessPage import OrderPaySuccessPage
from Core.Assert import Assert


@test_case
def private_class_course(*args, **kwargs):
    """
    小班课程购买
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    # 指定搜索内容
    search_content = '小班课'
    kwargs['search_content'] = search_content
    # 指定搜索1vs1类型课程
    course_type = '直播小班课'
    kwargs['course_type'] = course_type
    # 搜索课程
    result = search_course(*args, **kwargs)
    course_detail_page = CourseDetailPage(project)
    # 点击购买
    course_detail_page.click_course_detail_goods_buy_button_action()
    # 立即购买
    course_detail_page.click_course_detail_dialog_goods_buy_button_action()
    order_ensure_page = OrderEnsurePage(project)
    # 点击协议链接
    order_ensure_page.click_live_exhibition_protocol_button_action()
    order_ensure_page.click_register_agree_button_action()
    # 点击支付
    order_ensure_page.click_pay_button_action()
    order_success_page = OrderPaySuccessPage(project)
    # 等待搜索结果出现
    project.wait_until(order_success_page._pay_text_tag)
    pay_text = order_success_page.pay_text.get_attribute('text')
    Assert.is_equal(expected_value='您已购买成功！\n请点击【学习中心】去学习。', actual_value=pay_text)
    return result
