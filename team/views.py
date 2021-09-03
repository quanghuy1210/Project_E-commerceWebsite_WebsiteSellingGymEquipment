from django.shortcuts import render, get_object_or_404, redirect
from course.models import NhanVienPT
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View

# Create your views here.
def getteamView(request):
    nvpt= NhanVienPT.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(nvpt, 14)
    try:
        nvpt = paginator.page(page)
    except PageNotAnInteger:
        nvpt = paginator.page(1)
    except EmptyPage:
        nvpt = paginator.page(paginator.num_pages)
    return render(request, 'team/team.html',{'NhanVienPT':nvpt}) 