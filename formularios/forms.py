from django import forms

class CrearEmpleado(forms.Form):
    nombre = forms.CharField(label="Nombre del empleado", max_length=200)
    apellido = forms.CharField(label="Apellido del empleado", max_length=200)
    cargo = forms.CharField(label="Cargo del empleado", max_length=200)

class CrearProducto(forms.Form):
    nombre = forms.CharField(label="Producto", max_length=200)
    valor = forms.IntegerField(label="Valor")
    
class CrearCliente(forms.Form):
    nombre = forms.CharField(label="Nombre del cliente", max_length=200)
    apellido = forms.CharField(label="Apellido del cliente", max_length=200)
    
class Buscar(forms.Form):
    valor = forms.CharField(label="Valor a buscar", max_length=200)
