# Generated by Django 4.0 on 2021-12-29 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_dathang1'),
    ]

    operations = [
        migrations.AddField(
            model_name='dathang1',
            name='qhuyendh',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dathang1',
            name='thanhphodh',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dathang1',
            name='xaphdh',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
