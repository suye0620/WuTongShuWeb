from django.urls import path
from . import views

urlpatterns = [
    # 在URL中分隔单词，应该尽可能使用连字符"-"
    path('brand-activities/', views.brand_details, name='brand_details'),
    path('departments/', views.department_details, name='department_details'),
]
