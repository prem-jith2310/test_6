from django.db import models

# Create your models here.
class tbl_school(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    hmname = models.CharField(max_length=100)
    typee = models.CharField(max_length=100)
    class Meta:
        db_table = 'tbl_school'


class tbl_teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    qualification = models.CharField(max_length=100)
    experience = models.IntegerField()
    salary = models.IntegerField()
    class Meta:
        db_table = 'tbl_teacher'


class tbl_student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    school = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    class Meta:
        db_table = 'tbl_student'


class tbl_staff(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    experience = models.IntegerField()
    salary = models.IntegerField()
    class Meta:
        db_table = 'tbl_staff'