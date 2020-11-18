
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  handler404, handler403, handler500

handler404 = 'pages.views.view_404'
handler500 = 'pages.views.view_500'
handler403 = 'pages.views.view_403'

urlpatterns = [
    path('',include('pages.urls')),
    path('listings/',include('listings.urls', namespace='listings')),
    path('accounts/',include('allauth.urls')),
    path('accounts/dash/',include('accounts.urls', namespace='accounts')),
    path('contacts/',include('contacts.urls')),
    path('realtors/',include('realtors.urls', namespace='realtors')),
    path('admin/', admin.site.urls),
]  

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

