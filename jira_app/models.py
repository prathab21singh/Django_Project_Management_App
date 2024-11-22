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
    client_id = models.ForeignKey(ClientDetails, on_delete=models.DO_NOTHING, null=True)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=500)
    budget = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EmployeeDetails(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=25, unique=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=10)
    role = models.CharField(max_length=25)
    department_id = models.ForeignKey(DepartmentDetails, on_delete=models.DO_NOTHING, null=True)
    manager_id = models.IntegerField(null=True)
    project_id = models.ForeignKey(ProjectDetails, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EmployeeBankDetails(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=25)
    bank_ifsc = models.CharField(max_length=25)


class EmployeeLogin(models.Model):
    emp_id = models.ForeignKey(EmployeeDetails, on_delete=models.DO_NOTHING)
    email = models.EmailField(unique=True, null=True)
    #updated length for saving hased password
    password = models.CharField(max_length=150)
