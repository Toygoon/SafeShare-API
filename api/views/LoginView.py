from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializer import UserSerializer


class LoginView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
            user = User.objects.all.filter(user_id=user_id, user_pw=user_pw)
        except:
            pass

        # Failed to find user, or password error
        if user is None:
            return Response({'error': 'authentication error'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({'result': 'ok'}, status=status.HTTP_200_OK)
