
from django.db import models

from django.contrib.auth.models import User

# Create your models here.
STATUS_CHOICE = (
        (1, '未开始'),
        (2, '正在进行'),
        (3, '已完成'),
)


class Project(models.Model):

    project_name = models.CharField(verbose_name='项目名称', max_length=50)
    owner = models.ForeignKey(User, models.CASCADE)
    project_status = models.IntegerField(verbose_name='项目状态', choices=STATUS_CHOICE)
    project_info = models.CharField(max_length=300)
    start_time = models.DateField()
    end_time = models.DateField()

    def __str__(self):
        return self.project_name


class Task(models.Model):

    task_name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task_status = models.IntegerField(choices=STATUS_CHOICE)
    task_info = models.CharField(max_length=300)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_time = models.DateField()
    end_time = models.DateField()

    def __str__(self):
        return self.task_name