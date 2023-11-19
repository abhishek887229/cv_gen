from django.db import models

# Create your models here.

class profile(models.Model):
    
    def __str__(self):
        return self.name,self.id

    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    summary=models.TextField(max_length=1000,default="Effective communication and collaboration are at the core of my professional approach. I thrive in dynamic, fast-paced environments and am adept at adapting to evolving challenges. A natural problem-solver, I am confident in my ability to contribute positively to any team or project.")
    degree=models.CharField(max_length=200)
    school=models.CharField(max_length=200)
    university=models.CharField(max_length=200)
    previous_work=models.CharField(max_length=200)
    skills=models.CharField(max_length=1000)
    

