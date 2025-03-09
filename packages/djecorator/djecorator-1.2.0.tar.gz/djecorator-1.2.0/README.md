# Djecorator

Write Django routes in the same style as Flask.

## Installation

```
pip install djecorator
```

## Usage

### views.py

```python
from django.shortcuts import render
from djecorator import Route

route = Route()

@route("/")
def index(request):
    return render(request, "index.html")

# With path and name parameters
@route("/about/", name="about_page")
def about(request):
    return render(request, "about.html")

# With login required protection
@route("/dashboard/", login_required=True)
def dashboard(request):
    # Only accessible to authenticated users
    return render(request, "dashboard.html")
```

### urls.py

```python
import views

urlpatterns = [
    ...
]

urlpatterns += views.route.patterns
```

## Features

- **Flask-like routing**: Define your routes directly above your view functions
- **Prefixing**: Add URL and name prefixes to group related routes
- **Authentication**: Protect routes with Django's `login_required` decorator
- **Class-based views**: Works with both function-based and class-based views

### Route Parameters

The `Route` class accepts the following parameters:

- `url_prefix`: Prefix added to all URL paths
- `name_prefix`: Prefix added to all URL names

The `@route()` decorator accepts the following parameters:

- `path`: The URL path (defaults to the function name)
- `name`: The URL name (defaults to the function name)
- `login_required`: Whether the view requires authentication (defaults to False)

### Example with prefixes

```python
# Create a route with prefixes
admin_route = Route(url_prefix="/admin", name_prefix="admin_")

@admin_route("/users/")
def admin_users(request):
    # This will be available at /admin/users/
    # and have the URL name "admin_users"
    return render(request, "admin/users.html")

@admin_route("/settings/", login_required=True)
def admin_settings(request):
    # This will be available at /admin/settings/
    # and have the URL name "admin_settings"
    # and require login
    return render(request, "admin/settings.html")
```
