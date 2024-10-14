from django.db import models

# Create your models here.
class AlumnoT(models.Model):
    Apaterno=models.CharField(max_length=50,verbose_name="Apellido Paterno jaja")
    Amaterno=models.CharField(max_length=50,verbose_name="Apellido Materno")
    Nombres=models.CharField(max_length=100,verbose_name="Nombre (s)")
    Fecha_nacimiento=models.DateField(verbose_name="Fecha de Nacimiento",null=False,blank=False)
    Fecha_ingreso=models.DateField(verbose_name="Fecha de Ingreso",null=False,blank=False)