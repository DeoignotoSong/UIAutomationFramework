from Core.Decorator import test_case
from Core.Base import Base
from Core.Global import Data
from Core.Request import Request
from ..TestCases.search_course import search_course
from Projects.Android.Pages.Common.CourseDetailPage import CourseDetailPage
from Projects.Android.Pages.Common.OrderEnsurePage import OrderEnsurePage
from Projects.Android.Pages.Common.OrderPaySuccessPage import OrderPaySuccessPage
from Core.Assert import Assert
import json


@test_case
def course1vs1(*args, **kwargs):
    """
    1对1课程购买
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    instance = args[3]  # type: Android_2021
    url = instance.config.get('Remote', 'remote_path')
    if not Data.RECORD_DATA.get('course1vs1'):
        data = {"projectName": "PC", "scenario": "ConsolePass1v1Course", "env": "LAN"}
        response = Request.send_post_request_by_json(url=url, data=data)
        response_dic = json.loads(response)
        if response_dic['scenario_result'].lower() == 'pass':
            question_title = response_dic['data']['1v1Course_name']
            kwargs['1v1Course_name'] = question_title
            Data.RECORD_DATA['course1vs1'] = question_title
    # 指定搜索内容
    search_content = Data.RECORD_DATA.get('course1vs1')
    kwargs['search_content'] = search_content
    # 指定搜索1vs1类型课程
    course_type = '直播1对1'
    kwargs['course_type'] = course_type
    # 搜索课程
    result = search_course(*args, **kwargs)
    course_detail_page = CourseDetailPage(project)
    # 点击购买
    course_detail_page.click_course_detail_goods_buy_button_action()
    order_ensure_page = OrderEnsurePage(project)
    # 点击协议链接
    order_ensure_page.click_protocol_button_action()
    order_ensure_page.click_register_agree_button_action()
    # 预约课程
    appoinments = project.driver.find_elements_by_xpath(order_ensure_page._appointment_button_tag)
    appoinments[0].click()
    # appoinments[1].click()

    # 点击支付
    order_ensure_page.click_pay_button_action()
    order_success_page = OrderPaySuccessPage(project)
    # 等待搜索结果出现
    project.wait_until(order_success_page._pay_text_tag)
    pay_text = order_success_page.pay_text.get_attribute('text')
    Assert.is_equal(expected_value='您已购买成功！\n请点击【学习中心】去学习。', actual_value=pay_text)
    return result
