from django.shortcuts import render, redirect
from django.views import View
from .models import DonHang, ChiTietDonHang
from product.views import Product
from customer.views import KhachHang
from django.core.mail import send_mail
from django.conf import settings
import smtplib
# Create your views here.

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('diachi')
        phone = request.POST.get('sdt')
        email = request.POST.get('gmail')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)
        
        totalPrice = 0
        for item in products:
            sl = cart.get(str(item.masp))
            totalPrice += (item.gia * sl)

        idCus = KhachHang.objects.get(pk = customer)
        order = DonHang(
                            makh = idCus,
                            dia_chi = address,
                            sdt = phone,
                            email = email,
                            tongtien = totalPrice
                        )
        order.save()

        for product in products:
            orderDetail = ChiTietDonHang(
                                            masp = Product(pk = product.masp),
                                            madh = order,
                                            dongia = product.gia,
                                            thanhtien = product.gia * cart.get(str(product.masp)),
                                            soluong = cart.get(str(product.masp))
                                        ) 
            orderDetail.save()
            print(orderDetail.masp, orderDetail.madh)

        request.session['cart'] = {}

        send_mail(
            'Subject - Django Email Testing', 
            'Hello , Don Hang cua ban da duoc sat thuc va dg trong qua trinh van chuyen', 
            'letanquanghuy1210@gmail.com',
            [email]
        ) 
        return redirect('home:index')