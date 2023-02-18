import io
from difflib import SequenceMatcher

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

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
    k = gen_key()
    return HttpResponse(
        f"<p>Registered {len(q)} objects."
        "You can download SQLite dump <a href=/dump>here</a>. </p>"
        '<p><a href="https://g.hs-ldz.pl/5F1vJ66Eic">Example form</a> || '
        f'<a href="https://g.hs-ldz.pl/{k}">Add new object</a></p>'
        '<p><form action="/search"><input name="query">'
        '<input type="submit" value="Search"></p></form>'
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


def dumpDbView(request):
    test_file = open('db.sqlite3', 'rb')
    response = HttpResponse(content=test_file)
    response['Content-Type'] = 'application/x-sqlite3'
    response['Content-Disposition'] = 'attachment; filename="db.sqlite"'
    return response


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


@csrf_exempt
def searchView(request):
    arg = request.GET.get("query").lower()
    if arg is None:
        return HttpResponse(
            """<form><input name="query"><input type="submit">"""
        )
    objects = list(Gnuj.objects.all())
    matcher = SequenceMatcher(a=arg)
    objects.sort(
        key=lambda obj: matcher.set_seq2(obj.tytul.lower()) or matcher.ratio(),
        reverse=True,
    )
    ret = "<ul>"
    for obj in objects[:30]:
        ret += '<li><a href="/' + obj.id + '">' + obj.tytul + "</a></li>"
    return HttpResponse(ret)
