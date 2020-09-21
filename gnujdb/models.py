import os

from django.db import models

import base58


def gen_key():
    return base58.b58encode(os.getrandom(7)).decode()


class Gnuj(models.Model):
    id = models.CharField(primary_key=True, default=gen_key, max_length=10)
    contents = models.TextField()
