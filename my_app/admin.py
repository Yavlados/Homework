from django.contrib import admin
from .models import *


class TovarAdmin(admin.ModelAdmin):
    fields = ('name_tovar', 'type_tovar', 'photo_tovar', 'opisanie_tovar')
    list_display = [ "name_tovar", "type_tovar",  "photo_tovar", "opisanie_tovar"]  # Выводит 3 поля
    search_fields = ('id_tovar','name_tovar', 'type_tovar',)
    list_filter = ["id_tovar"]
    list_per_page = 10
    class Meta:
        model = Tovar


class ShopAdmin(admin.ModelAdmin):
    fields =('name_shop', 'adr_shop')
    list_display = ("name_shop", "adr_shop", "get_tovar" )  # Выводит 3 поля
    search_fields = ('name_shop', 'adr_shop')
    list_filter = ["id_shop"]
    list_per_page = 10
    class Meta:
        model = Shop


class FBAdmin(admin.ModelAdmin):
    list_per_page = 10


admin.site.register(Shop, ShopAdmin)
admin.site.register(Tovar, TovarAdmin)
admin.site.register(Feedback, FBAdmin)
