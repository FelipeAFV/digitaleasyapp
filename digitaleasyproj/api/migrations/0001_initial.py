# Generated by Django 4.0.5 on 2022-06-20 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('business_name', models.CharField(max_length=200)),
                ('business_creation_year', models.CharField(max_length=4)),
                ('business_category', models.CharField(max_length=100)),
                ('business_goals', models.CharField(max_length=200)),
                ('ig_account', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=12)),
                ('more_details', models.CharField(max_length=300)),
            ],
        ),
    ]
