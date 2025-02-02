from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('discount_id', models.AutoField(primary_key=True, serialize=False)),
                ('discount_name', models.CharField(max_length=255)),
                ('discount_type', models.CharField(choices=[('fixed', 'Fixed'), ('percentage', 'Percentage')], max_length=10)),
                ('discount_value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='RoomRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('room_name', models.CharField(max_length=255)),
                ('default_rate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OverriddenRoomRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overridden_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stay_date', models.DateField()),
                ('room_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='overridden_rates', to='room_rates.roomrate')),
            ],
        ),
        migrations.CreateModel(
            name='DiscountRoomRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_rates', to='room_rates.discount')),
                ('room_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='room_rates.roomrate')),
            ],
        ),
    ]
