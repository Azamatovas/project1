# Generated by Django 5.1.3 on 2024-12-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_tour_average_rating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='average_rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
