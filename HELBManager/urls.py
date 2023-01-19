from django.urls import path, include
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    taskCreate,
    taskUpdate,
    taskDelete
)
from . import views

urlpatterns = [
    path('', ProjectListView.as_view(), name='home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('project/<int:pk>/task-create/', taskCreate, name='task-create'),
    path('project/<int:pk>/task-update/', taskUpdate, name='task-update'),
    path('project/<int:pk>/task-delete/', taskDelete, name='task-delete'),
    path('about/', views.about, name='about'),
]
