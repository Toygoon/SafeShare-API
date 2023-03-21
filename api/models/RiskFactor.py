from django.db import models


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
