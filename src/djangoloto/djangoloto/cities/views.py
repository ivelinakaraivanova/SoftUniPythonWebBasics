from django.http import HttpResponse
from django.shortcuts import render, redirect

from djangoloto.cities.models import Person


def show_forms_demo(request):
    return render(request,'forms_demo.html')


def index(req):
    context = {
        'name': 'Peter',
        'people': Person.objects.all(),
    }

    return render(req, 'index.html', context)


def create_person(req):
    Person(
        name='Pesho',
        age=11,
        home_town='Sofia',
    ).save()

    return redirect('/cities')


def test_index(req):
    return HttpResponse('{"name": "John"}',
                        content_type='application/json')


def list_phones(request):
    context = {
        'phones': [
            {
                'name':'Galaxy S500',
                'quantity': 3,
            },
            {
                'name': 'iPhone 12',
                'quantity': 5,
            },
            {
                'name': 'Xiaomi Redmi T9',
                'quantity': 0,
            },
        ]
    }
    context['message'] = 'Phone list'
    return render(request, 'phones.html', context)
