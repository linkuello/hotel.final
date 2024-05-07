from django.db import models

class Room(models.Model):
    number = models.CharField(max_length=10)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"Room {self.number}"
