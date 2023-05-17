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
            form.save()
            return redirect(main)
        else:
            error = 'form was filled wrong'

    form = ExcursionForm()
    return render(request, 'excursion.html', {'form': form,
                                              'error': error})


def news(request):
    return render(request, 'news.html')


def excursionReg(request):
    date = request.GET.get("date")
    time = request.GET.get("time")
    phone = request.GET.get("phone")
    peopleAmount = request.GET.get("peopleAmount")

    excursion = Excursion(date, time, phone, peopleAmount)
    Excursion.addExcursion(excursion)
    print(Excursion.excursionsToString())
    return render(request, 'main.html')


def getAllExcursions(request):
    data = Excursions.objects.all()
    return render(request, "allExcursions.html", {"data": data})


def getExcursion(request, id):
    global excursion
    for item in Excursions.objects.all():
        if item.id == id:
            excursion = item
    return render(request, 'excursionDetail.html', {'excursion': excursion})
