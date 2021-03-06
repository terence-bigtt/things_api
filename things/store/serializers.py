from django.contrib.auth.models import User, Group
from rest_framework import serializers
from things.store.models import ThingData


class ThingDataSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ThingData
        fields = ('device_id', 'created_at', 'name1', 'value1', 'name2', 'value2', 'name3', 'value3', 'name4', 'value4',
                  'name5', 'value5', 'name6', 'value6', 'name7', 'value7', 'name8', 'value8')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
