# Generated by Django 3.2.13 on 2022-06-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_examplepreviewmodel_tag3'),
    ]

    operations = [
        migrations.AddField(
            model_name='examplepreviewmodel',
            name='picture_description',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
