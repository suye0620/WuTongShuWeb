from django.db import models
from datetime import datetime
from django.utils.html import format_html


# Create your models here.
class Site(models.Model):
    """ some settings of the site """
    site_name = models.CharField(default='梧桐树学生工作品牌', max_length=30, verbose_name='网站名字')
    keywords = models.CharField(default='关键字测试', max_length=50, verbose_name='网站关键词')
    logo = models.URLField(default='http://42.193.14.111/static/upload/tsxywts/wutongshu-logo.png', max_length=100,
                           verbose_name='网站logo')
    desc = models.CharField(max_length=100, verbose_name='网站描述')
    slogan = models.CharField(max_length=100, verbose_name='网站标语')
    dynamic_slogan = models.CharField(max_length=100, verbose_name='动态标语', blank=True)
    icp_number = models.CharField(max_length=40, verbose_name='备案号')
    icp_url = models.URLField(default='http://www.beian.miit.gov.cn/', max_length=100, verbose_name='备案链接')

    class Meta:
        verbose_name = '网站设置'
        verbose_name_plural = verbose_name

    def logo_preview(self):  # logo预览
        return format_html('<img src="{}" width="40px" height="40px" alt="logo" />', self.logo)

    logo_preview.short_description = 'logo预览'

    def __str__(self):
        return self.site_name


class Category(models.Model):
    """文章分类"""
    name = models.CharField(max_length=20, verbose_name='工作品牌')
    index = models.IntegerField(default=1, verbose_name='品牌展示顺序')
    add_menu = models.BooleanField(default=False, verbose_name='添加到导航栏')
    icon = models.CharField(max_length=30, default='fas fa-home', verbose_name='导航栏图标')
    banner = models.URLField(max_length=200, default='http://42.193.14.111/static/upload/tsxywts/banner6.jpg',
                             verbose_name='品牌封面')
    primary_color = models.CharField(max_length=7, default="#FFD700", verbose_name="颜色1")
    secondary_color = models.CharField(max_length=7, default="#fd614a", verbose_name="颜色2")

    class Meta:
        verbose_name = '工作品牌'
        verbose_name_plural = verbose_name
        ordering = ('index',)  # 以index顺序排列

    # 统计分类对应文章数,并放入后台
    def get_items(self):
        return len(self.article_set.all())

    get_items.short_description = '文章数'  # 设置后台显示表头

    #
    def banner_preview(self):
        return format_html('<img src="{}" width="200px" height="150px"/>', self.banner, )

    banner_preview.short_description = '品牌封面预览'

    # 后台图标预览
    def icon_data(self):  # 引入Font Awesome Free 5.11.1
        return format_html('<h1><i class="{}"></i></h1>', self.icon)  # 转化为<i class="{self.icon}"></i>

    icon_data.short_description = '图标预览'

    def __str__(self):
        return self.name


class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=20, verbose_name='标签名称')
    add_to_index = models.BooleanField(default=False, verbose_name='添加到首页')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    # 统计分类对应文章数,并放入后台
    def get_items(self):
        return len(self.article_set.all())

    get_items.short_description = '文章数'  # 设置后台显示表头

    def __str__(self):
        return self.name


class Article(models.Model):
    """文章"""
    title = models.CharField(max_length=50, verbose_name='文章标题')
    author = models.CharField(max_length=10, verbose_name='作者', default='作者', blank=True, null=True)
    desc = models.CharField(max_length=100, verbose_name='文章描述')
    cover = models.URLField(max_length=200, default='http://42.193.14.111/static/upload/tsxywts/%E6%99%9A%E9%9C%9E.jpg',
                            verbose_name='文章封面')

    content_url = models.URLField(max_length=250, default='https://mp.weixin.qq.com/s/gkeOZMPFoQQdMH5kM_sYCQ',
                            verbose_name='文章链接')
    click_count = models.PositiveIntegerField(default=0, verbose_name='阅读量')

    is_recommend = models.BooleanField(default=False, verbose_name='是否在首页推荐')
    index = models.IntegerField(default=1, verbose_name='在首页子版块中展示的顺序',blank=True)
    cover_square = models.URLField(max_length=200, default='http://42.193.14.111/static/upload/tsxywts/6.png',
                            verbose_name='在首页子版块中展示的方形封面',blank=True)

    # 文章创建时间。参数 default=datetime.now 指定其在创建数据时将默认写入当前的时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    # 文章更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='文章分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True, verbose_name='文章标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ('-add_time',)  # 以创建时间倒序排列

    def cover_preview(self):
        return format_html('<img src="{}" width="200px" height="150px"/>', self.cover, )

    cover_preview.short_description = '文章封面预览'

    def cover_square_preview(self):
        return format_html('<img src="{}" width="200px" height="200px"/>', self.cover_square, )

    cover_square_preview.short_description = '首页方形封面预览'

    def __str__(self):
        return self.title  # 将文章标题返回


class Department(models.Model):
    """部门"""
    name = models.CharField(max_length=10, verbose_name='部门名称')
    url = models.URLField(verbose_name='介绍链接', blank=True)
    avatar = models.URLField(default='http://42.193.14.111/static/upload/tsxywts/testi2.jpg', verbose_name='头像')
    # 这边字放多一些
    desc = models.TextField(max_length=500, verbose_name='描述')
    button_word = models.CharField(default='详情', max_length=10, verbose_name='跳转文字')

    class Meta:
        verbose_name = verbose_name_plural = '成员'

    # 后台头像预览
    def avatar_admin(self):
        return format_html('<img src="{}" width="50px" height="50px" style="border-radius: 50%;" />', self.avatar, )

    avatar_admin.short_description = '头像预览'

    def __str__(self):
        return self.name


class Banner(models.Model):
    """首页横幅管理"""
    title = models.CharField(max_length=50, verbose_name='标题')
    banner_url = models.URLField(max_length=200, default='http://42.193.14.111/static/upload/tsxywts/banner1.jpg',
                                 verbose_name='横幅图片链接')
    index = models.IntegerField(default=1, verbose_name='横幅展示顺序')

    class Meta:
        verbose_name = '首页横幅'
        verbose_name_plural = verbose_name
        ordering = ('index',)  # 以index字段排列

    def banner_preview(self):
        return format_html('<img src="{}" width="300px" height="150px"/>', self.banner_url, )

    banner_preview.short_description = '首页横幅预览'

    def __str__(self):
        return self.title  # 返回横幅标题
