# Generated by Django 3.2.5 on 2021-07-08 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_bloger_business'),
        ('blogdiy', '0003_remove_resource_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diyproject',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.bloger'),
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
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.bloger')),
                ('required_skill', models.ManyToManyField(blank=True, to='blogdiy.Skills')),
                ('resources', models.ManyToManyField(blank=True, to='blogdiy.Resource')),
            ],
        ),
        migrations.AddField(
            model_name='diyproject',
            name='tasks',
            field=models.ManyToManyField(to='blogdiy.DiyTask'),
        ),
    ]
