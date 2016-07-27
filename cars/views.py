from django.core.mail import send_mail
from django.utils.timezone import datetime
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.conf import settings
from.models import Cars, UsedCars


def main(request):
    cars = Cars.objects.filter(launch_date__gt=datetime.now())
    return render(request, 'cars/main.html', {'gadi': cars})


def upcoming(request):
    c = Cars.objects.filter(launch_date__gt=datetime.now())
    return render(request, 'cars/upcoming.html', {'cars': c})


def details(request):
    if request.method == 'POST':
        x = request.POST['faaltu']
        return HttpResponse('%s' % x)

    # return render(request, 'cars/findcars.html', {'automob': gaadia})


def formfill(request, which_car):
    return render(request, 'cars/userrequest.html', {
        'name': which_car
    })


def mail(request, which_car):
    email = request.POST['send']
    name = request.POST['naaam']
    city = request.POST['city']
    subject = 'Alert Confirmation request'
    from_email = settings.EMAIL_HOST_USER
    to_email = [email]
    contact_message = "Dear %s we have received your request to get an alert for %s ,you will be alerted when launched in %s"%(
        name, which_car, city)

    send_mail(subject,
              contact_message,
              from_email,
              to_email,
              fail_silently=False)
    return render(request, 'cars/thankyou.html', {'message': 'email sent succesfully'})


def used(request, city):
    vehicle = UsedCars.objects.filter(place__startswith=city)
    return render(request, 'cars/used.html', {'vehicle': vehicle})
