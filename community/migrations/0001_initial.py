# Generated by Django 4.0.6 on 2022-08-26 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('description', models.TextField()),
                ('url', models.URLField(max_length=1024)),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
    ]
