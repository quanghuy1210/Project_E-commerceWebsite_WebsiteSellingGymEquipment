from django.shortcuts import render
from django.http import HttpResponse
from promotions.models import promotions 
from product.models import Product, Category
from django.views import View

# Create your views here.
def index(request):
	km =  promotions.objects.all()
	return render(request , 'promotions/index.html' , {'promotions': km} )



# def chitiet(request, category_id):
# 	result = Product.objects.filter(ma_loai_san_pham = category_id)

#     return render(request, 'promotions/details.html', {'list': result })


def Promotions_Product(request, id_category):
    result = Product.objects.filter(ma_loai_san_pham = id_category)
    obj_cat = Category.objects.get(pk = id_category)
    km = promotions.objects.filter(ma_loai_san_pham = id_category)
    if( km.count != 0 ):
        for value in km :
            for item in result : 
                item.discount = item.gia - (item.gia * value.phantram_giam/100)
                item.save()
    else:
    	for item in result : 
                item.discount = item.gia
                item.save()
    return render(request, 'product/product_type.html', {'list': result, 'category': obj_cat, 'promotions': km } )