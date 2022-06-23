# Generated by Django 3.2.13 on 2022-06-11 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRecipientInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('surname', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=150)),
                ('parent_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient_relation', to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
            ],
            options={
                'verbose_name': 'recipient info',
                'verbose_name_plural': 'Recipients info',
                'ordering': ['parent_sender'],
            },
        ),
        migrations.CreateModel(
            name='DeliveryParcelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('length', models.IntegerField()),
                ('status', models.CharField(choices=[('NEW', 'New parcel'), ('TBC', 'Took by courier'), ('SCW', 'S.C.Warehouse'), ('TRP', 'Transporting'), ('COS', 'Customer Service'), ('DEL', 'going to recipient'), ('COM', 'Completed'), ('RET', 'Returned')], default='NEW', max_length=3)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm_employees.customerrecipientinfomodel')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'deliver order',
                'verbose_name_plural': 'Deliver orders',
            },
        ),
        migrations.CreateModel(
            name='BoxOrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_ten', models.IntegerField(blank=True, default='0', help_text='Count of boxes', verbose_name='10')),
                ('size_twenty', models.IntegerField(blank=True, default='0', help_text='Count of boxes', verbose_name='15')),
                ('size_thirty', models.IntegerField(blank=True, default='0', help_text='Count of boxes', verbose_name='20')),
                ('ordering_date', models.DateTimeField(auto_now=True)),
                ('completed_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'box order',
                'verbose_name_plural': 'Boxes orders',
            },
        ),
    ]
