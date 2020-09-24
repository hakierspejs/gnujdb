import io

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from .models import Gnuj, gen_key
from .forms import GnujForm

import qrcode
import qrcode.image.svg


def gen_svg(box_size):
    bio = io.BytesIO()
    k = gen_key()
    url = "https://g.hs-ldz.pl/" + k
    qrcode.make(
        url,
        image_factory=qrcode.image.svg.SvgPathImage,
        border=0,
        box_size=box_size,
    ).save(bio)
    return k, bio.getvalue().decode()


def showStatisticsView(request):
    q = Gnuj.objects.all()
    return HttpResponse(
        f"Registered {len(q)} objects. TODO: display a list."
        "<p>You can create new stickers by printing "
        '<a href="/create">this page<a>. Play with URL to change size '
        "and number of stickers!</p>"
    )


def createQrCodesView(request):
    if "num_rows" not in request.GET:
        return redirect("/create?num_rows=4&num_columns=3&box_size=16")
    num_rows = int(request.GET.get("num_rows", 21))
    num_columns = int(request.GET.get("num_columns", 18))
    box_size = int(request.GET.get("box_size", 3))
    body = (
        "<style>* { font-family: monospace; padding: 0px; margin: 0px; "
        f"font-size: {box_size/2.0}mm"
        " }</style><table border=1>"
    )

    for x in range(num_rows):
        body += "<tr>"
        for y in range(num_columns):
            k, svg = gen_svg(box_size)
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
