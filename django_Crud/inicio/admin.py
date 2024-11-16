from django.contrib import admin
from inicio.models import Pessoa, Tarefa

# Register your models here.registrar os modelos (objetos)

class PessoaAdmin(admin.ModelAdmin):
    #Mostra os CAMPOS desejados na rota 'admin/'
    list_display = ('nome', 'idade', 'email')
    search_fields = ('nome', 'idade', 'email')

    #Apresenta um filtro interativo pelos CAMPOS definidos
    list_filter = ('nome','email' )
    
admin.site.register(Pessoa,PessoaAdmin) #adicionado por kelvem

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'descricao')
    

admin.site.register(Tarefa,TarefaAdmin)