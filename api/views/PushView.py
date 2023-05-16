from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializer import PushSerializer


class PushView(APIView):
    """
    Firebase를 통해 target_user에게 msg를 전송하는 API

    Args:
        request (Request): 정보를 입력받기 위한 HttpRequest
    """

    serializer_class = PushSerializer

    @swagger_auto_schema(
        operation_id='POST /push',
        operation_description='(메시지 전송) POST 요청으로 정보를 입력받고, 메시지를 보냅니다.',
        manual_parameters=[openapi.Parameter('target_user', openapi.IN_PATH, description='수신자 ID', required=True,
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('msg', openapi.IN_PATH, description='내용', required=True,
                                             type=openapi.TYPE_STRING)],
        responses={202: openapi.Response(
            description='전송 요청 성공',
            examples={
                'application/json': {
                    'result': 'requsted',
                }
            }
        ), 400: openapi.Response(
            description='입력된 값이 잘못됨',
            examples={
                'application/json': {
                    'error': 'input error'
                }
            }
        ), 401: openapi.Response(
            description='전송 실패',
            examples={
                'application/json': {
                    'error': 'error'
                }
            })
        })
    def post(self, request):
        target_user = request.data.get('target_user')
        msg = request.data.get('msg')

        return Response({'result': 'requested'}, status=status.HTTP_202_ACCEPTED)
