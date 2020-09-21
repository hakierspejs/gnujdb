import os

from django.db import models

import base58


def gen_key():
    return base58.b58encode(os.getrandom(7)).decode()


class Gnuj(models.Model):
    id = models.CharField(primary_key=True, default=gen_key, max_length=10)
    image = models.ImageField(upload_to='static/', blank=True)
    tytul = models.TextField(blank=True)
    wartosc = models.TextField(blank=True)
    wlasnosc = models.TextField(blank=True)
    dodatkowe_info = models.TextField(blank=True)
