# Generated by Django 4.2 on 2023-07-03 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_alter_item_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bidding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('bidder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.item')),
            ],
        ),
    ]