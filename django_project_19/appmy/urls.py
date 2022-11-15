from django.urls import path
from .views import index
from .views import show_post
from .views import about
from .views import feedback
from .views import login
from .views import show_professions
from .views import show_interests

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('show_professions/', show_professions, name='show_professions'),
    path('show_interests/', show_interests, name='show_interests'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('login/', login, name='login'),

]
