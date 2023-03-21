from django.db import models


class RiskReport(models.Model):
    """
    발생된 재난 정보의 상세 내용을 저장하는 Model

    Args:
        summary (TextField): 위험 발생시 기재된 내용
        reported_at (DateTimeField): 재난 신고된 시각
        is_solved (BooleanField): 재난 신고가 해결된지 여부
        risk_factor (ForeignKey): RiskFactor의 외래키, 위험 종류
        latlng (ForeignKey): LatLng의 외래키
        user (ForeignKey): User의 외래키
    """

    summary = models.TextField(max_length=500)
    reported_at = models.DateTimeField(auto_now=True)
    is_solved = models.BooleanField(default=False)
    risk_factor = models.ForeignKey(on_delete=models.SET_NULL, null=True, default=None, to='RiskFactor')
    latlng = models.ForeignKey(on_delete=models.SET_NULL, null=True, default=None, to='LatLng')
    user = models.ForeignKey(on_delete=models.SET_NULL, null=True, default=None, to='User')

    class Meta:
        db_table = 'risk_report'
        verbose_name = 'risk_report'
        verbose_name_plural = 'risk_reports'