from audioop import maxpp
from distutils.command.upload import upload
from statistics import mode
from tabnanny import verbose
from django.db import models


# Create your models here.
class ExamplePreviewModel(models.Model):
    description = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='media/portfolio/examples/pictures')
    picture_description = models.CharField(max_length=30)
    example_url = models.CharField(max_length=50)
    tag1 = models.ForeignKey('ExampleCategoryModel', db_index=True, on_delete=models.PROTECT, related_name='example_category_tag_one')
    tag2 = models.ForeignKey('ExampleCategoryModel', db_index=True, on_delete=models.PROTECT, related_name='example_category_tag_two', blank=True, null=True)
    tag3 = models.ForeignKey('ExampleCategoryModel', db_index=True, on_delete=models.SET_NULL, related_name='example_category_tag_three', blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'example preview'
        verbose_name_plural = 'Examples previews'


class ExampleCategoryModel(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'example category'
        verbose_name_plural = 'Example categories'