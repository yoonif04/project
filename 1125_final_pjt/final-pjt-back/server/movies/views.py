from django.shortcuts import render, get_list_or_404, get_object_or_404
from .serializers import MovieListSerializer, CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Movie, Comment
from django.views.decorators.http import require_POST
from django.http import JsonResponse

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieListSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    if request.user == comment.user:
        if request.method == 'DELETE':
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def likes(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    # 현재 게시글에 좋아요를 누른 유저중에 현재 좋아요를 요청하는 유저를 검색해서 존재하는지를 확인 
    if movie.like_users.filter(username=request.user.username).exists():
        # 좋아요 취소 (remove)
        movie.like_users.remove(request.user)
        is_liked = False
    else:
        # 좋아요 추가 (add)
        movie.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return JsonResponse(context)

@api_view(['GET'])
def likes_check(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    print(request.user)
    if movie.like_users.filter(pk=request.user.id).exists():
        is_liked = True
    else:
        is_liked = False
    context = {
        'is_liked': is_liked,
    }
    return JsonResponse(context)

