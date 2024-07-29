from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomRateViewSet, OverriddenRoomRateViewSet, DiscountViewSet, DiscountRoomRateViewSet, get_lowest_rate

router = DefaultRouter()
router.register(r'roomrates', RoomRateViewSet)
router.register(r'overriddenrates', OverriddenRoomRateViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'discountroomrates', DiscountRoomRateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('lowest_rate/<int:room_id>/<str:start_date>/<str:end_date>/', get_lowest_rate, name='lowest_rate'),

]
