from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(null=True, blank=True, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    completed = models.BooleanField(default=False, verbose_name="Concluído")
    due_date = models.DateTimeField(null=True, blank=True, verbose_name="Data de Entrega")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Tarefa" 
    
    def __str__(self):
        return f'{self.title} - {self.completed}'