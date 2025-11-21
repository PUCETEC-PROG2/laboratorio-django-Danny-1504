from django.http import HttpResponse
from django.template import loader
from .models import Pokemon
from .models import Trainer
from django.shortcuts import redirect, render
from pokedex.forms import pokemonform
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    pokemons = Pokemon.objects.all()
    trainer=Trainer.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons, "trainers":trainer}, request))

def pokemon(request, id: int):
    pokemon=Pokemon.objects.get(id=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer_list(request):
    trainers = Trainer.objects.all()
    template = loader.get_template('trainer_list.html')
    return HttpResponse(template.render({'trainers': trainers}, request))

def trainer (request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    template = loader.get_template("display_trainer.html")
    context = {
        "trainer":trainer
    }
    return HttpResponse (template.render(context, request))

@login_required
def add_pokemon(request):
    if request.method == "POST":
        form = pokemonform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pokedex:index")
    else:
        form = pokemonform()
    
    return render(request, "pokemon_form.html",{"form":form})

@login_required
def edit_pokemon(request, id: int):
    pokemon=Pokemon.objects.get(id=id)
    if request.method == "POST":
        form = pokemonform(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect("pokedex:index")
    else:
        form = pokemonform(instance=pokemon)
    
    return render(request, "pokemon_form.html",{"form":form})

@login_required
def delete_pokemon(request, id: int):
     pokemon=Pokemon.objects.get(id=id)
     pokemon.delete()
     return redirect('pokedex:index')
 
class CustomLoginView(LoginView):
    template_name = 'login_form.html'