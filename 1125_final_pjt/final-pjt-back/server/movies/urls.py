from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('<int:movie_pk>/comments/', views.comment_create),
    path('<int:movie_pk>/check/', views.likes, name='check'),
    path('<int:movie_pk>/likes/', views.likes, name='likes'),
]
