from django.contrib import admin

from .models import Atencion, Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'telefono',
        'correo',
        'direccion',
        'saldo_pendiente',
        'fecha_registro',
    )
    list_filter = ('fecha_registro',)
    search_fields = ('nombre', 'telefono', 'correo')


@admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
    list_display = (
        'mascota',
        'cliente',
        'especie',
        'motivo',
        'veterinario',
        'monto',
        'fecha_atencion',
    )
    list_filter = ('especie', 'fecha_atencion')
    search_fields = ('mascota', 'cliente__nombre', 'motivo', 'veterinario')
