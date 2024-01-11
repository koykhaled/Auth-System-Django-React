from django.shortcuts import render

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

# Create your views here.


class TestView(APIView):
    serializer_class = None
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response("khaled is here")