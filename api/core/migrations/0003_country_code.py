# Generated by Django 5.2 on 2025-05-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_city_options_alter_country_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='code',
            field=models.CharField(default='UK', max_length=2, unique=True),
            preserve_default=False,
        ),
    ]
