# STORE VIEWS.PY

from django.shortcuts import render


def home(request):
    return render(request, "home.html", {})
