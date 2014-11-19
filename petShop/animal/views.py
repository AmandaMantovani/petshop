from django.shortcuts import render
from animal.models import Animal
from animal.forms import AnimalForm

def index(request):
	form = AnimalForm();
	return render(request, 'index.html', {'form':form})