from django.urls import path
from . import views

urlpatterns = [
    # 在URL中分隔单词，应该尽可能使用连字符"-"
    # index page
    path('', views.index, name='index'),
    path('brand-activities/', views.brand_details, name='brand_details'),
    path('departments/', views.department_details, name='department_details'),
    # 文章分类详情页
    path('article_category/(?P<id>[0-9]+)$', views.article_category, name='article_category'),
]
