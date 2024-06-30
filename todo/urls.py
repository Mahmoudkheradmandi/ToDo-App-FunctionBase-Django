from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path("", views.home, name="home"),
    path("update/<str:pk>/", views.update, name="update"),
    path("complete/<str:pk>/", views.complete, name="complete"),
    path("delete/<str:pk>/", views.delete, name="delete"),
]