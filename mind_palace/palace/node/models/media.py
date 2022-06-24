from django.db import models

from mind_palace.palace.node.enums import NodeMediaTypeEnum


class Media(models.Model):
    """
    Responsible for storing one media object with image or other king of media.

    Currently, only image or icon or youtube video media available.
    """
    node = models.ForeignKey(
        'node.PalaceNode',
        on_delete=models.CASCADE,
        related_name='media'
    )
    type = models.CharField(
        max_length=100,
        choices=NodeMediaTypeEnum.choices(),
        default=NodeMediaTypeEnum.NOT_SET,
    )
    title = models.CharField(max_length=500, null=True, default=None)
    description = models.TextField(null=True, default=None)

    image = models.ImageField(upload_to='node_media/')
    config = models.JSONField(default=dict)