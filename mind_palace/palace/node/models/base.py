from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class BaseMindPalaceNode(MPTTModel):

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children',
        verbose_name='Parent',
    )
    name = models.CharField('Name', max_length=500)

    class Meta:
        abstract = True
