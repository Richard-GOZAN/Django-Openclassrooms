from django.http import HttpResponse
# from django.shortcuts import render
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(
        f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
    """
    )


def about(request):
    return HttpResponse("<h1>À propos</h1> <p> Nous adorons merch !</p>")


def listings(request):
    return HttpResponse(
        """
        <h1>Listings</h1>
        <p>Voici la liste des annonces.</p>
        """
    )


def contact(request):
    return HttpResponse(
        "<h1>Contact Us</h1> <p>Contactez-nous pour plus d'informations</p>"
    )
