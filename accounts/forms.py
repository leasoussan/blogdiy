from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import Form
from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import MyUser
import django.forms.widgets
from django.contrib.auth import get_user_model



class MyUserCreationForm(UserCreationForm):
    USER_TYPE = [
        ('is_bloger', _('bloger')),
        ]
    usertype = forms.ChoiceField(choices=USER_TYPE, label='registration_type')
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2', 'language_code']

        #   labels ={
        #     'language_code': 'Language'
        # }



class BlogerProfileCreationForm(forms.ModelForm):
    pass




class BusinessProfileCreateForm(forms.ModelForm):
    pass




class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'profile_pic',
            'city']
