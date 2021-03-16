from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from . form import SignUpForm, EditProfileForm
from django.views.generic import UpdateView
from django.contrib.auth.views import PasswordChangeView
from .form import PasswordChangingForm

def password_success(request):
	return render(request, 'registration/password_success.html', {})




class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	# form_class = PasswordChangeForm
	success_url = reverse_lazy('members:password_success')
	# success_url = reverse_lazy('blog:home')


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('blog:home')

	def get_object(self):
		return self.request.user
