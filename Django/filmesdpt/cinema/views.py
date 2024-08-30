from django.views.generic import DetailView, ListView
from .models import Post, Usuario
from django.shortcuts import render

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

def login(request):
    return render(request,'cinema/login.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()
    
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    return render(request,'cinema/usuarios.html',usuarios)

def duna(request):
    return render(request,'cinema/duna.html')

def menino(request):
    return render(request,'cinema/menino.html')

def todos(request):
    return render(request,'cinema/todos.html')

def bob(request):
    return render(request,'cinema/bob.html')

def dias(request):
    return render(request,'cinema/dias.html')

def emcartaz(request):
    return render(request,'cinema/emcartaz.html')

def godzila(request):
    return render(request,'cinema/godzila.html')

def login2(request):
    return render(request,'cinema/login2.html')

def kong(request):
    return render(request,'cinema/kong.html')

def trailer(request):
    return render(request,'cinema/trailer.html')

def sala(request):
    return render(request,'cinema/sala.html')
