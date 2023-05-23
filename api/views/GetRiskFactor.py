from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import RiskFactor


class GetRiskFactor(APIView):
    """
    RiskFactor 목록을 전달하는 API

    Args:
        request (Request): 입력 파라미터 없음, 단순 데이터 전달
    """

    @swagger_auto_schema(
        operation_id='GET /app_token',
        operation_description='(재난 종류 수신) 발생할 수 있는 모든 재난의 종류를 수신합니다.',
        responses={200: openapi.Response(
            description='정보 수신',
            examples={
                'application/json': {
                    "result": [
                        "환자 발생",
                        "폭력 사태",
                        "화재",
                        "태풍",
                        "낙석",
                        "붕괴"
                    ]
                }
            }
        )}
    )
    def get(self, request):
        return Response({'result': [x.name for x in RiskFactor.objects.all()]}, status=status.HTTP_200_OK)
