from django.forms import ModelForm, ModelChoiceField
from django import forms
from .models import Scp, Tales, Profile, Canon
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from datetime import datetime
from django_quill.forms import QuillFormField

class CanonModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name
class QuillFieldForm(forms.Form) :
    content = QuillFormField()
class RegisterForm(UserCreationForm):
    summary = forms.CharField(max_length=250, widget=forms.Textarea)
    class Meta:
        model = Profile
        fields = ("username", "summary", "email")
class EditUserForm(UserChangeForm):
    summary = forms.CharField(max_length=250)
    username = forms.CharField(max_length=254, required=False)
    password=None
    class Meta:
        model = Profile
        exclude = ("password1", "password2")
        fields = ("username", "summary",)
        help_text=""
class Scp_Form(ModelForm):
    title = forms.CharField(max_length=50, required=True)
    number = forms.IntegerField(required=True)
    body = QuillFieldForm()
    canon = CanonModelChoiceField(queryset=Canon.objects.all())
    class Meta:
        model = Scp
        fields=['title','number','canon','body']
class Edit_Scp_Form(ModelForm):
    title = forms.CharField(max_length=50, required=False)
    number = forms.IntegerField(required=False)
    body = QuillFieldForm()
    canon = CanonModelChoiceField(queryset=Canon.objects.all())
    class Meta:
        model = Scp
        fields=['title','number','canon','body']
class Tale_Form(ModelForm):
    title = forms.CharField(max_length=50)
    body = QuillFieldForm()
    canon = CanonModelChoiceField(queryset=Canon.objects.all())
    class Meta:
        model = Tales
        fields = ['title','canon','body']
class Edit_Tale_Form(ModelForm):
    title = forms.CharField(max_length=50, required=False)
    canon = CanonModelChoiceField(queryset=Canon.objects.all())
    body = QuillFieldForm()
    class Meta:
        model = Tales
        fields =['title','canon','body']