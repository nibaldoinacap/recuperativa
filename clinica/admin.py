from django.contrib import admin
from django.utils.html import format_html

from .models import Atencion, Cliente


def formato_pesos(valor):
    return format_html('${}', f'{int(valor):,}'.replace(',', '.'))


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'telefono',
        'correo',
        'direccion',
        'saldo_pendiente_formateado',
        'fecha_registro',
    )
    list_filter = ('fecha_registro',)
    search_fields = ('nombre', 'telefono', 'correo')

    @admin.display(description='Saldo pendiente', ordering='saldo_pendiente')
    def saldo_pendiente_formateado(self, obj):
        return formato_pesos(obj.saldo_pendiente)


@admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
    list_display = (
        'mascota',
        'cliente',
        'especie',
        'motivo',
        'veterinario',
        'monto_formateado',
        'fecha_atencion',
    )
    list_filter = ('especie', 'fecha_atencion')
    search_fields = ('mascota', 'cliente__nombre', 'motivo', 'veterinario')

    @admin.display(description='Monto', ordering='monto')
    def monto_formateado(self, obj):
        return formato_pesos(obj.monto)
