from django.contrib import admin
from django.urls import path, include
from main import views


urlpatterns = [

    path('admin/', include("django_admin_kubi.urls")),

    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
