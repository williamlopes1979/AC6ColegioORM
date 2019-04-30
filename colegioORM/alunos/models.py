from django.db import models

class alunos(models.Model):
	nome = models.CharField("Nome", max_length=120)
	ra = models.IntegerField("RA", max_length = 10, primary_key=True)
	
	def _str_(self):
		return self.nome