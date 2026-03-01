from django.urls import path
from . import views

urlpatterns = [
    path("", views.dragon_ui, name="dragon-ui"),
    path("dragons/", views.DragonListCreate.as_view(), name="dragon-view-create"),
    path("dragons/<int:pk>", views.DragonRetrieveUpdateDestroy.as_view(), name="dragon-update"),
]