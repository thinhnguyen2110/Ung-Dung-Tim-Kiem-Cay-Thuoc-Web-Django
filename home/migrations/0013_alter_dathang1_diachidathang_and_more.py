# Generated by Django 4.0 on 2022-01-04 03:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_thongtin_ngaydangbai_alter_thongtin_noidungthongtin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dathang1',
            name='diachidathang',
            field=models.TextField(max_length=500, verbose_name='Địa chỉ'),
        ),
        migrations.AlterField(
            model_name='dathang1',
            name='giadathang',
            field=models.IntegerField(verbose_name='Giá sản phẩm'),
        ),
        migrations.AlterField(
            model_name='dathang1',
            name='hinhdathang',
            field=models.ImageField(upload_to='', verbose_name='Hình đặt hàng'),
        ),
        migrations.AlterField(
            model_name='dathang1',
            name='maildathang',
            field=models.EmailField(max_length=100, verbose_name='Mail người đặt hàng'),
        ),
        migrations.AlterField(
            model_name='dathang1',
            name='ngaydathang',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Ngày đặt hàng'),
        ),
        migrations.AlterField(
            model_name='dathang1',
            name='qhuyendh',
            field=models.CharField(default='', max_length=100, verbose_name='Quận/Huyện'),
        ),
        migrations.AlterField(
            model_name='dathang1',
            name='sanphamdathang',
            field=models.CharField(default='', max_length=1000, verbose_name='Sản phẩm đặt hàng'),
        ),
        migrations.AlterField(
            model_name='dathang1',
            name='sdtdathang',
            field=models.CharField(max_length=20, verbose_name='Số điện thoại'),
        ),
        migrations.AlterField(
            model_name='dathang1',
            name='soluongdathang',
            field=models.CharField(max_length=10, verbose_name='Số lượng đặt hàng'),
        ),
        migrations.AlterField(
            model_name='dathang1',
            name='tendathang',
            field=models.CharField(max_length=100, verbose_name='Tên người đặt hàng'),
        ),
        migrations.AlterField(
            model_name='dathang1',
            name='thanhphodh',
            field=models.CharField(default='', max_length=100, verbose_name='Tỉnh/Thành Phố'),
        ),
        migrations.AlterField(
            model_name='dathang1',
            name='tongtien',
            field=models.CharField(default='', max_length=1000, verbose_name='Tổng tiền'),
        ),
        migrations.AlterField(
            model_name='dathang1',
            name='xaphdh',
            field=models.CharField(default='', max_length=100, verbose_name='Xã/Phường'),
        ),
    ]
