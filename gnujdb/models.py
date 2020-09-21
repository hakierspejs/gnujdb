import os

from django.db import models

import base58


def gen_key():
    return base58.b58encode(os.getrandom(7)).decode()


class Gnuj(models.Model):
    id = models.CharField(primary_key=True, default=gen_key, max_length=10)
    tytul = models.TextField()
    wartosc = models.TextField()
    wlasnosc = models.TextField()
    dodatkowe_info = models.TextField(blank=True)
