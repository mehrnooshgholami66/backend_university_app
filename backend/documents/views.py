from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Document
from .serializers import DocumentSerializer
from rest_framework import status

class DocumentByProfessorAPIView(ListAPIView):
    serializer_class = DocumentSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        professor_id = self.kwargs["professor_id"]
        return Document.objects.filter(professor_id=professor_id)
    



class DocumentUploadAPIView(APIView):
    """
    Upload document/article by professor
    Auth فعلاً نداریم
    """

    def post(self, request):
        serializer = DocumentSerializer(
            data=request.data
        )

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        document = serializer.save()

        return Response(
            {
                "id": document.id,
                "title": document.title,
                "file": document.file.url,
                "file_type": document.file_type,
                "professor_id": document.professor_id,
                "created_at": document.created_at,
            },
            status=status.HTTP_201_CREATED
        )