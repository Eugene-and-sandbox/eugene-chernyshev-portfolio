# Generated by Django 3.2.13 on 2022-06-14 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20220614_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='picture',
            field=models.ImageField(blank=True, upload_to='images/users/'),
        ),
    ]