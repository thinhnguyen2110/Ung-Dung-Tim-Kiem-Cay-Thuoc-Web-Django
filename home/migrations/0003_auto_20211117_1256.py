# Generated by Django 3.2.8 on 2021-11-17 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_sanpham'),
    ]

    operations = [
        migrations.AddField(
            model_name='thongtin',
            name='noidungthongtin',
            field=models.CharField(max_length=3000, null=True, verbose_name='Nội dung bài'),
        ),
        migrations.AlterField(
            model_name='sanpham',
            name='giaban',
            field=models.IntegerField(verbose_name='Giá bán'),
        ),
        migrations.AlterField(
            model_name='sanpham',
            name='soluong',
            field=models.IntegerField(verbose_name='Số lượng'),
        ),
    ]
