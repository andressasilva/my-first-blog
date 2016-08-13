from django.db import models
from django.utils import timezone

class Post (models.Model):
    author = models.ForeignKey('auth.User') #models.ForeignKey este é um link para outro modelo
    title = models.CharField(max_length=200) #models.CharField define um texto com um numero limitado de caracteres
    text = models.TextField() #TextField serve para escrever textos longos sem um limite de caracteres
    created_date = models.DateTimeField( #models.DateTimeField define data e hora
    default=timezone.now)
    published_date = models.DateTimeField(
    blank=True, null=True)

    def publish(self): #def, significa que se trata de um função\metodo. publish é o nome do metodo.
        self.published_date = timezone.now()
        self.save()

    def __str__ (self):
        return self.title
