from django import forms
from .models import Pessoa , Tarefa

class CadastrarForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'idade','email']

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['tarefa', 'prioridade','descricao']
