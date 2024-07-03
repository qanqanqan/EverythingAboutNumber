from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Number, NumberInfo
from .forms import NumberInputForm

from .addons import generate_number_info


def index(r):
    form = NumberInputForm()
    nums = Number.objects.all()
    return render(r, 'mynumbers/index.html', {'form': form, 'nums': [i.number for i in nums]})


def handle_number(r):
    if r.method == 'POST':
        form = NumberInputForm(r.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            found_number = Number.objects.filter(number=number)
            if not found_number:
                number_obj = Number.objects.create(number=number)
                number_info = generate_number_info(number) | {'number': number_obj}
                NumberInfo.objects.create(**number_info)
            return redirect('show-number-info', number=number)
    else:
        form = NumberInputForm()
    return render(r, 'mynumbers/index.html', {'form': form})


def show_number_info(r, number):
    number_obj = get_object_or_404(Number, number=number)
    number_info = NumberInfo.objects.get(number=number_obj)

    return render(r, 'mynumbers/show_number_info.html', {'numinf': number_info})
