from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class RiskFactor(models.Model):
    """
    사전 정의된 재난 정보

    Args:
        name (CharField): 위험 정보에 대한 이름
        risk_level (PositiveIntegerField): 재난에 대한 위험 수준, 최소 0 ~ 최대 5
        risk_impact (PositiveIntegerField): 재난이 끼치는 영향, 최소 0 ~ 최대 100
    """

    name = models.CharField(max_length=100)
    risk_level = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    risk_impact = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'risk_factor'
        verbose_name = 'risk_factor'
        verbose_name_plural = 'risk_factors'

    def to_dict(self):
        return {
            'name': self.name,
            'risk_level': self.risk_level,
            'risk_impact': self.risk_impact
        }
