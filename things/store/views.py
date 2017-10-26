from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, views
from things.store.serializers import UserSerializer, GroupSerializer, ThingDataSerializers
from things.store.models import ThingData
from rest_framework.decorators import list_route
from rest_framework.views import Response
from rest_framework import status


class ThingDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ThingData.objects.all()
    serializer_class = ThingDataSerializers

    @list_route(methods=['get'])
    def device(self, request):
        device_id = request.GET.get("id")
        if device_id is not None:
            device_data= self.queryset.filter(device_id=device_id)
            return Response([self.serializer_class(d).data for d in device_data])
        else : return Response("No device found", status.HTTP_204_NO_CONTENT)
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
