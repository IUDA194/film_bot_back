from django.db import models

import uuid

class User(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    ref_id = models.CharField(max_length=100, blank=True, null=True)
    subscribed = models.BooleanField(default=False)
    subscription_start_date = models.DateField(null=True, blank=True, default=None)
    free_daily_limit = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.ref_id:
            self.ref_id = str(uuid.uuid4())
        super().save(*args, **kwargs)