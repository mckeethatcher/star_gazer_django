from django.db import models

# class Star(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self): return self.name

# class Weather(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return self.name
    
class Crud(models.Model):
        location = models.CharField(max_length=50)
        coordinates = models.CharField(max_length=50)
        image = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.location