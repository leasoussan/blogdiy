
import django
# os to interact with computer
import os

from django.utils import timezone
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
from django.core.exceptions import ObjectDoesNotExist

from django.forms.models import model_to_dict

import json
import urllib
import requests

fak = Faker()


MyUser = get_user_model()

# longitude = -80.191788
# latitude = 25.761681
#
# user_location = Point(longitude, latitude, srid=4326)
#


def pop_business(n):
    business_name = ['store1', 'store2', 'store3']
    if Business.objects.count() ==0:
        for i in range(n):
            user = MyUser.objects.create_user(
                first_name=fak.first_name(),
                last_name=fak.last_name(),
                email=f'artizen18+bs{i}@gmail.com',
                username=fak.user_name(),
                password='123456',
                phone_number='+972 500000000',
                profile_pic='media/profile/avatar.png',
                city=City.objects.get(name='tel-aviv'),
                is_business=True,

            )

            user.save()
            business = Business.objects.create(
                user=user,
                name = random.choice(business_name),
                category = random.choice(Category.objects.all()),
                profile_pic = 'images/default.png',
                address = 'undefine Adress yet',
                website = 'www.google.com',
                description = 'School for the people',
                location = [-80.191788, 25.761681]
            )



            business.save()

            print(f"the Business  {business} was created")





def pop_blogers(n):
    if Bloger.objects.count() ==0:
        for bl in range(n):
            user = MyUser.objects.create_user(
                first_name=fak.first_name(),
                last_name=fak.last_name(),
                email=f'artizen18+bl{bl}@gmail.com',
                username=fak.user_name(),
                password='123456',
                phone_number='+972 500000000',
                profile_pic='media/profile/avatar.png',
                city=City.objects.get(name='tel-aviv'),
                is_business=True,
            )

            user.save()
            bloger = Bloger.objects.create(
                user=user,
            )
            bloger.save()

            print(f"the Business  {bloger} was created")



tool_category_list=['hardware', 'kitchen_wear', 'garden', 'arts_craft', 'jewleries', 'paint']
def pop_toll_cat():
    if ToolsCategory.objects.count() ==0:
        for category in tool_category_list:
            cat_name = random.choice(tool_category_list)
            cat = ToolsCategory.objects.get_or_create(name =cat_name)

            print(f'The Tools Category{category} was created')


safty_choice =['s','ks''d']

def pop_tools(n):
    if Tools.objects.count() ==0:
        for tool in range(n):
            tool_cat = random.choice(ToolsCategory.objects.all())
            tool_obj = Tools.objects.get_or_create(
                name = f'Tool{tool}',
                extra_details ="some other details on manipulation etc",
                safty = random.choice(safty_choice),
                category = tool_cat,
            )

            print(f'The Tool {tool} was created')




def pop_resources(n):
    if Resource.objects.count() == 0:
        for r in range(n):
            name = f'Resource {r}'
            link = "www.google.com"
            image =  'image/default.png'
            file_rsc = 'null'
            text = 'This is aresource about.......'
            owner = random.choice(MyUser.objects.all())


            r = Resource(name=name, link=link, image=image, file_rsc=file_rsc, text=text,owner=owner)
            r.save()
            print(f'resource :{r.name} was created')

        print(f"Finished...{n} Resource populated.")








stages_choice =10
level_choice=['h', 'i', 'a' ]

def pop_tasks(stages):
    for stage in range(stages):
        level =random.choice(level_choice)
        created_date =timezone.now()

        task = DiyTask(
            level=level,
            stage=stage,
            name='Here is what you have to do next',
            description = 'here is how you ll do it next',
            created_date = created_date,
        )
        task.save()
        required_skills = list(Skills.objects.all())
        resources = list(Resource.objects.all())
        task.required_skill.add(*random.sample(required_skills, 2))
        task.resources.add(*random.sample(resources, 2))
        print(f'task was {stage}created')




levels = ['beginner', 'intermidiate', 'advanced']
bool = [True, False]

def pop_project(n):
    if DiyProject.objects.count() == 0:
        for project in range(n):
            name = f"DiY  {project}"
            title = "Welcome to Blogdiy Project "
            description = "This Project is about Blbalabal"
            time_to_complete = random.randrange(60, 120, 10)
            # user = random.choice(Bloger.objects.all()),

            p = DiyProject(
                name = name,
                title =title,
                description = description,
                time_to_complete =time_to_complete,
                level = random.choice(levels),
                user=random.choice(Bloger.objects.all()),
            )
            p.save()

            required_tools = list(Tools.objects.all())
            required_skills = list(Skills.objects.all())
            category = list(Category.objects.all())
            resources = list(Resource.objects.all())
            tasks = list(DiyTask.objects.all())
            p.required_tools.add(*random.sample(required_tools, 2))
            p.required_skills.add(*random.sample(required_skills,2))
            p.category.add(*random.sample(category,2))
            p.resources.add(*random.sample(resources, 2))
            p.tasks.add(*random.sample(tasks, 2))

            print(f'Project:{p.id}')
            print(f"Finished...{n} Projects populated.")


pop_business(4)

pop_blogers(10)

pop_resources(20)
pop_toll_cat()
pop_tools(20)

pop_resources(20)
pop_tasks(stages_choice)


pop_project(10)
