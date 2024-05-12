import os
import re

from django.db import models

import base58


GNUJDB_KEY_REGEX = r"^[0-9A-HJ-NP-Za-km-z]{10}$"
GNUJDB_KEY_REGEX_COMPILED = re.compile(GNUJDB_KEY_REGEX)


def gen_key():
    ret = ""
    while not GNUJDB_KEY_REGEX_COMPILED.match(ret):
        ret = base58.b58encode(os.getrandom(7)).decode()
    return ret


class Gnuj(models.Model):
    # FTS index actualisation after migrate command:
    # INSERT INTO gnujdb_gnuj_fts_idx(gnujdb_gnuj_fts_idx) VALUES('rebuild');
    POKOJE = ("Mainroom", "HARDRoom", "LAZIENKA", "Narnia", "Korytaz", "403")
    id = models.CharField(primary_key=True, default=gen_key, max_length=10)
    image = models.ImageField(upload_to="static/", blank=True)
    tytul = models.TextField(blank=True)
    wartosc = models.TextField(blank=True)
    wlasnosc = models.TextField(blank=True)
    miejsce = models.TextField(blank=True)
    pokoj = models.CharField(max_length=255, default="Mainroom", choices=list(map(lambda x: (x, x), POKOJE)))
    dodatkowe_info = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)
    fts_tags = models.TextField(blank=True)
    is_lost = models.BooleanField(default=False) 
