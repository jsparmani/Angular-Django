from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse


from . import models
from . import serializers

from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt


def get_data(request):
    data = models.ExampleModel.objects.all()
    if request.method == 'GET':
        serializer = serializers.ExampleModelSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
