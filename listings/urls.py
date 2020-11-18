from django.urls import path
from . import views

app_name= 'listings'
urlpatterns = [
    path('', views.index ,name='listings'),  # /listings
    path('<int:listing_id>', views.listing ,name='listing'),  # listings/120
    path('search/',views.search,name='search'),    #listings/search
    path('add_steps/',views.Add_steps.as_view(),name='add_steps'), 
    path('add_property/',views.add_property,name='add_property'),    #/add_property
    path('<int:listing_id>/delete_property/',views.delete_property,name='delete_property'),    #/delete_property
    path('ajax/load-arrondissements/',views.load_arrondissements, name='ajax_load_arrondissements'), # AJAX
    path('ajax/load-districts/',views.load_districts, name='ajax_load_districts'), # AJAX
    
]