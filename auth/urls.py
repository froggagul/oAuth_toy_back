from django.urls import path
from auth.views import MeView

urlpatterns = [
    path("me/", MeView.as_view(), name="me"),
]
