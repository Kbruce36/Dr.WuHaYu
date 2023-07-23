#a form is an interface where a user creates data
from django.forms import ModelForm

#accessing our models such that we link them to the form
from .models import *

class AddForm(ModelForm):
    #class meta helps a\us access a model and manipulate it
    class Meta:
        model = Product
        #we are updating the already existing stock
        fields = ['received_quantity']
#we modeling a form basing on our model for us to record a given product sale
class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity','amount_recieved','issued_to']


