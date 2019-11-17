from django.db import models

# Create your models here.
# login/models.py
from django.db import models


class User(models.Model):
    """用户表"""
    gender = (
        ('male', 'man'),
        ('female', 'woman'),
    )

    users = (
        ('admin', 'administrator'),
        ('user', 'generaluser'),
    )

    name = models.CharField(max_length=20)
    password = models.CharField(max_length=256)
    email = models.EmailField(max_length=20, unique="true")
    sex = models.CharField(max_length=32, choices=gender, default='man')
    c_time = models.DateTimeField(auto_now_add=True)
    permission = models.CharField(max_length=30, choices=users, default='generaluser')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = 'user'
        verbose_name_plural = 'user'


class Student(models.Model):
    """学生表"""

    name = models.CharField(max_length=20)
    grade = models.CharField(max_length=4)
    studentid = models.CharField(max_length=13, unique="true")
    college = models.CharField(max_length=20)
    profession = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'student'
        verbose_name_plural = 'student'


class Grade(models.Model):
    """成绩表"""

    name = models.CharField(max_length=20)
    studentid = models.CharField(max_length=13, unique="true")
    Chinese = models.CharField(max_length=20)
    Mathematics = models.CharField(max_length=20)
    English = models.CharField(max_length=20)
    Physical = models.CharField(max_length=20)
    Chemistry = models.CharField(max_length=20)
    PE = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'grade'
        verbose_name_plural = 'grade'