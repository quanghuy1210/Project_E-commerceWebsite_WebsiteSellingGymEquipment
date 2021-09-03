from django.shortcuts import render, redirect
from course.models import KhoaTap, LoaiMonTapLuyen
from django.views import View

# Create your views here.


def getLoaimontapluyenView(request, id_loaimon):
    loai_mon = LoaiMonTapLuyen.objects.get(pk=id_loaimon)
    course = KhoaTap.objects.filter(ma_mon_tap_luyen=loai_mon.ma_mon_tap_luyen)
    
    return render(request, 'course/loaimon.html', {'KhoaTap': course, 'LoaiMonTapLuyen': loai_mon})


def getCourseView(request):
    course = KhoaTap.objects.all()
    loai_mon = LoaiMonTapLuyen.objects.all()
    return render(request, 'course/course.html', {'KhoaTap': course, 'LoaiMonTapLuyen': loai_mon})
