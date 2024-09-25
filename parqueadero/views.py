from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import VehiculoForm, BuscarVehiculoForm , FuncionarioForm
from .models import Vehiculo, ControlIngreso, Funcionario
from django.core.paginator import Paginator
from django.contrib import messages


@login_required
def bienvenida(request):
    return render(request, 'parqueadero/bienvenida.html', {'usuario': request.user})

@login_required
def registrar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bienvenida')  # Redirige a la página de bienvenida o donde prefieras
    else:
        form = VehiculoForm()
    return render(request, 'parqueadero/registrar_vehiculo.html', {'form': form})

@login_required
def listar_vehiculos(request):
    query = request.GET.get('q', '')
    if query:
        vehiculos = Vehiculo.objects.filter(
            placas__icontains=query
        ) | Vehiculo.objects.filter(
            propietario__icontains=query
        )
    else:
        vehiculos = Vehiculo.objects.all()

    return render(request, 'parqueadero/listar_vehiculos.html', {
        'vehiculos': vehiculos
    })

@login_required
def bienvenida(request):
    mensaje = None
    ultimos_ingresos = ControlIngreso.objects.order_by('-fecha_ingreso')[:4]
    
    if request.method == 'POST':
        form = BuscarVehiculoForm(request.POST)
        if form.is_valid():
            placa = form.cleaned_data['placa']
            try:
                vehiculo = Vehiculo.objects.get(placas=placa)
                if vehiculo.esta_autorizado:
                    # Guardar el ingreso del vehículo
                    ControlIngreso.objects.create(
                        vehiculo=vehiculo,
                        registrado_por=request.user
                    )
                    mensaje = f"El vehículo con placa {placa} está autorizado."
                else:
                    mensaje = f"El vehículo con placa {placa} no está autorizado."
            except Vehiculo.DoesNotExist:
                mensaje = f"El vehículo con placa {placa} no se encuentra registrado."
    else:
        form = BuscarVehiculoForm()

    return render(request, 'parqueadero/bienvenida.html', {
        'form': form,
        'mensaje': mensaje,
        'ultimos_ingresos': ultimos_ingresos
    })

@login_required
def eliminar_vehiculo(request, pk):
    if request.method == 'POST':
        vehiculo = get_object_or_404(Vehiculo, pk=pk)
        vehiculo.delete()
        messages.success(request, 'Vehículo eliminado exitosamente.')
        return redirect('listar_vehiculos')
    else:
        messages.error(request, 'Método no permitido.')
        return redirect('listar_vehiculos')
    

@login_required
def editar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo actualizado exitosamente.')
            return redirect('listar_vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)
    
    return render(request, 'parqueadero/editar_vehiculo.html', {'form': form})


@login_required
def registrar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_funcionarios')  # Redirigir a la lista de funcionarios después de registrar
    else:
        form = FuncionarioForm()
    
    return render(request, 'funcionarios/registrar_funcionario.html', {'form': form})

@login_required
def eliminar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('listar_funcionarios')  # Redirigir después de eliminar
    return render(request, 'funcionarios/eliminar_funcionario.html', {'funcionario': funcionario})

@login_required
def editar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('listar_funcionarios')
    else:
        form = FuncionarioForm(instance=funcionario)
    
    return render(request, 'funcionarios/editar_funcionario.html', {'form': form, 'funcionario': funcionario})

@login_required
def listar_funcionarios(request):
    query = request.GET.get('q')  # Obtiene el término de búsqueda del input 'q'
    
    if query:
        funcionarios = Funcionario.objects.filter(nombre__icontains=query)  # Filtrar por nombre que contenga la consulta
    else:
        funcionarios = Funcionario.objects.all()  # Mostrar todos si no hay búsqueda

    return render(request, 'funcionarios/listar_funcionarios.html', {'funcionarios': funcionarios})

