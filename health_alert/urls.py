from django.urls import path

from health_alert.views import UploadDataView

urlpatterns = [
    path("employee/<str:pk>/upload_data", UploadDataView.as_view(), name="upload_data"),
]
