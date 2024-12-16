from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'ชื่อผู้ใช้มีอยู่แล้ว')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'ลงทะเบียนผู้ใช้งานสำเร็จแล้ว')
                return redirect('login')
        else:
            messages.error(request, 'รหัสผ่านไม่ตรงกัน')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'ข้อมูลประจำตัวไม่ถูกต้อง')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'ออกจากระบบสำเร็จแล้ว')
    return redirect('login')

def homepage(request):
    return render(request,'homepage.html')

def new(request):
    return render(request,'new.html')

def booking(request):
    return render(request,'booking.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Equipment, User

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

def News(request):
    return render(request,'Admin manage/Admin News.html')

def Petanque(request):
    return render(request,'Admin manage/Admin Petanque.html')

def AdUser(request):
    
    return render(request,'Admin manage/Admin user.html',{"q_user":User.objects.all()})