from rest_framework import generics
from .models import Incident
from .serializers import IncidentSerializer
# Create your views here.

HANDELRS = ["Alice", "Bob", "Charlie"]


class IncidentListCreateView(generics.ListCreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    def perform_create(self, serializer):
        incident = serializer.save()
        self.handle_incident(incident)

    def handle_incident(self, incident):
        if incident.severity == 1:
            self.assign_to_first_available_handler(incident)
        elif incident.severity == 3:
            self.assign_based_on_timestamp(incident)
        elif incident.status == 'Resolved':
            self.assign_next_pending_incident()
        elif self.all_handlers_busy():
            incident.status = 'Pending'
            incident.save()
        elif incident.severity == 4:
            incident.type = "Security Breach"
            incident.save()
            self.escalate_incident(incident)

    def assign_to_first_available_handler(self, incident):
        handlers = ["Alice", "Bob", "Charlie"]
        incident.assigned_to = handlers[0]
        incident.save()

    def assign_based_on_timestamp(self, incident):
        handlers = ["Alice", "Bob", "Charlie"]
        incidents = Incident.objects.filter(
                severity=3, status='Open').order_by('timestamp')
        if incidents.exists():
            next_handler_index = len(incidents) % len(handlers)
            incident.assigned_to = handlers[next_handler_index]
            incident.save()

    def assign_next_pending_incident(self):
        handlers = ["Alice", "Bob", "Charlie"]
        pending_incidents = Incident.objects.filter(
                status='Pending').order_by('severity')
        if pending_incidents.exits():
            next_handler_index = len(pending_incidents) % len(handlers)
            pending_incident = pending_incidents.first()
            pending_incident.assigned_to = handlers[next_handler_index]
            pending_incident.status = 'Open'
            pending_incident.save()

    def all_handlers_busy(self):
        handlers = ["Alice", "Bob", "Charlie"]
        busy_handlers = set(Incident.objects.exclude(
                status='Pending').values_list('assigned_to', flat=True))
        return set(handlers) == busy_handlers

    def escalate_incident(self, incident):
        if incident.severity == 4:
            incident.severity = 1
            incident.save()


class IncidentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    print('queryset', queryset)
    print('serializer_class', serializer_class)
    http_method_names = ['put']

    def perform_update(self, serializer):
        update_fields = serializer.validated_data.keys()
        if set(update_fields) <= {'status', 'assigned_to'}:
            serializer.save()
