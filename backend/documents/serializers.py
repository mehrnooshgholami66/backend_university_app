from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    professor = serializers.CharField(source="professor.username")

    class Meta:
        model = Document
        fields = [
            "id",
            "title",
            "file_type",
            "professor",
            "file",
            "created_at"
        ]
