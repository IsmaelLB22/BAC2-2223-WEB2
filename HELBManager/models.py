from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

# Create your models here.

class Task(models.Model):

    title = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    assignedMember = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignedMember', null=True, blank=True)
    lastUpdateDate = models.DateField(default=timezone.now)
    creationDate = models.DateField(default=timezone.now)
    def __str__(self):
        return self.title

    def get_update_date(self):
        updateDate = self.lastUpdateDate.strftime('%d.%m.%Y')
        return updateDate

    def get_creation_date(self):
        formatCreationDate = self.creationDate.strftime('%d.%m.%Y')
        return formatCreationDate



class Project(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='members', null=True, blank=True)
    status = models.CharField(max_length=100, default='TODO;In Progress;In Revision;Done')
    tasks = models.ManyToManyField(Task, related_name='tasks')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})

    def get_status_as_list(self):
        return self.status.split(';')

    def get_tasks_as_list(self):
        return self.tasks.split(';')

    def get_date_posted(self):
        format_date_posted = self.date_posted.strftime('%d.%m.%Y')
        return format_date_posted




