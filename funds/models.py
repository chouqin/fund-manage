#coding=utf-8
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=32)
    department = models.ForeignKey(Department)
    is_dean = models.BooleanField()

    def __unicode__(self):
        return self.name

class ProjectType(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    project_type = models.ForeignKey(ProjectType)
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField()
    ended_at = models.DateTimeField()

    teachers = models.ManyToManyField(Teacher)

    def __unicode__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=64)
    specification = models.CharField(max_length=32)
    maker = models.CharField(max_length=32)
    is_import = models.BooleanField()
    price = models.FloatField()
    amount = models.IntegerField()
    remain_amount = models.IntegerField()
    position = models.CharField(max_length=32)
    usage = models.CharField(max_length=64)
    year = models.DateTimeField()

    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name

class Business(models.Model):
    total = models.FloatField()
    remain = models.FloatField()
    year = models.DateTimeField()

    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.total


class DeviceExpense(models.Model):
    device = models.ForeignKey(Device)
    amount = models.IntegerField()
    created_at = models.DateTimeField()
    status = models.IntegerField()

    def __unicode__(self):
        return self.amount

class BusinessExpense(models.Model):
    business = models.ForeignKey(Business)
    amount = models.FloatField()
    created_at = models.DateTimeField()
    status = models.IntegerField()

    def __unicode__(self):
        return self.amount

# Create your models here.
