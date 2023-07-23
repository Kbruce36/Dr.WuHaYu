from django.db import models

# Create your models here.

#models means description of the space in the database where we store things
#models are python classes
class Category(models.Model):
    name = models.CharField(max_length = 50, null = True, blank = True)
    def __str__(self):
        return self.name


class Product(models.Model):
    #here we are connecting the product model to the category model
    #a froreign is a column in one table that is being referenced in another table
    category_name = models.ForeignKey(Category, on_delete = models.CASCADE, null = True, blank=True)
    item_name = models.CharField(max_length = 50, null = True, blank = True)
    total_quantity = models.IntegerField(default = 0, null = True, blank = True)
    issued_quantity =  models.IntegerField(default = 0, null = True, blank = True)
    received_quantity =  models.IntegerField(default = 0, null = True, blank = True)
    unit_price =  models.IntegerField(default = 0, null = True, blank = True)
    manufacturer =  models.CharField(max_length = 50, null = True, blank = True)
    brand =  models.CharField(max_length = 50, null = True, blank = True)
    
    def __str__(self):
        return self.item_name



class Sale(models.Model):
    #the item name, the price, purchasers name, date of purchase, quantity purchased, VAT,
    item = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0, null = False, blank = True)
    amount_recieved = models.IntegerField(default = 0, null = False, blank = True)
    issued_to = models.CharField(max_length = 50, null = True, blank = True)
    unit_price = models.IntegerField(default = 0, null = True, blank = True)
    #date = models.DateTimeField(auto_now_add = True)
    #the method below calculates the total sale 
    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)
    #we calculate the change using the method below
    def get_change(self):
        change = self.get_total() - self.amount_recieved
        return abs(int(change))
    #we can add as many fields as possible depending on your preference
    def get_vat(self):
        pass

    def __str__(self):
        return self.item.item_name
    
#appointment model
