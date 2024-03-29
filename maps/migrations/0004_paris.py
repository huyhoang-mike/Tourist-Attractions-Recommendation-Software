# Generated by Django 4.2.7 on 2024-01-09 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_user_dist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paris',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('location', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('subCategory', models.CharField(max_length=255)),
                ('popularity', models.IntegerField()),
                ('numReviews', models.IntegerField()),
            ],
        ),
    ]
