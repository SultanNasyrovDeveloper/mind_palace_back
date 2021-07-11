from django.db import models


class BaseMindPalace(models.Model):

    root = models.OneToOneField(
        'node.MindPalaceNode', on_delete=models.SET_DEFAULT, default=None, null=True, blank=True,
    )

    class Meta:
        abstract = True


class UserMindPalace(BaseMindPalace):

    user = models.OneToOneField('account.User', on_delete=models.CASCADE)
