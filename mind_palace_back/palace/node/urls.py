from rest_framework import routers

from mind_palace_back.palace.node import views


router = routers.DefaultRouter()
router.register('nodes', views.MindPalaceNodeViewSet)

urlpatterns = router.urls