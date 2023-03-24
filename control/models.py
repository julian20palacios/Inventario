from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import RegexValidator
from datetime import datetime, timedelta

#--------------------------------Tienda 1---------------------#
class Tienda1(models.Model):
        numero_tienda = models.CharField(max_length=50)
        layer_code = models.CharField(max_length=50)
        fecha_ingreso = models.DateField()
        fecha_actual = models.DateField(auto_now_add=True)
        dias = models.IntegerField()
        
        def save(self, *args, **kwargs):
            self.dias = (datetime.now().date() - self.fecha_ingreso).days
            super(Tienda1, self).save(*args, **kwargs)

        @property
        def comentario(self):
            if self.dias < 75:
                return 'Menor a 75'
            elif self.dias <= 90:
                return 'Esta entre 75 y 90'
            else:
                return 'Es mayor a 90'
            
            
#--------------------------------Tienda 2---------------------#

class Tienda2(models.Model):
    numero_tienda = models.CharField(max_length=50)
    layer_code = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    fecha_actual = models.DateField(auto_now_add=True)
    dias = models.IntegerField()

    def save(self, *args, **kwargs):
        self.dias = (datetime.now().date() - self.fecha_ingreso).days
        super(Tienda2, self).save(*args, **kwargs)

    @property
    def comentario(self):
        if self.dias < 75:
            return 'Menor a 75'
        elif self.dias <= 90:
            return 'Esta entre 75 y 90'
        else:
            return 'Es mayor a 90'


#--------------------------------Tienda 3---------------------#
class Tienda3(models.Model):
    numero_tienda = models.CharField(max_length=50)
    layer_code = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    fecha_actual = models.DateField(auto_now_add=True)
    dias = models.IntegerField()

    def save(self, *args, **kwargs):
        self.dias = (datetime.now().date() - self.fecha_ingreso).days
        super(Tienda3, self).save(*args, **kwargs)

    @property
    def comentario(self):
        if self.dias < 75:
            return 'Menor a 75'
        elif self.dias <= 90:
            return 'Esta entre 75 y 90'
        else:
            return 'Es mayor a 90'
        

#--------------------------------Tienda 4---------------------#
class Tienda4(models.Model):
    numero_tienda = models.CharField(max_length=50)
    layer_code = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    fecha_actual = models.DateField(auto_now_add=True)
    dias = models.IntegerField()

    def save(self, *args, **kwargs):
        self.dias = (datetime.now().date() - self.fecha_ingreso).days
        super(Tienda4, self).save(*args, **kwargs)

    @property
    def comentario(self):
        if self.dias < 75:
            return 'Menor a 75'
        elif self.dias <= 90:
            return 'Esta entre 75 y 90'
        else:
            return 'Es mayor a 90'
        

#--------------------------------Tienda 5---------------------#
class Tienda5(models.Model):
    numero_tienda = models.CharField(max_length=50)
    layer_code = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    fecha_actual = models.DateField(auto_now_add=True)
    dias = models.IntegerField()

    def save(self, *args, **kwargs):
        self.dias = (datetime.now().date() - self.fecha_ingreso).days
        super(Tienda5, self).save(*args, **kwargs)

    @property
    def comentario(self):
        if self.dias < 75:
            return 'Menor a 75'
        elif self.dias <= 90:
            return 'Esta entre 75 y 90'
        else:
            return 'Es mayor a 90'