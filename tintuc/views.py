from django.shortcuts import render
from tintuc.models import tin_tuc, loai_tin_tuc
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from promotions.models import promotions

# Create your views here.
def getloaitintucView(request, id_tintuc):
    tintuc = tin_tuc.objects.get(pk = id_tintuc)
    loai_tin = loai_tin_tuc.objects.all()
    return render(request, 'tintuc/tin_tuc.html', {'tin_tuc': tintuc, 'loai_tin_tuc': loai_tin}) 


def gettintucView(request):
    km = promotions.objects.all()
    tintuc=tin_tuc.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(tintuc, 4) 
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, 'tintuc/tintuc.html',{'tin_tuc':news}) 
    