from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import KhachHang
from course.models import KhoaTap

# Create your views here.

def getRegister(request):
    if request.method == 'GET':
        obj_khoatap = KhoaTap.objects.all()
        return render(request, 'customer/register.html', {'listKhoaTap': obj_khoatap})
    else:
        postData = request.POST
        ho_ten = postData.get('hoten')
        cmnd = postData.get('cmnd')
        sdt = postData.get('sdt')
        khoa_tap = postData.get('khoatap')
        print(khoa_tap)
        email = postData.get('email')
        password = postData.get('password')

        #validation
        value = {
            'hoten': ho_ten,
            'cmnd': cmnd,
            'sdt': sdt,
            'khoatap': khoa_tap,
            'email': email
        }
        makhoa = KhoaTap.objects.get(pk = khoa_tap)
        customer = KhachHang(
                                tenkh = ho_ten,
                                cmnd = cmnd,
                                sdt = sdt,
                                ma_khoa = makhoa,
                                email = email,
                                password = password
                            )

        error_message = None
        if not ho_ten:
            error_message = "Họ tên không được trống."
        elif not cmnd:
            error_message = "Số CMND không được trống."
        elif len(cmnd) < 12:
            error_message = "Số CMND phải đủ 12 số."
        elif not sdt:
            error_message = "Số điện thoại không được trống."
        elif len(sdt) < 10:
            error_message = "Số điện thoại phải đủ 10 số."
        elif len(password) < 4:
            error_message = "Mật khẩu phải đủ hơn 6 kí tự."
        elif customer.isExists():
            error_message = "Email đã tồn tại."

        #saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('customer:login')
        else:
            obj_khoatap = KhoaTap.objects.all()
            data = {
                'error': error_message,
                'values': value,
                'listKhoaTap': obj_khoatap
            }
            return render(request, 'customer/register.html', data)


def getLogin(request):
    if request.method == 'GET':
        return render(request, 'customer/login.html')
    else:
        postData = request.POST
        email = postData.get('email')
        password = postData.get('password')
        customer = KhachHang.get_customer_by_email(email)
        print(customer)
        print(email, password)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.makh
                request.session['customer_name'] = customer.tenkh
                request.session['customer_email'] = customer.email
                return redirect('home:index')
            else:
                error_message = "Password không hợp lệ."
        else:
            error_message = "Email không hợp lệ."

        return render(request, 'customer/login.html', {'error': error_message})


def getLogOut(request):
    # del request.session['customer_id']
    # del request.session['customer_name']
    # del request.session['customer_email']
    request.session.clear()
    return redirect('home:index')