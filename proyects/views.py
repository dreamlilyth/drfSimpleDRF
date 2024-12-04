from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto
from .forms import ProyectoForm
# Create your views here.
def index(request):
    return render(request, 'base.html')

def proyecto_list(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyecto/proyecto_list.html', {'proyectos': proyectos})

def proyecto_create(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyecto_list')
    else:
        form = ProyectoForm()
    return render(request, 'proyecto/proyecto_form.html', {'form': form})
def proyecto_update(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyecto_list')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'proyecto/proyecto_form.html', {'form': form})

def proyecto_delete(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('proyecto_list')
    return render(request, 'proyecto/proyecto_confirm_delete.html', {'proyecto': proyecto})
