from django.conf.urls import url
from . import views

app_name = "connect"
   
urlpatterns = [
    url(r'^$', views.connect, name="home")
]
