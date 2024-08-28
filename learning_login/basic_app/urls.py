from django.contrib import admin
from django.urls import path,include
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
   
    path('registration/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
