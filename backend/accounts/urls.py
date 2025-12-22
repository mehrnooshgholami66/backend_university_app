from django.urls import path
from .views import ProfessorListAPIView, LoginAPIView, CreateUserApiView, BlockUserApiView, UnBlockUserApiView, DeleteUserApiView

urlpatterns = [
    path("login/", LoginAPIView.as_view()),
    path("professors/", ProfessorListAPIView.as_view()),
    path("create-user/", CreateUserApiView.as_view(), name="create-user-api"),
    path("block-user/<str:username>/", BlockUserApiView.as_view(), name="block-user-api"),
    path("unblock-user/<str:username>/", UnBlockUserApiView.as_view(), name="unblock-user-api"),
    path("delete-user/<str:username>/", DeleteUserApiView.as_view(), name="delete-user-api"),
]

