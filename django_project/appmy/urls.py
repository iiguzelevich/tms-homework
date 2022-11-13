from django.urls import path


from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('addinformation/', add_information, name='add_information'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:category_id>/', show_category, name='category'),
]
