import json
from datetime import date
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Project, Task, User


class ProjectListView(ListView):
    model = Project
    template_name = 'HELBManager/home.html'
    context_object_name = 'projects'
    ordering = ['-date_posted']


class ProjectDetailView(DetailView):
    model = Project
    members = model.members
    colors = ["#80c492",
              "#ed8080",
              "#80d5ed",
              "#eded80",
              "#8090ed",
              "#c7ed80"
              ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colors'] = self.colors
        return context


# CREATE TASK MODEL ✔ , ADD TASK ✔ -> METHOD TASKCREATEVIEW  ✔ -> ATTACH TO PROJECT ✔ -> DISPLAY BY DIV
def taskCreate(request, pk):
    # récup des données
    task_title = request.POST.get('task_title')
    task_status = request.POST.get('task_status')
    userId = request.POST.get('assigned_members')
    project_id = request.POST.get('project_id')
    # nouvel objet Task
    task = Task.objects.create(title=task_title, status=task_status)
    task.save()
    # sauvegarde
    user = User.objects.get(id=userId)
    task.assignedMember = user
    task.save()
    # attribution de la task au projet
    currentProject = Project.objects.get(id=project_id)
    currentProject.tasks.add(task)
    currentProject.save()
    # notification
    messages.success(request, f'Task has been created!')
    return redirect('project-detail', pk)


@csrf_exempt
def taskUpdate(request, pk):
    if request.method == 'POST':
        # récup des données
        data = json.loads(request.body)
        taskId = data["taskId"]
        newStatus = data["newStatus"]

        task = Task.objects.get(pk=taskId)
        # Màj de la task si nouveau status
        if task.status != newStatus:
            task.status = newStatus
            task.lastUpdateDate = date.today()
            task.save()
            # notification
            messages.success(request, f'Task has been updated!')

        result = 'task ID : ' + str(taskId) + " - New Status : " + str(newStatus)
        return JsonResponse({'result': "ok"})
    else:
        return JsonResponse({'result': 'nok'})


def taskDelete(request, pk):
    if request.method == 'POST':
        # suppression de la task
        taskID = request.POST.get('task_to_delete')
        Task.objects.get(id=taskID).delete()
        # notification
        messages.success(request, f'Task has been deleted!')

        return redirect('project-detail', pk)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'content', 'members', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # Cette méthode permet de mettre à jour un projet, seul l'auteur peut le faire
    model = Project
    fields = ['title', 'content', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False


def about(request):
    return render(request, 'HELBManager/about.html', {'title': 'About Us Page'})  # don t put the same name
