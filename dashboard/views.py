from django.shortcuts import render

from weather.models import FMIShortTerm


def index(request):
    return render(request, 'dashboard/base.html')


def weather(request):

    fmi_short_term = FMIShortTerm.objects.order_by('event_hour')[:22]

    context = {
        'page_title': 'Weather Forecast',
        'fmi_short_term': fmi_short_term
    }
    return render(request, 'dashboard/weather.html', context)
