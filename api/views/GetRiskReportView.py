from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User, RiskReport
from api.serializer import UserSerializer


class GetRiskReportView(APIView):
    """
    발생한 재난 목록을 전문 요원이 받기 위한 API

    Args:
        request (Request): 재난 정보를 입력받기 위한 HttpRequest
    """

    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_id='POST /get_risk_report',
        operation_description='(정보 요청) POST 요청으로 전문 요원의 ID와 비밀번호를 전달합니다.',
        manual_parameters=[openapi.Parameter('user_id', openapi.IN_PATH, description='아이디', required=True,
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('user_pw', openapi.IN_PATH, description='비밀번호', required=True,
                                             type=openapi.TYPE_STRING)],
        responses={202: openapi.Response(
            description='요청 완료',
            examples={
                'application/json': {
                    'result': 'accepted'
                }
            }

        ), 400: openapi.Response(
            description='인증 실패',
            examples={
                'application/json': {
                    'error': 'input error'
                }
            }
        ), 401: openapi.Response(
            description='권한 없음',
            examples={
                'application/json': {
                    'error': 'authentication error'
                }
            }
        )
        })
    def post(self, request):
        # User inputs the ID, and Password
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')

        # If the user input has some errors
        if user_id is None or user_pw is None \
                or len(user_id) < 2 or len(user_pw) < 2:
            return Response({'error': 'input error'}, status=status.HTTP_400_BAD_REQUEST)

        # Find the user from table
        user: User = None
        try:
            user = User.objects.all().filter(user_id=user_id, user_pw=user_pw).last()
        except:
            pass

        # Failed to find user, or password error
        if user is None:
            return Response({'error': 'authentication error'}, status=status.HTTP_401_UNAUTHORIZED)

        true = sorted(list(RiskReport.objects.all().filter(is_solved=True)))
        false = sorted(list(RiskReport.objects.all().filter(is_solved=False)))

        return Response({'result': [x.to_json() for x in false + true]}, status=status.HTTP_200_OK)
