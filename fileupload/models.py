from django.db import models


# Create your models here.
class FileUpLoad(models.Model):
    title = models.TextField()
    content = models.TextField()
    isStart = models.BooleanField(default=1)
