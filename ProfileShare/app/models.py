from django.db import models
from django.contrib.auth.models import User
# Create your models here.


EDUCATION_CHOICE = (
 ('B.TECH', 'B.TECH'),
 ('B.E', 'B.E'),
 ('Bsc', 'Bsc'),
 ('OTHER', 'OTHER'),
)

class Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , unique=True)
    name = models.CharField(max_length=255)
    Education = models.CharField(choices=EDUCATION_CHOICE, max_length=50)
    email = models.EmailField(max_length=300)
    image = models.ImageField(upload_to='profile')

class LinkData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nameLink = models.CharField(max_length=255)
    link = models.URLField(max_length=300)


class ProjectDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projectname = models.CharField(max_length=255)
    githublink = models.URLField(max_length=300)
    image1 = models.ImageField(upload_to='project')
    image2 = models.ImageField(upload_to='project')
    desc = models.CharField(max_length=900)
class Achivement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nameofachivement = models.CharField(max_length=255)


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skillname = models.CharField(max_length=255)

class ShareDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nameid = models.CharField(max_length=500,unique=True)