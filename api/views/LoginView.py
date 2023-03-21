from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User
from api.serializer import UserSerializer


class LoginView(APIView):
    """
    로그인을 담당하는 API

    Args:
        request (Request): id, pw를 입력받기 위한 HttpRequest
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_id='POST /login',
        operation_description='(로그인) POST 요청으로 아이디와 비밀번호를 입력받고, 성공 여부를 반환합니다.',
        manual_parameters=[openapi.Parameter('user_id', openapi.IN_PATH, description='아이디', required=True,
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('user_pw', openapi.IN_PATH, description='비밀번호', required=True,
                                             type=openapi.TYPE_STRING)],
        responses={200: openapi.Response(
            description='로그인 성공',
            examples={
                'application/json': {
                    'result': 'ok'
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
            description='로그인 실패',
            examples={
                'application/json': {
                    'error': 'authentication error'
                }
            })
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
        user = None
        try:
            user = User.objects.all().filter(user_id=user_id, user_pw=user_pw).last()
        except:
            pass

        print(user)
        # Failed to find user, or password error
        if user is None:
            return Response({'error': 'authentication error'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({'result': 'ok'}, status=status.HTTP_200_OK)
