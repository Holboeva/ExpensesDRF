from django.urls import path

from auth_apps.views import Login_api_view, Register_api_view

urlpatterns = [
    path('register', Register_api_view),
    path('login', Login_api_view)
]