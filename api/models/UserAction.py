from django.db import models


class UserAction(models.Model):
    """
    사용자의 재난 요청을 저장하는 Model

    Args:
        startTime (DateTimeField): 시작 시간
        endTime (DateTimeField): 종료 시간
        user (ForeignKey): User의 외래키
        lng (ForeignKey): LatLng의 외래키
    """

    id = models.AutoField(primary_key=True)
    startTime = models.DateTimeField(auto_now=False, default=None, null=True)
    endTime = models.DateTimeField(auto_now=False, default=None, null=True)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, default=None)
    latlng = models.ForeignKey('LatLng', on_delete=models.SET_NULL, null=True, default=None)

    class Meta:
        db_table = 'user_action'
        verbose_name = 'user_action'
        verbose_name_plural = 'user_actions'
