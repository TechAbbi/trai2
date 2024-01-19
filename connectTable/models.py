from django.db import models


# Create your models here.

class ModelA(models.Model):
    name = models.CharField(max_length=20)


class ModelB(models.Model):
    middel_name = models.CharField(max_length=20)


class ConnectingModel(models.Model):
    model_a = models.ForeignKey(ModelA, on_delete=models.CASCADE)
    model_b = models.ForeignKey(ModelB, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=20)

