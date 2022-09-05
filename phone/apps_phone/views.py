from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .forms import CreateForm, UpdateForm
from .models import Contact


def main_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'base.html')


def creator(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("contact_name")
            phone = form.cleaned_data.get("phone_value")
            if not (Contact.objects.filter(contact_name=name) or Contact.objects.filter(phone_value=phone)):
                Contact.objects.create(contact_name=name, phone_value=phone)
                return render(request, 'creator_final.html')
            else:
                return render(request, 'creator_error.html')
    else:
        form = CreateForm()
    return render(request, 'creator.html', {'form': form})


def reader(request: HttpRequest) -> HttpResponse:
    result = Contact.objects.all()
    return render(request, 'reader.html', {'data': result})


def updatertemp(request: HttpRequest) -> HttpResponse:
    result = Contact.objects.all()
    return render(request, 'updater.html', {'data': result})


def updater(request: HttpRequest, name: str) -> HttpResponse:
    if request.method == "POST":
        update_form = UpdateForm(request.POST)
        if update_form.is_valid():
            new_name = update_form.cleaned_data.get("contact_name")
            new_phone = update_form.cleaned_data.get("phone_value")

            Contact.objects.filter(contact_name=name).update(contact_name=new_name, phone_value=new_phone)
            return render(request, 'updater_success.html')

    else:
        phone = Contact.objects.filter(contact_name=name).values()[0].get('phone_value')
        update_form = UpdateForm(initial={'contact_name': name, 'phone_value': phone})
    return render(request, 'updater_final.html', {'form': update_form})


def deletertemp(request: HttpRequest) -> HttpResponse:
    result = Contact.objects.all()
    return render(request, 'deleter.html', {'data': result})


def deleter(request: HttpRequest, name: str) -> HttpResponse:
    return render(request, 'deleter_submit.html', {'name': name})


def deleter_final(request: HttpRequest, name: str) -> HttpResponse:
    Contact.objects.filter(contact_name=name).delete()
    return render(request, 'deleter_success.html')
