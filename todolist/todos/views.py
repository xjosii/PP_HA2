from django.shortcuts import render, redirect

from .models import ListEntry
from .forms import TodoForm

# Create your views here.

#Startseite mit der Tabelle, die alle Todos enthält
def todos_table(request):
    context = {'todos_table':ListEntry.objects.all()}
    return render(request, "todo_table.html",context)

#TODO: Löschen
def todos_delete(request):
    return

#Todos bearbeiten GET und POST
def todos_edit(request,id=0):
    if request.method == "GET":
        listEntry = ListEntry.objects.get(pk=id)
        form = TodoForm(instance=listEntry)
        return render(request, "todo_edit.html",{'form': form})
    else:
        listEntry = ListEntry.objects.get(pk=id)
        form = TodoForm(request.POST,instance=listEntry)
        if form.is_valid():
            form.save()
        return redirect('/todos/')
       
#Todos hinzufügen GET und POST
def todos_add(request):
    if request.method == "GET":
        form = TodoForm()
        return render(request, "todo_add.html",{'form': form})
    else: 
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todos')