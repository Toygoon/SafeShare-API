from django.db import models


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

    class Meta:
        db_table = 'latlng'
        verbose_name = 'latlng'
        verbose_name_plural = 'latlngs'

    def to_dict(self):
        return {
            'lat': self.lat,
            'lng': self.lng
        }
