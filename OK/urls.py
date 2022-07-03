"""OK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from numpy.testing._private.parameterized import param

from home import views
from django.conf import settings
from django.conf.urls.static import static
from home.views import timkiemhinhanh
app_name='home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('gioithieu/', views.gioithieu, name='giới thiệu'),
    path('cuahang/', views.cuahang, name='cửa hàng'),
    path('giohang/', views.giohang, name='giỏ hàng'),
    path('timkiem/', views.search, name='search'),
    path('chitiet/<int:id>', views.chitiet, name= 'chi tiết'),
    path('timkiemmoi/', views.timkiemmoi, name= 'trang tìm kiếm'),
    path('dangki/', views.dangki.as_view(), name= 'đăng kí'),
    path('dangnhap/', views.dangnhap.as_view(), name= 'đăng nhập'),
    path('chitietcuahang/<int:idch>', views.chitietcuahang, name= 'chi tiết cửa hàng'),
    path('timkiemanh/',views.timkiemhinhanh,name= 'tìm kiếm ảnh'),
    # path('update_item/', views.updateitem, name="update_item"),
    path('logout/',views.logoutUser, name="logout"),
    path('thongtindathang/',views.thongtindathang, name='thông tin đặt hàng'),
    path('dathang/',views.dathang, name='đặt hàng'),
    path('lichsudathang/', views.lichsudathang, name='lịch sử đặt hàng'),

    #add to cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
