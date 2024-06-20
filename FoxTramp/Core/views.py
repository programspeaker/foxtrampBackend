from django.shortcuts import render
from django.http import HttpResponse


def Index(self):
    return HttpResponse(
        "Welcome to FOXTRAMP! New changes reflected, Auto integration"
    )
