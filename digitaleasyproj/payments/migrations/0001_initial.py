# Generated by Django 4.0.5 on 2022-07-06 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'db_table': 'services',
            },
        ),
        migrations.CreateModel(
            name='ServiceOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=26)),
                ('session_token', models.CharField(max_length=61)),
                ('ammount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date', models.DateField()),
                ('tx_token', models.CharField(max_length=70)),
                ('approved', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.client')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.service')),
            ],
            options={
                'db_table': 'service_orders',
            },
        ),
    ]
