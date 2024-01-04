from rest_framework import serializers
from .models import Incident


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'
        read_only_fields = ['incident_id']
        extra_kwargs = {
            'type': {'required': False},
            'timestamp': {'required': False},
            'description': {'required': False},
            'severity': {'required': False},

        }
