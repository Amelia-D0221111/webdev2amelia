from django.db import models

# Create your models here.
class Pendaftaran(models.Model):
    nama = models.CharField()
    alamat = models.CharField()
    no_telepon = models.CharField(max_length=50)

    def __str__(self):
        return self.nama
