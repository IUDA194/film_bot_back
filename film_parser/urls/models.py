from django.db import models

import uuid

class Url(models.Model):
    
    channel_name = models.CharField(max_length=100, unique=True, verbose_name="Имя канала")
    channel_url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ссылка на канал")
    channel_chat_id = models.CharField(max_length=255, verbose_name="Чат айди канала, взятый из @username_to_id_bot")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ссылка на канал"
        verbose_name_plural = "Ссылки на каналы"

    def __str__(self):
        return f"Канал {self.id}: {self.channel_name}"