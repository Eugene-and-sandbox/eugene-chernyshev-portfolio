# Generated by Django 3.2.13 on 2022-06-18 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PortfolioExampleTagModel',
            new_name='PortfolioExampleCategoryModel',
        ),
        migrations.AlterModelOptions(
            name='portfolioexamplecategorymodel',
            options={'verbose_name': 'example category', 'verbose_name_plural': 'Example categories'},
        ),
    ]