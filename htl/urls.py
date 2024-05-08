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
    path('i18n/', include('django.conf.urls.i18n')),


]
