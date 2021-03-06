# Generated by Django 3.2.13 on 2022-06-14 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_myuser_user_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='user_position',
            new_name='user_position_1',
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_position_2',
            field=models.CharField(choices=[('MEN', 'Manager'), ('CEO', 'Chief Executive Officer'), ('FOU', 'Founder')], default=1, max_length=3),
            preserve_default=False,
        ),
    ]
