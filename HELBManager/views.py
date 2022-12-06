from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView, 
    UpdateView, 
    DeleteView
)
from .models import Project

# Create your views here.



def home(request):
    context = {
        'projects' : Project.objects.all(),
        'title' : 'Content Page'
    }
    return render(request, 'HELBManager/home.html', context)#don t put the same name (login/login.html)
    #return HttpResponse('<h1>Welcome home</h1>')

class ProjectListView(ListView):
    model = Project
    template_name = 'HELBManager/home.html'
    context_object_name = 'projects'
    ordering = ['-date_posted']



class ProjectDetailView(DetailView):
    model = Project
    members = model.members

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'content', 'members', 'status']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    #Cette méthode permet de mettre à jour un projet, seul l'auteur peut le faire
    model = Project
    fields = ['title', 'content', 'members', 'status']

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
    return render(request, 'HELBManager/about.html', {'title' : 'About Us Page'})#don t put the same name
