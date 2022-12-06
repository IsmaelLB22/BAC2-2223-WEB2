from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class Project(models.Model):
    #for user in User.object.all:
    #    userList.append(user)

    #User = get_user_model()
    #userList = User.objects.all


    title= models.CharField(max_length=100)
    content= models.TextField()
    date_posted= models.DateTimeField(default=timezone.now)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='members', null=True, blank=True)
    status = models.CharField(max_length=100, default='TODO;In Progress;In Revision;Done')
    #members = models.ExpressionList(User, related_name='members')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})
    
    def get_status_as_list(self):
        return self.status.split(';')

#class Member(models.Model):
 #   member = models.ForeignKey(User, on_delete=models.CASCADE)
 #   project = models.ManyToManyField(Post, related_name='project')


