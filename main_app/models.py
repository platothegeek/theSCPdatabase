from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import AbstractUser, User
import django.utils.timezone
from django_quill.fields import QuillField

# Create your models here.
class Profile(AbstractUser):
    email = models.CharField(max_length=50)
    summary =  models.CharField(max_length=250)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
class Canon(models.Model):
    name = models.CharField(max_length=500)
    summary = models.CharField(max_length=50000)
class Scp(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    number = models.IntegerField(unique=True)
    body = QuillField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="scps", default=1)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
    canon = models.ForeignKey(Canon, on_delete=models.CASCADE, related_name="scps", default=1)
class Tales(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="tales", default=1)
    body = QuillField()
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
    canon = models.ForeignKey(Canon, on_delete=models.CASCADE, related_name="tales", default=1)