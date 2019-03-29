from django.db import models
from django.conf import settings

class Project_ings(models.Model):
    id_no=models.BigIntegerField(unique=True)
    username=models.CharField(max_length=200)
    link_username=models.CharField(max_length=200)
    problem_name=models.CharField(max_length=200)
    problem_link=models.CharField(max_length=200)
    time_string=models.CharField(max_length=200)
    result=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    def __str__(self):
        return self.username
