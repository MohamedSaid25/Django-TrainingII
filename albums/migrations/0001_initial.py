# Generated by Django 4.1.2 on 2022-10-20 08:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='New Album', max_length=100)),
                ('creationTime', models.DateTimeField(default=datetime.datetime.now)),
                ('release', models.DateTimeField(default=datetime.datetime.now)),
                ('cost', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('isApproved', models.BooleanField(default=False, help_text='Approve the album if its name is not explicit')),
                ('artistName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.artist')),
            ],
        ),
    ]
