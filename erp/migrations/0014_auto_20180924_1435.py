# Generated by Django 2.1.1 on 2018-09-24 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0013_auto_20180918_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rent_books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Available'), ('RENT', 'Rent'), ('BOOKED', 'Booked'), ('MAINTENANCE', 'Maintenance')], default='MAINTENANCE', max_length=20),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='has_rent_issue',
            field=models.BooleanField(default=False),
        ),
    ]