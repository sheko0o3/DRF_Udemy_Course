from .views import (HelloApiView, HelloViewSet, UserProfileViewSet,
                    UserLoginApiView,
                    ProfileFeedItemViewSet)

from django.urls import path, include

from rest_framework.routers import DefaultRouter   # >>>>  ViewSet

router = DefaultRouter()
router.register(prefix='CBV-ViewSet', viewset=HelloViewSet, basename="ViewSet")
router.register(prefix="profile", viewset=UserProfileViewSet)
router.register(prefix="feed", viewset=ProfileFeedItemViewSet)

urlpatterns = [
    path("CBV-APIView/", HelloApiView.as_view()),
    path('CBV-ViewSet/', include(router.urls)),
    path('login/', UserLoginApiView.as_view()),

]
