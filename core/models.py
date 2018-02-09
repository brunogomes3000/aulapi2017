from django.db import models

class Usuario(models.Model):
	nome = models.CharField('Nome', max_length=200)
	perfil = models.CharField('Perfil', max_length=500)
	imagem_perfil = models.ImageField(upload_to='img/usuarios/', verbose_name='Imagem de Perfil', default='img/usuarios/noperfil.png', null=True, blank=True)
	email = models.CharField('E-mail', max_length=100)
	celular = models.CharField('Celular', max_length=11)
	residencial = models.CharField('Residêncial', max_length=11)
	def __str__(self):
		return self.nome
	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'


class Publico(models.Model):
	descricao = models.CharField("Nome", max_length=100)
	def __str__(self):
		return self.descricao
	class Meta:
		verbose_name = 'Público-alvo'
		verbose_name_plural = 'Público-alvo'


class Area(models.Model):
	descricao = models.CharField("Nome", max_length=100)
	def __str__(self):
		return self.descricao
	class Meta:
		verbose_name = 'Área'
		verbose_name_plural = 'Áreas'


class Curso(models.Model):
	nome = models.CharField("Nome", max_length=100)
	descricao = models.CharField("Descrição", max_length=500)
	data_inicio = models.DateField('Data de Início', null=True, blank=True)
	imagem = models.ImageField(upload_to='img/cursos/', verbose_name='Imagem', default='img/cursos/noperfil.png', null=True, blank=True)
	vagas = models.IntegerField('Vagas')
	autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='autor_curso')
	area = models.ForeignKey(Area, on_delete=models.CASCADE)
	data_criacao = models.DateField('Data de Criação', auto_now_add=True)
	data_modificacao = models.DateField('Data de Modificação', auto_now=True)
	publico = models.ManyToManyField(Publico)
	inscritos = models.ManyToManyField(Usuario, null=True, blank=True)
	def __str__(self):
		return self.nome
	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'


		