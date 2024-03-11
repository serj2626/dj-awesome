from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from users.models import Profile
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm


class ProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(user=self.request.user)
        return context


class ProfileEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('profile')
    success_message = "Профиль успешно отредактирован"




class ProfileDeleteView(LoginRequiredMixin, SuccessMessageMixin,DeleteView):
    model = Profile
    template_name = 'users/profile_delete.html'
    success_url = reverse_lazy('profile')
    success_message = "Профиль успешно удален"