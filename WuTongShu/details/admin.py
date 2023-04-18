from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Site, Category, Tag, Article, Department, Banner

# Register your models here.

# 修改后台管理页面头部显示内容和后台名称
admin.site.site_header = '梧桐树学生工作品牌'
admin.site.site_title = '梧桐树 | 后台管理'


@admin.register(Site)
class SiteAdmin(ImportExportModelAdmin):
    list_display = ['site_name', 'logo_preview', 'keywords', 'desc', 'slogan', 'dynamic_slogan', 'icp_number',
                    'icp_url']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'index', 'add_menu', 'icon', 'icon_data', 'banner', 'banner_preview', 'get_items']
    list_editable = ['index', 'add_menu', 'icon', 'banner']
    search_fields = ('name',)
    list_display_links = ('name',)  # 设置哪些字段可以点击进入编辑界面


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_items']
    search_fields = ('name',)


@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    list_display = ['name', 'url', 'avatar_admin', 'desc', 'button_word']
    list_editable = ['url', 'button_word']
    search_fields = ('name', 'desc')


@admin.register(Banner)
class BannerAdmin(ImportExportModelAdmin):
    list_display = ['title', 'index', 'banner_url', 'banner_preview']
    list_editable = ['index', 'banner_url']


@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    # 设置要显示在后台列表中的字段
    list_display = (
        'add_time', 'title', 'content_url', 'cover_preview', 'category', 'show_tag', 'is_recommend', 'click_count',
        'update_time')
    list_per_page = 10  # 设置每页显示多少条记录，默认是100条
    list_editable = ['category', 'content_url', 'is_recommend']  # 设置默认可编辑字段，在列表里就可以编辑
    ordering = ('-add_time', 'is_recommend')  # 设置默认排序字段，负号表示降序排序
    list_display_links = ('title',)  # 设置哪些字段可以点击进入编辑界面
    search_fields = ('title', 'desc', 'tag')  # 置哪些字段可以查询
    list_filter = ('category', 'add_time')  # 过滤器，按字段进行筛选
    date_hierarchy = 'add_time'  # 详细时间分层筛选　
    readonly_fields = ('cover_preview',)  # 只读字段，添加该字段才能在后台预览封面，否则报错
    fieldsets = (  # 后台文章编辑页面排版
        ('文章信息', {
            'fields': ('title', 'author', 'cover', 'cover_preview', 'desc', 'content_url')
        }),
        ('其他设置', {
            'classes': ('collapse',),
            'fields': ('is_recommend', 'category', 'tag', 'add_time'),
        }),
    )

    def show_tag(self, obj):
        """在后台展示文章的所有tag"""
        return [t.name for t in obj.tag.all()]

    show_tag.short_description = "标签"  # 设置后台表头
