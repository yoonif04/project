from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/like_movies/', views.like_movies, name='like_movies'),
    path('user_list/', views.user_list, name='user_list'),
    path('profile/<username>/movies_wordcloud/', views.movies_wordcloud, name='movies_wordcloud'),
    path('<username>/follow/', views.follow, name='follow'),
    path('<username>/follow_check/', views.follow_check, name='follow_check'),
]
