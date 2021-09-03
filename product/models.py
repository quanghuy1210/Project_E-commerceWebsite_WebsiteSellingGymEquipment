from django.db import models
from django.db import connections
# Create your models here.

class Category(models.Model):
    ma_loai_san_pham = models.AutoField(primary_key=True, unique=True)
    tenloai = models.CharField(max_length=100, default='')
    trang_thai = models.IntegerField(null=False, default=1)
    class Meta:
        db_table = "loai_san_pham"
    
    def __str__(self):
        # return self.ma_loai_san_pham, self.tenloai
        template = '{0.ma_loai_san_pham}'
        return template.format(self)


class Manufacturer(models.Model):
    ma_nha_san_xuat = models.AutoField(primary_key=True, unique=True)
    tennsx = models.CharField(max_length=100, default='')
    sdt = models.CharField(max_length=100, default='', null=False)
    email = models.EmailField(max_length = 254)
    class Meta:
        db_table = "nha_san_xuat"
    
    def __str__(self):
        return self.tennsx

class Product(models.Model):
    masp = models.AutoField(primary_key=True, unique=True)
    tensp = models.CharField(max_length=100, default='')
    chi_tiet_sp = models.TextField(null=False, default='')
    xuat_xu = models.CharField(max_length=100)
    hinh = models.ImageField(upload_to='product_imgs/', null=False)
    ma_nha_san_xuat = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, db_column='ma_nha_san_xuat')
    nam_san_xuat = models.DateField()
    ma_loai_san_pham = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='ma_loai_san_pham')
    gia = models.IntegerField(null=True, default=0)
    discount = models.IntegerField(null=True, default=0)
    dvt = models.CharField(max_length=5, default='VND')
    class Meta:
        db_table = "san_pham"
    
    def __str__(self):
        return self.tensp

        
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(masp__in = ids)