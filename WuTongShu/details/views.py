from django.shortcuts import render
from .models import Banner

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
        str_banners = ",".join(["\""+banner.banner_url+"\"" for banner in all_banners])
        # 需要传递给模板（templates）的对象
        context = {
            'all_banners': str_banners,
        }
    return render(request, "index.html", context=context)