from django.shortcuts import render


# Create your views here.
def brand_details(request):
    # render introduction pages for different student-work brands
    return render(request, "details/brand_details.html")


def department_details(request):
    # render introduction pages for different administrative departments
    return render(request, "details/department_details.html")
