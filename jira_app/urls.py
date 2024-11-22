from django.urls import path
from . import views
from . import AdminViews


urlpatterns = [
    path('', views.loginPage, name="login"),
    path('signup/', views.signupPage, name= "signup"),
    path('admin_home/', AdminViews.admin_home, name= "admin_home"),
    path('add_employee/', AdminViews.add_employee, name= "add_employee"),
    path('add_employee_save/', AdminViews.add_employee_save, name="add_employee_save"),
    path('check_email_exist/', AdminViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', AdminViews.check_email_exist, name="check_username_exist"),
    path('manage_employee/',AdminViews.manage_employee, name="manage_employee"),
    path('edit_employee/<emp_id>/', AdminViews.edit_employee, name= "edit_employee"),
    path('edit_employee_save/<emp_id>', AdminViews.edit_employee_save, name="edit_employee_save"),
    path('delete_employee/<emp_id>/', AdminViews.delete_employee, name="delete_employee"),
]
