# Generated by Django 4.0 on 2021-12-29 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_dathang1_sanphamdathang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dathang1',
            name='qhuyendh',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='dathang1',
            name='thanhphodh',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='dathang1',
            name='xaphdh',
            field=models.CharField(default='', max_length=100),
        ),
    ]
