from django.shortcuts import render
from django.http import HttpResponse


def Index(self):
    return HttpResponse("Hii team, Welcome to FoxTramp")
