# SETUP & RUN INSTRUCTIONS

## Quick Start Guide for Employee Management System

### Step 1: Install Dependencies
Open PowerShell and run:
```
cd "d:\Django_total_projects\AI Django pro\emp_details"
pip install -r requirements.txt
```

### Step 2: Create Database & Migrations
Run these commands in order:
```
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Admin Account
```
python manage.py createsuperuser
```
When prompted, enter:
- Username: admin
- Email: admin@example.com
- Password: admin123 (or your choice)

### Step 4: Start Development Server
```
python manage.py runserver
```

### Step 5: Access the Application

**Web Interface:**
- Open browser: http://127.0.0.1:8000/
- Add/View/Edit/Delete employees here

**Admin Panel:**
- Open browser: http://127.0.0.1:8000/admin/
- Login with the credentials you created
- Manage employees from admin panel

## What's Included

✅ Complete Django Project Structure
✅ Employee Model with all required fields:
   - emp_id (Auto-generated)
   - emp_name
   - emp_role
   - emp_loc
   - emp_ph_no

✅ CRUD Operations:
   - Create new employees
   - Read/View employee details
   - Update existing employees
   - Delete employees

✅ Beautiful Templates:
   - Employee list page
   - Add/Edit form
   - Detail page
   - Responsive design

✅ Professional Styling:
   - Modern color scheme
   - Mobile-responsive
   - Smooth animations
   - Professional UI

✅ Django Admin Panel:
   - Manage employees
   - Search functionality
   - Filter options
   - List display

## File Structure

emp_details/
├── emp_details/              # Project settings
│   ├── settings.py          
│   ├── urls.py              
│   └── wsgi.py              
├── employees/                # Employee app
│   ├── models.py            # Employee model
│   ├── views.py             # CRUD operations
│   ├── forms.py             # Employee form
│   ├── admin.py             # Admin configuration
│   ├── urls.py              # App URLs
│   ├── templates/           # HTML templates
│   │   ├── base.html
│   │   └── employees/
│   │       ├── employee_list.html
│   │       ├── employee_detail.html
│   │       ├── employee_form.html
│   │       └── employee_confirm_delete.html
│   └── static/css/
│       └── style.css
├── manage.py
└── requirements.txt

## Testing the Application

### Add Employees:
1. Go to http://127.0.0.1:8000/employee/add/
2. Fill in all fields
3. Click "Add Employee"

### View Employees:
1. Go to http://127.0.0.1:8000/
2. See all employees in table format

### Edit Employees:
1. From list, click "Edit" button
2. Modify information
3. Click "Update Employee"

### Delete Employees:
1. From list, click "Delete" button
2. Confirm deletion
3. Employee is removed

### Admin Panel:
1. Go to http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Click "Employees" to manage
4. Use search and filters
5. Add/Edit/Delete from here

## Database

- SQLite3 (automatically created as db.sqlite3)
- Stores all employee records
- Admin panel to manage data

## Stop Server

Press Ctrl+C in the terminal to stop the development server

## Troubleshooting

Q: Port 8000 in use?
A: Run: python manage.py runserver 8001

Q: Database errors?
A: Run: python manage.py migrate --run-syncdb

Q: Forgot admin password?
A: Create new superuser: python manage.py createsuperuser

Q: Static files not loading?
A: Run: python manage.py collectstatic

## Support

All features are working. You can:
- See data from UI in Django ORM
- Store data into SQLite database
- Manage data from admin panel
- Perform full CRUD operations

Happy coding! 🚀
