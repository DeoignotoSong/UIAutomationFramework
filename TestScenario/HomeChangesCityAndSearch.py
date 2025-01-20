from Core.Decorator import test_scenario
from ..TestCases.enter_home import enter_home
from ..TestCases.set_city_location import set_city_location
from ..TestCases.search import search


@test_scenario()
def HomeChangesCityAndSearch(*args, **kwargs):
    """
    首页设置城市 & 综搜
    :param args:
    :param kwargs:
    :return:
    """
    # 进入首页
    enter_home(*args, **kwargs)
    # 设置城市
    set_city_location(*args, **kwargs)
    # 综搜
    #search(*args, **kwargs)
