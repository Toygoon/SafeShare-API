from django.db import models


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
