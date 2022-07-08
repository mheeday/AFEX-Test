from django.db import models
from .update_ws import update_websocket
 


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 

class Client(BaseModel):
    cid = models.CharField(max_length=60, unique=True, db_index=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(
        max_length=300, null=True, blank=True, default="")
    country_code = models.CharField(
        max_length=30, blank=True, null=True, default="")
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=50, null=True, blank=True, default="")

    class Meta:
        ordering = ['cid']

    def __str__(self):
        return self.cid

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class ClientWallet(BaseModel):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='clientwallet')
    total_balance = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    available_balance = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    lien_balance = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.client.cid} - {self.available_balance}"

    @property
    def cid(self):
        return self.client.cid


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        update_websocket(self.total_balance)