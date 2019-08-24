
from rest_framework import serializers
from . import models


class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExampleModel
        fields = ('firstname', 'lastname')
