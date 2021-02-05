from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('scp/<int:scp_number>/', views.scp_show, name='scp_show'),
    path('tale/<int:tale_number>/', views.scp_show, name='tale_show'),
]