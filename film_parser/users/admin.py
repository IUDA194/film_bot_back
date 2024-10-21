from django.contrib import admin
from django.contrib.auth.models import Group, User

# Удаляем модель Group из админки
admin.site.unregister(Group)
admin.site.unregister(User)
