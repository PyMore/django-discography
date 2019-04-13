from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect

from rest_framework import status

# Create your views here.

def not_found(request):
    """Not found view"""
    response = JsonResponse(data={
        'detail': 'not found.'
    })
    response.status_code = status.HTTP_404_NOT_FOUND
    return response
