from django.db import models

class MyTeacher(models.Model):
    teacher_name = models.CharField(max_length=200,null=True) 
    def __unicode__(self):             
            return str(self.teacher_name)  

class MyStudent(models.Model):
    student_name = models.CharField(max_length=200,null=True)
    link = models.CharField(max_length=200,null=True)
    def __unicode__(self):             
            return str(self.student_name)

class SpritualGuru(models.Model):
    SpritualGuru_name = models.CharField(max_length=500,null=True)
    def __unicode__(self):             
            return str(self.SpritualGuru_name)

class Workshop(models.Model):
    workshop_name = models.TextField(max_length=200,null=True)
    def __unicode__(self):             
            return str(self.workshop_name)
