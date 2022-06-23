# Generated by Django 3.2.13 on 2022-06-20 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_employees', '0027_customerdiscountmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryparcelmodel',
            name='discount',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='crm_employees.customerdiscountmodel'),
        ),
    ]