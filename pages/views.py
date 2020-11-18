from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Propriete,Ville
from realtors.models import Profile,Demande

from listings.choices import bedroom_choices,price_choices,ville_choices,arrondissement_choices,price_choices_sell,type_immo,gender_choices

# Create your views here.
def index(request):
    listings=Propriete.objects.order_by('-list_date').filter(is_published=True)[:3]
    villes=Ville.objects.all()
    context={
        'listings':listings,
        'villes':villes,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'price_choices_sell':price_choices_sell,
        'ville_choices':ville_choices,
        'arrondissement_choices':arrondissement_choices,
        'gender_choices':gender_choices,
        'type_immo':type_immo,
    }
    return render(request,'pages/index.html',context) 

def about(request):

    realtors=Demande.objects.all()
    #mvp_realtors=Profile.objects.all().filter(is_mvp=True)

    context={
        'realtors':realtors,
        #'mvp_realtors': mvp_realtors
    }
    return render(request,'pages/about.html',context)

    
def view_404(request, exception):
    return render(request, '404.html')

def view_403(request, exception):
    return render(request, '403.html')

def view_500(request):
    return render(request, '500.html')