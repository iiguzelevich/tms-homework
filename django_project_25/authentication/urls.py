from django.urls import path
from django.urls import include
from django.urls import re_path

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

from .views import UserPofileCreateView
from .views import UserPofileDetailView

urlpatterns = [
    re_path(r'^all-profile/', UserPofileCreateView.as_view()),
    re_path(r'^profile/<int:pk>', UserPofileDetailView.as_view()),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    re_path(r'^api/auth/', include('djoser.urls')),
    path(
        'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'
         ),
    path(
        'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
    path(
        'api/token/refresh/', TokenVerifyView.as_view(), name='token_refresh'
    ),
]
