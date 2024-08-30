from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    venue_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ("-created",)

    def get_absolute_url(self):
        return reverse("cinema:detail", kwargs={"slug": self.slug})
    
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    senha = models.IntegerField()
    
    def save(self,*args,**kwargs):
        if Usuario.objects.filter(nome=self.nome, senha=self.senha).exists():
            pass
        else:
            super(Usuario,self).save(*args,**kwargs)