from django.urls import path
from . import views
from . import AdminViews


urlpatterns = [
    path('', views.loginPage, name="login"),
    path('signup/', views.signupPage, name= "signup"),
    path('admin_home/', AdminViews.admin_home, name= "admin_home"),
]
