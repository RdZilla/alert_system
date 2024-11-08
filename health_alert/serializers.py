from rest_framework import serializers

from health_alert.models import HealthMeasurements


class UploadDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMeasurements
        fields = "__all__"
