from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('scp/<int:scp_number>/', views.scp_show, name='scp_show'),
    path('scp/new/', views.scp_new, name='scp_new'),
    path('tale/<int:tale_id>/', views.tale_show, name='tale_show'),
    path('tale/new/', views.tale_new, name='tale_show'),
]