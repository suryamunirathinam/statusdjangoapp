from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from status.models import Status
from .serializers import StatusSerializers
from rest_framework import generics
# Create your views here.
class StatusListSearchAPIView(APIView):
    permission_classes              = []
    authentication_classes          = []

    def get(self,request,format=None):
        qs =Status.objects.all()
        serializer = StatusSerializers(qs,many=True)
        return Response(serializer.data)

# class StatusAPIView(generics.ListAPIView):
#     permission_classes              = []
#     authentication_classes          = []

#     queryset = Status.objects.all()

class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes              = []
    authentication_classes          = []

    queryset = Status.objects.all()
    serializer_class =StatusSerializers

class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes              = []
    authentication_classes          = []

    queryset = Status.objects.all()
    serializer_class =StatusSerializers
    # lookup_field = 'id' if not specified change to pk

class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes              = []
    authentication_classes          = []

    queryset = Status.objects.all()
    serializer_class =StatusSerializers
    


class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes              = []
    authentication_classes          = []

    queryset = Status.objects.all()
    serializer_class =StatusSerializers
    



