from django.contrib import admin
from urls.models import Url

from unfold.admin import ModelAdmin

admin.site.site_title = "Сайт по администрированию бота"
admin.site.index_title = "Управление ботом"

@admin.register(Url)
class CustomAdminClass(ModelAdmin):
    pass