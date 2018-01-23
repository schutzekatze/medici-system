from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class MediciUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    last_updated = models.DateTimeField(default=timezone.now)

    @receiver(post_save, sender=User)
    def create_user(sender, instance, created, **kwargs):
        if created:
            MediciUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user(sender, instance, **kwargs):
        instance.mediciuser.save()

    def __str__(self):
        return self.user.username

class Shop(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.address

class Item(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

'''
    Each shop has its own items, but items from different shops
    may have different names, but they, in reality, refer to the same thing,
    so all shop items are tied to the item that they actually are.
'''
class ShopItem(models.Model):
    name = models.CharField(max_length=256)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    last_updated = models.DateTimeField()

    def __str__(self):
        return self.name

class Receipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

class ReceiptItem(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    shop_item = models.ForeignKey(ShopItem, on_delete=models.CASCADE)
    price_at_the_time = models.DecimalField(max_digits=20, decimal_places=10)
