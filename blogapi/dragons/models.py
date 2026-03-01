from django.db import models

class Dragon(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    diet = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    abilities = models.TextField()
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.name