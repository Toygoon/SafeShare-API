from django.db import models
from django.utils.timezone import now


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

    title = models.TextField(max_length=50)
    summary = models.TextField(max_length=500)
    reported_at = models.DateTimeField(default=now)
    is_solved = models.BooleanField(default=False)
    risk_factor = models.ForeignKey(on_delete=models.SET_NULL, null=True, default=None, to='RiskFactor')
    latlng = models.ForeignKey(on_delete=models.SET_NULL, null=True, default=None, to='LatLng')
    user = models.ForeignKey(on_delete=models.SET_NULL, null=True, default=None, to='User')

    class Meta:
        db_table = 'risk_report'
        verbose_name = 'risk_report'
        verbose_name_plural = 'risk_reports'

    def to_dict(self):
        return {
            'title': self.title,
            'summary': self.summary,
            'reported_at': self.reported_at,
            'is_solved': self.is_solved,
            'risk_factor': self.risk_factor.to_dict(),
            'latlng': self.latlng.to_dict(),
            'user': self.user.user_id
        }

    def __lt__(self, other):
        is_solved = self.is_solved and other.is_solved

        if is_solved:
            return self.reported_at < other.reported_at
        else:
            return not self.is_solved
