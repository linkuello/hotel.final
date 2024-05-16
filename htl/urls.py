from django.contrib import admin
from django.urls import path, include
from views import views
# Уточните, из какого приложения импортируются представления
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),  # Добавлен аргумент name для удобства использования в шаблонах
    path('room/', views.Room, name='room'),
    path('book/<str:room>/<str:in_d>/<str:out_d>/<str:details>', views.Book, name='book'),
    path('list_booked/', views.list_booked, name='list_booked'),
    path('debook/<str:room>', views.deBook, name='debook'),
    path('nav/', include('nav.urls')),  # Подключение URL из приложения nav
    path('i18n/', include('django.conf.urls.i18n')),  # URL-адреса для смены языка
    path('rooms/', include('rooms.urls')),

]
