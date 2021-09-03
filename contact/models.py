from django.db import models
from django.db import connections
from customer.models import KhachHang

# Create your models here.
class GopY(models.Model):
    magopy = models.AutoField(primary_key=True, unique=True)
    makh = models.ForeignKey(KhachHang, on_delete=models.CASCADE, db_column='makh')
    tenkh = models.CharField(max_length=100)
    noi_dung = models.TextField(default='')
    class Meta:
        db_table = 'gop_y'
        
class ds_phonggym(models.Model):
    mapg=models.AutoField(primary_key='true')
    sdt=models.IntegerField()
    gmail=models.CharField(max_length=100)
    diachi=models.CharField(max_length=100)
    class Meta:
        db_table = 'ds_phonggym'
       
class slide_quangcao(models.Model):
    maqc=models.AutoField(primary_key='true')
    tieu_de=models.CharField(max_length=100)
    hinh=models.ImageField(upload_to='slide_quangcao_imgs/', null=False)
    class Meta:
        db_table = 'slide_quangcao'
 

  