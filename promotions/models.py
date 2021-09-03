from django.db import models
from django.db import connections
from product.models import Category
# Create your models here.


class promotions(models.Model):
    ma_chuong_trinh = models.AutoField(primary_key=True, unique=True)
    ten_chuong_trinh = models.CharField(max_length=150, default='')
    ma_loai_san_pham = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='ma_loai_san_pham')
    noi_dung = models.TextField(null=False, default='')
    phantram_giam = models.IntegerField(null=False, default=1)
    ngay_bat_dau = models.DateField()
    thoi_gian_ket_thuc = models.DateField()
    class Meta:
        db_table = "chuong_trinh_khuyen_mai"
    
    def __str__(self):
        return self.ten_chuong_trinh










