from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import logout

from .forms import EditProfileModelForm, ChangePasswordForm
from account_module.models import User


# Create your views here.


class UserPanelDashboard(TemplateView):
    template_name = 'user_panel_dashboard/user_panel_page.html'


class EditProfilePage(View):
    def get(self, request: HttpRequest):
        current_user: User = User.objects.filter(id=request.user.id).first()
        edit_profile = EditProfileModelForm(instance=current_user)
        context = {
            'edit_form': edit_profile,
            'current_user': current_user
        }
        return render(request, 'user_panel_dashboard/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_profile = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_profile.is_valid():
            edit_profile.save(commit=True)

        context = {
            'edit_form': edit_profile,
            'current_user': current_user
        }

        return render(request, 'user_panel_dashboard/edit_profile_page.html', context)


class ChangePasswordView(View):
    def get(self, request: HttpRequest):
        context = {
            'change_form': ChangePasswordForm()
        }
        return render(request, 'user_panel_dashboard/change_password_page.html', context)

    def post(self, request: HttpRequest):
        change_form = ChangePasswordForm(request.POST)
        if change_form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(change_form.cleaned_data.get('current_password')):
                current_user.set_password(change_form.cleaned_data.get('password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                change_form.add_error('password', 'کلمه عبور وارد شده اشتباه می باشد')
        context = {
            'change_form': change_form
        }
        return render(request, 'user_panel_dashboard/change_password_page.html', context)


def user_panel_component(request):
    return render(request, 'user_panel_dashboard/component/panel_component.html', {})
