from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    Nome = models.CharField(max_lenght=100)
    
class Clinica(models.Model):
	Nome = models.CharField(max_lenght=100)

class Medico(models.Model):
	Nome = models.ForeignKey('auth.User')
	Email = models.CharField(max_lenght=100)
	Especialidade = models.CharField(max_lenght=300)

class Telefone(models.Model):
	DDD = models.Charfield(masx_lenght=3)
	Tel_da_Clinica = models.CharField(max_lenght=9)
	Tel_do_Medico = models.CharField(max_lenght=9)

class Endereco(models.Model):
	Bairro = models.CharField(max_lenght=50)
	Cidade = models.CharField(max_lenght=50)
	Estado = models.CharField(max_lenght=50)

class Horario_Disponivel(models.Model):
	Horario = models.DateTimeField(
            default=timezone.now)
 
class Post(model.Model):
	Texto = TextField()
	Data_de_postagem = models.DateTimeField(
            blank=True, null=True)
	def publish(self):
		self.Data_de_postagem = timezone.now()
		self.save()
			    
class Comentario(model.Models):
	Comentario = models.TextField()
