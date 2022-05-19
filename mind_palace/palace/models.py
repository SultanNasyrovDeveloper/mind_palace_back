from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from mind_palace.account.models import User
from mind_palace.palace.node.models import MindPalaceNode


class BaseMindPalace(models.Model):

    root = models.OneToOneField(
        'node.MindPalaceNode', on_delete=models.SET_DEFAULT, default=None, null=True, blank=True,
        related_name='mind_palace'
    )

    class Meta:
        abstract = True


class UserMindPalace(BaseMindPalace):

    user = models.OneToOneField('account.User', on_delete=models.CASCADE, related_name='mypalace')


@receiver(post_save, sender=User)
def create_user_mind_palace(instance, created, **kwargs):
    if created:
        root_node = MindPalaceNode.objects.create(name='My palace', owner=instance)
        UserMindPalace.objects.create(user=instance, root=root_node)

