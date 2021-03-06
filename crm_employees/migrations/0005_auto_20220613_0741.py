# Generated by Django 3.2.13 on 2022-06-13 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm_employees', '0004_auto_20220613_0738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerrecipientinfomodel',
            options={'ordering': ['parent_sender'], 'verbose_name': 'recipient info', 'verbose_name_plural': 'Recipients info'},
        ),
        migrations.AddField(
            model_name='customerrecipientinfomodel',
            name='parent_sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recipient_relation', to='accounts.myuser', verbose_name='Sender'),
            preserve_default=False,
        ),
    ]
