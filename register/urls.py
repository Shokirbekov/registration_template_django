from django.contrib import admin
from django.urls import path
from login.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginview),
    path('register/', registerview),
    path('home/', home),
    path('logout/', logoutview),
]
