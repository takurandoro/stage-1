from django.urls import path
from .views import *

urlpatterns = [
    path("residents/create/", ResidentCreateAPIView.as_view(), name ="add_resident"),
    path("residents/", ResidentListAPIView.as_view(), name ="view_residents"),
    path("residents/<int:resident_id>", ResidentDetailAPIView.as_view(), name ="view_resident"),
    path("residents/update/<int:resident_id>", ResidentUpdateAPIView.as_view(), name ="edit_resident"),
    path("residents/delete/<int:resident_id>", ResidentDeleteAPIView.as_view(), name ="delete_resident"),
    path("rooms/create/", RoomCreateAPIView.as_view(), name ="add_room"),
    path("rooms/", RoomListAPIView.as_view(), name ="view_rooms"),
    path("rooms/<int:room_id>", RoomDetailAPIView.as_view(), name ="view_room"),
    path("rooms/update/<int:room_id>", RoomUpdateAPIView.as_view(), name ="edit_room"),
    path("rooms/delete/<int:room_id>", RoomDeleteAPIView.as_view(), name ="delete_room"),
]
