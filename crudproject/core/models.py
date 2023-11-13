from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=150, default=None)
    matricula = models.CharField(max_length=40)
    data_inscricao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Aluno'
    
    def __str__(self):
        return f'{self.nome} - {self.matricula}'
    
