import django_filters as filters

from mind_palace.palace.node import models


class MindPalaceNodeFilter(filters.FilterSet):

    class Meta:
        model = models.PalaceNode
        fields = {'description': ('icontains', )}
