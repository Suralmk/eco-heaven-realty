# Generated by Django 4.2.3 on 2023-07-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_location', models.CharField(max_length=20, verbose_name='City')),
                ('home_location', models.CharField(max_length=100, verbose_name='Home Location')),
                ('beds_rooms', models.IntegerField(verbose_name='Bed Rooms')),
                ('bath_rooms', models.IntegerField(verbose_name='Bed Rooms')),
                ('sqft', models.IntegerField(verbose_name='Square feet')),
                ('price', models.IntegerField(verbose_name='Home Price')),
                ('image', models.ImageField(upload_to='homes/')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]