from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Equipment, News, Field
from .forms import PetanqueBallForm, FieldForm, NewsForm


#Login
# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']

#         # ตรวจสอบรหัสผ่านตรงกัน
#         if password != confirm_password:
#             messages.error(request, 'รหัสผ่านไม่ตรงกัน')
#             return render(request, 'register.html')

#         # ตรวจสอบความยาวรหัสผ่าน (อย่างน้อย 8 ตัวอักษร)
#         if len(password) < 8:
#             messages.error(request, 'รหัสผ่านต้องมีความยาวอย่างน้อย 8 ตัวอักษร')
#             return render(request, 'register.html')

#         # ตรวจสอบว่า username เป็นอีเมล (ถ้าจำเป็น)
#         try:
#             validate_email(username)
#         except ValidationError:
#             messages.error(request, 'กรุณาใส่อีเมลที่ถูกต้อง')
#             return render(request, 'register.html')

#         # ตรวจสอบว่า username ไม่มีในระบบ
#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'ชื่อผู้ใช้มีอยู่แล้ว')
#             return render(request, 'register.html')

#         # สร้างผู้ใช้ใหม่
#         user = User.objects.create_user(username=username, password=password)
#         user.save()
#         messages.success(request, 'ลงทะเบียนผู้ใช้งานสำเร็จแล้ว')
#         return redirect('login')

#     return render(request, 'register.html')


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         # ตรวจสอบข้อมูลการล็อกอิน
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'เข้าสู่ระบบสำเร็จ')
#             return redirect('/')
#         else:
#             messages.error(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')

#     return render(request, 'login.html')


# def logout_view(request):
#     logout(request)
#     messages.success(request, 'ออกจากระบบสำเร็จแล้ว')
#     return redirect('login')


#********User*********

def homepage(request):
    return render(request,'homepage.html')

@login_required
def new(request):
    news_items = News.objects.all().order_by('-announcement_date')
    return render(request, 'new.html', {'news_items': news_items})

def field_user(request):
    fields = Field.objects.filter(status='available')
    return render(request,'field_user.html', {'fields': fields})

@login_required
def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment_list.html', {'equipments': equipments})

@login_required
def book_ball(request):
    if request.method == "POST":
        ball_id = request.POST.get('ball_id')
        ball = Equipment.objects.get(id=ball_id)

        if ball.status == 'available':
            ball.status = 'unavailable'
            ball.save()
            messages.success(request, f"จองลูกเปตอง {ball.name} สำเร็จ!")
        else:
            messages.error(request, "ลูกเปตองนี้ไม่สามารถจองได้!")
        
        return redirect('equipment_list')

def DashBoard(request):
    return render(request,'Admin manage/Admin Dashboard.html')

def AdUser(request):
    return render(request,'Admin manage/Admin user.html',{"q_user":User.objects.all()})

def Profile(request):
    return render(request,'Profile.html')

#*****************************************

#Admin User
def add_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        role = request.POST.get('role')

        # สร้างผู้ใช้ใหม่
        User.objects.create(first_name=first_name, phone_number=phone_number, email=email, role=role)
        messages.success(request, "เพิ่มผู้ใช้สำเร็จ!")
        return redirect('AdminUser')  # เปลี่ยนเป็นชื่อ path ของหน้า "จัดการผู้ใช้"

    return render(request, 'User/add_user.html')  # สร้าง template ชื่อ add_user.html

# แก้ไขผู้ใช้
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.phone_number = request.POST.get('phone_number')
        user.email = request.POST.get('email')
        user.role = request.POST.get('role')
        user.save()

        messages.success(request, "แก้ไขผู้ใช้สำเร็จ!")
        return redirect('AdminUser')  # เปลี่ยนเป็นชื่อ path ของหน้า "จัดการผู้ใช้"

    return render(request, 'User/edit_user.html', {'user': user})  # สร้าง template ชื่อ edit_user.html

# ลบผู้ใช้
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, "ลบผู้ใช้สำเร็จ!")
    return redirect('AdminUser')  # เปลี่ยนเป็นชื่อ path ของหน้า "จัดการผู้ใช้"

#************************************

#Admin Petanque
def petanque_list(request):
    balls = Equipment.objects.all()  # ดึงข้อมูลลูกเปตองทั้งหมด
    fields = Field.objects.all()
    return render(request, 'Admin manage/Admin Petanque.html', {'balls': balls , 'fields':fields})

def petanque_add(request):
    if request.method == 'POST':
        form = PetanqueBallForm(request.POST)
        if form.is_valid():
            form.save()  # บันทึกข้อมูลลงฐานข้อมูล
            return redirect('petanque_list')
    else:
        form = PetanqueBallForm()
    return render(request, 'Petanque/petanque_add.html', {'form': form})

def petanque_edit(request, id):
    ball = get_object_or_404(Equipment, id=id)
    if request.method == 'POST':
        form = PetanqueBallForm(request.POST, instance=ball)
        if form.is_valid():
            form.save()
            return redirect('petanque_list')
    else:
        form = PetanqueBallForm(instance=ball)
    return render(request, 'Petanque/petanque_edit.html', {'form': form})

def petanque_delete(request, id):
    ball = get_object_or_404(Equipment, id=id)
    if request.method == 'POST':
        ball.delete()  # ลบข้อมูลออกจากฐานข้อมูล
        return redirect('petanque_list')
    return render(request, 'Petanque/petanque_delete.html', {'ball': ball})

#*************************************************

def add_field(request):
    if request.method == "POST":
        form = FieldForm(request.POST, request.FILES)  # รับไฟล์และข้อมูล
        if form.is_valid():
            form.save()
            return redirect('petanque_list')  # เปลี่ยนไปยังหน้าหลักหลังเพิ่มสำเร็จ
    else:
        form = FieldForm()
    return render(request, 'field/add_field.html', {'form': form})

def edit_field(request, pk):
    field = Field.objects.get(pk=pk)
    if request.method == "POST":
        form = FieldForm(request.POST, request.FILES, instance=field)
        if form.is_valid():
            form.save()
            return redirect('petanque_list')
    else:
        form = FieldForm(instance=field)
    return render(request, 'field/edit_field.html', {'form': form})

def delete_field(request, pk):
    field = Field.objects.get(pk=pk)
    if request.method == "POST":
        field.delete()
        return redirect('petanque_list')
    return render(request, 'field/confirm_delete.html', {'field': field})

# *********************** Admin news
def news_list(request):
    news_items = News.objects.all()  # ดึงข้อมูลข่าวทั้งหมด
    return render(request, 'Admin manage/Admin news.html', {'news_items': news_items})



def edit_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = NewsForm(instance=news)
    return render(request, 'News/edit_news.html', {'form': form})


def delete_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == 'POST':
        news.delete()
        return redirect('news')
    return render(request, 'News/confirm_delete.html', {'news': news})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')  # หลังจากบันทึกแล้วให้กลับไปที่หน้ารายการข่าว
    else:
        form = NewsForm()
    return render(request, 'News/add_news.html', {'form': form})


#************test login*************
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"