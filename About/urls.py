from django.urls import path
from . import views

app_name = 'About'

urlpatterns = [
    path("", views.AboutView.as_view(), name="About"),
    path("FAQ/", views.FaqView.as_view(), name="FAQ")
]
