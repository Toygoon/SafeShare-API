from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User
from api.serializer import RegisterSerializer


class RegisterView(APIView):
    """
    회원가입을 담당하는 API

    Args:
        request (Request): 회원가입 정보를 입력받기 위한 HttpRequest
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    @swagger_auto_schema(
        operation_id='POST /register',
        operation_description='(회원가입) POST 요청으로 각 정보를 입력받고, 성공 여부를 반환합니다.',
        manual_parameters=[openapi.Parameter('user_id', openapi.IN_PATH, description='아이디', required=True,
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('user_pw', openapi.IN_PATH, description='비밀번호', required=True,
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('name', openapi.IN_PATH, description='실명', required=True,
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('mobile', openapi.IN_PATH, description='휴대폰 번호', required=True,
                                             type=openapi.TYPE_STRING)],
        responses={201: openapi.Response(
            description='회원가입 성공',
            examples={
                'application/json': {
                    'result': 'created'
                }
            }

        ), 226: openapi.Response(
            description='중복 아이디',
            examples={
                'application/json': {
                    'error': 'duplicated user_id'
                }
            }
        ), 400: openapi.Response(
            description='입력된 값이 잘못됨',
            examples={
                'application/json': {
                    'error': 'input error'
                }
            }
        )
        })
    def post(self, request):
        # User inputs the ID, and Password
        d = {'user_id': request.data.get('user_id'),
             'user_pw': request.data.get('user_pw'),
             'name': request.data.get('name'),
             'mobile': request.data.get('mobile')}

        for k in d.keys():
            # If the user input has some errors
            if len(d[k]) < 1:
                return Response({'error': 'input error'}, status=status.HTTP_400_BAD_REQUEST)

        # Find already existing user_id
        if len(User.objects.all().filter(user_id=d['user_id'])) > 0:
            return Response({'error': 'duplicated user_id'}, status=status.HTTP_226_IM_USED)

        # Create a user
        user = User(user_id=d['user_id'], user_pw=d['user_pw'], name=d['name'], mobile=d['mobile'])
        user.save()

        return Response({'result': 'created'}, status=status.HTTP_201_CREATED)
