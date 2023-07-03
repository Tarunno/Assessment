# Generated by Django 4.2 on 2023-07-03 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('photo', models.ImageField(null=True, upload_to='item/')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('end_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('bid', models.IntegerField(default=0)),
                ('last_bidder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
