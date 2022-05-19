from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from mind_palace.palace.node.enums import NodeBodyTypeEnum

from .node import MindPalaceNode


class NodeBody(models.Model):

    node = models.OneToOneField(
        MindPalaceNode,
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


@receiver(post_save, sender=MindPalaceNode)
def create_node_body(instance, created, **kwargs):
    if created:
        NodeBody.objects.create(node=instance)
