# Generated by Django 4.0 on 2021-12-14 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_timkiemanh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timkiemanh',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Hình tìm kiếm'),
        ),
    ]
