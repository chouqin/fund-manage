from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=32)

class Teacher(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=32)
    department = models.ForeignKey(Department)
    is_dean = models.BooleanField()

class ProjectType(models.Model):
    name = models.CharField(max_length=32)

class Project(models.Model):
    project_type = models.ForeignKey(ProjectType)
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField()
    ended_at = models.DateTimeField()

    teachers = models.ManyToManyField(Teacher)

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

class Business(models.Model):
    total = models.FloatField()
    remain = models.FloatField()
    year = models.DateTimeField()

    project = models.ForeignKey(Project)


class DeviceExpense(models.Model):
    device = models.ForeignKey(Device)
    amount = models.IntegerField()
    created_at = models.DateTimeField()
    status = models.IntegerField()

class BusinessExpense(models.Model):
    business = models.ForeignKey(Business)
    amount = models.FloatField()
    created_at = models.DateTimeField()
    status = models.IntegerField()

# Create your models here.
