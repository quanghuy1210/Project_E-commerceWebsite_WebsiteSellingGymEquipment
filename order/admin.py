from django.contrib import admin
from .models import DonHang, ChiTietDonHang

# Register your models here.
admin.site.register(DonHang)
admin.site.register(ChiTietDonHang)