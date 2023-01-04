from django.db import models

# Create your models here.
class Site(models.Model):
    img=models.ImageField(upload_to='image')
    name=models.CharField(max_length=350)
    desc=models.TextField()
    def __str__(self):
        return self.name
class School(models.Model):
    img1=models.ImageField(upload_to='im')
    name1=models.CharField(max_length=300)
    desc1=models.TextField()




    def __str__(self):
        return self.name1

