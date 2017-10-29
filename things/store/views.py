from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from things.store.serializers import UserSerializer, GroupSerializer, ThingDataReader, \
    ThingDataWriter, \
    ThingDeviceSerializer
from things.store.models import ThingData, ThingDevice
from rest_framework.decorators import list_route, detail_route
from rest_framework.views import Response
from rest_framework import status, permissions
from rest_framework.exceptions import PermissionDenied
import json

class ThingDeviceViewSet(viewsets.ModelViewSet):
    queryset = ThingDevice.objects.all()
    serializer_class = ThingDeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    @detail_route(permission_classes=[permissions.IsAdminUser], methods=['get'])
    def api_key(self, request, pk=None):
        device = self.queryset.get(id=pk)
        return Response(device.api_key)

    @detail_route(methods=['get'])
    def plot_data(self, request, pk=None):
        field = request.GET.get("field")
        device_data = ThingData.objects.filter(device_id=pk)
        if not field : return Response("Please specify a field number", status.HTTP_400_BAD_REQUEST)
        datae= [{'x': data.created_at, 'y':data['value'+str(field)]}  for data in device_data]

        return Response(json.dumps(datae), status.HTTP_200_OK)


class ThingDataWriteViewSet(viewsets.ModelViewSet):
    queryset = ThingData.objects.all()
    serializer_class = ThingDataWriter
    http_method_names = ['post']
    authentication_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        data = self.request.data
        api_key = data.get('api_key')
        device = ThingDevice.objects.all().filter(api_key=api_key)

        if device:
            device_id = device[0].id
            serializer.save(device_id=device_id)
        else:
            raise PermissionDenied


class ThingDataReadViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ThingData.objects.all()
    serializer_class = ThingDataReader
    permission_classes = [permissions.IsAuthenticated]

    @list_route(methods=['get'])
    def device(self, request):
        device_id = request.GET.get("id")
        if device_id is not None:
            device_data = self.queryset.filter(device_id=device_id)
            return Response([self.serializer_class(d).data for d in device_data])
        else:
            return Response("No device found", status.HTTP_204_NO_CONTENT)
            #    else:
            #        return self.queryset




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
