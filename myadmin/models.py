from django.db import models
from django.utils import timezone


class Thread(models.Model):
    auction_added = models.IntegerField(default=0)
    auction_completed = models.IntegerField(default=0)
    auction_value = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return str(self.created_at) + ' | ' + str(self.auction_added) + ' | ' + str(self.auction_completed) + ' | ' + str(self.auction_value)