# Employee Management System - Django Project

A complete Django-based web application for managing employee records with a user-friendly interface and admin panel.

## Features

- **Employee Management**: Add, view, update, and delete employee records
- **Admin Panel**: Built-in Django admin for managing employees
- **Responsive Design**: Mobile-friendly interface
- **Form Validation**: Client and server-side validation
- **Search & Filter**: Search employees by name, phone, or role in admin panel
- **Beautiful UI**: Modern, clean interface with professional styling

## Project Structure

```
emp_details/
├── emp_details/              # Main project settings
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # URL routing
│   └── wsgi.py               # WSGI configuration
├── employees/                # Employee app
│   ├── migrations/           # Database migrations
│   ├── static/
│   │   └── css/
│   │       └── style.css     # Application styles
│   ├── templates/
│   │   ├── base.html         # Base template
│   │   └── employees/
│   │       ├── employee_list.html
│   │       ├── employee_detail.html
│   │       ├── employee_form.html
│   │       └── employee_confirm_delete.html
│   ├── admin.py              # Admin configuration
│   ├── apps.py               # App configuration
│   ├── forms.py              # Employee form
│   ├── models.py             # Employee model with fields
│   ├── urls.py               # App URL routing
│   ├── views.py              # Views for CRUD operations
│   └── __init__.py
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
└── db.sqlite3               # SQLite database (auto-created)
```

## Employee Model Fields

- **emp_id**: Employee ID (Auto-incremented)
- **emp_name**: Employee Name (CharField - max 100 chars)
- **emp_role**: Employee Role (CharField - max 50 chars)
- **emp_loc**: Employee Location (CharField - max 100 chars)
- **emp_ph_no**: Phone Number (CharField - max 15 chars)
- **created_at**: Record creation timestamp
- **updated_at**: Record update timestamp

## Setup Instructions

### 1. Install Python & Django

Make sure you have Python 3.8+ installed. Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Navigate to Project Directory

```bash
cd emp_details
```

### 3. Create Database Migrations

```bash
python manage.py makemigrations
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account with username, email, and password.

### 6. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### Web Interface

- **Home Page**: `http://127.0.0.1:8000/` - View all employees
- **Add Employee**: Click "Add Employee" button or visit the form page
- **View Details**: Click "View" button on any employee row
- **Edit Employee**: Click "Edit" button to modify employee details
- **Delete Employee**: Click "Delete" button to remove an employee

### Admin Panel

- **Access Admin Panel**: `http://127.0.0.1:8000/admin/`
- **Login**: Use your superuser credentials
- **Manage Employees**: Add, edit, delete, and search employees
- **Features**: 
  - List view with sortable columns
  - Multi-field search
  - Filter by role and location
  - Date-based filtering

## URLs

| URL | Purpose |
|-----|---------|
| `/` | Employee list page |
| `/employee/add/` | Add new employee form |
| `/employee/<id>/` | View employee details |
| `/employee/<id>/edit/` | Edit employee form |
| `/employee/<id>/delete/` | Delete confirmation |
| `/admin/` | Django admin panel |

## Features in Detail

### 1. Employee List
- View all employees in a table format
- Shows ID, Name, Role, Location, and Phone Number
- Quick action buttons (View, Edit, Delete)

### 2. Add/Edit Employee
- Form with validation
- Required fields: Name, Role, Location, Phone
- Auto-generated Employee ID
- Success messages on save

### 3. Employee Details
- Complete employee information
- Formatted timestamps
- Phone number as clickable link
- Edit and Delete options

### 4. Admin Panel
- Comprehensive list display
- Search functionality
- Filtering options
- Read-only timestamps
- Organized fieldsets

## Styling

The application features a modern, responsive design with:
- Professional color scheme (Blue primary, Green success, Red danger)
- Smooth transitions and hover effects
- Mobile-responsive layout
- Consistent branding throughout
- Dark theme navbar with gradient
- Clean form styling

## Database

The project uses SQLite3 (default Django database):
- Database file: `db.sqlite3`
- Auto-creates on first migration
- Tables created for Employee model

## Security Notes

- Change `SECRET_KEY` in settings.py for production
- Set `DEBUG = False` for production
- Configure `ALLOWED_HOSTS` for your domain
- Use environment variables for sensitive data

## Troubleshooting

### Port 8000 Already in Use
```bash
python manage.py runserver 8001
```

### Database Errors
```bash
python manage.py migrate --run-syncdb
```

### Missing Migrations
```bash
python manage.py makemigrations employees
python manage.py migrate
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

## Admin Panel Features

### List Display
Shows columns: emp_id, emp_name, emp_role, emp_loc, emp_ph_no, created_at

### Filters
- Filter by Role
- Filter by Location
- Filter by Created Date

### Search
- Search by Employee Name
- Search by Phone Number
- Search by Role

### Actions
- Add new employee
- Edit existing employee
- Delete employee with confirmation

## Technologies Used

- **Django 4.2**: Web framework
- **SQLite3**: Database
- **HTML5**: Markup
- **CSS3**: Styling
- **Python 3.8+**: Programming language

## Future Enhancements

- User authentication for employees
- CSV import/export functionality
- Advanced reporting and analytics
- Department management
- Salary information management
- Document uploads
- Email notifications

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please check the Django documentation:
- Django Docs: https://docs.djangoproject.com/
- Django Admin: https://docs.djangoproject.com/en/stable/ref/contrib/admin/

---

**Created**: March 2026
**Version**: 1.0
