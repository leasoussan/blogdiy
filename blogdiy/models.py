from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save
from django.contrib.contenttypes.fields import GenericRelation
from datetime import datetime, timedelta
from accounts.models import MyUser, Bloger, Business
from django.utils.translation import ugettext_lazy as _

from extra.models import DiscussionModel


class Skills(models.Model):
    SKILL_TYPE = [
        ('m', _('manual')),
        ('st', _('strenght')),
        ('mnip', _('manipulations'))
    ]
    LEVEL_CHOICE=[
        ('h', _('hobbie')),
        ('i', _('intermediate')),
        ('a', _('advance')),
    ]
    level = models.CharField(max_length=50, choices=LEVEL_CHOICE)
    skill_type =models.CharField(max_length=10, choices=SKILL_TYPE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Subject{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return f"Subject{self.name}"



class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"Subject{self.name}"





class Resource(models.Model):

    name = models.CharField(max_length=200)
    link = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(default='media/image/default.png', upload_to='images/', null=True, blank=True)
    file_rsc = models.FileField(null=True, blank=True)
    text = models.TextField()
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)



    def __str__(self):
        return f"Subject{self.name}"




class ToolsCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Subject{self.name}"


class Tools(models.Model):
    SAFTY_CHOICES =[
        ('s', _('secure')),
        ('ks', _('kids_secure')),
        ('d', _('dangerous'))
    ]
    name = models.CharField(max_length=50)
    extra_details = models.TextField()
    safty= models.CharField(max_length=5, choices=SAFTY_CHOICES, default='s')
    category = models.ForeignKey(ToolsCategory, on_delete=models.CASCADE)
    def __str__(self):
        return f"Subject{self.name}"


class DiyTask(DiscussionModel):
    STAGE_CHOICE = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
    )

    LEVEL_CHOICE=[
        ('h', _('hobbie')),
        ('i', _('intermediate')),
        ('a', _('advance')),
    ]
    level = models.CharField(max_length=50, choices=LEVEL_CHOICE)
    stage = models.CharField(max_length=10, choices=STAGE_CHOICE, default='start')
    name = models.CharField(max_length=200)
    description = models.TextField()
    resources = models.ManyToManyField(Resource, blank=True)
    required_skill = models.ManyToManyField(Skills, blank=True)
    created_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Subject{self.name}"

    def get_absolute_url(self):
        return reverse('diy_detail',  kwargs ={'pk':self.id})



class DiyProject(DiscussionModel):
    LEVEL_CHOICE=[
        ('h', _('hobbie')),
        ('i', _('intermediate')),
        ('a', _('advance')),
    ]
    level = models.CharField(max_length=50, choices=LEVEL_CHOICE)

    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    description = models.TextField()
    required_tools = models.ManyToManyField(Tools, related_name="required_skills")
    required_skills = models.ManyToManyField(Skills, blank=True)
    time_to_complete = models.PositiveIntegerField()
    category = models.ManyToManyField(Category)
    resources = models.ManyToManyField(Resource, blank=True)
    user = models.ForeignKey(Bloger, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(DiyTask, blank=True)

    def __str__(self):
        return f"Subject{self.name}"

    def get_absolute_url(self):
        return reverse('diy_detail',  kwargs ={'pk':self.id})