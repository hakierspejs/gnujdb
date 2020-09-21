from django.http import HttpResponse

from .models import Gnuj


def homePageView(request):
    gnuj = Gnuj()
    gnuj.contents = "elo"
    gnuj.save()
    gnujs = Gnuj.objects.all()
    return HttpResponse(','.join([x.contents for x in gnujs]))
