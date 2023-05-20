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


class RiskReportSerializer(serializers.Serializer):
    """
    RiskReport에서 쓰이는 재난보고 직렬화 클래스
    """

    summary = serializers.CharField(max_length=500)
    risk_factor = serializers.CharField(max_length=100)
    lat = serializers.FloatField()
    lng = serializers.FloatField()
    user = serializers.CharField(max_length=50)


class AppTokenSerializer(serializers.Serializer):
    """
    Firebase의 token을 수신하기 위한 직렬화 클래스
    """

    token = serializers.CharField(max_length=500)
    user = serializers.CharField(max_length=50)


class PushSerializer(serializers.Serializer):
    """
    Push로 메시지를 보내기 위한 직렬화 클래스
    """

    target_user = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=100)
    msg = serializers.CharField(max_length=500)
