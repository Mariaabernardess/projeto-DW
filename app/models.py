from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.estudante} - {self.curso}"