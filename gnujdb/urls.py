"""gnujdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    createQrCodesView,
    displayFormView,
    showStatisticsView,
    dumpDbView,
    searchView,
    swiezyGnuj,
)


from gnujdb.models import GNUJDB_KEY_REGEX


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", showStatisticsView, name="statistics"),
    path("create", createQrCodesView, name="create_qr_codes"),
    path("dump", dumpDbView, name="dump_database"),
    path("search", searchView, name="searchView"),
    path("swiezygnuj", swiezyGnuj, name="swiezyGnuj"),
    re_path(GNUJDB_KEY_REGEX, displayFormView, name="form"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
