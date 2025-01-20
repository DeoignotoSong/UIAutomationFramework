from Core.Decorator import test_scenario
from ..TestCases.enter_home import enter_home
from ..TestCases.search_article import search_article
from ..TestCases.article_operate import article_operate
from ..TestCases.user_login import user_login
from ..TestCases.if_login_then_user_logout import if_login_then_user_logout


@test_scenario()
def LecturerCertificationArticle(*args, **kwargs):
    """
    机构入驻讲师认证文章相关操作(文章详情、文章评论、文章收藏、文章评论点赞)
    :param args:
    :param kwargs:
    :return:
    """
    # 进入首页
    enter_home(*args, **kwargs)
    # 如果登录则退出
    if_login_then_user_logout(*args, **kwargs)
    # 登录
    user_login(*args, **kwargs)
    search_content = '留学'
    kwargs['search_content'] = search_content
    # 搜索文章
    search_article(*args, **kwargs)
    # 文章操作相关
    article_operate(*args, **kwargs)
