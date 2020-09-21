from django.shortcuts import render
from django.http import HttpResponse

from .models import Gnuj
from .forms import GnujForm


def homePageView(request):
    gnuj = Gnuj()
    gnuj.contents = "elo"
    gnuj.save()
    gnujs = Gnuj.objects.all()
    form = GnujForm()
    return render(request, "index.html", {"gnujs": gnujs, "form": form})


def eloView(request):
    return HttpResponse(request.path)
