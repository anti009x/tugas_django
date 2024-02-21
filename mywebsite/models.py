from django.db import models

# Create your models here.

class TokoKomputer (models.Model):
    
    namaproduk = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10,decimal_places=2)
    stok = models.IntegerField()
    deskripsi = models.TextField()
    
    def __str__(self):
        return self.namaproduk

        