# Generated by Django 4.0.6 on 2022-08-13 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_card_flavor_text_alter_card_oracle_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='flavor_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='card',
            name='oracle_text',
            field=models.TextField(),
        ),
    ]