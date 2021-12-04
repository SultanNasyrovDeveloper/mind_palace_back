from django.db import models


class NodeTag(models.Model):

    name = models.CharField('Name', max_length=500)
