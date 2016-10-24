from django.db import models


class Item(models.Model):
    text = models.CharField(default='', max_length=100)
