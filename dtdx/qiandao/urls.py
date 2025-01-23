from django.urls import path
from qiandao import views


urlpatterns = [
    path('', views.main),
]