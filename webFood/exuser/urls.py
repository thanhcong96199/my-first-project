from django.urls import path, include
from exuser import views

app_name = 'exuser'

urlpatterns = [
    path('', views.home, name='home')
]