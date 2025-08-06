from django.shortcuts import render, redirect
from .forms import ShiftsForm
from .models import Shifts
# Create your views here.

def clock(request):
    if request == 'POST':
        form = ShiftsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else: form = ShiftsForm()
    return render (request, 'clocks/shifts_clock.html', {'form' : form})


def shifts_list(request):
    shifts = Shifts.objects.all()
    return render (request, 'clocks/shifts_list.html', {'shifts' : shifts})
