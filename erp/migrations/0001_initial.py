# Generated by Django 2.1.1 on 2018-08-31 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publish', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.Author')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueId', models.CharField(max_length=50)),
                ('due_back', models.DateField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Available'), ('RENTED', 'Rented'), ('BOOKED', 'Booked'), ('MAINTENANCE', 'Maintenance')], max_length=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.Genre'),
        ),
    ]