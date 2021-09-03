from django.db import models
from course.models import KhoaTap
# Create your models here.


class KhachHang(models.Model):
    makh = models.AutoField(primary_key=True, unique=True)
    tenkh = models.CharField(max_length=100)
    cmnd = models.CharField(max_length=100)
    sdt = models.CharField(max_length=15, default='', null=False)
    ma_khoa = models.ForeignKey(KhoaTap, on_delete=models.CASCADE, db_column='ma_khoa')
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=100)
    class Meta:
        db_table = 'khach_hang'
        
    def __str__(self):
        template = '{0.makh}    -   {0.tenkh}   -   email: {0.email}'
        return template.format(self)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return KhachHang.objects.get(email = email)
        except:
            return False

    def isExists(self):
        if KhachHang.objects.filter(email = self.email):
            return True
        return False