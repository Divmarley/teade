# Generated by Django 4.0.6 on 2022-07-22 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=400)),
                ('tracking_id', models.CharField(max_length=30)),
                ('deposit_number', models.CharField(max_length=30)),
                ('reference_number', models.CharField(max_length=30)),
            ],
        ),
    ]
