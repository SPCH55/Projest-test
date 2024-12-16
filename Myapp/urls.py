from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('new/',views.new,name='new'),
    path('booking/',views.booking,name='booking'),
    path('equipments/', views.equipment_list, name='equipment_list'),
    path('book_ball/', views.book_ball, name='book_ball'),
    path('Admin Dashboard/', views.DashBoard, name='DashBoard'),
    path('Admin news/', views.News, name='news'),
    path('Admin Petanque/', views.Petanque, name='petanque'),
    path('Admin User/', views.AdUser, name='AdminUser'),

]
