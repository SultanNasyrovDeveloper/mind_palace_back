from django.db import models
from django.dispatch import dispatcher
from django.contrib.postgres.fields import ArrayField

from mind_palace.palace.node.models import MindPalaceNode
from .enums import LearningCardField


def get_default_learning_card_fields():
    return [LearningCardField.name]


class UserMindPalaceNodeLearningConfiguration(models.Model):

    enable = models.BooleanField(default=True)
    learning_card_fields = ArrayField(
        models.CharField(max_length=30, choices=LearningCardField.choices()),
        default=get_default_learning_card_fields,
    )