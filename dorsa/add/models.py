from django.db import models


class AddModel(models.Model):
    first_number = models.IntegerField()
    second_number = models.IntegerField()
    total = models.IntegerField()
