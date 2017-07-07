from django.db import models
from django.utils import timezone

class Post(models.Model):
    Nome = models.ForeignKey('auth.User')
    Horario = models.CharField(max_length=200)
    Descricao = models.TextField()
    Data_de_criacao = models.DateTimeField(
            default=timezone.now)
    Data_de_postagem = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.Data_de_postagem = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Nome)
