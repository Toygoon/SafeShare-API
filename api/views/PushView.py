from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from firebase_admin import messaging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User
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
                           openapi.Parameter('title', openapi.IN_PATH, description='제목', required=True,
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('msg', openapi.IN_PATH, description='내용', required=True,
                                             type=openapi.TYPE_STRING)],
        responses={202: openapi.Response(
            description='전송 요청 성공',
            examples={
                'application/json': {
                    'result': 'projects/safeshare-d3070/messages/0:1684552631533612%443631bc443631bc',
                }
            }
        ), 400: openapi.Response(
            description='전송 요청 실패',
            examples={
                'application/json': {
                    'error': 'The registration token is not a valid FCM registration token'
                }
            }
        ), 401: openapi.Response(
            description='사용자 오류',
            examples={
                'application/json': {
                    'error': 'no user found'
                }
            }
        ), 406: openapi.Response(
            description='메시지 오류',
            examples={
                'application/json': {
                    'error': 'message format error'
                }
            })
        })
    def post(self, request):
        target_user = request.data.get('target_user')
        title = request.data.get('title')
        msg = request.data.get('msg')

        # Message error
        if len(msg) < 1:
            return Response({'error', 'message format error'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        # Find the user from table
        user: User = None
        try:
            user = User.objects.all().filter(user_id=target_user).last()
        except:
            pass

        # Failed to find user
        if user is None:
            return Response({'error': 'no user found'}, status=status.HTTP_401_UNAUTHORIZED)

        # Create a new message
        app_token = user.app_token
        notification = messaging.Notification(title=title, body=msg)
        message = messaging.Message(notification=notification, token=app_token)

        # Send a new message
        response = None
        try:
            response = messaging.send(message)
        except Exception as e:
            return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'result': response}, status=status.HTTP_202_ACCEPTED)
