from django.shortcuts import render,get_object_or_404,redirect
from .models import Propriete,Ville,Arrondissement,District
from realtors.models import Profile,Demande
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .choices import bedroom_choices,price_choices,ville_choices,arrondissement_choices,type_immo,gender_choices,price_choices_sell
from .forms import AddProperty
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,TemplateView
from django.http import JsonResponse
# Create your views here.

def index(request):
    listings=Propriete.objects.filter(is_published=True).order_by('-list_date')
    villes = Ville.objects.all()
    paginator=Paginator(listings,6)
    page=request.GET.get('page')
    
    try:
        paged_listing = paginator.page(page)
    except PageNotAnInteger:
        paged_listing = paginator.page(1)
    except EmptyPage:
        paged_listing = paginator.page(paginator.num_pages)
    context = {
        'listings' :  paged_listing,
        'paginate': True,
        'villes':villes,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'price_choices_sell':price_choices_sell,
        'ville_choices':ville_choices,
        'arrondissement_choices':arrondissement_choices,
        'gender_choices':gender_choices,
        'type_immo':type_immo,
    }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):

    listing=get_object_or_404(Propriete,pk=listing_id)
    dem=listing.realtor.demande_set.all()

    context={
        'listing':listing,
        'dem':dem
    }

    return render(request,'listings/listing.html',context)

def search(request):

    query_list=Propriete.objects.order_by('-list_date')
    villes=Ville.objects.all()

    # KeyWords

    if 'keywords' in request.GET:
        keywords=request.GET['keywords']

        if keywords:
            query_list=query_list.filter(description__icontains=keywords)


    if 'ville' in request.GET:
        ville=request.GET['ville']

        if ville:
            ville = Ville.objects.get(id=ville).name
            query_list=query_list.filter(ville__iexact=ville)
            
            
    
    if 'arrondissement' in request.GET:
       
        arrondissement=request.GET['arrondissement']

        if arrondissement:
            arrondissement = Arrondissement.objects.get(id=arrondissement).name
            query_list=query_list.filter(arrondissement__iexact=arrondissement)
    
    if 'district' in request.GET:
        district=request.GET['district']

        if district:
            district = District.objects.get(id=district).name
            query_list=query_list.filter(district__iexact=district)

    if 'bedrooms' in request.GET:
        bedroom=request.GET['bedrooms']

        if bedroom:
            query_list=query_list.filter(bedroom__lte=bedroom)
    
    if 'kitchen' in request.GET:
        kitchen=request.GET['kitchen']

        if kitchen:
            query_list=query_list.filter(kitchen__lte=kitchen)

    if 'rooms' in request.GET:
        room=request.GET['rooms']

        if room:
            query_list=query_list.filter(room__lte=room)
    
    if 'price' in request.GET:
        price=request.GET['price']

        if price:
            query_list=query_list.filter(price__lte=price)

    if 'sell_price' in request.GET:
        sell_price=request.GET['sell_price']

        if sell_price:
            query_list=query_list.filter(price__lte=sell_price)

    if 'type' in request.GET:
        type_l=request.GET['type']

        if type_l :
            query_list=query_list.filter(type_immo__iexact=type_l)
    
    if 'genre' in request.GET:
        genre=request.GET['genre']

        if genre :
            query_list=query_list.filter(gender__iexact=genre)

    if 'veranda' in request.GET:
        veranda=request.GET['veranda']

        if veranda :
            query_list=query_list.filter(veranda__iexact=veranda)
    
    context={
        'listings':query_list,
        'villes':villes,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'price_choices_sell':price_choices_sell,
        'ville_choices':ville_choices,
        'arrondissement_choices':arrondissement_choices,
        'gender_choices':gender_choices,
        'type_immo':type_immo,
        'values':request.GET
    }
    return render(request,'listings/search.html',context)


@login_required
def add_property(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        arrondissement = request.POST.get('arrondissement')
        district = request.POST.get('district')
        description = request.POST.get('description')
        price = request.POST.get('price')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        garage = request.POST.get('garage')
        rooms = request.POST.get('rooms')
        veranda = request.POST.get('veranda')
        genre = request.POST.get('genre')
        type_l= request.POST.get('type')
        sqft = request.POST.get('sqft')
        lot_size = request.POST.get('lot_size')
        photo_main = request.FILES.get('photo_main')
        photo_1 = request.FILES.get('photo_1')
        photo_2 = request.FILES.get('photo_2')
        photo_3 = request.FILES.get('photo_3')
        photo_4 = request.FILES.get('photo_4')
        photo_5 = request.FILES.get('photo_5')
        photo_6 = request.FILES.get('photo_6')
        
        
        realtor = request.user.profile
        demande=Demande.objects.filter(realtor=realtor)
        ville = Ville.objects.get(id = ville).name
        arrondissement = Arrondissement.objects.get(id = arrondissement).name
        district = District.objects.get(id = district).name
        type_l = type_immo[type_l]

        if genre =='MA':
            
            propriety = Propriete(title=title, address=address,room=rooms, veranda=veranda, ville =ville,arrondissement =arrondissement,realtor =realtor, district = district,description = description,price =price,bedroom =bedrooms,bathroom = bathrooms,garage = garage,sqft = sqft,gender = genre,type_immo = type_l, photo_main = photo_main,photo_1 =photo_1,photo_2 = photo_2,photo_3 = photo_3,photo_4 = photo_4,photo_5 = photo_5,photo_6 = photo_6)
            propriety.save()
            messages.success(request, 'good')
            return redirect('listings:listings')
    
        elif genre =='PA':
           propriety = Propriete(title=title, address=address, ville =ville,arrondissement =arrondissement,realtor =realtor, district = district,description = description,price =price,lot_size = lot_size, gender = genre,type_immo = type_l, photo_main = photo_main,photo_1 =photo_1,photo_2 = photo_2,photo_3 = photo_3,photo_4 = photo_4,photo_5 = photo_5,photo_6 = photo_6)
           propriety.save()
           messages.success(request, 'good')
           return redirect('listings:listings')
#else genre =='Studio':
        else:
            propriety = Propriete(title=title, address=address, ville =ville,arrondissement =arrondissement,realtor =realtor, district = district,description = description,price =price,gender = genre,type_immo = type_l, photo_main = photo_main,photo_1 =photo_1,photo_2 = photo_2,photo_3 = photo_3,photo_4 = photo_4,photo_5 = photo_5,photo_6 = photo_6)
            propriety.save()
            messages.success(request, 'good')
            return redirect('listings:listings')

        #elif genre =='Immeuble' or genre=='Appartement':
           # propriety = Lot(title=title, address=address,room=rooms,  ville =ville,arrondissement =arrondissement,realtor =realtor, district = district,description = description,price =price, gender = genre,type_immo = type_l, photo_main = photo_main,photo_1 =photo_1,photo_2 = photo_2,photo_3 = photo_3,photo_4 = photo_4,photo_5 = photo_5,photo_6 = photo_6)
            #propriety.save()
            #messages.success(request, 'good')
            #return redirect('listings:listings')

    else:
        villes =  Ville.objects.all()  
    context ={
        'villes':villes,
        'bedroom_choices':bedroom_choices,
        'ville_choices':ville_choices,
        'arrondissement_choices':arrondissement_choices,
        'gender_choices':gender_choices,
        'type_immo':type_immo,
    }

    return render(request, 'listings/add_property.html',context)

@login_required  
def delete_property(request,listing_id):
    Propriete(id= listing_id).delete()
    return redirect('listings:listings')


class Add_steps(TemplateView):
    template_name = 'listings/add_steps.html'


# AJAX
def load_arrondissements(request):
        title ='Arrondissement'
        ville_id = request.GET.get('ville')
        arrondissements = Arrondissement.objects.filter(ville_id=ville_id).order_by('name')
        return render(request, 'listings/arrondissement_dropdown_list_options.html', {'arrondissements': arrondissements,
        'title':title
        })

def load_districts(request):
        title ='District'
        arrondissement_id = request.GET.get('arrondissement')
        districts = District.objects.filter(arrondissement_id=arrondissement_id).order_by('name')
        return render(request, 'listings/arrondissement_dropdown_list_options.html', {'arrondissements': districts,
        'title':title 
        })
