from django.db import models


# Create your models here.
class DownLoad(models.Model):
    background = models.ImageField(upload_to='./media')
    color = models.ImageField(upload_to='./media')
    summed = models.FileField(upload_to='./media/result')
    isFinished = models.BooleanField(default=0)
