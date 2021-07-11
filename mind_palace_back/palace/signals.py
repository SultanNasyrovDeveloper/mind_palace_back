from django.dispatch import receiver
from django.db.models.signals import post_save

from mind_palace_back.account.models import User
from mind_palace_back.palace.models import UserMindPalace
from mind_palace_back.palace.node.models import MindPalaceNode


@receiver(post_save, sender=User)
def create_user_mind_palace(instance, created, **kwargs):
    if created:
        root_node = MindPalaceNode.objects.create(name='My palace')
        UserMindPalace.objects.create(user=instance, root=root_node)
