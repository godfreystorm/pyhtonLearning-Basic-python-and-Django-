from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("godfrey", views.godfrey, name="godfrey"),
    path("shifu", views.shifu, name="shifu")
]