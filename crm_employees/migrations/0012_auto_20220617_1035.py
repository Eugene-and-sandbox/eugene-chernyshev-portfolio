# Generated by Django 3.2.13 on 2022-06-17 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_employees', '0011_boxordermodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxordermodel',
            name='status',
            field=models.CharField(choices=[('NEW', 'New order')], default='NEW', max_length=3),
        ),
        migrations.AlterField(
            model_name='boxordermodel',
            name='size_thirty',
            field=models.IntegerField(blank=True, default='0', help_text='Count of boxes', verbose_name='30'),
        ),
        migrations.AlterField(
            model_name='boxordermodel',
            name='size_twenty',
            field=models.IntegerField(blank=True, default='0', help_text='Count of boxes', verbose_name='20'),
        ),
    ]
