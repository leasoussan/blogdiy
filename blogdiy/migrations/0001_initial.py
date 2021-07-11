
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
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
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('h', 'hobbie'), ('i', 'intermediate'), ('a', 'advance')], max_length=50)),
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
            name='DiyTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('h', 'hobbie'), ('i', 'intermediate'), ('a', 'advance')], max_length=50)),
                ('stage', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='start', max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('required_skill', models.ManyToManyField(blank=True, to='blogdiy.Skills')),
                ('resources', models.ManyToManyField(blank=True, to='blogdiy.Resource')),
            ],
        ),
        migrations.CreateModel(
            name='DiyProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('h', 'hobbie'), ('i', 'intermediate'), ('a', 'advance')], max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('time_to_complete', models.PositiveIntegerField()),
                ('category', models.ManyToManyField(to='blogdiy.Category')),
                ('required_skills', models.ManyToManyField(blank=True, to='blogdiy.Skills')),
                ('required_tools', models.ManyToManyField(related_name='required_skills', to='blogdiy.Tools')),
                ('resources', models.ManyToManyField(blank=True, to='blogdiy.Resource')),
                ('tasks', models.ManyToManyField(blank=True, to='blogdiy.DiyTask')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.bloger')),
            ],
        ),
    ]
