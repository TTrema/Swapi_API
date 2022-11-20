import json

import requests
from rest_framework.response import Response

from swapi.models import People, Planet


def Atualiza_Peoples(url):
    r = requests.get(url)
    info = r.json()

    for element in info["results"]:
        if People.objects.filter(name=element["name"]).exists():
            pass
        else:
            a = People(
                name=element["name"],
                height=element["height"],
                mass=element["mass"],
                hair_color=element["hair_color"],
                skin_color=element["skin_color"],
                eye_color=element["eye_color"],
                birth_year=element["birth_year"],
                gender=element["gender"],
                homeworld=element["homeworld"],
            )
            a.save()
    if info.get("next"):
        Atualiza_Peoples(info["next"])


def Atualiza_Planets(url):
    r = requests.get(url)
    info = r.json()
    for element in info["results"]:
        if Planet.objects.filter(name=element["name"]).exists():
            pass
        else:
            a = Planet(
                name=element["name"],
                rotation_period=element["rotation_period"],
                orbital_period=element["orbital_period"],
                diameter=element["diameter"],
                climate=element["climate"],
                gravity=element["gravity"],
                terrain=element["terrain"],
                surface_water=element["surface_water"],
                population=element["population"],
            )
            a.save()

    if info.get("next"):
        Atualiza_Planets(info["next"])
