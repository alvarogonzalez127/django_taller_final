from django.db import models

# Create your models here.

opciones_estado = [
    [0,"RESERVADO"],
    [1,"COMPLETADA"],
    [2,"ANULADA"],
    [3,"NO ASISTE"]
]

class Institucion(models.Model):
    institucion = models.CharField(max_length=50,verbose_name="Nombre de Institución")
    def __str__(self):
        return f'{self.institucion}'

    
class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,verbose_name="Nombre")
    telefono  = models.IntegerField(verbose_name="Teléfono")
    fechainscrito = models.DateField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, max_length=50)
    horainscrito = models.TimeField()
    estado = models.IntegerField(choices=opciones_estado,verbose_name="Estado")
    observaciones = models.TextField(max_length=255,verbose_name="Observaciones")
    
