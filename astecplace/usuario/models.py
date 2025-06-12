from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=20, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)



# Create your models here.
