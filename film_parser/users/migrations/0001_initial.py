# Generated by Django 5.1.1 on 2024-10-20 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100, unique=True)),
                ('ref_id', models.CharField(blank=True, max_length=100, null=True)),
                ('subscribed', models.BooleanField(default=False)),
                ('subscription_start_date', models.DateField(blank=True, default=None, null=True)),
                ('free_daily_limit', models.IntegerField(default=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_active', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
