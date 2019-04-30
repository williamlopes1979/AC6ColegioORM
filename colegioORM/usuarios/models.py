from django.db import models

class usuarios(models.Model):
	id = models.AutoField("ID", primary_key=True)
	nome = models.CharField("Nome", max_length=120)
	cpf = models.IntegerField("CPF", max_length = 11)
	
	def _str_(self):
		return self.id