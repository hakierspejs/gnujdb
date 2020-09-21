from django.shortcuts import render

from .models import Gnuj
from .forms import GnujForm


def homePageView(request):
    gnuj = Gnuj()
    gnuj.contents = "elo"
    gnuj.save()
    gnujs = Gnuj.objects.all()
    form = GnujForm()
    return render(request, 'index.html', {'gnujs': gnujs, 'form': form})
