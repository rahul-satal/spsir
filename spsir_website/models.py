from django.db import models

class MyTeacher(models.Model):
    teacher_name = models.CharField(max_length=200,null=True) 
    def __unicode__(self):             
            return str(self.teacher_name)  

class MyStudent(models.Model):
    student_name = models.CharField(max_length=200,null=True)
    def __unicode__(self):             
            return str(self.student_name)

'''
class MyTeacher(models.Model):
    teacher_name1 = models.CharField(max_length=200,null=True,blank=True)
    teacher_name2 = models.CharField(max_length=200,null=True,blank=True)
    teacher_name3 = models.CharField(max_length=200,null=True,blank=True)
    teacher_name4 = models.CharField(max_length=200,null=True,blank=True)
    teacher_name5 = models.CharField(max_length=200,null=True,blank=True)
    teacher_name6 = models.CharField(max_length=200,null=True,blank=True)
    teacher_name7 = models.CharField(max_length=200,null=True,blank=True)
    teacher_name8 = models.CharField(max_length=200,null=True,blank=True)
    teacher_name9 = models.CharField(max_length=200,null=True,blank=True)
    teacher_name10 = models.CharField(max_length=200,null=True,blank=True)
    def __unicode__(self):             
        	return str(self.teacher_name1)	

class MyStudent(models.Model):
    student_name1 = models.CharField(max_length=200,null=True,blank=True)
    student_name2 = models.CharField(max_length=200,null=True,blank=True)
    student_name3 = models.CharField(max_length=200,null=True,blank=True)
    student_name4 = models.CharField(max_length=200,null=True,blank=True)
    student_name5 = models.CharField(max_length=200,null=True,blank=True)
    student_name6 = models.CharField(max_length=200,null=True,blank=True)
    student_name7 = models.CharField(max_length=200,null=True,blank=True)
    student_name8 = models.CharField(max_length=200,null=True,blank=True)
    student_name9 = models.CharField(max_length=200,null=True,blank=True)
    student_name10 = models.CharField(max_length=200,null=True,blank=True)
    def __unicode__(self):             
        	return str(self.student_name1)
'''            	        