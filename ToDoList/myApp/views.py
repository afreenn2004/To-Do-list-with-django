#AfreenAjaz
from typing import Any
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import login
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.views import LoginView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from django import forms 

# Create your views here.
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'Task_List.html'
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input

        return context
    
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'Task_Detail.html'
    context_object_name = 'task'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'completed']

class TaskFormView(LoginRequiredMixin, FormView):
    form_class = TaskForm
    template_name = 'Task_Form.html'
    success_url = reverse_lazy('Task_List')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'deadline', 'completed']
    template_name = 'Task_Form.html'
    success_url = reverse_lazy('Task_List')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'Task_Delete_Confirm.html'
    success_url = reverse_lazy('Task_List')

class CustomLoginView(LoginView):
    template_name = 'Login.html'
    fields = ['username', 'password']
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('Task_List')
    
class UserCreationForm(FormView):
    template_name = 'Register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('Login')
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
    







