from django.forms import ModelForm
from .models import Gnuj


class GnujForm(ModelForm):
    class Meta:
        model = Gnuj
        exclude = ['id']
