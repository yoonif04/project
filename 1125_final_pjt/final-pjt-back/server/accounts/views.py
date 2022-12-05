from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, UserInfoSerializer
from movies.serializers import MovieListSerializer
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.http.response import JsonResponse
from krwordrank.word import summarize_with_keywords
from konlpy.tag import Okt

@api_view(['POST'])
def signup(request):
    # 비밀번호, 비밀번호 확인
    password = request.data.get('password')
    password_confirm = request.data.get('passwordConfirm')
    
    if password != password_confirm:
        return Response({"error : 비밀번호가 일치하지 않습니다!"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)
    # 데이터가 유효한지 검증
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 사용자의 암호를 해쉬함수를 통해 바꿔줌(암호화)
        user.set_password(request.data.get('password'))
        # 바꾼 비밀번호로 다시 저장
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    serializer = UserInfoSerializer(person)
    return Response(serializer.data)

    # User = get_user_model()
    # person = get_object_or_404(User, nickname=nickname)
    # movies = person.like_movies.all()
    # movieSerializer = MovieSerializer(movies, many=True)

    # context = {
    #     'person': person,
    # }
    # return render(request, 'accounts/profile.html', context)

@api_view(['GET'])
def like_movies(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    movies = person.like_movies.all()
    serializer = MovieListSerializer(movies,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movies_wordcloud(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    movies = person.like_movies.all()
    texts = []
    okt = Okt()
    for movie in movies:
        texts.append(' '.join(okt.nouns(movie.overview)))
        texts.append(' '.join(okt.nouns(movie.title)))
    
    
    # # 명사만 추출하기
    # okt = Okt()
    # texts = okt.nouns(texts)
    
    stopwords = {'자신','영화', '관람객', '너무', '정말', '보고', '일부', '완전히', '된다.', '하지만', '하는', '위해', '한다.', '있는'}
    keywords = summarize_with_keywords(texts, min_count=1, max_length=10,
    beta=0.85, max_iter=10, stopwords=stopwords, verbose=True)

    
    wordlist = []
    # count = 0
    for key, val in keywords.items():
        temp = {'name': key, 'value': int(val*100)}
        wordlist.append(temp)
        # count += 1
        # if count >= 30:
        #     break
    print(wordlist)
    return Response(wordlist)

@api_view(['POST'])
def follow(request, username):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), username=username)
        user = request.user
        if person != user:
            if person.followers.filter(username=user.username).exists():
                person.followers.remove(user)
                is_followed = False
            else:
                person.followers.add(user)
                is_followed = True
            context = {
                'is_followed': is_followed,
                'followers_count': person.followers.count(),
                'followings_count': person.followings.count(),
            }
            return JsonResponse(context)
    #     return redirect('accounts:profile', person.username)
    # return redirect('accounts:login')

@api_view(['GET'])
def follow_check(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    user = request.user
    if person.followers.filter(username=user.username).exists():
        is_followed = True
    else:
        is_followed = False
    context = {
        'is_followed': is_followed,
        'followers_count': person.followers.count(),
        'followings_count': person.followings.count(),
    }
    return JsonResponse(context)

@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':
        users = get_list_or_404(get_user_model())
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
