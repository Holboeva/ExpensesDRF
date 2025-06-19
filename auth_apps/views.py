from http import HTTPStatus

from django.http import JsonResponse
from django.shortcuts import render
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view

from serializers import UserModelSerializer


@extend_schema(request=UserModelSerializer, responses=UserModelSerializer)
@extend_schema(tags=['auth'])
@api_view(['POST'])
def Register_api_view(request):
    data = request.data
    serializer = UserModelSerializer(data=data)
    if serializer.is_valid():
        obj = serializer.save()
        return JsonResponse(UserModelSerializer(instance=obj).data)
    return JsonResponse(serializer.errors, status=  HTTPStatus.BAD_REQUEST)

@extend_schema(tags=['user'])
@api_view(['POST'])
@api_view(['POST'])
def Login_api_view(request):
    return JsonResponse({'message': 'Login'})