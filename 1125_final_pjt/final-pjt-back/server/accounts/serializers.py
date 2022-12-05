from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# from .models import User
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "email",)


class UserInfoSerializer(serializers.ModelSerializer):
    followers_cnt = serializers.IntegerField(source='followers.count', read_only=True)
    followers_info = serializers.CharField(source='followers', read_only=True)
    # like_info = serializers.CharField(source='like_movies', read_only=True
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "followings", "followers_info", "followers_cnt", "id",)


# jwt token 결과 커스텀 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)

        token = self.get_token(self.user)
        
        # response에 추가하고 싶은 key값들 추가
        data['username'] = self.user.username
        data['refresh'] = str(token)
        data['access'] = str(token.access_token)
        # data['isFirst'] = self.user.isFirst
        
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
