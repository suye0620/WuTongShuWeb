from django.shortcuts import render
from .models import Banner, Category, Site


# Create your views here.
def brand_details(request):
    # render introduction pages for different student-work brands
    return render(request, "details/brand_details.html")


def department_details(request):
    # render introduction pages for different administrative departments
    return render(request, "details/department_details.html")


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
    context = {
        'category': category,
        'id': id,
        'articles': articles
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