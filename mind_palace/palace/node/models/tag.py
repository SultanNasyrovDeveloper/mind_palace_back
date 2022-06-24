from django.db import models


class Tag(models.Model):

    name = models.CharField('Name', max_length=500)
