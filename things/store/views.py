from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, views
from things.store.serializers import UserSerializer, GroupSerializer, ThingDataReader, \
    ThingDataWriter, \
    ThingDeviceSerializer
from things.store.models import ThingData, ThingDevice
from rest_framework.decorators import list_route
from rest_framework.views import Response
from rest_framework import status


class ThingDeviceViewSet(viewsets.ModelViewSet):
    queryset = ThingDevice.objects.all()
    serializer_class = ThingDeviceSerializer


class ThingDataWriteViewSet(viewsets.generics.CreateAPIView):
    queryset = ThingData.objects.all()
    serializer_class = ThingDataWriter

    def post(self, request, *args, **kwargs):
        data = request.data
        api_key = data.get('api_key')
        if api_key:
            device_id = ThingDevice.objects.all().filter(api_key=api_key)
            data.pop(api_key)
            data.update({"device_id": device_id})
            serializer = self.serializer_class(data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
            else:
                return Response(status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status.HTTP_401_UNAUTHORIZED)


class ThingDataReadViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ThingData.objects.all()
    serializer_class = ThingDataReader

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
