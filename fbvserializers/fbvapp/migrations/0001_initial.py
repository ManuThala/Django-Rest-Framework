# Generated by Django 5.1.7 on 2025-04-17 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studentmodel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('score', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
    ]
