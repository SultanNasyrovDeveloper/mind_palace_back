from django.urls import include, path
from rest_framework import routers

from mind_palace.palace import views


router = routers.DefaultRouter()
router.register('palaces', views.UserMindPalaceViewSet)

urlpatterns = router.urls
