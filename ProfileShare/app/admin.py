from django.contrib import admin
from app.models import Details , LinkData , ProjectDetails ,Achivement , Skill
 

@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','image','Education']

@admin.register(LinkData)
class LinkDataAdmin(admin.ModelAdmin):
    list_display = ['id','user','nameLink','link']

@admin.register(ProjectDetails)
class ProjectDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','projectname','githublink','image1','image2','desc']


@admin.register(Achivement)
class AchimentAdmin(admin.ModelAdmin):
    list_display = ['id','nameofachivement','user']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id','skillname']