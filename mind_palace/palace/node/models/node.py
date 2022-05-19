from django.db import models

from mind_palace.palace.node.models import BaseMindPalaceNode


class MindPalaceNode(BaseMindPalaceNode):

    title = models.TextField('Title', default='', null=True, blank=True)
    audio = models.FileField('Audio', null=True, blank=True, upload_to='audios/')
    tags = models.ManyToManyField('node.NodeTag', verbose_name='Tags')

    def get_owner_id(self):
        # TODO: Cache or prevent +1 request other way.
        root_node = self
        if not self.is_root_node():
            # TODO: maybe prefetch related mind palace
            root_node = self.get_root()
        return root_node.mind_palace.user_id