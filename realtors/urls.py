from django.urls import path
from . import views

app_name = 'realtors'
urlpatterns = [
    path('', views.realtors,name='realtors'),  # /realtors
    path('<int:realtor_id>/', views.realtor_detail,name='realtors_detail'),  # /realtors/realtor_id
    path('realtor_search/', views.realtor_search,name='realtor_search'),  # /realtor_search
    path('demande/', views.Demande, name='demande'),
    path('profile/', views.Profile, name='profile'),
    path('show_div/', views.show_div, name='show_div'),
    

  

]

    
