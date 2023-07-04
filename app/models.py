from django.db import models
from PIL import Image
from django.utils import timezone
from user.models import User


class Item(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=1000, null=True)
  photo = models.ImageField(upload_to='item/', null=True)
  created_at = models.DateTimeField(default=timezone.now, blank=True)
  end_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
  bid = models.IntegerField(default=0)
  last_bidder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='bidder')

  def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height > 800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.photo.path)

  def __str__(self):
    return self.name


class Bidding(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    bid = models.IntegerField(default=0)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return str(self.item) + ' | ' + str(self.bid)