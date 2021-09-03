from django.db import models

# Create your models here.


class LoaiMonTapLuyen(models.Model):
    ma_mon_tap_luyen = models.AutoField(primary_key=True, unique=True)
    ten_mon = models.CharField(max_length=100)
    noi_dung = models.TextField(null=False, default='')
    thoi_luong = models.CharField(max_length=100)
    class Meta:
        db_table = 'loai_mon_tap_luyen'

    def __str__(self):
        return self.ten_mon


class NhanVienPT(models.Model):
    manv = models.AutoField(primary_key=True, unique=True)
    ten = models.CharField(max_length=100)
    sdt = models.CharField(max_length=15)
    hinh = models.ImageField(upload_to='nhanvienpt_imgs/', null=False)
    class Meta:
        db_table = 'nhan_vien_pt'

    def __str__(self):
        return self.ten


class KhoaTap(models.Model):
    ma_khoa = models.AutoField(primary_key=True, unique=True)
    ten_khoa = models.CharField(max_length=100)
    ma_mon_tap_luyen = models.ForeignKey(LoaiMonTapLuyen, on_delete=models.CASCADE, db_column='ma_mon_tap_luyen')
    manv = models.ForeignKey(NhanVienPT, on_delete=models.CASCADE, db_column='manv')
    thoi_gian_bat_dau = models.DateField()
    thoi_gian_ket_thuc = models.DateField()
    trang_thai = models.IntegerField(null=False, default=1)
    class Meta:
        db_table = 'khoa_tap'

    def __str__(self):
        return self.ten_khoa