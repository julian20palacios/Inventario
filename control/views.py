from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import Tienda1Form, Tienda2Form, Tienda3Form, Tienda4Form, Tienda5Form
from .models import Tienda1, Tienda2, Tienda3, Tienda4, Tienda5 
from django.http import HttpResponse
from openpyxl import Workbook
from datetime import datetime
import re
from decimal import Decimal
from django.db.models import Q, F, Count, Case, When
from django.http import JsonResponse
from django.contrib import messages
import pandas as pd
from django.db import transaction
from django.template.loader import get_template
from django.conf import settings
from django.templatetags.static import static
import matplotlib.pyplot as plt
import base64, json, datetime


#--------------------------------Inicio---------------------#

def inicio(request):
    return render(request, "inicio.html")

def grafica_tiendas(request):
    # Obtenemos la cantidad de objetos de cada categoría en cada modelo
    menor_75 = [Tienda1.objects.filter(dias__lt=75).count(),
                Tienda2.objects.filter(dias__lt=75).count(),
                Tienda3.objects.filter(dias__lt=75).count(),
                Tienda4.objects.filter(dias__lt=75).count(),
                Tienda5.objects.filter(dias__lt=75).count()]

    entre_75_90 = [Tienda1.objects.filter(dias__range=(75, 90)).count(),
                   Tienda2.objects.filter(dias__range=(75, 90)).count(),
                   Tienda3.objects.filter(dias__range=(75, 90)).count(),
                   Tienda4.objects.filter(dias__range=(75, 90)).count(),
                   Tienda5.objects.filter(dias__range=(75, 90)).count()]

    mayor_90 = [Tienda1.objects.filter(dias__gt=90).count(),
                Tienda2.objects.filter(dias__gt=90).count(),
                Tienda3.objects.filter(dias__gt=90).count(),
                Tienda4.objects.filter(dias__gt=90).count(),
                Tienda5.objects.filter(dias__gt=90).count()]

    # Sumamos las cantidades de cada modelo para obtener la cantidad total de objetos en cada categoría
    menor_75_total = sum(menor_75)
    entre_75_90_total = sum(entre_75_90)
    mayor_90_total = sum(mayor_90)

    # Preparamos los datos para la gráfica
    # Preparamos los datos para la gráfica
    labels = ['Menor a 75', 'Esta entre 75 y 90', 'Es mayor a 90']
    values_menor_75 = menor_75
    values_entre_75_90 = entre_75_90
    values_mayor_90 = mayor_90
    # Renderizamos la plantilla con los datos para la gráfica
    return render(request, 'grafica_comparativa.html', {
        'labels': labels,
        'values_menor_75': values_menor_75,
        'values_entre_75_90': values_entre_75_90,
        'values_mayor_90': values_mayor_90,
    })


def cantidad_datos(request):
    query_mayor_90 = Case(
        When(dias__gt=90, then=1)
    )
    query_entre_75_90 = Case(
        When(dias__gte=75, dias__lte=90, then=1)
    )
    query_menor_75 = Case(
        When(dias__lt=75, then=1)
    )
    tiendas = [
        ('Tienda 1', Tienda1.objects.aggregate(total=Count('id'), mayor_90=Count(query_mayor_90), entre_75_90=Count(query_entre_75_90), menor_75=Count(query_menor_75))),
        ('Tienda 2', Tienda2.objects.aggregate(total=Count('id'), mayor_90=Count(query_mayor_90), entre_75_90=Count(query_entre_75_90), menor_75=Count(query_menor_75))),
        ('Tienda 3', Tienda3.objects.aggregate(total=Count('id'), mayor_90=Count(query_mayor_90), entre_75_90=Count(query_entre_75_90), menor_75=Count(query_menor_75))),
        ('Tienda 4', Tienda4.objects.aggregate(total=Count('id'), mayor_90=Count(query_mayor_90), entre_75_90=Count(query_entre_75_90), menor_75=Count(query_menor_75))),
        ('Tienda 5', Tienda5.objects.aggregate(total=Count('id'), mayor_90=Count(query_mayor_90), entre_75_90=Count(query_entre_75_90), menor_75=Count(query_menor_75))),
    ]
    return render(request, 'cantidad_datos.html', {'tiendas': tiendas})
    

def grafica_comparativa(request):
    # Obtener la cantidad de registros para cada modelo
    tienda1_count = Tienda1.objects.count()
    tienda2_count = Tienda2.objects.count()
    tienda3_count = Tienda3.objects.count()
    tienda4_count = Tienda4.objects.count()
    tienda5_count = Tienda5.objects.count()
    
    # Pasar los valores a la plantilla HTML
    context = {
        'tienda1_count': tienda1_count,
        'tienda2_count': tienda2_count,
        'tienda3_count': tienda3_count,
        'tienda4_count': tienda4_count,
        'tienda5_count': tienda5_count,
    }
    
    # Renderizar la plantilla con los datos necesarios
    return render(request, 'grafica_comparativa.html', context)






#--------------------------------Tienda 1---------------------#
def crear_tienda(request):
    if request.method == 'POST':
        form = Tienda1Form(request.POST)
        if form.is_valid():
            tienda = form.save(commit=False)
            tienda.save()
            return redirect('/render_tienda1', pk=tienda.pk)
    else:
        form = Tienda1Form()
    return render(request, 'datos_tienda1.html', {'form': form})

def render_tienda1(request):
    tiendas = Tienda1.objects.all()
    return render(request, 'tienda1.html', {'tiendas': tiendas})

def import_data_tienda1(request):
    if request.method == 'POST':
        file = request.FILES['excel_file']
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            fecha_ingreso = datetime.datetime.strptime(str(row['fecha_ingreso']), '%Y-%m-%d %H:%M:%S').date()
            tienda = Tienda1(numero_tienda=row['numero_tienda'], layer_code=row['layer_code'], fecha_ingreso=fecha_ingreso)
            tienda.save()
        return redirect('render_tienda1')
    return render(request, 'import_data_tienda1.html')

def eliminar_registros_tienda1(request):
    Tienda1.objects.all().delete()
    return redirect('render_tienda1')

def get_comentario(tienda):
    return tienda.comentario

def export_data_tienda1(request):
    tienda1_data = Tienda1.objects.all()
    data = []
    for tienda in tienda1_data:
        tienda_dict = {
            'numero_tienda': tienda.numero_tienda,
            'layer_code': tienda.layer_code,
            'fecha_ingreso': tienda.fecha_ingreso,
            'fecha_actual': tienda.fecha_actual,
            'dias': tienda.dias,
            'comentario': get_comentario(tienda),
        }
        data.append(tienda_dict)
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="tienda1_data.xlsx"'
    df.to_excel(response, index=False)
    return response

def grafica_tienda1(request):
    tiendas_menor_75 = Tienda1.objects.filter(dias__lt=75).count()
    tiendas_entre_75_90 = Tienda1.objects.filter(dias__range=(75, 90)).count()
    tiendas_mayor_90 = Tienda1.objects.filter(dias__gt=90).count()

    labels = ['Menor a 75', 'Esta entre 75 y 90', 'Es mayor a 90']
    values = [tiendas_menor_75, tiendas_entre_75_90, tiendas_mayor_90]

    return render(request, 'grafica_tiendas.html', {'labels': labels, 'values': values})





#--------------------------------Tienda 2---------------------#



def crear_tienda2(request):
    if request.method == 'POST':
        form = Tienda2Form(request.POST)
        if form.is_valid():
            tienda = form.save(commit=False)
            tienda.save()
            return redirect('/render_tienda2')
    else:
        form = Tienda2Form()
    return render(request, 'datos_tienda2.html', {'form': form})

def render_tienda2(request):
    tiendas = Tienda2.objects.all()
    return render(request, 'tienda2.html', {'tiendas': tiendas})

def get_comentario2(tienda):
    return tienda.comentario

def export_data_tienda2(request):
    tienda2_data = Tienda2.objects.all()
    data = []
    for tienda in tienda2_data:
        tienda_dict = {
            'numero_tienda': tienda.numero_tienda,
            'layer_code': tienda.layer_code,
            'fecha_ingreso': tienda.fecha_ingreso,
            'fecha_actual': tienda.fecha_actual,
            'dias': tienda.dias,
            'comentario': get_comentario2(tienda),
        }
        data.append(tienda_dict)
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="tienda2_data.xlsx"'
    df.to_excel(response, index=False)
    return response


def grafica_tienda2(request):
    tiendas_menor_75 = Tienda2.objects.filter(dias__lt=75).count()
    tiendas_entre_75_90 = Tienda2.objects.filter(dias__range=(75, 90)).count()
    tiendas_mayor_90 = Tienda2.objects.filter(dias__gt=90).count()

    labels = ['Menor a 75', 'Esta entre 75 y 90', 'Es mayor a 90']
    values = [tiendas_menor_75, tiendas_entre_75_90, tiendas_mayor_90]

    return render(request, 'grafic_tiendas2.html', {'labels': labels, 'values': values})

def eliminar_registros_tienda2(request):
    Tienda2.objects.all().delete()
    return redirect('render_tienda2')

def import_data_tienda2(request):
    if request.method == 'POST':
        file = request.FILES['excel_file']
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            fecha_ingreso = datetime.datetime.strptime(str(row['fecha_ingreso']), '%Y-%m-%d %H:%M:%S').date()
            tienda = Tienda2(numero_tienda=row['numero_tienda'], layer_code=row['layer_code'], fecha_ingreso=fecha_ingreso)
            tienda.save()
        return redirect('render_tienda2')
    return render(request, 'import_data_tienda2.html')



#--------------------------------Tienda 3---------------------#


def crear_tienda3(request):
    if request.method == 'POST':
        form = Tienda3Form(request.POST)
        if form.is_valid():
            tienda = form.save(commit=False)
            tienda.save()
            return redirect('/render_tienda3')
    else:
        form = Tienda3Form()
    return render(request, 'datos_tienda3.html', {'form': form})

def render_tienda3(request):
    tiendas = Tienda3.objects.all()
    return render(request, 'tienda3.html', {'tiendas': tiendas})

def get_comentario3(tienda):
    return tienda.comentario

def export_data_tienda3(request):
    tienda3_data = Tienda3.objects.all()
    data = []
    for tienda in tienda3_data:
        tienda_dict = {
            'numero_tienda': tienda.numero_tienda,
            'layer_code': tienda.layer_code,
            'fecha_ingreso': tienda.fecha_ingreso,
            'fecha_actual': tienda.fecha_actual,
            'dias': tienda.dias,
            'comentario': get_comentario3(tienda),
        }
        data.append(tienda_dict)
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="tienda3_data.xlsx"'
    df.to_excel(response, index=False)
    return response

def import_data_tienda3(request):
    if request.method == 'POST':
        file = request.FILES['excel_file']
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            fecha_ingreso = datetime.datetime.strptime(str(row['fecha_ingreso']), '%Y-%m-%d %H:%M:%S').date()
            tienda = Tienda3(numero_tienda=row['numero_tienda'], layer_code=row['layer_code'], fecha_ingreso=fecha_ingreso)
            tienda.save()
        return redirect('render_tienda3')
    return render(request, 'import_data_tienda3.html')

def eliminar_registros_tienda3(request):
    Tienda3.objects.all().delete()
    return redirect('render_tienda3')

def grafica_tienda3(request):
    tiendas_menor_75 = Tienda3.objects.filter(dias__lt=75).count()
    tiendas_entre_75_90 = Tienda3.objects.filter(dias__range=(75, 90)).count()
    tiendas_mayor_90 = Tienda3.objects.filter(dias__gt=90).count()

    labels = ['Menor a 75', 'Esta entre 75 y 90', 'Es mayor a 90']
    values = [tiendas_menor_75, tiendas_entre_75_90, tiendas_mayor_90]

    return render(request, 'grafica_tiendas3.html', {'labels': labels, 'values': values})


#--------------------------------Tienda 4---------------------#

def render_tienda4(request):
    tiendas = Tienda4.objects.all()
    return render(request, 'tienda4.html', {'tiendas': tiendas})

def crear_tienda4(request):
    if request.method == 'POST':
        form = Tienda4Form(request.POST)
        if form.is_valid():
            tienda = form.save(commit=False)
            tienda.save()
            return redirect('/render_tienda4')
    else:
        form = Tienda4Form()
    return render(request, 'datos_tienda4.html', {'form': form})

def get_comentario4(tienda):
    return tienda.comentario

def export_data_tienda4(request):
    tienda4_data = Tienda4.objects.all()
    data = []
    for tienda in tienda4_data:
        tienda_dict = {
            'numero_tienda': tienda.numero_tienda,
            'layer_code': tienda.layer_code,
            'fecha_ingreso': tienda.fecha_ingreso,
            'fecha_actual': tienda.fecha_actual,
            'dias': tienda.dias,
            'comentario': get_comentario4(tienda),
        }
        data.append(tienda_dict)
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="tienda4_data.xlsx"'
    df.to_excel(response, index=False)
    return response

def import_data_tienda4(request):
    if request.method == 'POST':
        file = request.FILES['excel_file']
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            fecha_ingreso = datetime.datetime.strptime(str(row['fecha_ingreso']), '%Y-%m-%d %H:%M:%S').date()
            tienda = Tienda4(numero_tienda=row['numero_tienda'], layer_code=row['layer_code'], fecha_ingreso=fecha_ingreso)
            tienda.save()
        return redirect('render_tienda4')
    return render(request, 'import_data_tienda4.html')

def eliminar_registros_tienda4(request):
    Tienda4.objects.all().delete()
    return redirect('render_tienda4')

def grafica_tienda4(request):
    tiendas_menor_75 = Tienda4.objects.filter(dias__lt=75).count()
    tiendas_entre_75_90 = Tienda4.objects.filter(dias__range=(75, 90)).count()
    tiendas_mayor_90 = Tienda4.objects.filter(dias__gt=90).count()

    labels = ['Menor a 75', 'Esta entre 75 y 90', 'Es mayor a 90']
    values = [tiendas_menor_75, tiendas_entre_75_90, tiendas_mayor_90]

    return render(request, 'grafica_tiendas4.html', {'labels': labels, 'values': values})




#--------------------------------Tienda 5---------------------#

def render_tienda5(request):
    tiendas = Tienda5.objects.all()
    return render(request, 'tienda5.html', {'tiendas': tiendas})

def crear_tienda5(request):
    if request.method == 'POST':
        form = Tienda5Form(request.POST)
        if form.is_valid():
            tienda = form.save(commit=False)
            tienda.save()
            return redirect('/render_tienda5')
    else:
        form = Tienda5Form()
    return render(request, 'datos_tienda5.html', {'form': form})

def get_comentario5(tienda):
    return tienda.comentario

def export_data_tienda5(request):
    tienda4_data = Tienda5.objects.all()
    data = []
    for tienda in tienda4_data:
        tienda_dict = {
            'numero_tienda': tienda.numero_tienda,
            'layer_code': tienda.layer_code,
            'fecha_ingreso': tienda.fecha_ingreso,
            'fecha_actual': tienda.fecha_actual,
            'dias': tienda.dias,
            'comentario': get_comentario5(tienda),
        }
        data.append(tienda_dict)
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="tienda5_data.xlsx"'
    df.to_excel(response, index=False)
    return response

def import_data_tienda5(request):
    if request.method == 'POST':
        file = request.FILES['excel_file']
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            fecha_ingreso = datetime.datetime.strptime(str(row['fecha_ingreso']), '%Y-%m-%d %H:%M:%S').date()
            tienda = Tienda5(numero_tienda=row['numero_tienda'], layer_code=row['layer_code'], fecha_ingreso=fecha_ingreso)
            tienda.save()
        return redirect('render_tienda5')
    return render(request, 'import_data_tienda5.html')

def eliminar_registros_tienda5(request):
    Tienda5.objects.all().delete()
    return redirect('render_tienda5')

def grafica_tienda5(request):
    tiendas_menor_75 = Tienda5.objects.filter(dias__lt=75).count()
    tiendas_entre_75_90 = Tienda5.objects.filter(dias__range=(75, 90)).count()
    tiendas_mayor_90 = Tienda5.objects.filter(dias__gt=90).count()

    labels = ['Menor a 75', 'Esta entre 75 y 90', 'Es mayor a 90']
    values = [tiendas_menor_75, tiendas_entre_75_90, tiendas_mayor_90]

    return render(request, 'grafica_tiendas5.html', {'labels': labels, 'values': values})