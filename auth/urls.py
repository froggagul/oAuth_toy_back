from django.urls import path
from auth.views import MeView  # TestLoginView

urlpatterns = [
    # path('login/', TestLoginView.as_view(),name = "login"),
    path("me/", MeView.as_view(), name="me"),
]
