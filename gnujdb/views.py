from django.shortcuts import render

from .models import Gnuj


def homePageView(request):
    gnuj = Gnuj()
    gnuj.contents = "elo"
    gnuj.save()
    gnujs = Gnuj.objects.all()
    return render(request, 'index.html', {'gnujs': gnujs})
