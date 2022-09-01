from django.shortcuts import render
from django.http import HttpResponse
import random


def index(request):
    rnd = random.randint(1000, 9999)
    return HttpResponse(f"<h2> {rnd} </h2>")
