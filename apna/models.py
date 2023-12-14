from django.db import models
 
# Create your models here.

class language(models.Model):
    name = models.CharField(max_length=100,null=True)
    photo = models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return f"{self.name}"