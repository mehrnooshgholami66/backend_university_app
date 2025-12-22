from django.urls import path
from .views import (
    DocumentByProfessorAPIView,
    DocumentUploadAPIView,
)

urlpatterns = [
    path("professor/<int:professor_id>/", DocumentByProfessorAPIView.as_view()),
    path("upload/", DocumentUploadAPIView.as_view()),
]
