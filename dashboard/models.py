from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='notes/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes" 

    def __str__(self):
        return self.title

class References(models.Model): 
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='references/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = "references"
        verbose_name_plural = "references" 

    def __str__(self):
        return self.title