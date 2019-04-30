from django.db import models

class professores(models.Model):
	nome = models.CharField("Nome", max_length=120)
	rp = models.IntegerField("RP", max_length = 10, primary_key=True)
	
	def _str_(self):
		return self.nome
