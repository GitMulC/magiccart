# Generated by Django 4.0.6 on 2022-08-24 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='card_img_url',
            field=models.URLField(blank=True, max_length=1024),
        ),
    ]
