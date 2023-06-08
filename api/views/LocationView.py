from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.management import check_user
from api.models import UserAction, LatLng
from api.serializer import LocationSerializer


class LocationView(APIView):
    """
    사용자의 위치 정보를 전달하는 함수

    Args:
        request (Request): 정보를 입력받기 위한 HttpRequest
    """

    serializer_class = LocationSerializer

    @swagger_auto_schema(
        operation_id='POST /location',
        operation_description='(위치 갱신) POST 요청으로 위도, 경도, 아이디를 입력받고, 데이터베이스를 업데이트합니다.',
        manual_parameters=[openapi.Parameter('user', openapi.IN_PATH, description='아이디', required=True,
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('lat', openapi.IN_PATH, description='위도', required=True,
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('lng', openapi.IN_PATH, description='경도', required=True,
                                             type=openapi.TYPE_STRING)],
        responses={202: openapi.Response(
            description='업데이트 성공',
            examples={
                'application/json': {
                    'result': 'updated'
                }
            }
        ), 201: openapi.Response(
            description='위치 정보만 저장',
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
        lat = request.data.get('lat')
        lng = request.data.get('lng')
        user_id = request.data.get('user')

        # Find user
        user = check_user(user_id)

        if user is None:
            return Response({'error': 'user error'}, status=status.HTTP_400_BAD_REQUEST)

        # Get user action
        user_action = UserAction.objects.all().last()
        latlng = LatLng(lat=float(lat), lng=float(lng))

        if user_action:
            user_action.latlng = latlng
            user_action.save()

            return Response({'result': 'updated'}, status=status.HTTP_202_ACCEPTED)
        else:
            latlng.save()
            return Response({'result': 'ok'}, status=status.HTTP_201_CREATED)
