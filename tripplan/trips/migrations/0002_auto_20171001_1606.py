# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 23:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ItemOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accept_reqd', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Item')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SunTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trailhead_latitude', models.CharField(max_length=31)),
                ('trailhead_longitude', models.CharField(max_length=31)),
                ('dusk', models.TimeField()),
                ('dawn', models.TimeField()),
                ('sunrise', models.TimeField()),
                ('sunset', models.TimeField()),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TripMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizer', models.BooleanField(default=False)),
                ('accept_reqd', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='destination',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='trip',
            name='number_nights',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trip',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trailhead_latitude',
            field=models.CharField(max_length=31),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trailhead_longitude',
            field=models.CharField(max_length=31),
        ),
        migrations.AddField(
            model_name='tripmember',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Trip'),
        ),
        migrations.AddField(
            model_name='tripmember',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='suntime',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Trip'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_owners',
            field=models.ManyToManyField(through='trips.ItemOwner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Trip'),
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_members',
            field=models.ManyToManyField(through='trips.TripMember', to=settings.AUTH_USER_MODEL),
        ),
    ]
