from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Task(models.Model):
    titulo=models.CharField(max_length=100)
    descripcion=models.TextField(blank=True)
    creadodate=models.DateTimeField(auto_now_add=True)
    datecomplete=models.DateTimeField(null=True,blank=True)
    important=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo + " - de " + self.user.username 
