__author__ = 'Diego'

# imports
from users.models import User, FriendRequest, Friendship
from schedules.serializers import GapSerializer
from localization.serializers import LocationSerializer
from rest_framework import serializers

# --- USER ---
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('imageURL','created_on', 'friends', 'requests_sent')


class UserImageSerializer(serializers.ModelSerializer):
    # imageURL = serializers.ImageField(required=True, source='file')
    class Meta:
        model = User
        fields = ('imageURL',)

class UserLocationSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = User
        fields = ('login', 'location')

class UserSyncSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('login', 'schedule_updated_on', 'updated_on')

class UserIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('login', )

class FriendRequestSerializer(serializers.ModelSerializer):

    fromUser = UserSerializer()
    toUser = UserSerializer()
    class Meta:
        model = FriendRequest
        fields = ('fromUser','toUser')

class FriendshipSerializer(serializers.ModelSerializer):
    secondUser = UserSerializer()
    class Meta:
        model = Friendship
        fields = ('firstUser','secondUser')

# Mixed serializers
class UserSerializerWithSchedule(serializers.ModelSerializer):
    gap_set = GapSerializer(many=True)
    class Meta:
        model = User
        depth = 1
        exclude = ('created_on', 'friends', 'requests_sent')