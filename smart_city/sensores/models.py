from django.db import models

class Ambiente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Sensor(models.Model):
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE, related_name='sensores')
    temperatura = models.FloatField()
    luminosidade = models.FloatField()
    umidade = models.FloatField()
    contador = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sensor {self.id} - {self.ambiente.nome}"
