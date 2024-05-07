from django.shortcuts import render
from .models import MenuItem

def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'templates/menu_list.html', {'items': items})
