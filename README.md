# py2proj2
# Blockchain analytics tool using Django

### Installation
```
pip install django
pip install beautifulsoup4
```
### Usage
chart-django-project comes with its own `/index.html`, which extends your master `base.html`. All content lives inside of:

`{% block content %}{% endblock %}`

If you use some other name for your main content area, you'll need to override and alter the provided templates.

```
Your own API token should be used from etherscan.io in toAccounts()
```
apitoken="FMPY7CZC816282C49VUN44R8MHYIAQQG9V"

### Examples
PS py2projChart> python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

You have 1 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): auth.

Run 'python manage.py migrate' to apply them.

February 11, 2022 - 00:21:03

Django version 4.0.1, using settings 'chart_django_project.settings'

Starting development server at http://127.0.0.1:8000/

Quit the server with CTRL-BREAK.
![image](https://user-images.githubusercontent.com/70998876/153472710-5d44c071-f31d-46d1-867e-36c086ab6b6a.png)
