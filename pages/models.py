from django.db import models


class State(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        #managed = True
        db_table = 'pages_state'

class Lga(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        #managed = True
        db_table = 'pages_lga'

class Person(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    lga = models.ForeignKey(Lga, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        #managed = True
        db_table = 'pages_person'


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    is_discount = models.BooleanField(default=False)

    def discount_price(self):
        discount = 0
        if self.is_discount == True:
            discount = self.price - self.discount
        return discount
