from django.shortcuts import render
from .models import Banner, Category, Site, Department
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def brand_details(request):
    # render introduction pages for different student-work brands
    return render(request, "details/brand_details.html")


def department_details(request):
    # render introduction pages for different administrative departments
    departments = Department.objects.all()
    context = {
        'departments': departments
    }
    return render(request, "details/department_details.html", context)


def index(request):
    # index page
    if request.method == "GET":
        # 取出所有横幅
        all_banners = Banner.objects.all()
        str_banners = ",".join(["\"" + banner.banner_url + "\"" for banner in all_banners])

        # 取出所有品牌
        categories = Category.objects.all()
        # 需要传递给模板（templates）的对象
        context = {
            'all_banners': str_banners,
            'categories': categories,
        }
    return render(request, "index.html", context=context)


def article_category(request, id):
    """文章分类详情页"""
    category = Category.objects.get(id=id)
    articles = Category.objects.get(id=id).article_set.all()  # 获取该id对应的所有的文章

    paginator = Paginator(articles, 9)  # 实例化一个分页对象, 每页显示10个
    page = request.GET.get('page')  # 从URL通过get页码，如?page=3

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)  # 如果传入page参数不是整数，默认第一页
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False  # 如果页数小于1不使用分页
    context = {
        'category': category,
        'id': id,
        'page_obj': page_obj,
        'is_paginated': is_paginated,
        'querystring': request.GET.urlencode(),
        'max_page_num_before': 2,
        'max_page_num_after': 2
    }
    return render(request, 'details/article_category.html', context=context)


def global_params(request):
    """全局变量"""
    category_nav = Category.objects.filter(add_menu=True).order_by('index')
    site_name = Site.objects.first().site_name
    keywords = Site.objects.first().keywords
    logo = Site.objects.first().logo
    desc = Site.objects.first().desc
    slogan = Site.objects.first().slogan
    dynamic_slogan = Site.objects.first().dynamic_slogan
    icp_number = Site.objects.first().icp_number
    icp_url = Site.objects.first().icp_url
    return {
        'category_nav': category_nav,
        'SITE_NAME': site_name,
        'KEYWORDS': keywords,
        'LOGO': logo,
        'DESC': desc,
        'SLOGAN': slogan,
        'DYNAMIC_SLOGAN': dynamic_slogan,
        'ICP_NUMBER': icp_number,
        'ICP_URL': icp_url,
    }
