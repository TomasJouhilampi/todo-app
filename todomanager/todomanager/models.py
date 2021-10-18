from django.db import models

class Tehtava(models.Model):
     otsikko = models.CharField(max_length=100)

     def __str__(self):
        return self.otsikko