from django.urls import path
from django.urls import include


from .views import BooksList
from .views import AuthorsList
from .views import AuthorDetail
from .views import GenresList
from .views import GenreDetail
from .views import PostViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    path('api/bookslist/', BooksList.as_view()),
    path('api/authorslist/', AuthorsList.as_view()),
    path('api/authorslist/<int:pk>/', AuthorDetail.as_view()),
    path('api/generslist/', GenresList.as_view()),
    path('api/generslist/<int:pk>/', GenreDetail.as_view()),
    path('api/', include(router.urls)),
]
