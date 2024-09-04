from django.shortcuts import render
from .models import Home, Bodies, Teams

# Home View
def home(request):
    home = Home.objects.all()
    data = {'home': home}
    return render(request, "home.html", data)

# Bodies View
def bodies(request):
    body = Bodies.objects.all()
    data = {'body': body}
    return render(request, "bodies.html", data)

# Single Body View
def body(request, id):
    body = Bodies.objects.get(id=id)
    data = {'body': body}
    return render(request, "body.html", data)

# Team View
def team(request):
    team = Teams.objects.all()
    data = {'team': team}
    return render(request, "team.html", data)
