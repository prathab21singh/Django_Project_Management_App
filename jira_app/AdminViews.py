from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from jira_app.models import EmployeeDetails, DepartmentDetails, ClientDetails, ProjectDetails, CustomUser
from django.views.decorators.csrf import csrf_exempt
import traceback
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required


@login_required
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

@login_required
def add_employee(request):
    return render(request, "admin_template/add_employee_template.html")

@login_required
def add_employee_save(request):
    if request.method != 'POST':
        messages.error(request, "Invalid Method ")
        return redirect('add_employee')
    else:
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        phone = request.POST['phone']
        gender = request.POST['gender']
        role = request.POST['role']
        department_id = request.POST['department']
        manager_id = request.POST['manager_id']

        try:
            if email and username and password and name and password and phone and gender and role:
                user_details = EmployeeDetails.objects.create(name=name, username=username, email=email, phone=phone, gender=gender, role=role, department_id=department_id, manager_id=manager_id)
                user_details.save() 
                # hashed_password = make_password(password)
                id = EmployeeDetails.objects.get(username=username).id
                user = CustomUser.objects.create(id=id ,email=email, password=password,user_data_type="3")
                user.save()
                messages.success(request, "Employee Added Successfully!")
                return redirect('add_employee')
            else:
                messages.error(request, "Please Fill All Fields!")
                return redirect('add_employee')

        except:
            messages.error(request, "Failed to Add Employee!" + traceback.format_exc())
            return redirect('add_employee')

@login_required
def manage_employee(request):
    employees = EmployeeDetails.objects.all()
    context = {
        "employees": employees
    }
    return render(request, "admin_template/manage_employee_template.html", context=context)

@login_required
def edit_employee(request, emp_id):
    employee = EmployeeDetails.objects.get(id=emp_id)

    context = {
        'employee': employee,
        'employee_id':employee.id,
    }
    return render(request, "admin_template/edit_employee_template.html",context)

@login_required
def edit_employee_save(request, emp_id):
    if request.method != 'POST':
        messages.error(request, "Invalid Method ")
        return redirect('add_employee')
    else:
        emp_id = request.POST['employee_id']
        email = request.POST['email']
        username = request.POST['username']
        name = request.POST['name']
        role = request.POST['role']
        phone = request.POST['phone']
        manager_id = request.POST['manager_id']

        try:
            if email and username and role:
                user_details = EmployeeDetails.objects.get(id=emp_id)
                user_details.name = name
                user_details.email = email
                user_details.username =username
                user_details.role = role
                user_details.phone = phone
                user_details.manager_id = manager_id
                user_details.save() 
                user = CustomUser.objects.get(emp_id=emp_id)
                user.email = email
                user.save()
                messages.success(request, "Employee Updated Successfully!")
                return redirect('manage_employee')
            else:
                messages.error(request, "Please Fill All Fields!")
                return redirect('edit_employee')
            
        except:
            messages.error(request, "Failed to Add Employee!" + traceback.format_exc())
            return redirect('add_employee')

@login_required
def delete_employee(request, emp_id):
    user = CustomUser.objects.get(emp_id=emp_id)
    user.delete()
    user_details = EmployeeDetails.objects.get(id=emp_id)
    user_details.delete()
    return redirect('manage_employee')

@csrf_exempt
def check_email_exist(request):
    email = request.POST['email']
    user_obj = EmployeeDetails.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def check_username_exist(request):
    username = request.POST['username']
    user_obj = EmployeeDetails.objects.filter(username=username).exists()
    if user_obj:
        print(2222)
        return HttpResponse(True)
    else:
        return HttpResponse(False)
    

# Client Functions

def add_client(request):
    return render(request, "add_client_template.html")