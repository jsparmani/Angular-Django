from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse


from . import models
from . import serializers
import time
import datetime


from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt


def get_data(request):
    data = models.ExampleModel.objects.all()
    if request.method == 'GET' or request.method == 'POST:
        serializer = serializers.ExampleModelSerializer(data, many=True)
	temp = [x%7 for x in range(1:100)]
        return JsonResponse(serializer.data, safe=False)
