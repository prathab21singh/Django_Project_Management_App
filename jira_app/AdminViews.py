from django.shortcuts import render, redirect
from django.contrib import messages
from jira_app.models import EmployeeDetails, DepartmentDetails, ClientDetails, ProjectDetails

def admin_home(request):
    employee_count = EmployeeDetails.objects.all().count()
    client_count = ClientDetails.objects.all().count()
    project_count = ProjectDetails.objects.all().count()
    department_count = DepartmentDetails.objects.all().count()

    #Total number of employees in each department
    
    context = {
        "employee_count": employee_count,
        "client_count": client_count,
        "project_count" : project_count,
        "department_count": department_count,
    }

    return render(request, "admin_template/home_content.html", context=context)



