from django.shortcuts import render
from django.views.generic import ListView, CreateView
#from pages import Person, Lga, Product
from . models import Person, Lga, Product
from django.urls import reverse_lazy
from .forms import PersonForm, ProductForm



def home_view(request):
    return render(request, 'pages/index.html', {})

class PersonListView(ListView):
    model = Person
    context_object_name = 'people'
    template_name = 'pages/person_list.html'

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'pages/person_form.html'
    success_url = reverse_lazy('person_changelist')



def load_lgas(request):
    state_id = request.GET.get('state')
    lgas = Lga.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'pages/lga_dropdown_list_options.html', {'lgas':lgas})



def product_view(request):
    products = Product.objects.all()

    return render(request, 'pages/products.html', {"products":products})



class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'pages/products_form.html'
    success_url = reverse_lazy('product-add')

def contact_view(request):
    return render(request, 'pages/contact.html')

def about_view(request):
    return render(request, 'pages/about.html')