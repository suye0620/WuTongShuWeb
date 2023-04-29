from django.shortcuts import render
from .models import Banner, Category


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
