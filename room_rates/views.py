from rest_framework import viewsets
from .models import RoomRate, OverriddenRoomRate, Discount, DiscountRoomRate
from .serializers import RoomRateSerializer, OverriddenRoomRateSerializer, DiscountSerializer, DiscountRoomRateSerializer

class RoomRateViewSet(viewsets.ModelViewSet):
    queryset = RoomRate.objects.all()
    serializer_class = RoomRateSerializer

class OverriddenRoomRateViewSet(viewsets.ModelViewSet):
    queryset = OverriddenRoomRate.objects.all()
    serializer_class = OverriddenRoomRateSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class DiscountRoomRateViewSet(viewsets.ModelViewSet):
    queryset = DiscountRoomRate.objects.all()
    serializer_class = DiscountRoomRateSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.dateparse import parse_date

@api_view(['GET'])
def get_lowest_rate(request, room_id, start_date, end_date):
    from django.db.models import Q

    start_date = parse_date(start_date)
    end_date = parse_date(end_date)

    rates = RoomRate.objects.filter(room_id=room_id)
    results = []

    for rate in rates:
        default_rate = rate.default_rate
        overridden_rates = OverriddenRoomRate.objects.filter(room_rate=rate, stay_date__range=[start_date, end_date])
        discounts = DiscountRoomRate.objects.filter(room_rate=rate).select_related('discount')

        for date in (start_date + timedelta(days=n) for n in range((end_date - start_date).days + 1)):
            rate_for_date = overridden_rates.filter(stay_date=date).first().overridden_rate if overridden_rates.filter(stay_date=date).exists() else default_rate
            max_discount_value = max([discount.discount_value for discount in discounts], default=0)

            if discounts.exists():
                if discounts.first().discount.discount_type == 'percentage':
                    discount_amount = (rate_for_date * max_discount_value) / 100
                else:
                    discount_amount = max_discount_value

                final_rate = rate_for_date - discount_amount
            else:
                final_rate = rate_for_date

            results.append({
                'date': date,
                'final_rate': final_rate
            })

    return Response(results)
