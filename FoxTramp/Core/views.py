from django.shortcuts import render
from django.http import HttpResponse


def Index(self):
    return HttpResponse(
        "Hi team, Welcome to FOXTRAMP. We are grateful to see you here. Now we are under maintenance. We will get back here soon."
    )
