# Generated by Django 4.0 on 2022-01-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_dathang1_diachidathang_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dathang1',
            name='trangthaidathang',
            field=models.CharField(choices=[('Đã nhận đơn', 'Đã nhận đơn'), ('Đang vận chuyển', 'Đang vận chuyển'), ('Đã giao hàng', 'Đã giao hàng')], default='', max_length=50, verbose_name='Trạng thái'),
        ),
    ]
