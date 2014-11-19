from django.shortcuts import render
from animal.models import Animal
from animal.forms import AnimalForm

def index(request):
	form = AnimalForm();
	return render(request, 'index.html', {'form':form})

def validar(request):
	if request.method == 'POST':
		form = AnimalForm(request.POST)

		if form.is_valid(): #valida o tamanho e o tipo do campo de acordo com o que foi determinado
			animal = Animal(**form.cleaned_data) #esse cleaned_data transforma campos em branco para campos NULL, o ** significa lista
			animal.save()

			animal = Animal.objects.all().order_by('nome') #select * from
			
			return render(request,'validar.html',{'form':form, 'animal':animal})
		else:
			return render(request,'index.html',{'form':form})

def listar(request):
	animal = Animal.objects.all()
	return render(request, 'listar.html', {'animal': animal})

