# Generated by Django 3.2.5 on 2021-07-07 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('h', 'hobbie'), ('i', 'intermediate'), ('a', 'advance')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_type', models.CharField(choices=[('m', 'manual'), ('st', 'strenght'), ('mnip', 'manipulations')], max_length=10)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ToolsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('extra_details', models.TextField()),
                ('safty', models.CharField(choices=[('s', 'secure'), ('ks', 'kids_secure'), ('d', 'dangerous')], default='s', max_length=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogdiy.toolscategory')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogdiy.category')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='media/image/default.png', null=True, upload_to='images/')),
                ('file_rsc', models.FileField(blank=True, null=True, upload_to='')),
                ('text', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiyProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('time_to_complete', models.PositiveIntegerField()),
                ('completed', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='blogdiy.Category')),
                ('difficulty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogdiy.level')),
                ('required_skills', models.ManyToManyField(to='blogdiy.Skills')),
                ('required_tools', models.ManyToManyField(related_name='required_skills', to='blogdiy.Tools')),
                ('resources', models.ManyToManyField(blank=True, to='blogdiy.Resource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
