# Generated by Django 4.0.4 on 2022-05-15 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoJson',
            fields=[
                ('GeoJsonId', models.AutoField(primary_key=True, serialize=False)),
                ('GeoJsonName', models.CharField(max_length=50)),
                ('GeoJsonPrice', models.CharField(max_length=50)),
                ('GeoJsonData', models.JSONField()),
                ('GeoProviderName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('ProviderId', models.AutoField(primary_key=True, serialize=False)),
                ('ProviderName', models.CharField(max_length=50, unique=True)),
                ('ProviderEmail', models.EmailField(max_length=50)),
                ('ProviderPhoneNumber', models.CharField(max_length=50)),
                ('ProviderLanguage', models.CharField(max_length=50)),
                ('ProviderCurrency', models.CharField(max_length=50)),
            ],
        ),
    ]