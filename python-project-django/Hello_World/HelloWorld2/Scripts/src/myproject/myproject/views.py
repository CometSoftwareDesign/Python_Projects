#from django.http import HttpResponse

from django.shortcuts import render


def home(request):
    profiles = ["John Wayne", "Clint Eastwood", "Zazie Beets", 'Mary Winchester', 'Elizabeth Austin', "Fanny Mae"]
    context ={
        'profiles': profiles,
    }
    return render(request, "home.html", context)