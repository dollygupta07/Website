from django.db import models

# Create your models here.
class Tag(models.Model):
	id = models.BigAutoField(primary_key=True)
	name=models.CharField(max_length=150)
	def __str__(self):
		return self.name


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=150)
    summary = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    team_members = models.TextField(max_length=500,null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    picture = models.ImageField(upload_to='project', null=True, blank=True)
    source_code = models.URLField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    def __str__(self):
    	return self.name

