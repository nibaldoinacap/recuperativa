from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=30)
    correo = models.EmailField()
    direccion = models.CharField(max_length=180)
    saldo_pendiente = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    fecha_registro = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.nombre


class Atencion(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='atenciones',
    )
    mascota = models.CharField(max_length=100)
    especie = models.CharField(max_length=60)
    motivo = models.CharField(max_length=200)
    veterinario = models.CharField(max_length=120)
    monto = models.DecimalField(max_digits=12, decimal_places=0)
    fecha_atencion = models.DateField()

    class Meta:
        ordering = ['-fecha_atencion', 'mascota']
        verbose_name = 'atención'
        verbose_name_plural = 'atenciones'

    def __str__(self):
        return f'{self.mascota} - {self.cliente.nombre}'
