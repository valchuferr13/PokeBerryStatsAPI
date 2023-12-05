from django.db import models

class Berry(models.Model):
    name = models.CharField(max_length=100)
    growth_time = models.IntegerField()

    def __str__(self):
        return self.name
