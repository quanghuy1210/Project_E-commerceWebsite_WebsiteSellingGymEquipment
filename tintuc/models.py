from django.db import models
from django.db import connection
# Create your models here.

class loai_tin_tuc(models.Model):
    ma_loai_tin=models.AutoField(primary_key='true')
    ten_loai=models.CharField(max_length=100)
    class Meta:
        db_table = 'loai_tin_tuc'

    def __str__(self):
        return self.ten_loai
    
     

    
class tin_tuc(models.Model):
    matin= models.AutoField(primary_key='true')
    ma_loai_tin_tuc=models.ForeignKey(loai_tin_tuc, on_delete=models.CASCADE, db_column='ma_loai_tin')
    tieu_de=models.CharField(max_length=100)
    noi_dung=models.TextField(null=False)
    ngaydang=models.DateField()
    class Meta:
        db_table = "tin_tuc"

    def __str__(self):
          return self.tieu_de
      

    
