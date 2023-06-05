from django.shortcuts import render, redirect

from zoo.forms import ExcursionForm
from zoo.models import Excursions
from zoo.models1.excursion import Excursion


def main(request):
    return render(request, 'main.html')


def prices(request):
    return render(request, 'prices.html')


def rules(request):
    return render(request, 'rules.html')


def history(request):
    return render(request, 'history.html')


def excursion(request):
    error = ''
    if request.method == 'GET':
        form = ExcursionForm(request.GET)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            peopleAmount = form.cleaned_data['peopleAmount']
            guide = form.cleaned_data['guide']
            Excursions.objects.create(date=date, time=time, name=name, phone=phone, peopleAmount=peopleAmount,
                                      guide=guide, isFinished=False)
            return redirect(main)
        else:
            error = 'form was filled wrong'

    form = ExcursionForm()
    return render(request, 'excursion.html', {'form': form,
                                              'error': error})


def news(request):
    return render(request, 'news.html')


def getAllExcursions(request):
    data = Excursions.objects.all()
    return render(request, "allExcursions.html", {"data": data})


def getExcursion(request, id):
    global excursion
    for item in Excursions.objects.all():
        if item.id == id:
            excursion = item
    return render(request, 'excursionDetail.html', {'excursion': excursion})
