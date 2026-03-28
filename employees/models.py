from django.db import models


class Employee(models.Model):
    """Employee model to store employee details"""
    
    emp_id = models.AutoField(primary_key=True, verbose_name="Employee ID")
    emp_name = models.CharField(max_length=100, verbose_name="Employee Name")
    emp_role = models.CharField(max_length=50, verbose_name="Employee Role")
    emp_loc = models.CharField(max_length=100, verbose_name="Employee Location")
    emp_ph_no = models.CharField(max_length=15, verbose_name="Phone Number")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.emp_name} - {self.emp_role}"
