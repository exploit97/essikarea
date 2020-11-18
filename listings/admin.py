from django.contrib import admin

# Register your models here.
from .models import Propriete,Arrondissement,Ville,District


class ProprieteAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published','price','list_date','realtor')
    list_display_links=('id','title')
    list_filter=('realtor',)
    list_editable=('is_published',)
    search_fields=('title','address','ville','arrondissement', 'district','price')
    list_per_page=25
admin.site.register(Propriete,ProprieteAdmin)

admin.site.register(Arrondissement)
admin.site.register(Ville)
admin.site.register(District)


