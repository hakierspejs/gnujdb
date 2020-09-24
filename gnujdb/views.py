import io

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .models import Gnuj, gen_key
from .forms import GnujForm

import qrcode
import qrcode.image.svg


def gen_svg():
    bio = io.BytesIO()
    k = gen_key()
    url = "https://g.hs-ldz.pl/" + k
    qrcode.make(
        url, image_factory=qrcode.image.svg.SvgPathImage, border=0, box_size=3
    ).save(bio)
    return k, bio.getvalue().decode()


def createQrCodesView(request):
    body = (
        "<style>* { padding: 0px; margin: 0px; font-size: 1.5mm}"
        "</style><table border=1>"
    )
    for x in range(21):
        body += "<tr>"
        for y in range(18):
            k, svg = gen_svg()
            body += "<td>" + svg + "<p>" + k + "</td>"
        body += "</tr>"
    return HttpResponse(body)


def displayFormView(request):
    k = request.path.split("/")[-1]
    try:
        gnuj = Gnuj.objects.get(pk=k)
    except Gnuj.DoesNotExist:
        gnuj = Gnuj()
        gnuj.id = k
    if request.method == "POST":
        form = GnujForm(request.POST, request.FILES, instance=gnuj)
        if form.is_valid():
            form.save()
    else:
        form = GnujForm(instance=gnuj)
    return render(
        request,
        "index.html",
        {"form": form, "gnuj": gnuj, "MEDIA_URL": settings.MEDIA_URL},
    )
