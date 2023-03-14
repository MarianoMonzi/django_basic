from django.shortcuts import render, redirect
from .forms import CrearCliente, CrearEmpleado, CrearProducto, Buscar
from .models import Empleado, Producto, Cliente

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = Buscar(request.POST)
        if form.is_valid():
            clientes = list(Cliente.objects.values())
            # Se comprueba si el valor es un cliente
            for cliente in clientes:
                if form.cleaned_data['valor'] == cliente['nombre'] or form.cleaned_data['valor'] == cliente['apellido']:
                    result = cliente['nombre'] + ' ' + cliente['apellido']

                    return render(request, 'index.html', {'form': form, 'value': result + " es un cliente"})
                else:
                    # Se comprueba si el valor es un empleado
                    empleados = list(Empleado.objects.values())
                    for empleado in empleados:
                        if form.cleaned_data['valor'] == empleado['nombre'] or form.cleaned_data['valor'] == empleado['apellido']:
                            result = empleado['nombre'] + ' ' + empleado['apellido']

                            return render(request, 'index.html', {'form': form, 'value': result + " es un empleado"})
                        else:
                            # Se comprueba si el valor es un producto
                            productos = list(Producto.objects.values())
                            for producto in productos:
                                if form.cleaned_data['valor'] == producto['nombre']:
                                    result = producto['nombre']

                                    return render(request, 'index.html', {'form': form, 'value': result + " es un producto"})
                                
                    else:
                        return render(request, 'index.html', {'form': form, 'value': 'No se encontro el valor buscado'})

    else:
        form = Buscar()

    return render(request, 'index.html', {'form': form})


def empleados(request):
    empleados = list(Empleado.objects.values())
    empleados = Empleado.objects.all()
    return render(request, 'empleados/empleados.html', {
        'empleados': empleados
    })


def crear_empleado(request):
    if request.method == 'POST':
        form = CrearEmpleado(request.POST)
        if form.is_valid():
            Empleado.objects.create(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                cargo=form.cleaned_data['cargo']
            )
            return redirect('empleados')
    else:
        form = CrearEmpleado()

    return render(request, 'empleados/crear_empleado.html', {'form': form})


def productos(request):
    productos = list(Producto.objects.values())
    productos = Producto.objects.all()
    return render(request, 'productos/productos.html', {
        'productos': productos
    })


def crear_producto(request):
    if request.method == 'POST':
        form = CrearProducto(request.POST)
        if form.is_valid():
            Producto.objects.create(
                nombre=form.cleaned_data['nombre'],
                valor=form.cleaned_data['valor'],
            )
            return redirect('productos')
    else:
        form = CrearProducto()

    return render(request, 'productos/crear_producto.html', {'form': form})


def clientes(request):
    clientes = list(Cliente.objects.values())
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {
        'clientes': clientes
    })


def crear_clientes(request):
    if request.method == 'POST':
        form = CrearCliente(request.POST)
        if form.is_valid():
            Cliente.objects.create(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
            )
            return redirect('clientes')
    else:
        form = CrearCliente()

    return render(request, 'clientes/crear_clientes.html', {'form': form})
