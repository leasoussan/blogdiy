from django import forms
from django.forms import ModelForm
from .models import DiyProject,



class AddDiyProject(ModelForm):

    class Meta:
        model = DiyProject
        exclude = ['user']
