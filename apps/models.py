from django.db import models


class User(models.Model):
    name = models.CharField(max_length=21, verbose_name='用户名')
    age = models.CharField(max_length=21, verbose_name='年龄')
