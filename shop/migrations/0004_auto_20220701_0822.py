# Generated by Django 3.2.13 on 2022-07-01 05:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_productadditionalphoto_productmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=13)),
                ('value', models.IntegerField(help_text='In percent', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'verbose_name': 'discount',
                'verbose_name_plural': 'Discounts',
                'ordering': ['value'],
            },
        ),
        migrations.CreateModel(
            name='ProductCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'product category',
                'verbose_name_plural': 'Products category',
            },
        ),
        migrations.AlterField(
            model_name='menutagmodel',
            name='link',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('need_delivery', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('notes', models.TextField(blank=True)),
                ('date_order', models.DateTimeField(auto_now_add=True)),
                ('date_send', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('NEW', 'New order'), ('APR', 'Aprowed'), ('PAY', 'Payed'), ('CNL', 'Canceled')], default='NEW', max_length=3)),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.discountmodel')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderLineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('count', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.ordermodel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.productmodel')),
            ],
            options={
                'verbose_name': 'order line',
                'verbose_name_plural': 'Orders lines',
            },
        ),
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='shop.productcategorymodel'),
            preserve_default=False,
        ),
    ]
