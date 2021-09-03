# Generated by Django 3.2 on 2021-04-23 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoaiMonTapLuyen',
            fields=[
                ('ma_mon_tap_luyen', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ten_mon', models.CharField(max_length=100)),
                ('noi_dung', models.TextField(default='')),
                ('thoi_luong', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'loai_mon_tap_luyen',
            },
        ),
        migrations.CreateModel(
            name='NhanVienPT',
            fields=[
                ('manv', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ten', models.CharField(max_length=100)),
                ('sdt', models.CharField(max_length=15)),
                ('hinh', models.ImageField(upload_to='nhanvienpt_imgs/')),
            ],
            options={
                'db_table': 'nhan_vien_pt',
            },
        ),
        migrations.CreateModel(
            name='KhoaTap',
            fields=[
                ('ma_khoa', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ten_khoa', models.CharField(max_length=100)),
                ('thoi_gian_bat_dau', models.DateField()),
                ('thoi_gian_ket_thuc', models.DateField()),
                ('trang_thai', models.IntegerField(default=1)),
                ('ma_mon_tap_luyen', models.ForeignKey(db_column='ma_mon_tap_luyen', on_delete=django.db.models.deletion.CASCADE, to='course.loaimontapluyen')),
                ('manv', models.ForeignKey(db_column='manv', on_delete=django.db.models.deletion.CASCADE, to='course.nhanvienpt')),
            ],
            options={
                'db_table': 'khoa_tap',
            },
        ),
    ]
