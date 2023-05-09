from django.db import models


class DeviceToken(models.Model):
    """
    FCM에서 사용될 Device Token을 저장하기 위한 Model

    Args:
        user (ForeignKey): 사용자 ForeignKey
        token (CharField): Token 값
    """

    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, default=None)
    token = models.CharField(max_length=500)

    class Meta:
        db_table = 'device_token'
        verbose_name = 'device_token'
        verbose_name_plural = 'device_tokens'
