"""inventario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from control import views

app_name = 'control'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    
#--------------------------------Tienda 1---------------------#
    path('render_tienda1/', views.render_tienda1, name='render_tienda1'),
    path('crear_tienda/', views.crear_tienda, name='crear_tienda'),
    path('import_data_tienda1/', views.import_data_tienda1, name='import_data1'),
    path('eliminar_registros/', views.eliminar_registros_tienda1, name='eliminar_registros'),
    path('export_data_tienda1/', views.export_data_tienda1, name='export_data_tienda1'),
    path('grafica_tienda1/', views.grafica_tienda1, name='grafica_tienda1'),
    

#--------------------------------Tienda 2---------------------#
    path('crear_tienda2/', views.crear_tienda2, name='crear_tienda2'),
    path('render_tienda2/', views.render_tienda2, name='render_tienda2'),
    path('export_data_tienda2/', views.export_data_tienda2, name='export_data_tienda2'),
    path('grafica_tienda2/', views.grafica_tienda2, name='grafica_tienda2'),
    path('eliminar_registros_tienda2/', views.eliminar_registros_tienda2, name='eliminar_registros_tienda2'),
    path('import_data_tienda2/', views.import_data_tienda2, name='import_data_tienda2'),
    
    
#--------------------------------Tienda 3---------------------#
    path('render_tienda3/', views.render_tienda3, name='render_tienda3'),
    path('crear_tienda3/', views.crear_tienda3, name='crear_tienda3'),
    path('export_data_tienda3/', views.export_data_tienda3, name='export_data_tienda3'),
    path('import_data_tienda3/', views.import_data_tienda3, name='import_data_tienda3'),
    path('eliminar_registros_tienda3/', views.eliminar_registros_tienda3, name='eliminar_registros_tienda3'),
    path('grafica_tienda3/', views.grafica_tienda3, name='grafica_tienda3'),
   
   
#--------------------------------Tienda 4---------------------#
    path('render_tienda4/', views.render_tienda4, name='render_tienda4'),
    path('crear_tienda4/', views.crear_tienda4, name='crear_tienda4'),
    path('export_data_tienda4/', views.export_data_tienda4, name='export_data_tienda4'),
    path('import_data_tienda4/', views.import_data_tienda4, name='import_data_tienda4'),
    path('eliminar_registros_tienda4/', views.eliminar_registros_tienda4, name='eliminar_registros_tienda4'),
    path('grafica_tienda4/', views.grafica_tienda4, name='grafica_tienda4'),
    
    
#--------------------------------Tienda5---------------------#
    path('render_tienda5/', views.render_tienda5, name='render_tienda5'),
    path('crear_tienda5/', views.crear_tienda5, name='crear_tienda5'),
    path('export_data_tienda5/', views.export_data_tienda5, name='export_data_tienda5'),
    path('import_data_tienda5/', views.import_data_tienda5, name='import_data_tienda5'),
    path('eliminar_registros_tienda5/', views.eliminar_registros_tienda5, name='eliminar_registros_tienda5'),
    path('grafica_tienda5/', views.grafica_tienda5, name='grafica_tienda5'),
    
    
    path('cantidad-datos/', views.cantidad_datos, name='cantidad_datos'),
    path('grafica_tiendas/', views.grafica_tiendas, name='grafica_tiendas'),
    path('grafica_comparativa/', views.grafica_comparativa, name='grafica_comparativa'),
    
         
]
