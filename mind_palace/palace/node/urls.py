from rest_framework import routers

from mind_palace.palace.node.api.node import MindPalaceNodeViewSet
from mind_palace.palace.node.api.media import MindPalaceNodeMediaViewSet


router = routers.DefaultRouter()
router.register('nodes/media', MindPalaceNodeMediaViewSet)
router.register('nodes', MindPalaceNodeViewSet)



urlpatterns = router.urls