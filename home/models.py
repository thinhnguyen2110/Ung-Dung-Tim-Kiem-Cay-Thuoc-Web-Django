import os.path
from django.contrib.auth.models import User
from django.db import models
import datetime
from ckeditor.fields import RichTextField
# Create your models here.
class thongtin(models.Model):
    idthongtin = models.AutoField(primary_key = True, null = False )
    tieude = models.CharField('Tiêu đề', max_length= 100)
    # noidungthongtin = models.TextField('Nội dung bài', max_length= 3000,null=True)
    nguoidang = models.CharField('Người đăng', max_length= 100)
    hinh = models.ImageField ('Hình ảnh', max_length=100)
    ngaydangbai = models.DateField(default=datetime.datetime.today)
    noidungthongtin = RichTextField(blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Thông Tin Bài Báo'
    def __str__(self):
        return f"{self.idthongtin},{self.tieude}, {self.nguoidang}, {self.hinh}, {self.noidungthongtin}, {self.ngaydangbai}"

class sanpham(models.Model):
    dvt = (
        ('kg','kg'),
        ('g','g'),
        ('lít','lít'),
        ('chai','chai'),
    )
    masp = models.AutoField(primary_key = True, null = False)
    name = models.CharField('Tên sản phẩm', max_length= 100)
    price = models.IntegerField('Giá bán')
    image = models.ImageField('Hình SP', max_length=100)
    noidungsp = models.TextField('Nội dung sản phẩm', default='' )
    donvitinh = models.CharField('Đơn vị tính', max_length= 50, choices= dvt)
    soluong = models.IntegerField('Số lượng')
    class Meta:
        verbose_name_plural = 'Sản phẩm'
    def __str__(self):
        return f"{self.masp},{self.name}, {self.price}, {self.image}, {self.noidungsp}, {self.donvitinh}, {self.soluong}"


class thongtindathang(models.Model):
    hoten = models.CharField('Họ Tên',max_length=100)
    sdt = models.CharField('Số điện thoại',max_length=15)
    email = models.EmailField('Email',max_length=100)
    diachi = models.CharField('Địa chỉ',max_length=200)
    xaphuong = models.CharField('Xã/Phường',max_length=100)
    quanhuyen = models.CharField('Quận/Huyện',max_length=100)
    tinhthanhpho = models.CharField('Tỉnh/Thành phố',max_length=100)
    class Meta:
        verbose_name_plural = 'Thông tin đặt hàng'



class DatHang1(models.Model):
    trangthai = (
        ('Đã nhận đơn', 'Đã nhận đơn'),
        ('Đang vận chuyển', 'Đang vận chuyển'),
        ('Đã giao hàng', 'Đã giao hàng'),
    )
    hinhdathang = models.ImageField('Hình đặt hàng',max_length=100)
    sanphamdathang = models.CharField('Sản phẩm đặt hàng',max_length=1000, default='')
    usedathang = models.ForeignKey(User, on_delete=models.CASCADE)
    soluongdathang = models.CharField('Số lượng đặt hàng',max_length=10)
    giadathang = models.IntegerField('Giá sản phẩm')
    tendathang = models.CharField('Tên người đặt hàng',max_length=100)
    maildathang = models.EmailField('Mail người đặt hàng',max_length=100)
    diachidathang = models.TextField('Địa chỉ',max_length=500)
    xaphdh = models.CharField('Xã/Phường',max_length=100, default='')
    qhuyendh = models.CharField('Quận/Huyện',max_length=100, default='')
    thanhphodh = models.CharField('Tỉnh/Thành Phố',max_length=100, default='')
    sdtdathang = models.CharField('Số điện thoại',max_length=20)
    tongtien = models.CharField('Tổng tiền',max_length=1000, default='')
    ngaydathang = models.DateField('Ngày đặt hàng',default=datetime.datetime.today)
    trangthaidathang = models.CharField('Trạng thái', max_length= 50, choices= trangthai,default='')
    class Meta:
        verbose_name_plural = 'Đơn đặt hàng'
    def __str__(self):
        return self.sanphamdathang