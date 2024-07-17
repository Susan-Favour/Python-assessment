# Generated by Django 5.0.6 on 2024-07-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('course_id', models.SmallIntegerField()),
                ('country', models.CharField(max_length=28)),
                ('gender', models.CharField(max_length=20)),
                ('bio', models.TextField()),
                ('national_id_number', models.CharField(max_length=30)),
                ('education_level', models.CharField(max_length=28)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
    ]
