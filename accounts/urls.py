from django.urls import path
from . import views

urlpatterns = [
    path("register/",views.register, name='register'),
    path("verify-otp/", views.verify_otp, name="verify_otp"),
    path("resend-otp/", views.resend_otp, name="resend_otp"),
    path("login/",views.login, name='login'),
    path("forgot_password/",views.forgot_password, name='forgot_password'),
    path("change_password/",views.change_password, name='change_password'),
    path("profile/",views.profile, name='profile'),
    path("edit_profile/",views.edit_profile, name='edit_profile'),
    path("logout/",views.logout, name='logout'),
]
