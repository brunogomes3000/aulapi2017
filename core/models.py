from django.db import models

class Usuario(models.Model):
	nome = models.CharField('Nome', max_length=100)
	perfil = models.CharField('Nome', max_length=100)
	email = models.CharField('E-mail', max_length=100)
	celular = models.CharField('Celular', max_length=100)
	residencial = models.CharField('Residêncial', max_length=100)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'


class Curso(models.Model):
	nome = models.CharField("Nome", max_length=100)
	descricao = models.CharField("Descrição", max_length=100)
	data_inicio = models.DateField('Data de Início', null=True, blank=True)
	imagem = models.ImageField(upload_to='img/curso', verbose_name='Imagem', default='imagens/perfil/noperfil.png', null=True, blank=True)
	autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

	data_criacao = models.DateField('Data de Criação', auto_now_add=True)
	data_modificacao = models.DateField('Data de Modificação', auto_now=True)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'


class Inscritos(models.Model):
	nome = models.CharField("Nome", max_length=100)
	matricula = models.CharField("Descrição", max_length=100)
	email = models.CharField("Descrição", max_length=100)
	celular = models.CharField('Celular', max_length=100)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)