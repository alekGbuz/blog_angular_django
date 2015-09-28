from django.conf.urls import url,include
from blog.views import index_page

from rest_framework.routers import DefaultRouter
from blog.viewsets import BlogArticleViewSet, BlogCategoryViewSet,articles_by_category,\
    article_by_detail,articles_by_keys
from site_utils.viewsets import send_message,site_page,index_first_page
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'articles', BlogArticleViewSet)
router.register(r'categories',BlogCategoryViewSet)

urlpatterns = [
    url(r'^my_api/', include(router.urls)),
    url(r'^my_api/articles_by_category/(?P<category_slug>[-\w]+)',articles_by_category),
    url(r'^my_api/detail_article/(?P<article_slug>[-\w]+)',article_by_detail),
    url(r'^my_api/articles_by_keys',articles_by_keys),
    url(r'my_api/send_message',send_message),
    url(r'^my_api/site_page/(?P<page_slug>[-\w]+)',site_page),
    url(r'^my_api/index_first_page',index_first_page),


    url(r'^category_articles.html$',TemplateView.as_view(template_name='articles/category_articles.html')),
    url(r'^detail_article.html$',TemplateView.as_view(template_name='articles/detail_article.html')),
    url(r'^articles_by_keys.html$',TemplateView.as_view(template_name='articles/articles_by_keys.html')),


    url(r'^site_page.html$',TemplateView.as_view(template_name='pages/site_page.html')),
    url(r'^index_first_page.html$',TemplateView.as_view(template_name='pages/index_first_page.html')),
    url(r'^connect.html$',TemplateView.as_view(template_name='connect/connect.html')),

    url(r'^', index_page, name='index_page'),
]