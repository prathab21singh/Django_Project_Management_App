# Generated by Django 5.0.6 on 2024-11-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jira_app', '0006_employeedetails_project_id_projectdetails_client_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='manager_id',
            field=models.IntegerField(null=True),
        ),
    ]