"""htl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an im im import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from views import views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('room', views.Room),
    path('book/<str:room>/<str:in_d>/<str:out_d>/<str:details>',views.Book),
    path('list_booked', views.list_booked),
    path('debook/<str:room>', views.deBook),
    path('nav/', include('nav.urls')),
    path('rooms/', include('rooms_1.urls')),

]
