from django.db import models

from api.models import RiskFactor


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
    risk_factor = models.ForeignKey(on_delete=models.SET_NULL, null=True, default=None, to=RiskFactor)
    summary = models.TextField(max_length=500)
    latlng = models.ForeignKey(on_delete=models.SET_NULL, null=True, default=None)
    user = models.ForeignKey(on_delete=models.SET_NULL, null=True, default=None)
    reported_at = models.DateTimeField(auto_now=True)
    is_solved = models.BooleanField(default=False)
