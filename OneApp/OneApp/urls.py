"""
DefinitionofurlsforOneApp.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
from app import forms, views

urlpatterns=[
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('classes/',views.classes,name='classes'),
    path('login/',LoginView.as_view
        (template_name='app/login.html',
        authentication_form=forms.BootstrapAuthenticationForm,
        extra_context={'title':'Login','year':datetime.now().year}),
        name='login'),
    path('logout/',LogoutView.as_view(next_page='/'),name='logout'),
    path('register/',views.register,name='register'),
    path('admin/',admin.site.urls),
]

