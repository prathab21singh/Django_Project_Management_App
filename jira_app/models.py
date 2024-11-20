from django.db import models

# Create your models here.

class ClientDetails(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    location = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DepartmentDetails(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    manager_id = models.IntegerField()


class ProjectDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=500)
    budget = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EmployeeDetails(models.Model):

    #Choices for role
    role_choice = {
        'Software Developer':'Software Developer',
        'Intern' : 'Intern',
        'SQL Developer' : 'SQL Developer',
        'Business Analyst' : 'Business Analyst',
        'Junior Software Developer' : 'Junior Software Developer'
    }

    gender_choice = {
        'Male' : 'Male',
        'Female': 'Female'
    }

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=10, choices=gender_choice)
    role = models.CharField(max_length=25 ,choices=role_choice)
    department_id = models.ForeignKey(DepartmentDetails, on_delete=models.DO_NOTHING)
    manager_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EmployeeBankDetails(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=25)
    bank_ifsc = models.CharField(max_length=25)


class EmployeeLogin(models.Model):
    emp_id = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)