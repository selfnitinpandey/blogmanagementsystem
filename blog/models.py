from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    desc=models.TextField()
    