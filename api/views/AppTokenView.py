from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.management import check_user
from api.serializer import AppTokenSerializer


class AppTokenView(APIView):
    """
    Firebase에서 사용되는 token을 User 테이블에서 갱신하는 API

    Args:
        request (Request): 정보를 입력받기 위한 HttpRequest
    """

    serializer_class = AppTokenSerializer

    @swagger_auto_schema(
        operation_id='POST /app_token',
        operation_description='(Token 갱신) POST 요청으로 아이디와 token을 입력받고, 데이터베이스를 업데이트합니다.',
        manual_parameters=[openapi.Parameter('user_id', openapi.IN_PATH, description='아이디', required=True,
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('token', openapi.IN_PATH, description='token', required=True,
                                             type=openapi.TYPE_STRING)],
        responses={202: openapi.Response(
            description='업데이트 성공',
            examples={
                'application/json': {
                    'result': 'ok'
                }
            }
        ), 400: openapi.Response(
            description='존재하지 않는 사용자',
            examples={
                'application/json': {
                    'error': 'user error'
                }
            }
        )}
    )
    def post(self, request):
        token = request.data.get('token')
        user_id = request.data.get('user_id')

        # Find user
        user = check_user(user_id)

        if user is None:
            return Response({'error': 'user error'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'result': 'ok'}, status=status.HTTP_202_ACCEPTED)
