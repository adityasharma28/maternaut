from django.shortcuts import render

def connect(request):
    return render(request, 'connect/connect.html')