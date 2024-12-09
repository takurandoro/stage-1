from rest_framework import generics
from .models import Room, Resident
from .serializers import ResidentSerializer, RoomSerializer

# Create your views here.


class ResidentCreateAPIView(generics.CreateAPIView):
    model = Resident
    serializer_class = ResidentSerializer


class ResidentListAPIView(generics.ListAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer


class ResidentDetailAPIView(generics.RetrieveAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    lookup_url_kwarg = "resident_id"


class ResidentUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    lookup_url_kwarg = "resident_id"


class ResidentDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    lookup_url_kwarg = "resident_id"


class RoomCreateAPIView(generics.CreateAPIView):
    model = Room
    serializer_class = RoomSerializer


class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_url_kwarg = "room_id"


class RoomUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_url_kwarg = "room_id"


class RoomDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_url_kwarg = "room_id"
