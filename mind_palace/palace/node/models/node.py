from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class PalaceNode(MPTTModel):
    
    owner = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='nodes',
        default=None,
        null=True
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children',
        verbose_name='Parent',
    )
    name = models.CharField('Name', max_length=500)

    description = models.TextField('Description', default='', null=True, blank=True)
    tags = models.ManyToManyField('node.Tag', verbose_name='Tags')
