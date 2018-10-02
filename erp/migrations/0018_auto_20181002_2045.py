# Generated by Django 2.1.1 on 2018-10-02 20:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0017_auto_20181001_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_made_on', models.DateField(auto_now_add=True)),
                ('book_booked_on', models.DateField(blank=True, null=True)),
                ('book_withdrawn_during_booking_period', models.BooleanField(blank=True, null=True)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='erp.Book')),
                ('generic_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='erp.GenericBook')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='rental',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rentals', to='erp.Book'),
        ),
        # this migration looks a bit stupid, no point to hardcode the date every day of every migration
        migrations.AlterField(
            model_name='rental',
            name='due_for',
            field=models.DateField(default=datetime.date(2018, 10, 16)),
        ),
        migrations.AlterField(
            model_name='rental',
            name='late',
            field=models.BooleanField(default=False),
        ),
    ]
