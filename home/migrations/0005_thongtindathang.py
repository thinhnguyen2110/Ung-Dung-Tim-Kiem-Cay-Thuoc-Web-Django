# Generated by Django 4.0 on 2021-12-28 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_thongtin_noidungthongtin'),
    ]

    operations = [
        migrations.CreateModel(
            name='thongtindathang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoten', models.CharField(max_length=100)),
                ('sdt', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('diachi', models.CharField(max_length=200)),
                ('xaphuong', models.CharField(max_length=100)),
                ('quanhuyen', models.CharField(max_length=100)),
                ('tinhthanhpho', models.CharField(max_length=100)),
            ],
        ),
    ]
