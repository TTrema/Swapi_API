from rest_framework import serializers
from swapi.models import Planet, People


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = "__all__"


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = "__all__"
