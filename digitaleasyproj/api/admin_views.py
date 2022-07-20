import traceback

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .permissions import AdminPermission
from rest_framework.response import Response
from rest_framework.request import Request
from uuid import uuid4
from payments.serializers import CustomServiceSerializer
from payments.models import CustomService
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

@api_view(['POST'])
@permission_classes([AllowAny])
def generateCustomService(request):

    serializer = CustomServiceSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        ## Deserilize object from post data

        ## If valid, save
        custom_service: CustomService = serializer.save()

        ## Add custom token to pass to client
        uuid = uuid4()
        custom_service.token = str(uuid)
        custom_service.save()
        return Response(status=200, data={
            'message': 'Creation of custom service successfully',
            'service_token': custom_service.token
        })
    except Exception:
        print(traceback.print_exc())
        return Response(status=400, data='Error in creating custom service')


