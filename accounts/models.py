# import secrets

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse
import datetime
from django.utils.translation import ugettext_lazy as _



# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


# email had to be cahnged to login with email

class MyUser(AbstractUser):
    """ Basic User is the base of all users- using Django Implementation"""

    email = models.EmailField()
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    profile_pic = models.ImageField(default='profile/avatar.png', upload_to='media/profile/', blank=True, null=True)
    joined_date = models.DateField(auto_now_add=True, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    language_code = models.CharField(_('language'), choices=settings.LANGUAGES, default='en', max_length=50)
    is_bloger = models.BooleanField(default=False)
    is_business = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.id},{str(self.username)}, {self.email}"

    def get_user_type(self):
        user_type = {
            'is_bloger': Bloger,
            'is_business': Business,
        }

        for key, value in user_type.items():

            if value.objects.filter(user=self).exists():
                return key

    def profile(self):
        types = [Bloger, Business]

        for value in types:
            qs = value.objects.filter(user=self)
            if qs.exists():
                return qs.first()

    def profilepic_or_default(self, default_path='media/profile/avatar.png'):
        if self.profile_pic:
            return self.profile_pic.url
        return default_path


class Bloger(models.Model):
    LEVEL_CHOICE = [
        ('h', _('hobbie')),
        ('i', _('intermediate')),
        ('a', _('advance')),
    ]
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICE)
    def __str__(self):
        return f'{self.user.username}'

    # # to be able to call it as class name in lower case
    # def name(self):
    #     return self.__class__.__name__.lower()


class Business(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    category = models.ForeignKey('blogdiy.Category', on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='profile/avatar.png', upload_to='media/profile/', blank=True, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField()
    description = models.TextField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

    # # to be able to call it as class name in lower case
    #
    # def name(self):
    #     return self.__class__.__name__.lower()
