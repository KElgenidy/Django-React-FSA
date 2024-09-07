"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
"""
Provides JWT authentication views for obtaining and refreshing access tokens.

The `TokenObtainPairView` is used to obtain a new access and refresh token pair by providing valid user credentials.
The `TokenRefreshView` is used to obtain a new access token by providing a valid refresh token.

These views are part of the Django REST Framework Simple JWT library, which provides a simple JWT-based authentication mechanism for Django REST Framework.
"""
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

"""
Defines the URL patterns for the backend Django project.

The `urlpatterns` list maps URLs to Django views and includes the following:

- `admin/`: The Django admin site URL.
- `api/user/register/`: The URL for registering a new user, handled by the `CreateUserView` view.
- `api/token/`: The URL for obtaining a new access and refresh token pair, handled by the `TokenObtainPairView` view.
- `api/token/refresh/`: The URL for refreshing an access token, handled by the `TokenRefreshView` view.
- `api_auth/`: The URL for the Django REST Framework authentication views.
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api_auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
]
