# Generated by Django 4.0.6 on 2022-08-21 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='defaullt_country',
            new_name='default_country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defaullt_county',
            new_name='default_county',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defaullt_phone_number',
            new_name='default_phone_number',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defaullt_postcode',
            new_name='default_postcode',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defaullt_street_address1',
            new_name='default_street_address1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defaullt_street_address2',
            new_name='default_street_address2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defaullt_town_or_city',
            new_name='default_town_or_city',
        ),
    ]
