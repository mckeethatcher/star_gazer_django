from django.db import models

class Crud(models.Model):
    astronomer = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.TextField()
    id = models.AutoField(primary_key=True)
    def __str__(self) -> str:
        return self.location