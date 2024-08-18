from django.contrib import admin
from django.utils.html import format_html

from .models import Zapatillas , Zapatilla_Talle , Zapatilla_Precio


class ZapatillaTalleAdmin(admin.TabularInline):
    verbose_name = "Talle"
    model = Zapatilla_Talle
    extra = 1

class ZapatillaPrecioAdmin(admin.TabularInline):
    verbose_name = "Precio"
    model = Zapatilla_Precio
    extra = 1

class ZapatillaAdmin(admin.ModelAdmin):
    list_display = ('image_tag' , 'nombre', 'link', 'reintentos' , 'get_talles' , 'get_precios' )
    search_fields = ( 'nombre' , 'reintentos' )
    inlines = [ZapatillaTalleAdmin,ZapatillaPrecioAdmin]
    empty_value_display = "-empty-"

    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" height="150" />'.format(obj.img))
    image_tag.short_description = 'img'

    def link(self, obj):
        return format_html('<a href="{}" target=blank>Link Producto</a>'.format(obj.url))
    link.short_description = 'url'

    def get_talles(self, obj):
        return [ obj_talle.talle for obj_talle in obj.talles.all() ]
    
    get_talles.short_description = 'Talles'

    def get_precios(self, obj):
        elements_li = ''
        for precio in obj.precios.all():
            elements_li += f'<li display: block>{precio.precio}</li>' 
        return format_html(f'<ul>{elements_li}</ul>')
    get_precios.short_description = 'Precios'


admin.site.register( Zapatillas , ZapatillaAdmin )