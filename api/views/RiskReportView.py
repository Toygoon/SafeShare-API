from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import RiskFactor, RiskReport, LatLng, User
from api.serializer import RiskReportSerializer


class RiskReportView(APIView):
    """
    재난 요청을 수신하는 API

    Args:
        request (Request): 재난 정보를 입력받기 위한 HttpRequest
    """

    queryset = RiskReport.objects.all()
    serializer_class = RiskReportSerializer

    @swagger_auto_schema(
        operation_id='POST /risk_report',
        operation_description='(회원가입) POST 요청으로 재난 정보를 요청받습니다.',
        manual_parameters=[openapi.Parameter('summary', openapi.IN_PATH, description='내용', required=True,
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('risk_factor', openapi.IN_PATH, description='재난 유형', required=True,
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('lat', openapi.IN_PATH, description='위도', required=True,
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('lng', openapi.IN_PATH, description='경도', required=True,
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('user', openapi.IN_PATH, description='아이디', required=True,
                                             type=openapi.TYPE_STRING)],
        responses={202: openapi.Response(
            description='요청 완료',
            examples={
                'application/json': {
                    'result': 'accepted'
                }
            }

        ), 400: openapi.Response(
            description='존재하지 않는 회원',
            examples={
                'application/json': {
                    'error': 'not existing user'
                }
            }
        )
        })
    def post(self, request):
        summary = request.data.get('summary')
        risk_factor_name = request.data.get('risk_factor')
        lat = request.data.get('lat')
        lng = request.data.get('lng')
        user_id = request.data.get('user')

        # Check risk factor is pre-defined
        risk_factor = RiskFactor.objects.all().filter(name=risk_factor_name)

        # If not pre-defined data has input, create the new risk_factor
        if len(risk_factor) < 1:
            risk_factor = RiskFactor(name=risk_factor_name)
            risk_factor.save()
        else:
            risk_factor = risk_factor.last()

        # Create latlng record
        latlng = LatLng(lat=lat, lng=lng)
        latlng.save()

        # Find user
        user = User.objects.all().filter(user_id=user_id)

        if len(user) < 1:
            return Response({'error': 'not existing user'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = user.last()

        # Create risk report
        risk_report = RiskReport(summary=summary, latlng=latlng, risk_factor=risk_factor, user=user)
        risk_report.save()

        return Response({'result': 'accepted'}, status=status.HTTP_202_ACCEPTED)
