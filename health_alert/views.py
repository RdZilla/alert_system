from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.response import Response

from health_alert.models import HealthMeasurements
from health_alert.serializers import UploadDataSerializer
from health_alert.statuses import SwaggerStatuses


class UploadDataView(generics.CreateAPIView):
    serializer_class = UploadDataSerializer
    queryset = HealthMeasurements.objects.all()

    @extend_schema(
        tags=["Upload data"],
        summary="Upload data to the system",
        responses={
            status.HTTP_201_CREATED: UploadDataSerializer,
            **SwaggerStatuses.SCHEMA_GET_POST_STATUSES,
        }
    )
    def post(self, request, *args, **kwargs):
        employee_id = kwargs.get("pk")

        if not employee_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        employee = get_object_or_404(HealthMeasurements, id=employee_id)
        health_measurement_id = employee.health_measurement.id
        health_measurements = get_object_or_404(HealthMeasurements, id=employee_id)

        return super().post(request, *args, **kwargs)
