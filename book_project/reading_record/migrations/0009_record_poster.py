# Generated by Django 4.1 on 2023-06-07 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reading_record', '0008_alter_record_impression_alter_record_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='poster',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
