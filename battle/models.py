from django.db import models


# Create your models here.
from django.urls import reverse


def daily_image_way(instance, filename):
    return 'media/battle/images/' + instance.day_number + '/'


class GeneralDayDescriptionModel(models.Model):
    day_number = models.CharField(max_length=4)
    date = models.DateField(auto_now_add=False)
    day_title = models.CharField(max_length=200)
    daily_image = models.ImageField(upload_to='media/battle/images/')

    def __str__(self):
        return f'День {self.day_number}'

    class Meta:
        verbose_name = 'day'
        verbose_name_plural = 'Days'


class DayEventModel(models.Model):
    day = models.ForeignKey(GeneralDayDescriptionModel, db_index=True, on_delete=models.PROTECT)
    event_time = models.TimeField(auto_now_add=False)
    description = models.TextField()
    event_preview = models.ImageField(upload_to='media/battle/images/event_preview/', default='default_image.png', blank=True)
    quote1 = models.TextField(blank=True)
    quote2 = models.TextField(blank=True)
    quote3 = models.TextField(blank=True)
    url = models.CharField(max_length=100, blank=True)

    def profilepic_or_default(self, default_path="default_image.png"):
        if self.event_preview:
            return self.event_preview
        return default_path

    def __str__(self):
        return f'{self.day} {self.event_time}'

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'Events'


class DayPhotoModel(models.Model):
    parent = models.ForeignKey(GeneralDayDescriptionModel, db_index=True, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    media = models.ImageField(upload_to='media/battle/photo/%Y/%m/%d')
    parent_event_time = models.ForeignKey(DayEventModel, db_index=True, on_delete=models.PROTECT, blank=True)
    category = models.ForeignKey('ItemCategoryModel', db_index=True, on_delete=models.PROTECT, related_name='photocategory')

    def get_absolute_url(self):
        return reverse('image', kwargs={'image': self.pk})

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'Photos'


class DayVideoModel(models.Model):
    parent = models.ForeignKey(GeneralDayDescriptionModel, db_index=True, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    media = models.FileField(upload_to='media/battle/video/%Y/%m/%d')
    parent_event_time = models.ForeignKey(DayEventModel, db_index=True, on_delete=models.PROTECT, blank=True)
    category = models.ForeignKey('ItemCategoryModel', db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'Videos'


class DayAudioModel(models.Model):
    parent = models.ForeignKey(GeneralDayDescriptionModel, db_index=True, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    media = models.FileField(upload_to='media/battle/audio/%Y/%m/%d')
    parent_event_time = models.ForeignKey(DayEventModel, db_index=True, on_delete=models.PROTECT, blank=True)
    category = models.ForeignKey('ItemCategoryModel', db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'audio'
        verbose_name_plural = 'Audios'


class DayArticleModel(models.Model):
    parent = models.ForeignKey(GeneralDayDescriptionModel, db_index=True, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    article = models.FileField(upload_to='media/battle/video/%Y/%m/%d')
    parent_event_time = models.ForeignKey(DayEventModel, db_index=True, on_delete=models.PROTECT, blank=True)
    category = models.ForeignKey('ItemCategoryModel', db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'Articles'


class ItemCategoryModel(models.Model):
    category = models.CharField(max_length=10)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categores'


class LostItemsListModel(models.Model):
    date = models.ForeignKey(GeneralDayDescriptionModel, db_index=True, on_delete=models.PROTECT, default='1')
    team = models.CharField(max_length=16)
    tanks = models.CharField(max_length=16)
    battle_armored_vehicle = models.CharField(max_length=16)
    artilery_system = models.CharField(max_length=16)
    rszo = models.CharField(max_length=16)
    antyair_missle = models.CharField(max_length=16)
    airplanes = models.CharField(max_length=16)
    helicopters = models.CharField(max_length=16)
    vehicles = models.CharField(max_length=16)
    ships_and_boats = models.CharField(max_length=16)
    bpla = models.CharField(max_length=16)
    special_vehicle = models.CharField(max_length=16)
    rockets = models.CharField(max_length=16)
    
    def __str__(self):
        return self.team
    
    class Meta:
        verbose_name = 'or change items info'
        verbose_name_plural = 'Lost items list'