from django.db import models


class Cryptocurrency(models.Model): 
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.price




