from rest_framework.routers import DefaultRouter

from mind_palace_back.learning.stats import views


router = DefaultRouter()
router.register('', views.NodeLearningStatisticsViewSet)

urlpatterns = router.urls