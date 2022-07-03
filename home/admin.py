from django.contrib import admin
from .models import thongtin as ThongTinBaiBao
from .models import sanpham as ThongTinSanPham
from .models import thongtindathang as ThongTinKhachHang
from .models import DatHang1 as ThongTinDatHang
from django.utils.html import format_html
# Register your models here.
class Thongtin(admin.ModelAdmin):
    list_display = ('idthongtin', 'tieude','NoiDung', 'nguoidang', 'hinh')
    def NoiDung(self, obj):
        return format_html(f'<span style="color:green">{obj.noidungthongtin[:100]}</span>')
admin.site.register(ThongTinBaiBao, Thongtin)
class Sanpham (admin.ModelAdmin):
    list_display = ('masp','name', 'price', 'image', 'noidungsp', 'donvitinh','soluong')
admin.site.register(ThongTinSanPham,Sanpham)

class ThongTinNguoiDat(admin.ModelAdmin):
    list_display =('hoten','sdt','email','diachi','xaphuong','quanhuyen', 'tinhthanhpho')
admin.site.register(ThongTinKhachHang,ThongTinNguoiDat)

class DatHang(admin.ModelAdmin):
    list_display =('hinhdathang','sanphamdathang','usedathang','soluongdathang','giadathang','tendathang','maildathang','diachidathang','xaphdh', 'qhuyendh','thanhphodh','sdtdathang','tongtien','ngaydathang','trangthaidathang','Check')
    def Check(self, obj):
        return format_html(f'<a href = "/admin/home/dathang1/{obj.id}/change/" class = "default">Kiểm tra đơn hàng</a>')
admin.site.register(ThongTinDatHang, DatHang)

