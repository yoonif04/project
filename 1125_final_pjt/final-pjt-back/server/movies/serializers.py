from rest_framework import serializers
from .models import Movie, Comment, Genre
from accounts.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie',)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)

class MovieListSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(read_only=True, many=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'