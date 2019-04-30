from django.db import models

class disciplinas(models.Model):
	nome = models.CharField("Nome", max_length=50)
	carga_horaria = models.IntegerField("CARGA HORARIA", max_length = 4)
	
	def _str_(self):
		return self.nome
