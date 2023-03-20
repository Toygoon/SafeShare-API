from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
class User(models.Model):
    """
    사용자 정보를 저장하는 Model
    
    Args:
        user_id (CharField): 아이디
        user_pw (CharField): 비밀번호
        name (CharField): 이름
        mileage (PositiveIntegerField): 마일리지
        mobile (CharField): 전화번호
    """

    user_id = models.CharField(max_length=10)
    user_pw = models.CharField(max_length=50)
    name = models.CharField(max_length=10)
    mileage = models.PositiveIntegerField()
    mobile = models.CharField(max_length=50)


class LatLng(models.Model):
    """
    위도(Lat), 경도(Lng)를 저장하는 Model

    Args:
        lat (FloatField): latitude, 위도
        lng (FloatField): longitude, 경도
        addr (CharField): 상세 주소
    """
    lat = models.FloatField()
    lng = models.FloatField()
    addr = models.CharField(max_length=200)


class UserAction(models.Model):
    """
    사용자의 재난 요청을 저장하는 Model

    Args:
        startTime (DateTimeField): 시작 시간
        endTime (DateTimeField): 종료 시간
        user (ForeignKey): User의 외래키
        lng (ForeignKey): LatLng의 외래키
    """
    startTime = models.DateTimeField(auto_now=False, default=None, null=True)
    endTime = models.DateTimeField(auto_now=False, default=None, null=True)
    user = models.ForeignKey(on_delete=models.SET_NULL, null=True, default=None)
    latlng = models.ForeignKey(on_delete=models.SET_NULL, null=True, default=None)


class RiskReport(models.Model):
    """
    발생된 재난 정보의 상세 내용을 저장하는 Model

    Args:
        risk_factor (ForeignKey): RiskFactor의 외래키, 위험 종류
        summary (TextField): 위험 발생시 기재된 내용
        latlng (ForeignKey): LatLng의 외래키
        user (ForeignKey): User의 외래키
        reported_at (DateTimeField): 재난 신고된 시각
        is_solved (BooleanField): 재난 신고가 해결된지 여부
    """
    risk_factor = models.ForeignKey(on_delete=models.SET_NULL, null=True, default=None)
    summary = models.TextField(max_length=500)
    latlng = models.ForeignKey(on_delete=models.SET_NULL, null=True, default=None)
    user = models.ForeignKey(on_delete=models.SET_NULL, null=True, default=None)
    reported_at = models.DateTimeField(auto_now=True)
    is_solved = models.BooleanField(default=False)


class RiskFactor(models.Model):
    """
    사전 정의된 재난 정보

    Args:
        name (CharField): 위험 정보에 대한 이름
        risk_level (PositiveIntegerField): 재난에 대한 위험 수준
    """
    name = models.CharField(max_length=100)
    risk_level = models.PositiveIntegerField()
    risk_impact = models.PositiveIntegerField()
