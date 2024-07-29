from django.db import models

class RoomRate(models.Model):
    room_id = models.IntegerField()
    room_name = models.CharField(max_length=255)
    default_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.room_name} ({self.room_id})"

class OverriddenRoomRate(models.Model):
    room_rate = models.ForeignKey(RoomRate, related_name='overridden_rates', on_delete=models.CASCADE)
    overridden_rate = models.DecimalField(max_digits=10, decimal_places=2)
    stay_date = models.DateField()

class Discount(models.Model):
    DISCOUNT_TYPE_CHOICES = [
        ('fixed', 'Fixed'),
        ('percentage', 'Percentage'),
    ]
    discount_id = models.AutoField(primary_key=True)
    discount_name = models.CharField(max_length=255)
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPE_CHOICES)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.discount_name

class DiscountRoomRate(models.Model):
    room_rate = models.ForeignKey(RoomRate, related_name='discounts', on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, related_name='room_rates', on_delete=models.CASCADE)
