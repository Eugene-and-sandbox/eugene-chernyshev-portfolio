from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class MenuTagModel(models.Model):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'menu tag'
        verbose_name_plural = 'Menu tags'


class DiscountModel(models.Model):
    code = models.CharField(max_length=13)
    value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], help_text='In percent')

    def __str__(self):
        return '{0} ({1}%)'.format(self.code, self.value)

    class Meta:
        ordering = ['value']
        verbose_name = 'discount'
        verbose_name_plural = 'Discounts'


class ProductCategoryModel(models.Model):
    category = models.CharField(max_length=15)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'product category'
        verbose_name_plural = 'Products category'


class ProductModel(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=False)
    description = models.TextField()
    category = models.ForeignKey(ProductCategoryModel, db_index=True, on_delete=models.PROTECT)
    main_photo = models.ImageField(upload_to='media/shop/products/')

    def __str__(self):
        return '{0}: {1}, {2}'.format(self.name, self.price, self.in_stock)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'Products'


class ProductAdditionalPhoto(models.Model):
    parent = models.ForeignKey(ProductModel, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='media/shop/products/')

    def __str__(self):
        return f'Product: {self.parent.name}'

    class Meta:
        verbose_name = 'product additional photo'
        verbose_name_plural = 'Products additional photo'


class OrderModel(models.Model):
    need_delivery = models.BooleanField(default=False)
    address = models.CharField(max_length=150)
    discount = models.ForeignKey(DiscountModel, db_index=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    notes = models.TextField(blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    date_send = models.DateTimeField(auto_now=False, null=True, blank=True)

    STATUSES = [
        ('NEW', 'New order'),
        ('APR', 'Aprowed'),
        ('PAY', 'Payed'),
        ('CNL', 'Canceled'),
    ]
    status = models.CharField(choices=STATUSES, max_length=3, default='NEW')

    def __str__(self):
        return f'self.date_order | self.status | self.name: self.address, self.phone, self.email'

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'Orders'


class OrderLineModel(models.Model):
    order = models.ForeignKey(OrderModel, db_index=True, on_delete=models.PROTECT)
    product = models.ForeignKey(ProductModel, db_index=True, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    count = models.IntegerField(validators=[MinValueValidator(1)], default=1)

    def __str__(self):
        return 'Order (ID {0}) {1}: {2}'.format(self.order.id, self.product.title, self.count)

    class Meta:
        verbose_name = 'order line'
        verbose_name_plural = 'Orders lines'
