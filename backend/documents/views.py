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
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class DocumentByProfessorAPIView(ListAPIView):
    serializer_class = DocumentSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        professor_id = self.kwargs["professor_id"]
        return Document.objects.filter(professor_id=professor_id)
    



class DocumentUploadAPIView(APIView):
    """
    Upload document/article by professor
    """

    def post(self, request):
        professor_id = request.data.get("professor")

        if not professor_id:
            return Response(
                {"detail": "professor is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            professor = User.objects.get(id=professor_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "Professor not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DocumentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        document = serializer.save(professor=professor)

        return Response(
            DocumentSerializer(document).data,
            status=status.HTTP_201_CREATED
        )
    