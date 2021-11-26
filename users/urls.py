from rest_framework import routers
from django.urls import path, include

import users.views as views

router = routers.DefaultRouter()
router.register("user", views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
