from django.shortcuts import render
from django.http import HttpResponse


def index(r):
    return HttpResponse('Hello world!')
