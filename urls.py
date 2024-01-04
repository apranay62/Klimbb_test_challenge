from django.urls import path
from .views import IncidentListCreateView, IncidentUpdateView

urlpatterns = [
    path(
        'incidents/', IncidentListCreateView.as_view(),
        name='incident-list-create'),
    path(
        'incidents/<uuid:pk>/', IncidentUpdateView.as_view(),
        name='incident-update'),
]
