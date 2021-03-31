from django.db import models

# Create your models here.
from django.db import models

class Role(models.Model):
    ROLES = (
        ('Convener','Convener'),
        ('Chairperson','Chairperson'),
        ('Executive Member','Executive Member'),
        ('Technical Head','Technical Head')
    )
    role : models.CharField(choices= ROLES)

class Member(models.Model):
    name : models.CharField(max_length=200)
    description : models.TextField
    core : models.BooleanField(default=False)
    #role : models.ManyToManyField(Roles)
    instagram_link : models.URLField
    linkedIn_link : models.URLField
    email : models.EmailField

class Article(models.Model):
    title : models.CharField(max_length=200)
    description: models.TextField
    #thumbnail : models.ImageField(upload_to='/articles')
    #date : models.DateField()
    link : models.URLField