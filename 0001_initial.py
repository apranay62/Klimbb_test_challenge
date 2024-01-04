# Generated by Django 2.1.7 on 2024-01-04 10:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('incident_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
                ('severity', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('assigned_to', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
