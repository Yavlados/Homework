from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tovar(models.Model):
    class Meta():
        db_table = "Tovar"
        verbose_name_plural = "Товары"
        verbose_name = "Товар"
    id_tovar = models.AutoField(primary_key=True)
    name_tovar = models.CharField(max_length=50, verbose_name='Название товара')
    type_tovar = models.CharField(max_length=50, verbose_name='Тип товара')
    photo_tovar = models.ImageField(null=True, blank=True, verbose_name='Фото Товара')
    opisanie_tovar = models.CharField(max_length=2055, blank=True, verbose_name='Описание товара')
    user = models.ManyToManyField(User,  verbose_name='ID отзыва', through="Feedback", through_fields=('tovar','fb_users'))

    def get_user(self):
        return [{'id': user.id, 'name': user.username} for user in self.user.all()]


class Feedback(models.Model):
    class Meta():
        db_table= "Feedback"
        verbose_name_plural = "Отзывы"
        verbose_name = "Отзыв"
    fb_users = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    tovar=models.ForeignKey(Tovar, on_delete=models.CASCADE)
    information = models.CharField(max_length=2055, blank=True, verbose_name='Отзыв о товаре')
    photo = models.ImageField(null=True, blank=True, verbose_name='Фото')


    def __str__(self):
        return '%s %s' % (self.fb_users, self.information)

    def get_tovar_show(self):
        return [{'id_tovar': tovar.id_tovar, 'name_tovar': tovar.name_tovar, 'type_tovar': tovar.type_tovar, 'photo_tovar': tovar.photo_tovar, 'opisanie_tovar': tovar.opisanie_tovar} for tovar in self.id_tovar_fb.objects.all()]



class Shop(models.Model):
    class Meta():
        db_table = "Shop"
        verbose_name_plural = "Магазины"
        verbose_name = "Магазин"
    id_shop =  models.AutoField(primary_key=True)
    name_shop = models.CharField(max_length=20, verbose_name='Название магазина')
    adr_shop = models.CharField(max_length=100, verbose_name='Адрес магазина')
    assort_shop = models.ManyToManyField(Tovar, verbose_name='Ассортимент магазина')

    def get_tovar(self):
        return ", ".join([f.name_tovar for f in self.assort_shop.all()])

    def __str__(self):
        return self.name_shop

    def get_assort(self):
        return ", ".join([s.type_tovar for s in self.assort_shop.all()])
    get_assort.short_description = 'Ассортимент магазина'


