from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Canon, Scp, Tales
# Register your models here.
UserAdmin.list_display = ('username', 'email', 'is_active', 'date_joined', 'is_staff')
admin.site.register(Profile, UserAdmin) 
admin.site.register(Scp)
admin.site.register(Tales)
admin.site.register(Canon)
