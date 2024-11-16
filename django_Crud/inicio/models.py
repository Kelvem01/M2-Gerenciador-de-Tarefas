from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100 )
    idade = models.IntegerField(verbose_name="Idade",blank=True, null=True)
    email = models.EmailField(verbose_name="E-mail",max_length=150)
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        ordering = ["nome"]
        
    def __str__(self):
        return self.nome
    
class Tarefa(models.Model):
    PRIORIDADE_OPCOES = (
        (0, 'Baixa'),
        (1, 'Média'),
        (2, 'Alta'),
    )

    tarefa = models.CharField(verbose_name="Tarefa",max_length=100)
    prioridade = models.IntegerField(verbose_name="Prioridade",max_length=10, choices=PRIORIDADE_OPCOES)
    descricao = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        ordering = ["tarefa"]

    def __str__(self):
        return self.tarefa