from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=100, default= None)
    about = models.TextField()

    def __str__(self):
        return self.title


class Teams(models.Model):
    name = models.CharField(max_length=100, default= None)
    about = models.TextField()




class Bodies(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, default= None)
    about = models.TextField()


    