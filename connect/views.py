from django.shortcuts import render
from connect.models import user_info
from django.db.models import Q

def connect(request):
    city = user_info.objects.get(user=request.user).city
    nearby_users = user_info.objects.filter(~Q(user=request.user)).filter(city=city)
    print(nearby_users)
    return render(request, 'connect/connect.html', {'users': nearby_users})