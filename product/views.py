from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from promotions.models import promotions
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
# def getCategory_Navbar(request):
#     result = Category.objects.all()
#     nameCategory = {
#         'objects': result
#     }
#     return render(request, 'navbar.html', nameCategory)

def getProductView(request):
    result = Product.objects.all()
    for item in result :
        km = promotions.objects.filter(ma_loai_san_pham = item.ma_loai_san_pham)
        if km.count != 0 :
            for value in km :
                item.discount = item.gia - (item.gia * value.phantram_giam/100)
                item.save()
        else:
            item.discount = item.gia
            item.save()

    page = request.GET.get('page', 1)

    paginator = Paginator(result, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'product/product.html', {'products': products}) 


class ProductDetail(View):
    def get(self, request, id_product):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        # obj = get_object_or_404(Product, id = id_product)
        obj = Product.objects.get(pk = id_product)
        obj_cat = Category.objects.all()
        obj_type = Product.objects.all()
        km = promotions.objects.filter(ma_loai_san_pham = obj.ma_loai_san_pham)
        if km.count != 0 :
            for value in km :
                obj.discount = obj.gia - (obj.gia * value.phantram_giam/100)
                obj.save()
        else:
            obj.discount = obj.gia
            obj.save()
        return render(request, 'product/product_details.html', {'product': obj, 'categories': obj_cat, 'type': obj_type,'km':km}) 

    def post(self, request, id_product):
        if not request.session.get('customer_email'):
            return redirect('customer:login')
        else:
            product = request.POST.get('product')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity <= 1:
                            cart.pop(product)
                        else:
                            cart[product] = quantity - 1
                    else:
                        cart[product] = quantity + 1
                else:
                    cart[product] = 1
            else:
                cart = {}
                cart[product] = 1
            
            request.session['cart'] = cart
            print('cart:', request.session['cart'])
            return redirect('product:product_detail', id_product) 


# def getProductDetailsView(request, id_product):
#     # obj = get_object_or_404(Product, id = id_product)
#     obj = Product.objects.get(pk = id_product)
#     obj_cat = Category.objects.all()
#     obj_type = Product.objects.all()
#     return render(request, 'product/product_details.html', {'product': obj, 'categories': obj_cat, 'type': obj_type}) 


def getProductTypeView(request, id_category):
    result = Product.objects.filter(ma_loai_san_pham = id_category)
    obj_cat = Category.objects.get(pk = id_category)
    km = promotions.objects.filter(ma_loai_san_pham = id_category)
    if km.count != 0 :
        for value in km :
            for item in result : 
                item.discount = item.gia - (item.gia * value.phantram_giam/100)
                item.save()
    else:
        for item in result : 
            item.discount = item.gia
            item.save()
    return render(request, 'product/product_type.html', {'list': result, 'category': obj_cat ,'promotions': km})


def searchProduct(request):
    try:
        s = request.GET.get('s')
    except:
        s = None
    if s:
        products = Product.objects.filter(tensp__icontains = s)
        count = products.count()
        context = { 'query': s, 'list': products, 'count': count }
        template = 'product/product_search.html'
    else:
        context = {}
        template = 'home/index.html'

    return render(request, template, context)