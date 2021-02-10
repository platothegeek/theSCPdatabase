from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('scp/<int:scp_number>/', views.scp_show, name='scp_show'),
    path('scp/new/', views.scp_new, name='scp_new'),
    path('scp/', views.scp_index, name='scp_index'),
    path('tale/<int:tale_id>/', views.tale_show, name='tale_show'),
    path('tale/new/', views.tale_new, name='tale_new'),
    path('staff/self', views.staff_self, name='tale_new'),
    path('staff/new/', views.staff_new, name='staff_new'),
    path('minor/', views.minor_index, name='minor_index'),
    path('minor/events/', views.minor_events, name='minor_events'),
    path('minor/locations/', views.minor_locations, name='minor_locations'),
    path('minor/items/', views.minor_items, name='minor_items'),
    path('minor/items/1/', views.minor_items1, name='minor_items1'),
    path('minor/items/2/', views.minor_items2, name='minor_items2'),
]