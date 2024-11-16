from django.shortcuts import render , redirect
from .forms import CadastrarForm , TarefaForm
from inicio.models import Pessoa, Tarefa

def inicio(request):
    tarefas = Tarefa.objects.all()
    return render(request,"inicio.html",{"tarefas":tarefas})

# # insert objects on database
# def cadastrar(request):
#     contexto = {'sucesso': False}
#     form = CadastrarForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         contexto['sucesso'] = True
#     contexto['form'] = form
#     return render(request,"cadastrar.html" ,contexto)

# # list pessoas on database

# def listar(request):
#     pessoas = Pessoa.objects.all()
#     return render(request,"listar.html",{"pessoas":pessoas})

# # edit objects on database
# def update(request,id):
#     pessoa = Tarefa.objects.get(id=id)
#     form = TarefaForm(request.POST or None, instance=pessoa)
#     if form.is_valid():
#         form.save()
#         return redirect('listar')
#     return render(request,"update.html",{'form':form})

# #show detail object on database
# def detalhes(request):
#     pessoas = Tarefa.objects.all()
#     return render(request,"detalhes.html",{"pessoas":pessoas})

# #delete object on database
# def delete(request,id):
#     pessoa = Tarefa.objects.get(id=id)
#     pessoa.delete()
#     return redirect('listar')









## cria tarefeas para gerenciamento


def cadastrar_tarefa(request):
    contexto = {'sucesso': False}
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        contexto['sucesso'] = True
    contexto['form'] = form
    return render(request,"cadastrar.html" ,contexto)

def listar_tarefa(request):
    tarefas = Tarefa.objects.all()
    return render(request,"listar.html",{"tarefas":tarefas})

# edit objects on database
def atualizar_tarefa(request,id):
    tarefa = Tarefa.objects.get(id=id)
    form = TarefaForm(request.POST or None, instance=tarefa)
    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request,"update.html",{'form':form})

#show detail object on database
def detalhes_tarefa(request):
    tarefas = Tarefa.objects.all()
    return render(request,"detalhes.html",{"tarefas":tarefas})

#delete object on database
def delete_tarefa(request,id):
    pessoa = Tarefa.objects.get(id=id)
    pessoa.delete()
    return redirect('listar')