from django.shortcuts import render
from .models import Banner, Category, Site, Department, Tag, Video, Friendshiplink, Teammember
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def duplicate(one_list: list):
    new_list = list(set(one_list))
    new_list.sort(key=one_list.index)
    return new_list


# Create your views here.
def department_details(request):
    # render introduction pages for different administrative departments
    departments = Department.objects.all()
    teammembers = Teammember.objects.all()
    context = {
        'departments': departments,
        'teammembers': teammembers,
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

        list_items_categories = []
        for category_count, category in enumerate(categories):
            recommended_articles_of_the_category = category.article_set.filter(is_recommend=True).all()
            tags_of_recommended_articles = duplicate(
                [article.tag for article in recommended_articles_of_the_category])
            dict_tag2filter = {}
            for tag_count, tag in enumerate(tags_of_recommended_articles):
                # format函数：https://blog.csdn.net/xyx_x/article/details/90202813
                dict_tag2filter[tag] = "filter-{category_count}-{tag_count}".format(category_count=category_count,
                                                                                    tag_count=tag_count)
            list_items_categories.append({
                'category': category,
                'recommended_articles_of_the_category': recommended_articles_of_the_category,
                'tags_of_recommended_articles': tags_of_recommended_articles,
                'dict_tag2filter': dict_tag2filter
            })

        category0_articles = categories[0].article_set.filter(is_recommend=True).all()

        tags_category0_articles = duplicate([article.tag for article in category0_articles])
        dict_tag2filter = {}
        for count, tag in enumerate(tags_category0_articles):
            dict_tag2filter[tag] = "filter-0-{}".format(count)
        # 需要传递给模板（templates）的对象
        context = {
            'all_banners': str_banners,
            'categories': categories,
            'list_items_categories': list_items_categories,
        }
    return render(request, "index.html", context=context)


def article_category(request, id):
    """文章分类详情页"""
    category = Category.objects.get(id=id)
    tag_id = request.GET.get('tag', default=None)
    if tag_id == None:
        articles = Category.objects.get(id=id).article_set.all()  # 获取该id对应的所有的文章
    else:
        articles = Tag.objects.get(id=tag_id).article_set.all()  # 获取该id对应的所有的文章

    tags_of_category = Category.objects.get(id=id).tag_set.all()  # 获取该id对应的所有的文章

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
        'tags_of_category': tags_of_category,
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
    friendshiplinks = Friendshiplink.objects.all()
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
        'FRIENDSHIP_LINKS': friendshiplinks,
    }
