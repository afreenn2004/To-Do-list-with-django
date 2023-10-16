"""
URL configuration for ToDoList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#AfreenAjaz
from django.contrib import admin
from django.urls import path
from myApp.views import TaskListView
from myApp.views import TaskDetailView
from myApp.views import TaskFormView, TaskUpdateView
from myApp.views import TaskDeleteView
from myApp.views import CustomLoginView
from myApp.views import UserCreationForm
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TaskListView.as_view(), name='Task_List'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='Task_Detail'),
    path('tasks-Form/', TaskFormView.as_view(), name='Task_Form'),
    path('tasks/update/<int:pk>/', TaskUpdateView.as_view(), name='Task_Update'),
    path('tasks/Delete/<int:pk>/', TaskDeleteView.as_view(), name='Task_Delete'),
    path('Login/', CustomLoginView.as_view(), name='Login'),
    path('Logout/', LogoutView.as_view(next_page='Login'), name='Logout'),
    path('Register/', UserCreationForm.as_view(), name='Register'),
]
