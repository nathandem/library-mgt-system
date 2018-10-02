# Generated by Django 2.1.1 on 2018-09-12 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_address_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('book_books', 'Can book books'), ('change_books_status', 'Can change the status of books'), ('create_subscriber_accounts', 'Can create subscriber accounts'), ('create_librarian_accounts', 'Can create librarian accounts'))},
        ),
    ]