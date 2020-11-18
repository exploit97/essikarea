from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from realtors.forms import profileUpdateForm, userUpdateForm
from realtors.models import Profile as Pro
from realtors.models import  Demande as Dem
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import JsonResponse


# Create your views here.

def realtors(request):
    realtors=Pro.objects.all()
    paginator=Paginator(realtors,6)
    page=request.GET.get('page')
    paged_listing=paginator.get_page(page)
    context={
    'realtors' :  paged_listing
    
}
    return render(request,'realtors/realtors.html',context)

def realtor_detail(request,realtor_id):

    realtor =get_object_or_404(Pro,pk=realtor_id)

    context={
        'realtor':realtor
    }

    return render(request,'realtors/realtor_detail.html',context)

def realtor_search(request):

    query_list=Pro.objects.all()

    # KeyWords

    if 'keywords' in request.GET:
        keywords=request.GET['keywords']

        if keywords:
            query_list=query_list.filter(name__icontains=keywords)

    
    
    context={
        'realtor_search':query_list,
    }
    return render(request,'realtors/realtor_search.html',context)




@login_required
def Profile(request):
    
    if request.method == 'POST':
        u_form = userUpdateForm(request.POST,instance=request.user)
        p_form = profileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Votre compte a été mis à jour avec succès!')
            return redirect('listings:add_property')
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = profileUpdateForm(instance=request.user.profile)

    context= {
        'u_form':u_form,
        'p_form':p_form,
        
    }
    return render(request,'profile/profile.html',context)

def Demande(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('e-mail')
        phone = request.POST.get('phone')
        realtor = request.user.profile
        demande = Dem(profile=realtor, name=name, email=email, phone_number=phone)
        demande.save()
        realtor_id = realtor.id
        Pro.objects.filter(id=realtor_id).update(is_mvp=True)
        
        message = 'Votre demande de compte enseignant a été acceptée! Vous pouvez maintenant retourner sur Essikarea et télécharger des cours et des conférences, bon travail!'
        send_mail(
            'Essikarea, la demande a été acceptée.',
            message,
            'yvindjhonnelmahoukou@gmail.com',
            [email],
            fail_silently=False,
        )
        send_mail(
            'Essikarea',
            'Quelqu\'un a demandé un compte enseignant. Moi info: ' + name + ' , ' + email + ' , ' + phone + ' , ' + str(realtor) + '.',
            'yvindjhonnelmahoukou@gmail.com',
            ['yvindjhonnelmahoukou@gmail.com'],
            fail_silently=False,
        )
        messages.info(request, 'La demande a été envoyée avec succès, vous serez averti par email.')
        return redirect('listings:add_property')


def show_div(request):
    prop_hidden = request.Get.get('prop_hidden')
    
    data = {
        'prop_hidden':prop_hidden
    }
    return JsonResponse(data)
