from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    nome_completo = models.CharField(max_length=50, null=True)
    bi = models.CharField(max_length=14, null=True, verbose_name="BI")
    telefone = models.CharField(max_length=16, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_completo or self.usuario.username
