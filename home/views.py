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

            mapping = {'c??y th??ng m???c': 0, 'c??y trinh n???': 1, 'c??y rau sam': 2, 'c??y x??? ??en': 3, 'c??y s??i r???ng': 4,
                       'c??y rau m??': 5,
                       'c??y trinh n??? ho??ng cung': 6, 'c??y t???i': 7, 'c??y ?? d??': 8, 'c??y se': 9, 'c??y m??ng c???u': 10,
                       'c??y l???c l???c kh??ng cu???ng': 11, 'c??y ngh??? v??ng': 12, 'c??y ?? liu': 13, 'c??y kim ng??n hoa': 14,
                       'c??y l?????c v??ng': 15,
                       'c??y kha t???': 16, 'c??y n???m linh chi': 17, 'c??y ngh??? ??en': 18, 'c??y nha ??am': 19,
                       'c??y hoa x?? thi???t th???o': 20, 'c??y h??m ???ch': 21, 'c??y g???c': 22, 'c??y d???a c???n': 23, 'c??y c??c ??o': 24,
                       'c??y ho??ng c???m r??u': 25, 'c??y di???p c??': 26, 'c??y b??? k???t': 27, 'c??y ??u ?????': 28, 'c??y b??? qu??n': 29,
                       'c??y b??? ho??ng': 30, 'c??y b???ch tru???t': 31, 'c??y b??? c??ng anh': 32, 'c??y b???ch ?????u ??ng': 33}
            reverse_mapping = {0: 'c??y th??ng m???c', 1: 'c??y trinh n???', 2: 'c??y rau sam', 3: 'c??y x??? ??en', 4: 'c??y s??i r???ng',
                               5: 'c??y rau m??',
                               6: 'c??y trinh n??? ho??ng cung', 7: 'c??y t???i', 8: 'c??y ?? d??', 9: 'c??y se', 10: 'c??y m??ng c???u',
                               11: 'c??y l???c l???c kh??ng cu???ng', 12: 'c??y ngh??? v??ng', 13: 'c??y ?? liu', 14: 'c??y kim ng??n hoa',
                               15: 'c??y l?????c v??ng',
                               16: 'c??y kha t???', 17: 'c??y n???m linh chi', 18: 'c??y ngh??? ??en', 19: 'c??y nha ??am',
                               20: 'c??y hoa x?? thi???t th???o', 21: 'c??y h??m ???ch', 22: 'c??y g???c', 23: 'c??y d???a c???n',
                               24: 'c??y c??c ??o',
                               25: 'c??y ho??ng c???m r??u', 26: 'c??y di???p c??', 27: 'c??y b??? k???t', 28: 'c??y ??u ?????',
                               29: 'c??y b??? qu??n',
                               30: 'c??y b??? ho??ng', 31: 'c??y b???ch tru???t', 32: 'c??y b??? c??ng anh', 33: 'c??y b???ch ?????u ??ng'}

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

        mapping = {'c??y th??ng m???c': 0, 'c??y trinh n???': 1, 'c??y rau sam': 2, 'c??y x??? ??en': 3, 'c??y s??i r???ng': 4, 'c??y rau m??': 5,
                   'c??y trinh n??? ho??ng cung': 6, 'c??y t???i': 7, 'c??y ?? d??': 8, 'c??y se': 9, 'c??y m??ng c???u': 10,
                   'c??y l???c l???c kh??ng cu???ng': 11, 'c??y ngh??? v??ng': 12, 'c??y ?? liu': 13, 'c??y kim ng??n hoa': 14, 'c??y l?????c v??ng': 15,
                   'c??y kha t???': 16, 'c??y n???m linh chi': 17, 'c??y ngh??? ??en': 18, 'c??y nha ??am': 19,
                   'c??y hoa x?? thi???t th???o': 20, 'c??y h??m ???ch': 21, 'c??y g???c': 22, 'c??y d???a c???n': 23, 'c??y c??c ??o': 24,
                   'c??y ho??ng c???m r??u': 25, 'c??y di???p c??': 26, 'c??y b??? k???t': 27, 'c??y ??u ?????': 28, 'c??y b??? qu??n': 29,
                   'c??y b??? ho??ng': 30, 'c??y b???ch tru???t': 31, 'c??y b??? c??ng anh': 32, 'c??y b???ch ?????u ??ng': 33}
        reverse_mapping = {0: 'c??y th??ng m???c', 1: 'c??y trinh n???', 2: 'c??y rau sam', 3: 'c??y x??? ??en', 4: 'c??y s??i r???ng',
                           5: 'c??y rau m??',
                           6: 'c??y trinh n??? ho??ng cung', 7: 'c??y t???i', 8: 'c??y ?? d??', 9: 'c??y se', 10: 'c??y m??ng c???u',
                           11: 'c??y l???c l???c kh??ng cu???ng', 12: 'c??y ngh??? v??ng', 13: 'c??y ?? liu', 14: 'c??y kim ng??n hoa',
                           15: 'c??y l?????c v??ng',
                           16: 'c??y kha t???', 17: 'c??y n???m linh chi', 18: 'c??y ngh??? ??en', 19: 'c??y nha ??am',
                           20: 'c??y hoa x?? thi???t th???o', 21: 'c??y h??m ???ch', 22: 'c??y g???c', 23: 'c??y d???a c???n', 24: 'c??y c??c ??o',
                           25: 'c??y ho??ng c???m r??u', 26: 'c??y di???p c??', 27: 'c??y b??? k???t', 28: 'c??y ??u ?????', 29: 'c??y b??? qu??n',
                           30: 'c??y b??? ho??ng', 31: 'c??y b???ch tru???t', 32: 'c??y b??? c??ng anh', 33: 'c??y b???ch ?????u ??ng'}

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
            return HttpResponse('????ng k?? kh??ng th??nh c??ng')


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
            return HttpResponse('????ng nh???p kh??ng th??nh c??ng')

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
        return redirect('?????t h??ng')
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
    return redirect("c???a h??ng")


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





