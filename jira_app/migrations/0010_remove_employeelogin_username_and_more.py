# Generated by Django 5.0.6 on 2024-11-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jira_app', '0009_alter_employeelogin_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeelogin',
            name='username',
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='username',
            field=models.CharField(max_length=25, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='employeelogin',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
