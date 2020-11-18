from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from contacts.models import Contact
# Create your views here.


def dashboard(request):

    user_contact=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context={

        'contacts' :user_contact

    }


    return render(request,'account/dashboard.html',context)


class Demande_form(TemplateView):
    template_name = 'account/demande.html'
