from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Employee, Position
from .forms import EmployeeForm, PositionForm


def index(request):
    context = {
        'employees': Employee.objects.all(),
        'position_count': Position.objects.all().count()
    }
    return render(request, 'employee_list.html', context)

class Form(CreateView):
    template_name='form.html'
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('home')



def empUpdate(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form': form}
    return render(request, 'employee_update.html', context)


def empDelete(request, pk):
    emp = Employee.objects.get(id=pk)
    if request.method == 'POST':
        emp.delete()
        return redirect('home')
    context = {'emp': emp}
    return render(request, 'employee_delete.html', context)


def positonList(request):
    position=Position.objects.all()
    context={'positions':position}
    return render(request, 'position_list.html', context)

def positionUpdate(request, pk):
    position=Position.objects.get(id=pk)
    form=PositionForm(instance=position)
    if request.method == 'POST':
        form=PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
        return redirect('position-list')
    context={'form':form}
    return render(request, 'position_update.html', context)


def positionDelete(request, pk):
    position=Position.objects.get(id=pk)
    if request.method == 'POST':
        position.delete()
        return redirect('position-list')
    context={'position':position}
    return render(request, 'position_delete.html', context)