from django.db import models

from mind_palace_back.palace.node.models import BaseMindPalaceNode
from mind_palace_back.palace.node.enums import NodeBodyTypeEnum


class MindPalaceNode(BaseMindPalaceNode):

    title = models.TextField('Title', default='', null=True, blank=True)
    audio = models.FileField('Audio', null=True, blank=True, upload_to='audios/')
    tags = models.ManyToManyField('node.NodeTag', verbose_name='Tags')
    body_type = models.CharField(
        max_length=50,
        choices=NodeBodyTypeEnum.choices(),
        default=NodeBodyTypeEnum.TEXT,
    )
    body = models.JSONField('Body', default=dict)
