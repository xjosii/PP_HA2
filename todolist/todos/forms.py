from django import forms
from .models import ListEntry

#nötig für Bearbeiten und Hinzufügen der Todos
class TodoForm(forms.ModelForm):
   
    class Meta:
        model = ListEntry
        fields = '__all__'