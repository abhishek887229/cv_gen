from django.db import models

class profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    summary = models.TextField(default="Effective communication and collaboration are at the core of my professional approach. I thrive in dynamic, fast-paced environments and am adept at adapting to evolving challenges. A natural problem-solver, I am confident in my ability to contribute positively to any team or project.")
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    previous_work = models.CharField(max_length=200)
    skills = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name} - {self.id}"

class Skill(models.Model):
    user = models.ForeignKey(profile, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)

    def __str__(self):
        return self.skill_name

class EducationDetail(models.Model):
    user=models.ForeignKey(profile,on_delete=models.CASCADE)
    education= models.CharField(max_length = 150)
    starting_year=models.DateField()
    end_year=models.DateField()

    def __str__(self):
        return self.education    