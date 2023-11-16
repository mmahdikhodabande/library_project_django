from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboard.as_view(), name='user_panel_page'),
    path('edit-profile', views.EditProfilePage.as_view(), name='edit_profile_page'),
    path('change-password', views.ChangePasswordView.as_view(), name='change_password_page'),
]
