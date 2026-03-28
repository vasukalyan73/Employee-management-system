# Employee Management System - Deployment Guide

## GitHub Setup Instructions

### Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Create a new repository named "employee-management-system" (or your preferred name)
3. Do NOT initialize with README, .gitignore, or license (we already have them)
4. Click "Create repository"

### Step 2: Add Remote and Push Code
Run these commands in the project directory:

```bash
# Add the remote repository
git remote add origin https://github.com/YOUR-USERNAME/employee-management-system.git

# Rename branch to main (if needed)
git branch -M main

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Employee Management System with authentication"

# Push to GitHub
git push -u origin main
```

### Step 3: Generate Personal Access Token (PAT)
1. Go to https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Select scopes: `repo`, `admin:repo_hook`
4. Copy and save the token (you'll need it for authentication)
5. Use the token as password when pushing to GitHub

---

## Deployment Options

### Option 1: Deploy to Heroku (FREE - Recommended for beginners)

**Prerequisites:**
- Heroku account (free at heroku.com)
- Heroku CLI installed

**Steps:**

```bash
# 1. Install Heroku CLI if not already installed
# Download from: https://devcenter.heroku.com/articles/heroku-cli

# 2. Login to Heroku
heroku login

# 3. Create Heroku app
heroku create your-app-name

# 4. Add buildpacks
heroku buildpacks:add heroku/python

# 5. Create Postgres database
heroku addons:create heroku-postgresql:hobby-dev

# 6. Set environment variables
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secret-key-here
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com

# 7. Push to Heroku
git push heroku main

# 8. Run migrations
heroku run python manage.py migrate

# 9. Create superuser (optional)
heroku run python manage.py createsuperuser

# 10. View application
heroku open
```

**View logs:**
```bash
heroku logs --tail
```

---

### Option 2: Deploy to PythonAnywhere (FREE - Easy)

**Steps:**

1. Sign up at https://www.pythonanywhere.com (free account)
2. Create a new web app
3. Choose Django framework and Python 3.11
4. In the web app settings, set up:
   - Source code: Clone from GitHub
   - Virtualenv path
   - WSGI file location
5. Upload requirements.txt
6. Set environment variables in web app configuration
7. Reload the web app

---

### Option 3: Deploy to DigitalOcean (PAID - $4-6/month)

**Steps:**

1. Create DigitalOcean account
2. Create a Droplet (Ubuntu 22.04)
3. SSH into the server
4. Install Python, Nginx, Gunicorn, PostgreSQL
5. Clone repository from GitHub
6. Install dependencies
7. Configure Gunicorn and Nginx
8. Set up SSL with Let's Encrypt

---

### Option 4: Deploy to AWS, Google Cloud, Azure (PAID)

These platforms offer more control and scalability but require more configuration.

---

## Important Settings for Production

Before deploying, update `emp_details/settings.py`:

```python
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')

# Use PostgreSQL in production
if os.environ.get('DATABASE_URL'):
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600
        )
    }
```

---

## Post-Deployment

1. Create superuser account
2. Add employees to the system
3. Share login credentials securely
4. Monitor server logs
5. Set up automated backups

---

## Useful Links

- GitHub: https://github.com
- Heroku: https://www.heroku.com
- PythonAnywhere: https://www.pythonanywhere.com
- Django Documentation: https://docs.djangoproject.com
- Gunicorn: https://gunicorn.org

