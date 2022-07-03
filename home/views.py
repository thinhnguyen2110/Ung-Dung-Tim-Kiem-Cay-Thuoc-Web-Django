from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from .models import thongtin as thongtinbai
from .models import sanpham as spcuahang
from .models import thongtindathang as ttdathang
from .models import DatHang1
from .forms import FormDangKi, FormDangNhap
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.http.response import JsonResponse
import json
# from .models import uploadImage
# from .forms import UserImage
import tensorflow as tf
from keras.models import load_model
from django.views.generic import CreateView
from tensorflow.keras.models import load_model
from django.urls import reverse_lazy
from tensorflow.keras.preprocessing.image import load_img,img_to_array
import numpy as np
from django.core.files.storage import default_storage
import cv2
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.
model = load_model('Model31-28102021.h5')
def index(request):
    tt = thongtinbai.objects.all().order_by('-idthongtin')[:5]
    tt_slide = thongtinbai.objects.all().order_by('-idthongtin')[6:9]
    tt_timkiem = thongtinbai.objects.all().order_by('-idthongtin')[9:12]
    pb = thongtinbai.objects.all().order_by('-idthongtin')[1:4]
    context = {'tt':tt, 'tt_slide':tt_slide, 'tt_timkiem': tt_timkiem, 'pb':pb}
    request.session['cart'] = {}
    return render(request,"home/index.html",context)

def gioithieu(request):
    return  render(request,"home/gioithieu.html")

def cuahang (request):
        ch = spcuahang.objects.all().order_by('-masp')[:3]
        ch_1 = spcuahang.objects.all().order_by('-masp')[3:6]
        ch_2 = spcuahang.objects.all().order_by('-masp')[6:9]
        context = {'ch': ch, 'ch_1':ch_1, 'ch_2':ch_2}
        return  render(request, "home/cuahang.html", context)


def giohang(request):
    gh = spcuahang.objects.all()
    context = {'gh': gh}
    return  render(request, "home/giohang.html", context)

def search(request):
    tt_timkiem1 = thongtinbai.objects.all()
    # tt_timkiem2 = thongtinbai.objects.all().order_by('-idthongtin')[6:9]
    # tt_timkiem = thongtinbai.objects.all().order_by('-idthongtin')[9:12]
    context = {'tt_timkiem1':tt_timkiem1}
    return render(request, "home/timkiem.html", context)

def chitiet (request,id):
    try:
        ct = thongtinbai.objects.get(pk=id)
    except thongtinbai.DoesNotExist:
        raise Http404(" does not exist")
    return render(request,"home/chitietnoidung.html",{'ct':ct})

def chitietcuahang (request,idch):
    try:
        ctch = spcuahang.objects.get(pk=idch)
    except thongtinbai.DoesNotExist:
        raise Http404(" does not exist")
    return render(request,"home/chitietcuahang.html",{'ctch':ctch})

def timkiemmoi (request):
    if request.method == "POST":
        if request.POST['timkiembai']:
            timkiembai = request.POST['timkiembai']
            timkiemtt = thongtinbai.objects.filter(tieude__contains=timkiembai)
            return render(request, "home/timkiem.html",
                          {'timkiembai': timkiembai, 'timkiemtt': timkiemtt})
        elif request.FILES['imageFile']:
            timkiemhinh = request.FILES['imageFile']
            file_name = default_storage.save(timkiemhinh.name, timkiemhinh)
            file_url = default_storage.path(file_name)

            mapping = {'cây thông mộc': 0, 'cây trinh nữ': 1, 'cây rau sam': 2, 'cây xạ đen': 3, 'cây sói rừng': 4,
                       'cây rau má': 5,
                       'cây trinh nữ hoàng cung': 6, 'cây tỏi': 7, 'cây ý dĩ': 8, 'cây se': 9, 'cây mãng cầu': 10,
                       'cây lục lạc không cuống': 11, 'cây nghệ vàng': 12, 'cây ô liu': 13, 'cây kim ngân hoa': 14,
                       'cây lược vàng': 15,
                       'cây kha tử': 16, 'cây nấm linh chi': 17, 'cây nghệ đen': 18, 'cây nha đam': 19,
                       'cây hoa xà thiệt thảo': 20, 'cây hàm ếch': 21, 'cây gấc': 22, 'cây dừa cạn': 23, 'cây cúc áo': 24,
                       'cây hoàng cầm râu': 25, 'cây diếp cá': 26, 'cây bồ kết': 27, 'cây đu đủ': 28, 'cây bồ quân': 29,
                       'cây bồ hoàng': 30, 'cây bạch truật': 31, 'cây bồ công anh': 32, 'cây bạch đầu ông': 33}
            reverse_mapping = {0: 'cây thông mộc', 1: 'cây trinh nữ', 2: 'cây rau sam', 3: 'cây xạ đen', 4: 'cây sói rừng',
                               5: 'cây rau má',
                               6: 'cây trinh nữ hoàng cung', 7: 'cây tỏi', 8: 'cây ý dĩ', 9: 'cây se', 10: 'cây mãng cầu',
                               11: 'cây lục lạc không cuống', 12: 'cây nghệ vàng', 13: 'cây ô liu', 14: 'cây kim ngân hoa',
                               15: 'cây lược vàng',
                               16: 'cây kha tử', 17: 'cây nấm linh chi', 18: 'cây nghệ đen', 19: 'cây nha đam',
                               20: 'cây hoa xà thiệt thảo', 21: 'cây hàm ếch', 22: 'cây gấc', 23: 'cây dừa cạn',
                               24: 'cây cúc áo',
                               25: 'cây hoàng cầm râu', 26: 'cây diếp cá', 27: 'cây bồ kết', 28: 'cây đu đủ',
                               29: 'cây bồ quân',
                               30: 'cây bồ hoàng', 31: 'cây bạch truật', 32: 'cây bồ công anh', 33: 'cây bạch đầu ông'}

            def mapper(value):
                return reverse_mapping[value]

            image = load_img(file_url, target_size=(180, 180))

            image = img_to_array(image)
            image = image / 255.0
            prediction_image = np.array(image)
            prediction_image = np.expand_dims(image, axis=0)

            prediction = model.predict(prediction_image)
            value = np.argmax(prediction)
            move_name = mapper(value)
            print(move_name)
            timkiemanh = thongtinbai.objects.filter(tieude__contains= move_name)
            return render(request, "home/timkiem.html",{ 'move_name':move_name,'timkiemanh':timkiemanh,'timkiemhinh':timkiemhinh})
        else:
            return render(request, "home/timkiem.html",{'timkiembai': timkiembai})

def timkiemhinhanh (request):
    if request.method == "POST":
        timkiemhinh = request.FILES['imageFile']
        file_name = default_storage.save(timkiemhinh.name, timkiemhinh)
        file_url = default_storage.path(file_name)

        mapping = {'cây thông mộc': 0, 'cây trinh nữ': 1, 'cây rau sam': 2, 'cây xạ đen': 3, 'cây sói rừng': 4, 'cây rau má': 5,
                   'cây trinh nữ hoàng cung': 6, 'cây tỏi': 7, 'cây ý dĩ': 8, 'cây se': 9, 'cây mãng cầu': 10,
                   'cây lục lạc không cuống': 11, 'cây nghệ vàng': 12, 'cây ô liu': 13, 'cây kim ngân hoa': 14, 'cây lược vàng': 15,
                   'cây kha tử': 16, 'cây nấm linh chi': 17, 'cây nghệ đen': 18, 'cây nha đam': 19,
                   'cây hoa xà thiệt thảo': 20, 'cây hàm ếch': 21, 'cây gấc': 22, 'cây dừa cạn': 23, 'cây cúc áo': 24,
                   'cây hoàng cầm râu': 25, 'cây diếp cá': 26, 'cây bồ kết': 27, 'cây đu đủ': 28, 'cây bồ quân': 29,
                   'cây bồ hoàng': 30, 'cây bạch truật': 31, 'cây bồ công anh': 32, 'cây bạch đầu ông': 33}
        reverse_mapping = {0: 'cây thông mộc', 1: 'cây trinh nữ', 2: 'cây rau sam', 3: 'cây xạ đen', 4: 'cây sói rừng',
                           5: 'cây rau má',
                           6: 'cây trinh nữ hoàng cung', 7: 'cây tỏi', 8: 'cây ý dĩ', 9: 'cây se', 10: 'cây mãng cầu',
                           11: 'cây lục lạc không cuống', 12: 'cây nghệ vàng', 13: 'cây ô liu', 14: 'cây kim ngân hoa',
                           15: 'cây lược vàng',
                           16: 'cây kha tử', 17: 'cây nấm linh chi', 18: 'cây nghệ đen', 19: 'cây nha đam',
                           20: 'cây hoa xà thiệt thảo', 21: 'cây hàm ếch', 22: 'cây gấc', 23: 'cây dừa cạn', 24: 'cây cúc áo',
                           25: 'cây hoàng cầm râu', 26: 'cây diếp cá', 27: 'cây bồ kết', 28: 'cây đu đủ', 29: 'cây bồ quân',
                           30: 'cây bồ hoàng', 31: 'cây bạch truật', 32: 'cây bồ công anh', 33: 'cây bạch đầu ông'}

        def mapper(value):
            return reverse_mapping[value]


        image = load_img(file_url, target_size=(180, 180))

        image = img_to_array(image)
        image = image / 255.0
        prediction_image = np.array(image)
        prediction_image = np.expand_dims(image, axis=0)

        prediction = model.predict(prediction_image)
        value = np.argmax(prediction)
        move_name = mapper(value)
        print(move_name)
        # print("{}.".format(move_name))
        timkiemanh = thongtinbai.objects.filter(tieude__contains=move_name)

        return render(request, "home/timkiem.html",{'timkiemhinh':timkiemhinh,'timkiemanh':timkiemanh,'move_name':move_name})
    else:
        return render(request, "home/timkiem.html")

    return render(request,"home/timkiem.html")

class dangki (View):
    def get(self, request):
        dk = FormDangKi
        return render(request,"home/dangki.html", {'dk':dk})

    def post (self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.save()
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Đăng ký không thành công')


class dangnhap(View):
    def get(self,request):
        dn = FormDangNhap
        return render(request, "home/dangnhap.html", {'dn': dn})

    def post (self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Đăng nhập không thành công')

def logoutUser(request):
	logout(request)
	return redirect('index')

@login_required(login_url="/dangnhap/")
def thongtindathang(request):
    if request.method == "POST":
        contact = ttdathang(
            hoten = request.POST.get('hoten'),
            sdt = request.POST.get('sdt'),
            email = request.POST.get('email'),
            diachi = request.POST.get('diachi'),
            xaphuong = request.POST.get('xaphuong'),
            quanhuyen = request.POST.get('quanhuyen'),
            tinhthanhpho =request.POST.get('tinhthanhpho'),
        )
        contact.save()
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk=uid)
        tendh = contact.hoten
        maildh = contact.email
        diachidh = contact.diachi
        xaphdh = contact.xaphuong
        qhuyedh = contact.quanhuyen
        thanhphodh = contact.tinhthanhpho
        sdtdh =contact.sdt
        print(tendh, cart, user)
        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            tongtien = a * b
            print(a)
            Order = DatHang1(
                usedathang = user,
                hinhdathang = cart[i]['image'],
                sanphamdathang = cart[i]['name'],
                soluongdathang = cart[i]['quantity'],
                giadathang = cart[i]['price'],
                tongtien = tongtien,
                tendathang = tendh,
                maildathang = maildh,
                diachidathang = diachidh,
                xaphdh = xaphdh,
                qhuyendh = qhuyedh,
                thanhphodh = thanhphodh,
                sdtdathang = sdtdh,

            )
            Order.save()
        return redirect('đặt hàng')
    else:
        return render(request,'home/thongtindathang.html')

@login_required(login_url="/dangnhap/")
def dathang(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk=uid)
    order = DatHang1.objects.filter(usedathang = user)
    orders = DatHang1.objects.last()
    cart = request.session.get('cart')
    print(orders)
    context ={'orders':orders, 'order':order, 'cart':cart}
    return render(request,'home/dathang.html',context)

@login_required(login_url="/dangnhap/")
def lichsudathang(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk=uid)
    order = DatHang1.objects.filter(usedathang=user)
    context = {'order': order}
    return render(request, 'home/lichsudathang.html',context)


#addcart

@login_required(login_url="/dangnhap/")
def cart_add(request,id):
    cart = Cart(request)
    product = spcuahang.objects.get(masp=id)
    cart.add(product=product)
    return redirect("cửa hàng")


@login_required(login_url="/dangnhap/")
def item_clear(request, id):
    cart = Cart(request)
    product = spcuahang.objects.get(masp=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/dangnhap/")
def item_increment(request,id):
    cart = Cart(request)
    product = spcuahang.objects.get(masp=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/dangnhap/")
def item_decrement(request,id):
    cart = Cart(request)
    product = spcuahang.objects.get(masp=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/dangnhap/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/dangnhap/")
def cart_detail(request):
    return render(request, 'home/cart_detail.html')





