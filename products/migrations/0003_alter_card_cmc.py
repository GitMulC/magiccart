# Generated by Django 4.0.6 on 2022-08-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_card_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cmc',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2),
        ),
    ]