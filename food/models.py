from django.db import models


# Create your models here.

class Item(models.Model):
    def __str__(self):
        return f"{self.name}: {self.desc} : {self.price}"
    name = models.CharField(max_length=20, unique=True)
    desc = models.CharField(max_length=100)
    price = models.FloatField()
    pic = models.CharField(max_length=5000, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSS6Pq0Qe0oXY4wFa1hl-W3b1lrFfI0OXy3E2XaUnupF0O2b7MvmlzhnSLl-g&s")
