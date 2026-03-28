from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # Employee URLs
    path('', views.employee_list, name='employee_list'),
    path('employee/<int:emp_id>/', views.employee_detail, name='employee_detail'),
    path('employee/add/', views.employee_create, name='employee_create'),
    path('employee/<int:emp_id>/edit/', views.employee_update, name='employee_update'),
    path('employee/<int:emp_id>/delete/', views.employee_delete, name='employee_delete'),
]
