# Generated by Django 3.2.13 on 2022-06-13 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_employees', '0008_auto_20220613_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryparcelmodel',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
