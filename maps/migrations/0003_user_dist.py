# Generated by Django 4.2.7 on 2024-01-09 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dist',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]