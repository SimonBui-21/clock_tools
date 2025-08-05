from django.shortcuts import render
from models import Shifts
# Create your views here.

def shifts(request):
    return render (request, 'shifts_clock.html')