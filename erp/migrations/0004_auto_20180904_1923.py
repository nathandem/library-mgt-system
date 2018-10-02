# Generated by Django 2.1.1 on 2018-09-04 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_auto_20180904_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinstance',
            old_name='unique_id',
            new_name='uid',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='erp.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='erp.Genre'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book_instances', to='erp.Book'),
        ),
    ]
