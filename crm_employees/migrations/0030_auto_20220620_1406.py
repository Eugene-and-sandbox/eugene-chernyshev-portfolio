# Generated by Django 3.2.13 on 2022-06-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_employees', '0029_auto_20220620_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryparcelmodel',
            name='invoice',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/invoices'),
        ),
        migrations.AlterField(
            model_name='deliveryparcelmodel',
            name='receipt',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/receipts'),
        ),
    ]