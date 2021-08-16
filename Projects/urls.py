from django.urls import path
from . import views

app_name = 'Projects'

urlpatterns = [
    path("", views.ProjectView.as_view(), name="Project"),
    path("Projects/<slug>", views.ProjectDetail.as_view(), name="ProjectDetail"),
]


