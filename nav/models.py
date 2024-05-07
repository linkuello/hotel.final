from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
