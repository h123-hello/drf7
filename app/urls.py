from django.conf.urls import url
from rest_framework_jwt.views import ObtainJSONWebToken,obtain_jwt_token

from django.urls import path
# 只需注册路由,内部自动注册路由
from app import views

urlpatterns = [
    url(r"login/", ObtainJSONWebToken.as_view()),
    url(r"obt/", obtain_jwt_token),
    path("user/", views.UserDetailAPIView.as_view()),
    path("check/", views.LoginAPIView.as_view()),
]
