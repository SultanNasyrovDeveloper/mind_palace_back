from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from mind_palace.palace.node.enums import NodeBodyTypeEnum

from .node import PalaceNode


class Body(models.Model):

    node = models.OneToOneField(
        'node.PalaceNode',
        on_delete=models.CASCADE,
        related_name='body'
    )
    type = models.CharField(
        max_length=50,
        choices=NodeBodyTypeEnum.choices(),
        default=NodeBodyTypeEnum.TEXT
    )
    meta = models.JSONField(default=dict)
    data = models.JSONField(default=dict)


@receiver(post_save, sender=PalaceNode)
def create_node_body(instance, created, **kwargs):
    if created:
        Body.objects.create(node=instance)
