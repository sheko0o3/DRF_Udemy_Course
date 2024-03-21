from .views import HelloApiView, HelloViewSet
from django.urls import path, include

from rest_framework.routers import DefaultRouter   # >>>>  ViewSet
router = DefaultRouter()
router.register(prefix='CBV-ViewSet', viewset=HelloViewSet, basename="ViewSet")

urlpatterns = [
    path("CBV-APIView/", HelloApiView.as_view()),
    path('CBV-ViewSet/', include(router.urls)),

]
