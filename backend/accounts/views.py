from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import ProfessorSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import LoginSerializer
from .serializers import UserCreateSerializer
User = get_user_model()



class CreateUserApiView(APIView):
    """
    API برای ساخت یوزر توسط ادمین
    """
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # ساخت توکن برای API
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "username": user.username,
                "role": user.role,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProfessorListAPIView(ListAPIView):
    serializer_class = ProfessorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(
            role="professor",
            is_active=True
        )


class LoginAPIView(APIView):
    """
    Login API → return Token + user info
    """

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(
            request=request,
            username=username,
            password=password
        )

        if not user:
            return Response(
                {"detail": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not user.is_active:
            return Response(
                {"detail": "User is blocked"},
                status=status.HTTP_403_FORBIDDEN
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "user_id": user.id,
            "role": user.role,
            "username": user.username,
            "is_active": user.is_active
        })
    
class BlockUserApiView(APIView):

    def post(self, request, username):
        try:
            user = User.objects.get(username=username)
            if not user.is_active:
                return Response(
                    {"detail": f"User {username} is already blocked."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user.is_active = False
            user.save()
            return Response(
                {"detail": f"User {username} has been blocked."},
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )
class UnBlockUserApiView(APIView):
    def post(self, request, username):
        try:
            user = User.objects.get(username=username)
            if user.is_active:
                return Response(
                    {"detail": f"User {username} is already unblocked."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user.is_active = True
            user.save()
            return Response(
                {"detail": f"User {username} has been unblocked."},
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )
class DeleteUserApiView(APIView):
    def delete(self, request, username):
        try:
            user = User.objects.get(username=username)
            user.delete()
            return Response(
                {"detail": f"User {username} has been deleted."},
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )