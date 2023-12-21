from django.contrib import admin
from .models import profile,Skill,EducationDetail
# Register your models here.
admin.site.register(profile)
admin.site.register(Skill)
admin.site.register(EducationDetail)