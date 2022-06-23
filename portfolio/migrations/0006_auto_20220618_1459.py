# Generated by Django 3.2.13 on 2022-06-18 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20220618_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='examplepreviewmodel',
            name='tag3',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, related_name='example_category_tag_three', to='portfolio.examplepreviewmodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='examplepreviewmodel',
            name='tag2',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='example_category_tag_two', to='portfolio.examplepreviewmodel'),
        ),
    ]
