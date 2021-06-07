from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializer import QuotesSerializer, RecordsSerializer
from .models import Quotes, Records


class QuotesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (Quotes.objects.filter(level=pk)).exists():
            serializer_data = Quotes.objects.get(level=pk)
            serializer = QuotesSerializer(serializer_data)
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecordsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (Records.objects.filter(userProfile=pk)).exists():
            serializer_data = Records.objects.filter(userProfile=pk)
            serializer = RecordsSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        record = Records.objects.get(userProfile=pk)
        serializer = RecordsSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateRecordAPIView(APIView):

    def post(self, request):
        serializer = RecordsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
