
from django.contrib import admin
from django.urls import path,include
from message import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('articles/',include('message.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/register',views.register, name='register')
   
]
