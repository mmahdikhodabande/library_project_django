from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register_page'),
    path('login', views.LoginView.as_view(), name='login_page'),
    path('logout', views.LogoutView.as_view(), name='log_out'),
    path('forget_pass', views.ForgetPasswordView.as_view(), name='forget_pass'),
    path('reset_pass/<code_active>', views.ResetPasswordView.as_view(), name='reset_password'),
    path('activate_account/<active_code>', views.ActivateAccountView.as_view(), name='active_account')
]
