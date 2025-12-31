from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE


class Status(models.TextChoices):
    PENDENTE = 'pendente', 'Pendente'
    CONCLUIDO = 'concluido', 'Concluído'


class Task(models.Model):
    titulo = models.CharField(max_length=64)
    descricao = models.TextField(max_length=2000, blank=True)
    status = models.CharField(max_length=9, choices=Status.choices, default=Status.PENDENTE)
    user = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    criada_em = models.DateTimeField(auto_now_add=True)
