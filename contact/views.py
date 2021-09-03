from django.shortcuts import render, redirect
from django.views import View
from .models import GopY,slide_quangcao,ds_phonggym
from customer.models import KhachHang
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.



def getContactView(request):
    
    if request.method == 'GET':
        if request.session.get('customer_name'):
            slide=slide_quangcao.objects.all()
            ds=ds_phonggym.objects.all()
            page = request.GET.get('page', 1)
            paginator = Paginator(slide, 6)
            try:
                news = paginator.page(page)
            except PageNotAnInteger:
                news = paginator.page(1)
            except EmptyPage:
                news = paginator.page(paginator.num_pages)
            return render(request, 'contact/contact.html',{'slide_quangcao':news,'ds_phonggym':ds})
        else:
            return redirect('customer:login')
    else:
        postData = request.POST
        ten_kh = postData.get('tenkh')
        email = postData.get('email')
        sdt = postData.get('sdt')
        gop_y = postData.get('gopy')
        kh = request.session['customer_id']

        print(ten_kh, email, sdt, gop_y, kh)

        value = {
            'tenkh': ten_kh,
            'email': email,
            'sdt': sdt,
            'gopy': gop_y
        }
        idCus = KhachHang.objects.get(pk = kh)
        review = GopY(
                        makh = idCus,
                        tenkh = ten_kh,
                        noi_dung = gop_y
                     )
        #Rangbuoc
        
        review.save()
        
        return redirect('home:index')


   
