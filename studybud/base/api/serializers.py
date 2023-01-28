#serializers are classes that takes a certain (python) model or object and turn them into json objects etc so we can return them (like render)
from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'