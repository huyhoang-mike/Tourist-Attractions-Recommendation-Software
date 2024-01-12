# Generated by Django 4.2.7 on 2024-01-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_paris'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Venue name')),
                ('venue_image', models.ImageField(blank=True, null=True, upload_to='.')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]