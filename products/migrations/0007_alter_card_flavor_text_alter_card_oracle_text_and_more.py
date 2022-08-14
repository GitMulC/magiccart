# Generated by Django 4.0.6 on 2022-08-12 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_card_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='flavor_text',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='oracle_text',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='rarity',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='card',
            name='set',
            field=models.CharField(max_length=10),
        ),
    ]