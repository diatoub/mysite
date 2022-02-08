
from polls.forms import*
from polls.models import*
from django.shortcuts import (render,
redirect,
get_object_or_404 )

# Create your views here.

def isMajor(age: int) -> str :
    return "Majeur" if age>18 else "Min"

def index(request, *args, **kwargs):
       template_name = 'index.html'
       age = 18
       name ='Diats'
       sexe = 'Feminin'
       country = 'Senegal'
       major = isMajor(age)

       persons = Person.objects.all()
       persons_with_a = persons.filter(name__contains="a")
       person_with_a_and_age_superieur_20 = persons.filter(name__contains="a").filter(age__gt=20)
       
       magasins = Magasin.objects.all()
       profilMagasins = ProfilMagasin.objects.all()
       produits = Produit.objects.all()
       
       #put data in a template
       context = { 
           'age' : age,
           'name' : name,
           'sexe' : sexe,
           'country' : country,
           'isMajor' : major,
           'persons' : persons,
           'personsA' : persons_with_a,
           'personsA_20' : person_with_a_and_age_superieur_20,
           'magasins':magasins,
           'profilMagasins':profilMagasins,
           'produits':produits
           }
       return render(
           request = request,
           template_name = template_name,
           context = context )

def update_person(request, *args, **kwargs):
        template_name = 'update-person.html'
        obj = get_object_or_404(
           Person, 
           pk=kwargs.get('pk')
        )
        if request.method == 'GET':
            form = PersonForm(
                initial={
                    'name':obj.name,
                    'age':obj.age,
                }
            ) 
            context = {
                'form': form,
            }
            return render(
                request = request,
                template_name = template_name,
                context = context )

        if request.method == 'POST':
            form = PersonForm(
                request.POST,
                request.FILES,
                initial={
                    'name': obj.name,
                    'age' : obj.age,
                }
            ) 
        context = {
            'form':form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.sexe = form.cleaned_data.get('sexe')
            obj.age = form.cleaned_data.get('age')
            obj.country = form.cleaned_data.get('country')
            obj.save()
            redirect('home')

        return render(
           request = request,
           template_name = template_name,
           context = context )
