from django.urls import path
from accounts import views


app_name= 'accounts'
urlpatterns = [
  
    path('dashboard/', views.dashboard ,name='dashboard'),
    path('demandeform/', views.Demande_form.as_view() ,name='demande_form'),
    

]
