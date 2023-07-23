import django_filters
#from the same folder that filters is, there is models so use '.'
from .models import Category, Product

#creating a class to filter models 
#inheriting from FilterSet
class Product_filter(django_filters.FilterSet):
    #class Meta is used to alter/manipulate content of another class 
    class Meta: 
        model = Product
        #in brackets is what someone should search for 
        fields = ['item_name']

class Category_filter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['name']