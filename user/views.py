import json
import logging


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializers import RegisterSerializer

# Create your views here.


logger = logging.getLogger('django')

class UserRegisterApiView(APIView):

    def post(self, request):
        """
        post method for registering a user
        """
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                logger.info("User successfully Registered ")
                return Response({'message': 'Register successfully', 'data': serializer.data},
                                status=status.HTTP_201_CREATED)
            return Response({'message': 'serializer.errors'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Exception as e:
            logger.exception(e)
            return Response({'message': 'invalid details'}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginApi(APIView):

    def post(self, request):
        """
         post method for checking login operation
        """

        try:

            login_user = User.objects.filter(username=request.data.get("username"),password=request.data.get("password"))
            if  login_user:
                logger.info("User is successfully logged in")
                return Response({'success': True, 'message': 'Login Success'})

            return Response({'success': False, 'message': 'Invalid credentials used!'},
                            status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            logger.exception(e)
            return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)