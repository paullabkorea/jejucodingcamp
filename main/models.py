from django.db import models


class Cafe(models.Model):
    name = models.CharField(max_length=50)
    mainphoto = models.ImageField(blank=True, null=True)
    publishedDate = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modifiedDate = models.DateTimeField(blank=True, null=True, auto_now=True)
    content = models.TextField()
    
    def __str__(self):
        return self.name