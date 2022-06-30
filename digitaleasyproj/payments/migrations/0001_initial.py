# Generated by Django 4.0.5 on 2022-06-30 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
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
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.service')),
            ],
            options={
                'db_table': 'service_orders',
            },
        ),
    ]
