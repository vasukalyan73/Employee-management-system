from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm, RegistrationForm, LoginForm


def register(request):
    """Register a new user"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = RegistrationForm()
    
    context = {
        'form': form,
        'title': 'Register',
    }
    return render(request, 'employees/register.html', context)


def user_login(request):
    """Login user"""
    if request.user.is_authenticated:
        return redirect('employee_list')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('employee_list')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    context = {
        'form': form,
        'title': 'Login',
    }
    return render(request, 'employees/login.html', context)


def user_logout(request):
    """Logout user"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


@login_required(login_url='login')
def employee_list(request):
    """Display all employees"""
    employees = Employee.objects.all()
    context = {
        'employees': employees,
        'total_employees': employees.count(),
    }
    return render(request, 'employees/employee_list.html', context)


@login_required(login_url='login')
def employee_detail(request, emp_id):
    """Display employee detail"""
    employee = get_object_or_404(Employee, emp_id=emp_id)
    context = {
        'employee': employee,
    }
    return render(request, 'employees/employee_detail.html', context)


@login_required(login_url='login')
def employee_create(request):
    """Create a new employee"""
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully!')
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    
    context = {
        'form': form,
        'title': 'Add Employee',
    }
    return render(request, 'employees/employee_form.html', context)


@login_required(login_url='login')
def employee_update(request, emp_id):
    """Update an existing employee"""
    employee = get_object_or_404(Employee, emp_id=emp_id)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully!')
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    
    context = {
        'form': form,
        'employee': employee,
        'title': 'Edit Employee',
    }
    return render(request, 'employees/employee_form.html', context)


@login_required(login_url='login')
def employee_delete(request, emp_id):
    """Delete an employee"""
    employee = get_object_or_404(Employee, emp_id=emp_id)
    
    if request.method == 'POST':
        emp_name = employee.emp_name
        employee.delete()
        messages.success(request, f'Employee "{emp_name}" deleted successfully!')
        return redirect('employee_list')
    
    context = {
        'employee': employee,
    }
    return render(request, 'employees/employee_confirm_delete.html', context)
