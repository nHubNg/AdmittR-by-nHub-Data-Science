from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    subject_combo = models.ManyToManyField('Subject')
    
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
