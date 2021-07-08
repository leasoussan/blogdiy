import django
# os to interact with computer
import os
from faker import Faker
import random
# setting the env
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
# this line will check for the setting to know where to save it
django.setup()
# after the above step >> we can import models
from accounts.models import *
from blogdiy.models import *

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model





countries =['Israel', 'France', 'United Kingdom' , 'United State' ]
def pop_country():
    for country in countries:
        country = Country.objects.get_or_create(name=country)

        print(f"the Country  {country} was created")



def pop_city():
    city1 = City.objects.get_or_create(name='tel-aviv', country = Country.objects.filter(name='Israel')[0]),
    city2 = City.objects.get_or_create(name='paris', country=Country.objects.filter(name='France')[0]),
    print(f"the City  {city1}  {city2}was created")






skills_list = ['paint', 'cut_wood', 'hardware', 'liquid_materials', 'craftsman']
skills_type_list =['m', 'st', 'mnip']
level_choice = ['h', 'i', 'a']
def pop_skills(skills_list):

    for skill in skills_list:
        skill_type = random.choice(skills_type_list),
        level = random.choice(level_choice),
        skill = Skills.objects.get_or_create(
            name = skill,
            skill_type = skill_type,
            level=level_choice,
        )

        print(f'Skill:{skills_list} was created')



cat_list = ['kitchen', 'furnitures', 'bathroom', 'homeDecor', 'design', 'gardening']

def pop_category():
    for cat in cat_list:
        name = cat
        cat = Category.objects.get_or_create(name=name)

        print(f' category{cat} was created')



#
pop_country()

pop_city()

pop_skills(skills_list)

pop_category()