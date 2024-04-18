from django.db import models
from django import forms
from datetime import date

# Create your models here.
class Pengguna (models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    address_1 = models.TextField()
    address_2  = models.TextField(null=True, blank = True)
    city = models.CharField(max_length=20, help_text='Enter your city')
    state= models.TextField()
    zip_code= models.CharField(max_length = 7)
    tanggal_join = models.DateField(auto_now = True)

    def __str__(self):
        return f'{self.email}'


class Content(models.Model):
    pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


