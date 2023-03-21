from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User 객체의 직렬화 클래스
    """

    class Meta:
        model = User
        fields = ['user_id', 'user_pw']


class RegisterSerializer(serializers.ModelSerializer):
    """
    RegisterView에서 쓰이는 회원가입용 직렬화 클래스
    """

    class Meta:
        model = User
        fields = ['user_id', 'user_pw', 'name', 'mobile']
