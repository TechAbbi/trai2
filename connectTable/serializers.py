from rest_framework import serializers
from .models import ModelA, ModelB, ConnectingModel


class ModelASerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelA
        fields = "__all__"


class ModelBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelB
        fields = "__all__"


class ConnectingModelSerializer(serializers.ModelSerializer):
    model_a = ModelASerializer()
    model_b = ModelBSerializer()

    class Meta:
        model = ConnectingModel
        fields = "__all__"
