import django_filters as filters

from mind_palace_back.palace.node import models


class MindPalaceNodeFilter(filters.FilterSet):
    class Meta:
        model = models.MindPalaceNode
        fields = {'title': ('icontains', )}
