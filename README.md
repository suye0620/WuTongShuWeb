# WuTongShuWeb
zueltsxy展示网站

## Django运行环境创建

1. 使用conda创建一个具有指定版本Python的虚拟环境(如py39)
2. 然后往这个虚拟环境安装django包(如dj32)
3. `pip list --format=freeze > requirements.txt`在项目目录创建环境的requirements.txt文件
4. `django-admin startproject PROJECT_NAME`

## 模板设计(使用节日的模板)

1. base
2. header
3. footer
4. banner
5. slider
6. photo

## 参考

1. [为Django网站添加favicon.ico图标 - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1594579)
2. [vscode花括号跳转（快捷键）_weixin_38070782的博客-CSDN博客](https://blog.csdn.net/weixin_38070782/article/details/106818715)
3. [Meta标签中的format-detection属性及含义_BenjaminShih的博客-CSDN博客](https://blog.csdn.net/sjn0503/article/details/72897763)
4. [前端页面中的\<meta name="renderer" content="webkit"\>意义 - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1455896)
5. [解决Django中修改css或js文件但浏览器显示效果无法及时更新的问题_调皮李小怪的博客-CSDN博客_django js不生效](https://blog.csdn.net/qq_38388811/article/details/105625981)
6. [Bing Maps 开发入门 - 1_bcbobo21cn的博客-CSDN博客_bingmap](https://blog.csdn.net/bcbobo21cn/article/details/114469226)
7. [必应地图api文档，微软必应地图web开发版详解，可以在国内使用国外地图 - 汪培 - 博客园](https://www.cnblogs.com/aiyunyun/p/6292567.html)
8. [必应地图怎么查看经纬度-百度经验 ](https://jingyan.baidu.com/article/4f7d5712cf461e1a201927b4.html)
9. [Bing Maps V8 Interactive SDK](https://cn.bing.com/maps/sdkrelease/mapcontrol/isdk/Overview#SearchModule2)
10. [Simple UI | Simple UI](https://simpleui.72wo.com/docs/simpleui/doc.html#%E4%BB%8B%E7%BB%8D)
11. [模型 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/3.2/topics/db/models/#meta-inheritance)
12. [模型 Meta 选项 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/3.2/ref/models/options/)
13. [验证器 | Django 文档 | Django](https://docs.djangoproject.com/zh-hans/3.2/ref/validators/#django.core.validators.URLValidator)
14. [Pyecharts Document](https://gallery.pyecharts.org/#/)麻了，最新版基本不兼容之前的用法
15. [(1条消息) Django中Ajax的使用_忘尘~的博客-CSDN博客](https://blog.csdn.net/BobYuan888/article/details/84250116)
16. [Django使用JQuery实现Ajax请求 - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1456373)
17. [(1条消息) 【JavaScript】关于[object Object]_小绵杨Yancy的博客-CSDN博客](https://blog.csdn.net/ZHANGYANG_1109/article/details/124537388)
18. [(1条消息) Django怎么获取get请求里面的参数_django获取get请求参数_他-途的博客-CSDN博客](https://blog.csdn.net/au55555/article/details/80024375)
19. [4,000+张最精彩的“潮汐”图片 · 100%免费下载 · Pexels素材图片](https://www.pexels.com/zh-cn/search/%E6%BD%AE%E6%B1%90/)


## 页面设计

### index主页

1. banner
2. 梧桐树品牌介绍（网站的description及主旨介绍）
3. 下设版块（图片banner+图片平滑切换面板）

![img.png](README-imgs/img.png)

![img.png](README-imgs/img2.png)

### 各下设版块的内容详情页

![img.png](README-imgs/img3.png)

### 各职能机构的介绍页 

考虑使用原始模板的about us页面

![img.png](README-imgs/img4.png)

## 模型抽象
1. banner抽象（图片链接、图片名称）(√)
2. site抽象(√)
3. 版块抽象（banner、标签等）(√)
4. 职能机构抽象(√)

## 创建一个新页面的一般步骤

template → view → url → model(→admin→setting) → url → view → template

其中，admin细节为在admin.py文件中注册自己设计的模型；setting细节为自定义后台admin界面。


## TODO

1. 生成测试文章用于开发后续功能（√）
2. 先把归档页做好(√)
3. 看一下图片切换的js使用
4. 把所有的标签先导进去（√）
5. 因为每个文章有add_index选项，所以我们只用检查这些文章的标签，然后构建索引。这样不用遍历所有文章。
