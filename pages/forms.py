from django import forms
#from pages import Person, Lga, Product
from . models import Person, Lga, Product

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'birthday', 'state', 'lga')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lga'].queryset = Lga.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['lga'].queryset = Lga.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass #invalid input from the client

        elif self.instance.pk:
            self.fields['lga'] .queryset = self.instance.state.lga_set.order_by('name')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'is_discount', 'discount']