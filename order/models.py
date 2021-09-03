from django.db import models
from product.models import Product
from customer.models import KhachHang
from django.db import connections
import datetime

# Create your models here.

class DonHang(models.Model):
    madh = models.AutoField(primary_key=True, unique=True)
    makh = models.ForeignKey(KhachHang, on_delete=models.CASCADE, db_column='makh')
    ngay_lap_hoa_don = models.DateField(default=datetime.datetime.today)
    email = models.EmailField(max_length = 254)
    dia_chi = models.CharField(max_length=200, default='')
    sdt = models.CharField(max_length=100, default='')
    tongtien = models.IntegerField()
    class Meta:
        db_table = "don_hang"

    def saveOrder():
        self.save() 


class ChiTietDonHang(models.Model):
    mactdh = models.AutoField(primary_key=True, unique=True)
    masp = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='masp')
    madh = models.ForeignKey(DonHang, on_delete=models.CASCADE, db_column='madh')
    dongia = models.IntegerField()
    thanhtien = models.IntegerField()
    soluong = models.IntegerField(default=1)
    class Meta:
        db_table = "chi_tiet_don_hang"

    def saveOrderDetail(self):
        self.save()