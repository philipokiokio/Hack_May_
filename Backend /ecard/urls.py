"""ecard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from dj_rest_auth.registration.views import VerifyEmailView






urlpatterns = [
    path('admin/', admin.site.urls),


    # Local apps and Business logic 
    path('api/v1/', include('card.urls')),

    # User authentication and registration 
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/rest-auth/', include('allauth.urls')),
    path('api/v1/rest-auth/google/', include('user.urls')),
    path('api/v1/rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('api/v1/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('password/reset/', PasswordResetView.as_view(), name='reset_password_reset'),
    path('api/v1/rest-auth/password/reset/confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view(), name='password_reset_confirm')
]

