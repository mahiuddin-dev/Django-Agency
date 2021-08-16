from django.urls import path
from . import views

app_name = 'Services'

urlpatterns = [
    path('', views.ServicesView.as_view(), name='Services'),
    path('Service/<slug>/', views.ServiceListView.as_view(), name='ServiceList'),
]