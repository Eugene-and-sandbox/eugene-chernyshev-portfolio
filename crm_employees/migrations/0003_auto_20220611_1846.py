# Generated by Django 3.2.13 on 2022-06-11 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm_employees', '0002_auto_20220611_1845'),
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
        migrations.AlterField(
            model_name='deliveryparcelmodel',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm_employees.customerrecipientinfomodel'),
        ),
    ]