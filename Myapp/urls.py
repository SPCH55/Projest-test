from django.urls import path, include
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from .views import SignUpView
urlpatterns = [
    path('',views.homepage, name='home'),
    # path('register/', views.register, name='register'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    path('new/',views.new,name='new'),
    path('booking/',views.field_user,name='booking'),
    path('equipments/', views.equipment_list, name='equipment_list'),
    path('book_ball/', views.book_ball, name='book_ball'),
    path('Admin Dashboard/', views.DashBoard, name='DashBoard'),
    # path('Admin news/', views.News, name='news'),
    path('Admin Petanque/', views.petanque_list, name='petanque_list'),
    path('Admin User/', views.AdUser, name='AdminUser'),
    path('Profile User/', views.Profile, name='Profile'),
    
    path('add_user/', views.add_user, name='add_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

    path('petanque-add/', views.petanque_add, name='petanque_add'),
    path('petanque-edit/<int:id>/', views.petanque_edit, name='petanque_edit'),
    path('petanque-delete/<int:id>/', views.petanque_delete, name='petanque_delete'),

    # path('fields/', views.field_list, name='field_list'),

    path('fields/add/', views.add_field, name='add_field'),  # เพิ่มสนาม
    path('fields/edit/<int:pk>/', views.edit_field, name='edit_field'),  # แก้ไขสนาม
    path('fields/delete/<int:pk>/', views.delete_field, name='delete_field'),  # ลบสนาม

    path('Admin news/', views.news_list, name='news'),
    path('news/edit/<int:news_id>/', views.edit_news, name='edit_news'),
    path('news/delete/<int:news_id>/', views.delete_news, name='delete_news'),
    path('news/add/', views.add_news, name='add_news'),

    path("signup/", SignUpView.as_view(), name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
