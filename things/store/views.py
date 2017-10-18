from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from things.store.serializers import UserSerializer, GroupSerializer, ThingDataSerializers
from things.store.models import ThingData


class ThingDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ThingData.objects.all()
    serializer_class = ThingDataSerializers

class ThingDeviceDataView(APIView)
    pass


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